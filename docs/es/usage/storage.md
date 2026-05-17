# Almacenamiento (localStorage / sessionStorage)

Accede y manipula el almacenamiento local del navegador.

## `get_local_storage(key=None)`

Devuelve un valor de `localStorage`. Si `key=None`, devuelve todo.

```python
# Valor específico
token = driver.get_local_storage("token")
print(token)

# Todo
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

Establece un valor en `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "en-US"}')
```

## `get_session_storage(key=None)`

Devuelve un valor de `sessionStorage`. Si `key=None`, devuelve todo.

```python
# Valor específico
session_id = driver.get_session_storage("session_id")

# Todo
all_data = driver.get_session_storage()
```

## Ejemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # Leer token de autenticación de localStorage
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"Token encontrado: {token[:20]}...")
    else:
        print("Usuario no autenticado")
        driver.set_local_storage("auth_token", "new_token")
```
