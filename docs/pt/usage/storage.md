# Armazenamento (localStorage / sessionStorage)

Acessar e manipular o armazenamento local do navegador.

## `get_local_storage(key=None)`

Retorna um valor do `localStorage`. Se `key=None`, retorna tudo.

```python
# Valor específico
token = driver.get_local_storage("token")
print(token)

# Tudo
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

Define um valor no `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "pt-BR"}')
```

## `get_session_storage(key=None)`

Retorna um valor do `sessionStorage`. Se `key=None`, retorna tudo.

```python
# Valor específico
session_id = driver.get_session_storage("session_id")

# Tudo
all_data = driver.get_session_storage()
```

## Exemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # Ler token de autenticação do localStorage
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"Token encontrado: {token[:20]}...")
    else:
        print("Usuário não autenticado")
        driver.set_local_storage("auth_token", "new_token")
```
