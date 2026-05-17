# Ожидания

Ожидание определённых условий на странице перед продолжением.

## `wait_for_element(selector, timeout=10, interval=0.3)`

Ожидает появления элемента в DOM.

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("Элемент найден!")
else:
    print("Таймаут — элемент не появился")
```

### Типичное использование

```python
driver.navigate("https://site.com/products")

# Ожидание загрузки списка
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("Список товаров не загрузился")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

Ожидает появления указанного текста на странице.

```python
# Ожидание подтверждения
if driver.wait_for_text("Order confirmed", timeout=20):
    print("Заказ успешно подтверждён!")
else:
    print("Таймаут подтверждения")
```

## `wait_for_navigation(timeout=10)`

Ожидает завершения загрузки страницы (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("Страница загружена!")
```

## `sleep(seconds)`

Приостанавливает выполнение на N секунд. Аналогично `time.sleep()`, но более читаемо в потоке.

```python
driver.sleep(2)  # Подождать 2 секунды
```

## Комбинированный пример

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # Ожидание загрузки панели управления
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Welcome", timeout=5)
        print("Вход выполнен успешно!")
    else:
        driver.screenshot("login_error.png")
        print("Ошибка входа")
```
