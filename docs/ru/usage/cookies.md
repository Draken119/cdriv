# Cookies

Управление cookies сессии браузера.

## `get_cookies()`

Возвращает необработанный список cookies. Каждый cookie — это словарь с ключами:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly` и т.д.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (domain: {c['domain']})")
```

## `get_cookies_dict()`

Возвращает cookies в виде словаря `{name: value}` — идеально для использования с
`requests.Session()`.

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### Типичный сценарий: авторизованные запросы

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Вход в систему
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # Повторное использование авторизованных cookies
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # Выполнение авторизованных запросов
    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

Добавляет cookie вручную в сессию.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

Удаляет все cookies из сессии.

```python
driver.delete_all_cookies()
```
