# Cookies

Administra las cookies de la sesión del navegador.

## `get_cookies()`

Devuelve la lista cruda de cookies. Cada cookie es un diccionario con las claves:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (dominio: {c['domain']})")
```

## `get_cookies_dict()`

Devuelve las cookies como un diccionario `{name: value}` — ideal para usar con
`requests.Session()`.

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### Caso de Uso Típico: Peticiones Autenticadas

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Iniciar sesión
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # Reutilizar cookies autenticadas
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # Hacer peticiones autenticadas
    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

Añade una cookie manualmente a la sesión.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

Elimina todas las cookies de la sesión.

```python
driver.delete_all_cookies()
```
