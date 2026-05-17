# Извлечение данных

Методы для извлечения информации со страницы.

## `get_page_source()`

Возвращает **полный** HTML-код страницы в виде строки.

```python
html = driver.get_page_source()

# Сохранить в файл
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# Разобрать с помощью BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup не обязателен"
    `cdriv` не зависит от BeautifulSoup. Установите отдельно при необходимости:
    `pip install beautifulsoup4`

## `get_title()`

Возвращает заголовок страницы (содержимое тега `<title>`).

```python
title = driver.get_title()
print(f"Страница: {title}")
```

## Пример

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"Заголовок: {title}")
    print(f"Размер HTML: {len(html)} символов")
```
