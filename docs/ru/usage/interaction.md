# Взаимодействие с элементами

Методы для взаимодействия с элементами страницы через CSS-селекторы.

## `click(selector)`

Выполняет клик по элементу на странице.

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

Заполняет поле ввода значением. Автоматически вызывает события `input` и `change`.

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
driver.fill("input[type='search']", "search term")
```

## `get_text(selector)`

Возвращает видимый текст элемента.

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

Возвращает значение атрибута элемента.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

Возвращает список **внутренних текстов** **всех** элементов, соответствующих селектору.

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

Возвращает список значений атрибутов из нескольких элементов.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

Выбирает опцию в элементе `<select>`.

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## Полный пример

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # Получить все товары
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # Кликнуть на первый товар
    driver.click(".product-link:first-child")
```
