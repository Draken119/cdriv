# Cookies

Gerenciar cookies de sessão do navegador.

## `get_cookies()`

Retorna a lista bruta de cookies. Cada cookie é um dicionário com as chaves:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (domain: {c['domain']})")
```

## `get_cookies_dict()`

Retorna cookies como um dicionário `{name: value}` — ideal para usar com
`requests.Session()`.

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### Caso de Uso Tipico: Requisições Autenticadas

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Fazer login
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # Reutilizar cookies autenticados
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # Fazer requisições autenticadas
    resp = session.get("https://site.com/api/data")
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
