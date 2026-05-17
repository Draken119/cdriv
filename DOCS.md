# cdriv Documentation

Lib Python para controlar Chromium via ChromeDriver no **Termux** (Android aarch64).
Alternativa direta ao Playwright e Selenium, que **não funcionam** em Android/aarch64.

## Índice

- [Instalação](#instalação)
- [Uso básico](#uso-básico)
- [API Completa](#api-completa)
  - [Gerenciamento do ChromeDriver](#gerenciamento-do-chromedriver)
  - [Sessão do navegador](#sessão-do-navegador)
  - [Navegação](#navegação)
  - [Extração de dados](#extração-de-dados)
  - [Cookies](#cookies)
  - [JavaScript](#javascript)
  - [Interação com elementos](#interação-com-elementos)
  - [Scroll](#scroll)
  - [Espera (waits)](#espera-waits)
  - [Screenshot](#screenshot)
  - [Storage (localStorage / sessionStorage)](#storage-localstorage--sessionstorage)
  - [Utilitários](#utilitários)
- [Exemplos práticos](#exemplos-práticos)
- [Solução de problemas](#solução-de-problemas)

---

## Instalação

```bash
pip install cdriv
```

### Pré-requisitos no Termux

```bash
pkg update
pkg install chromium-browser chromedriver
```

### Pré-requisitos em outros Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

---

## Uso básico

### Context manager (recomendado)

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://exemplo.com")
    html = driver.get_page_source()
    print(driver.get_title())
```

### Gerenciamento manual

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://exemplo.com")
# ... faz o que precisa ...
driver.close()
driver.stop()
```

---

## API Completa

### Gerenciamento do ChromeDriver

#### `CDriv(port=9515, chromedriver_path=None, chromium_path=None)`

Construtor. Inicializa o controlador.

| Parâmetro | Padrão | Descrição |
|-----------|--------|-----------|
| `port` | `9515` | Porta HTTP do ChromeDriver |
| `chromedriver_path` | `None` (auto-detect) | Caminho do binário chromedriver |
| `chromium_path` | `None` (auto-detect) | Caminho do binário chromium-browser |

```python
driver = CDriv(port=9515)
driver = CDriv(chromedriver_path="/usr/bin/chromedriver")
```

#### `start()`

Inicia o processo do ChromeDriver. Aguarda até que ele responda na porta configurada.
Retorna `self` para encadeamento de métodos.

```python
driver.start()
```

#### `stop()`

Para o processo do ChromeDriver. Remove o registro do `atexit`.

```python
driver.stop()
```

#### `restart()`

Reinicia o ChromeDriver (stop + start).

```python
driver.restart()
```

---

### Sessão do navegador

#### `new_session()`

Abre uma nova janela do Chromium (cria uma sessão WebDriver). Retorna o `sessionId`.

O navegador inicia em modo **headless** com as seguintes configurações automáticas:
- Janela 1920x1080
- User-Agent Chrome 146 (Linux x86_64)
- Desabilita detecção de automação
- No-sandbox, disable-dev-shm-usage (necessário para Termux/container)

```python
session_id = driver.new_session()
```

#### `close()`

Fecha a sessão atual (fecha o navegador).

```python
driver.close()
```

---

### Navegação

| Método | Descrição |
|--------|-----------|
| `navigate(url)` | Navega para uma URL |
| `get_current_url()` | Retorna a URL atual |
| `back()` | Volta para página anterior |
| `forward()` | Avança para próxima página |
| `refresh()` | Recarrega a página |

```python
driver.navigate("https://site.com")
print(driver.get_current_url())
driver.back()
driver.forward()
driver.refresh()
```

---

### Extração de dados

#### `get_page_source()`

Retorna o HTML **completo** da página como string.

```python
html = driver.get_page_source()
```

#### `get_title()`

Retorna o título da página (conteúdo da tag `<title>`).

```python
titulo = driver.get_title()
```

---

### Cookies

#### `get_cookies()`

Retorna a lista bruta de cookies. Cada cookie é um dicionário com as chaves: `name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(c['name'], c['value'])
```

#### `get_cookies_dict()`

Retorna cookies como dicionário `{nome: valor}` — ideal para usar com `requests.Session()`.

```python
import requests

session = requests.Session()
session.cookies.update(driver.get_cookies_dict())
resp = session.get("https://site.com/api/dados")
print(resp.json())
```

#### `add_cookie(name, value, domain=None, path="/")`

Adiciona um cookie manualmente à sessão.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
```

#### `delete_all_cookies()`

Remove todos os cookies da sessão.

```python
driver.delete_all_cookies()
```

---

### JavaScript

#### `execute_script(script, *args)`

Executa JavaScript na página e retorna o resultado.

```python
# Ler dados da página
titulo = driver.execute_script("return document.title")
texto = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# Manipular a página
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Com argumentos
driver.execute_script("arguments[0].scrollIntoView()", elemento)
```

---

### Interação com elementos

#### `click(selector)`

Clica em um elemento via seletor CSS.

```python
driver.click("button#enviar")
driver.click("a.link-login")
driver.click(".btn-primary")
```

#### `fill(selector, value)`

Preenche um campo de input. Dispara eventos `input` e `change`.

```python
driver.fill("input#email", "usuario@email.com")
driver.fill("textarea#mensagem", "Olá, mundo!")
```

#### `get_text(selector)`

Retorna o texto visível de um elemento.

```python
nome = driver.get_text("h1.titulo")
preco = driver.get_text(".produto-preco")
```

#### `get_attribute(selector, attr)`

Retorna o valor de um atributo de um elemento.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#foto", "src")
alt = driver.get_attribute("img", "alt")
```

#### `get_all_texts(selector)`

Retorna uma lista com o texto de **todos** os elementos que correspondem ao seletor.

```python
itens = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]
```

#### `get_all_attributes(selector, attr)`

Retorna uma lista com valores de atributos de múltiplos elementos.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]
imgs = driver.get_all_attributes("img", "src")
```

#### `select_option(selector, value)`

Seleciona uma opção em um elemento `<select>`.

```python
driver.select_option("select#pais", "BR")
driver.select_option("select#categoria", "tecnologia")
```

---

### Scroll

#### `scroll_to(x=0, y=0)`

Rola a página para uma posição específica.

```python
driver.scroll_to(0, 500)  # Rola 500px para baixo
```

#### `scroll_to_bottom()`

Rola até o final da página.

```python
driver.scroll_to_bottom()
```

#### `scroll_to_element(selector)`

Rola até que o elemento fique visível (centralizado na tela).

```python
driver.scroll_to_element("#resultados")
```

---

### Espera (waits)

#### `wait_for_element(selector, timeout=10, interval=0.3)`

Aguarda até que um elemento apareça no DOM. Retorna `True` se encontrou, `False` se timeout.

```python
if driver.wait_for_element("#carregou", timeout=15):
    print("Elemento encontrado!")
else:
    print("Timeout — elemento não apareceu")
```

#### `wait_for_text(text, timeout=10, interval=0.5)`

Aguarda até que um texto apareça na página.

```python
if driver.wait_for_text("Pedido confirmado", timeout=20):
    print("Pedido confirmado!")
```

#### `wait_for_navigation(timeout=10)`

Aguarda a página terminar de carregar (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
```

#### `sleep(seconds)`

Pausa por N segundos. Mesmo que `time.sleep()`, mas mais legível no fluxo.

```python
driver.sleep(2)  # Aguarda 2 segundos
```

---

### Screenshot

#### `screenshot(filepath="screenshot.png")`

Tira um screenshot da página e salva em arquivo. Retorna o caminho do arquivo.

```python
driver.screenshot("pagina.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

#### `screenshot_as_base64()`

Retorna o screenshot como string base64 (sem salvar em arquivo).

```python
img_b64 = driver.screenshot_as_base64()
# útil para enviar para API, exibir em HTML, etc.
```

---

### Storage (localStorage / sessionStorage)

#### `get_local_storage(key=None)`

Retorna valor do `localStorage`. Se `key=None`, retorna tudo como string JSON.

```python
driver.get_local_storage("token")       # valor específico
driver.get_local_storage()              # tudo
```

#### `set_local_storage(key, value)`

Define um valor no `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
```

#### `get_session_storage(key=None)`

Retorna valor do `sessionStorage`. Se `key=None`, retorna tudo.

```python
driver.get_session_storage("session_id")
driver.get_session_storage()
```

---

### Utilitários

#### `get_user_agent()`

Retorna o User-Agent do navegador.

```python
ua = driver.get_user_agent()
```

#### `get_viewport_size()`

Retorna o tamanho da viewport como dicionário `{width, height}`.

```python
size = driver.get_viewport_size()
print(f"{size['width']}x{size['height']}")
```

---

## Exemplos práticos

### 1. Login + extrair cookies para API

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Preenche formulário
    driver.fill("input#username", "meu_login")
    driver.fill("input#password", "minha_senha")
    driver.click("button[type='submit']")

    # Aguarda redirecionamento
    driver.wait_for_navigation()

    # Pega cookies e faz requisição autenticada
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    dados = session.get("https://site.com/api/dados").json()
    print(dados)
```

### 2. Scraping de múltiplas páginas

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    for url in ["https://site.com/pag1", "https://site.com/pag2", "https://site.com/pag3"]:
        driver.navigate(url)
        driver.wait_for_element(".conteudo", timeout=10)

        titulo = driver.get_text("h1")
        texto = driver.get_text(".conteudo")
        links = driver.get_all_attributes("a", "href")

        print(f"=== {titulo} ===")
        print(f"Links: {len(links)} encontrados")
```

### 3. Navegação com paginação infinita (scroll)

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 scrolls
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.titulo")
    print(f"Posts carregados: {len(posts)}")
```

### 4. Screenshot para depuração

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#erro", timeout=5)
        print("Elemento de erro encontrado!")
    except:
        driver.screenshot("erro.png")
        print("Screenshot salvo como erro.png")
```

---

## Solução de problemas

### ChromeDriver não inicia

```bash
# Verifique se os binários estão instalados
which chromedriver
which chromium-browser

# Verifique a versão
chromedriver --version
chromium-browser --version
```

Se não estiverem instalados:
```bash
pkg install chromium-browser chromedriver
```

### Sessão não cria / navegador não abre

No Termux, é essencial que os pacotes `chromium-browser` e `chromedriver` sejam da mesma versão. Atualize ambos:

```bash
pkg upgrade chromium-browser chromedriver
```

### Porta ocupada

Se a porta 9515 estiver ocupada, use uma porta diferente:

```python
driver = CDriv(port=9516)
```

### Erro de permissão (sandbox)

O `CDriv` já inicia com `--no-sandbox` por padrão, que é necessário no Termux e em containers. Se ainda assim tiver erro, confirme que o chromium foi instalado corretamente.
