"""
CDriv — Control Chromium via ChromeDriver on Termux
Alternative to Playwright/Selenium (do not work on android/aarch64).

Usage:
    from cdriv import CDriv

    scraper = CDriv()
    scraper.start()
    scraper.new_session()
    scraper.navigate("https://site.com")
    html = scraper.get_page_source()
    cookies = scraper.get_cookies_dict()
    scraper.close()
    scraper.stop()
"""

import requests
import time
import subprocess
import atexit
import os
import signal
import base64
import shutil
from urllib.parse import urljoin


# ── Detecta caminhos automaticamente no Termux ────────────────────

def _find_binary(name):
    """Tenta encontrar o binário no PATH ou nos locais comuns do Termux."""
    path = shutil.which(name)
    if path:
        return path
    # Caminhos comuns do Termux
    termux_paths = [
        f"/data/data/com.termux/files/usr/bin/{name}",
        f"{os.path.expanduser('~')}/../usr/bin/{name}",
    ]
    for p in termux_paths:
        if os.path.isfile(p):
            return p
    return name  # fallback: confia que tá no PATH


class CDriv:
    """
    Controla Chromium via ChromeDriver usando o WebDriver Protocol (HTTP).
    Funciona no Termux (aarch64/android) onde Playwright e Selenium falham.
    """

    def __init__(self, port=9515, chromedriver_path=None, chromium_path=None):
        self.port = port
        self.base_url = f"http://localhost:{port}"
        self.chromedriver_path = chromedriver_path or _find_binary("chromedriver")
        self.chromium_path = chromium_path or _find_binary("chromium-browser")
        self.process = None
        self.session_id = None

    # ── Gerenciamento do ChromeDriver ──────────────────────────────

    def start(self):
        """Inicia o ChromeDriver como processo externo."""
        if self.process:
            return self

        self.process = subprocess.Popen(
            [self.chromedriver_path, f"--port={self.port}"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            preexec_fn=os.setsid,
        )
        atexit.register(self.stop)

        for _ in range(15):
            try:
                resp = requests.get(f"{self.base_url}/status", timeout=2)
                if resp.status_code == 200:
                    return self
            except requests.ConnectionError:
                time.sleep(0.5)

        self.stop()
        raise RuntimeError("ChromeDriver não iniciou a tempo")

    def stop(self):
        """Para o processo do ChromeDriver."""
        atexit.unregister(self.stop)
        if self.process:
            try:
                os.killpg(os.getpgid(self.process.pid), signal.SIGTERM)
            except (ProcessLookupError, AttributeError):
                pass
            self.process = None

    def restart(self):
        """Reinicia o ChromeDriver (stop + start)."""
        self.close()
        self.stop()
        time.sleep(1)
        return self.start()

    def __enter__(self):
        self.start()
        return self

    def __exit__(self, *args):
        self.close()
        self.stop()

    # ── Sessão do navegador ────────────────────────────────────────

    def new_session(self):
        """
        Cria uma nova sessão (abre uma janela do Chromium).
        Retorna o sessionId.
        """
        body = {
            "capabilities": {
                "alwaysMatch": {
                    "browserName": "chrome",
                    "goog:chromeOptions": {
                        "binary": self.chromium_path,
                        "args": [
                            "--headless=new",
                            "--no-sandbox",
                            "--disable-dev-shm-usage",
                            "--disable-gpu",
                            "--window-size=1920,1080",
                            "--disable-blink-features=AutomationControlled",
                            "--user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
                        ],
                    },
                }
            }
        }
        resp = requests.post(
            f"{self.base_url}/session", json=body, timeout=20
        )
        data = resp.json()
        if resp.status_code != 200:
            msg = data.get("value", {}).get("message", str(data))
            raise RuntimeError(f"Falha ao criar sessão: {msg}")
        self.session_id = data["value"]["sessionId"]
        return self.session_id

    def close(self):
        """Fecha a sessão atual (fecha o navegador)."""
        if self.session_id:
            try:
                requests.delete(
                    f"{self.base_url}/session/{self.session_id}",
                    timeout=10,
                )
            except requests.RequestException:
                pass
            self.session_id = None

    # ── Navegação ──────────────────────────────────────────────────

    def navigate(self, url):
        """
        Navega para uma URL. Aguarda o carregamento completo.
        """
        if not self.session_id:
            raise RuntimeError("Nenhuma sessão ativa. Chame new_session() primeiro.")

        resp = requests.post(
            f"{self.base_url}/session/{self.session_id}/url",
            json={"url": url},
            timeout=30,
        )
        if resp.status_code != 200:
            msg = resp.json().get("value", {}).get("message", "")
            raise RuntimeError(f"Falha ao navegar: {msg}")

    def get_current_url(self):
        """Retorna a URL atual da página."""
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/url", timeout=10
        )
        return resp.json()["value"]

    def back(self):
        """Volta para a página anterior."""
        requests.post(
            f"{self.base_url}/session/{self.session_id}/back", timeout=10
        )

    def forward(self):
        """Avança para a próxima página."""
        requests.post(
            f"{self.base_url}/session/{self.session_id}/forward", timeout=10
        )

    def refresh(self):
        """Recarrega a página atual."""
        requests.post(
            f"{self.base_url}/session/{self.session_id}/refresh", timeout=10
        )

    # ── Extração de dados ──────────────────────────────────────────

    def get_page_source(self):
        """Retorna o HTML completo da página."""
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/source", timeout=10
        )
        return resp.json()["value"]

    def get_title(self):
        """Retorna o título da página."""
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/title", timeout=10
        )
        return resp.json()["value"]

    # ── Cookies ────────────────────────────────────────────────────

    def get_cookies(self):
        """
        Retorna a lista bruta de cookies (cada um é um dict).
        Uso: cookies = scraper.get_cookies()
             for c in cookies: print(c['name'], c['value'])
        """
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/cookie", timeout=10
        )
        return resp.json()["value"]

    def get_cookies_dict(self):
        """
        Retorna cookies como dict {nome: valor} para usar com requests.
        Uso: session = requests.Session()
             session.cookies.update(scraper.get_cookies_dict())
        """
        cookies = self.get_cookies()
        return {c["name"]: c["value"] for c in cookies}

    def add_cookie(self, name, value, domain=None, path="/"):
        """Adiciona um cookie à sessão."""
        cookie = {"name": name, "value": value, "path": path}
        if domain:
            cookie["domain"] = domain
        requests.post(
            f"{self.base_url}/session/{self.session_id}/cookie",
            json={"cookie": cookie},
            timeout=10,
        )

    def delete_all_cookies(self):
        """Remove todos os cookies da sessão."""
        requests.delete(
            f"{self.base_url}/session/{self.session_id}/cookie", timeout=10
        )

    # ── JavaScript ─────────────────────────────────────────────────

    def execute_script(self, script, *args):
        """
        Executa JavaScript na página e retorna o resultado.
        Exemplos:
            scraper.execute_script("return document.title")
            scraper.execute_script("return document.querySelector('.x').innerText")
            scraper.execute_script("return localStorage.getItem('token')")
            scraper.execute_script("document.querySelector('#btn').click()")
        """
        resp = requests.post(
            f"{self.base_url}/session/{self.session_id}/execute/sync",
            json={"script": script, "args": list(args)},
            timeout=10,
        )
        return resp.json()["value"]

    # ── Interação com elementos ────────────────────────────────────

    def click(self, selector):
        """
        Clica em um elemento da página via seletor CSS.
        Exemplo: scraper.click("button#enviar")
        """
        return self.execute_script(
            f"document.querySelector('{selector}')?.click()"
        )

    def fill(self, selector, value):
        """
        Preenche um campo de input com um valor.
        Exemplo: scraper.fill("input#email", "teste@email.com")
        """
        return self.execute_script(
            f"""
            var el = document.querySelector('{selector}');
            if (el) {{
                el.value = '{value}';
                el.dispatchEvent(new Event('input', {{bubbles: true}}));
                el.dispatchEvent(new Event('change', {{bubbles: true}}));
            }}
            """
        )

    def get_text(self, selector):
        """
        Retorna o texto visível de um elemento.
        Exemplo: texto = scraper.get_text("h1.titulo")
        """
        return self.execute_script(
            f"return document.querySelector('{selector}')?.innerText || ''"
        )

    def get_attribute(self, selector, attr):
        """
        Retorna o valor de um atributo de um elemento.
        Exemplo: href = scraper.get_attribute("a.link", "href")
        """
        return self.execute_script(
            f"return document.querySelector('{selector}')?.getAttribute('{attr}') || ''"
        )

    def get_all_texts(self, selector):
        """
        Retorna uma lista com o texto de todos os elementos que
        correspondem ao seletor.
        Exemplo: itens = scraper.get_all_texts("li.item")
        """
        return self.execute_script(
            f"""
            return Array.from(document.querySelectorAll('{selector}'))
                .map(el => el.innerText)
            """
        )

    def get_all_attributes(self, selector, attr):
        """
        Retorna uma lista com valores de atributos de múltiplos elementos.
        Exemplo: links = scraper.get_all_attributes("a", "href")
        """
        return self.execute_script(
            f"""
            return Array.from(document.querySelectorAll('{selector}'))
                .map(el => el.getAttribute('{attr}') || '')
            """
        )

    def select_option(self, selector, value):
        """
        Seleciona uma opção em um <select>.
        """
        return self.execute_script(
            f"""
            var el = document.querySelector('{selector}');
            if (el) {{
                el.value = '{value}';
                el.dispatchEvent(new Event('change', {{bubbles: true}}));
            }}
            """
        )

    # ── Scroll ─────────────────────────────────────────────────────

    def scroll_to(self, x=0, y=0):
        """Rola a página para uma posição."""
        self.execute_script(f"window.scrollTo({x}, {y})")

    def scroll_to_bottom(self):
        """Rola até o final da página."""
        self.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    def scroll_to_element(self, selector):
        """Rola até que o elemento fique visível."""
        self.execute_script(
            f"document.querySelector('{selector}')?.scrollIntoView({{behavior: 'smooth', block: 'center'}})"
        )

    # ── Espera ─────────────────────────────────────────────────────

    def wait_for_element(self, selector, timeout=10, interval=0.3):
        """
        Aguarda até que um elemento apareça no DOM.
        Retorna True se encontrou, False se timeout.

        Exemplo:
            if scraper.wait_for_element("#carregou", timeout=15):
                print("Elemento encontrado!")
        """
        for _ in range(int(timeout / interval)):
            found = self.execute_script(
                f"return document.querySelector('{selector}') !== null"
            )
            if found:
                return True
            time.sleep(interval)
        return False

    def wait_for_text(self, text, timeout=10, interval=0.5):
        """
        Aguarda até que um texto apareça na página.
        """
        for _ in range(int(timeout / interval)):
            found = self.execute_script(
                f"return document.body.innerText.includes('{text}')"
            )
            if found:
                return True
            time.sleep(interval)
        return False

    def sleep(self, seconds):
        """Pausa por N segundos (igual time.sleep, mas mais legível no fluxo)."""
        time.sleep(seconds)

    def wait_for_navigation(self, timeout=10):
        """
        Aguarda a página terminar de carregar (readyState === 'complete').
        """
        for _ in range(timeout):
            ready = self.execute_script("return document.readyState")
            if ready == "complete":
                return True
            time.sleep(1)
        return False

    # ── Screenshot ─────────────────────────────────────────────────

    def screenshot(self, filepath="screenshot.png"):
        """
        Tira um screenshot da página e salva em arquivo.
        Exemplo: scraper.screenshot("pagina.png")
        """
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/screenshot",
            timeout=15,
        )
        data = resp.json()["value"]
        with open(filepath, "wb") as f:
            f.write(base64.b64decode(data))
        return filepath

    def screenshot_as_base64(self):
        """
        Retorna o screenshot como string base64 (sem salvar).
        """
        resp = requests.get(
            f"{self.base_url}/session/{self.session_id}/screenshot",
            timeout=15,
        )
        return resp.json()["value"]

    # ── Local / Session Storage ────────────────────────────────────

    def get_local_storage(self, key=None):
        """Retorna valor do localStorage. Se key=None, retorna tudo."""
        if key:
            return self.execute_script(f"return localStorage.getItem('{key}')")
        return self.execute_script("return JSON.stringify(JSON.stringify(localStorage))")

    def set_local_storage(self, key, value):
        """Define um valor no localStorage."""
        self.execute_script(f"localStorage.setItem('{key}', '{value}')")

    def get_session_storage(self, key=None):
        """Retorna valor do sessionStorage. Se key=None, retorna tudo."""
        if key:
            return self.execute_script(f"return sessionStorage.getItem('{key}')")
        return self.execute_script("return JSON.stringify(JSON.stringify(sessionStorage))")

    # ── Utilitários ────────────────────────────────────────────────

    def get_user_agent(self):
        """Retorna o User-Agent do navegador."""
        return self.execute_script("return navigator.userAgent")

    def get_viewport_size(self):
        """Retorna o tamanho da viewport como dict {width, height}."""
        return self.execute_script(
            "return {width: window.innerWidth, height: window.innerHeight}"
        )
