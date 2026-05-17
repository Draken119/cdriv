# Хранилище (localStorage / sessionStorage)

Доступ и управление локальным хранилищем браузера.

## `get_local_storage(key=None)`

Возвращает значение из `localStorage`. Если `key=None`, возвращает всё.

```python
# Конкретное значение
token = driver.get_local_storage("token")
print(token)

# Всё
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

Устанавливает значение в `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "en-US"}')
```

## `get_session_storage(key=None)`

Возвращает значение из `sessionStorage`. Если `key=None`, возвращает всё.

```python
# Конкретное значение
session_id = driver.get_session_storage("session_id")

# Всё
all_data = driver.get_session_storage()
```

## Пример

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # Чтение токена аутентификации из localStorage
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"Токен найден: {token[:20]}...")
    else:
        print("Пользователь не аутентифицирован")
        driver.set_local_storage("auth_token", "new_token")
```
