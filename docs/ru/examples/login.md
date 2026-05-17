# Вход + API

Реальный пример входа на веб-сайт и повторного использования cookies для API-запросов.

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Заполнение формы входа
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Ожидание перенаправления
    driver.wait_for_navigation()

    # Проверка успешности входа
    if driver.wait_for_element(".dashboard", timeout=5):
        print("Вход выполнен успешно!")

        # Извлечение cookies и создание авторизованной сессии
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # Выполнение авторизованных API-запросов
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("Ошибка входа")
        driver.screenshot("login_error.png")
```
