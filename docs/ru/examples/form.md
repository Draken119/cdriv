# Автоматизация форм

Пример автоматического заполнения и отправки форм.

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # Ожидание загрузки формы
    driver.wait_for_element("form#registration", timeout=10)

    # Заполнение полей
    driver.fill("input#name", "John Doe")
    driver.fill("input#email", "john@email.com")
    driver.fill("input#phone", "+1 (555) 123-4567")
    driver.fill("textarea#message", "Hello, I would like more information.")

    # Выбор опций
    driver.select_option("select#country", "US")
    driver.select_option("select#category", "support")

    # Отметка согласия с условиями
    driver.click("input#accept-terms")

    # Отправка формы
    driver.click("button[type='submit']")

    # Ожидание подтверждения
    if driver.wait_for_text("Registration successful", timeout=15):
        print("Форма успешно отправлена!")
        print(driver.get_text(".success-message"))
    else:
        print("Ошибка при отправке формы")
        driver.screenshot("form_error.png")
```
