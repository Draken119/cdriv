# cdriv

**Controle o Chromium via ChromeDriver no Termux (Android aarch64).**

Alternativa direta ao **Playwright** e **Selenium** — que **não funcionam** em Android/aarch64. Esta lib usa o protocolo WebDriver via HTTP para controlar o Chromium em modo headless, especificamente desenvolvida para rodar no Termux.

## ✨ Funcionalidades

- 🚀 **Leve e rápido** — depende apenas de `requests`, sem frameworks pesados
- 📱 **Feito pro Termux** — funciona nativamente em Android aarch64
- 🧩 **API simples e intuitiva** — em português, métodos diretos
- 🍪 **Extrai cookies** pronto pra usar com `requests.Session()`
- 📸 **Screenshot** da página
- 🖱️ **Interage com elementos** — clicar, preencher, selecionar
- 📜 **Executa JavaScript** na página
- 🔄 **Scroll**, waits, localStorage, navegação (back/forward/refresh)

## Instalação

```bash
pip install cdriv
```

### Pré-requisitos no Termux

```bash
pkg update
pkg install chromium-browser chromedriver
```

### Pré-requisitos em outros Linux

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Uso rápido

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://exemplo.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    titulo = driver.get_title()

    print(titulo)
```

### Login + cookies para requests

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site-alvo.com/login")
    driver.fill("input#username", "meu_login")
    driver.fill("input#password", "minha_senha")
    driver.click("button[type='submit']")

    # Reutiliza os cookies autenticados
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    resp = session.get("https://site-alvo.com/api/dados")
    print(resp.json())
```

## Documentação completa

Veja a [documentação completa](DOCS.md) com todos os métodos, parâmetros e exemplos práticos.

## Métodos principais

| Método | Descrição |
|--------|-----------|
| `start()` / `stop()` | Inicia/para o ChromeDriver |
| `new_session()` / `close()` | Abre/fecha janela do Chromium |
| `navigate(url)` | Navega para uma URL |
| `get_page_source()` | Retorna o HTML completo |
| `get_cookies_dict()` | Retorna cookies como dict |
| `execute_script(js)` | Executa JavaScript |
| `click(selector)` | Clica em um elemento |
| `fill(selector, value)` | Preenche campo de input |
| `screenshot(path)` | Tira screenshot |
| `wait_for_element()` | Aguarda elemento aparecer |
| `scroll_to_bottom()` | Rola até o final da página |

## Licença

MIT
