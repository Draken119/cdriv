# Навигация

Методы для навигации между веб-страницами.

## `navigate(url)`

Переходит по указанному URL. Ожидает полной загрузки страницы.

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

Возвращает URL текущей страницы.

```python
url = driver.get_current_url()
print(f"Вы находитесь на: {url}")
```

## `back()`

Возвращает на предыдущую страницу (как кнопка "Назад" в браузере).

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # Возврат на page1
```

## `forward()`

Переходит на следующую страницу (как кнопка "Вперед" в браузере).

```python
driver.forward()  # Возврат на page2
```

## `refresh()`

Перезагружает текущую страницу.

```python
driver.refresh()
```

## Полный пример

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # Имитация навигационного потока
    driver.navigate("https://site.com/dashboard")
    driver.back()      # Назад на login
    driver.forward()   # Вперед на dashboard
    driver.refresh()   # Перезагрузка dashboard
```
