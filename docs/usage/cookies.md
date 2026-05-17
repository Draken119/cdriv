# Cookies

Gerencie cookies da sessão do navegador.

## `get_cookies()`

Retorna a lista bruta de cookies. Cada cookie é um dicionário com as chaves:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (domínio: {c['domain']})")
```

## `get_cookies_dict()`

Retorna cookies como dicionário `{nome: valor}` — ideal para usar com
`requests.Session()`.

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### Uso típico: requisições autenticadas

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Faz login
    driver.fill("input#username", "meu_login")
    driver.fill("input#password", "minha_senha")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # Reutiliza os cookies autenticados
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # Agora faz requisições autenticadas
    resp = session.get("https://site.com/api/dados")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

Adiciona um cookie manualmente à sessão.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

Remove todos os cookies da sessão.

```python
driver.delete_all_cookies()
```
