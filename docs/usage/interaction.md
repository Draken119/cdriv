# Element Interaction

Methods for interacting with page elements via CSS selectors.

## `click(selector)`

Clicks on a page element.

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

Fills an input field with a value. Fires `input` and `change` events automatically.

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
driver.fill("input[type='search']", "search term")
```

## `get_text(selector)`

Returns the visible text of an element.

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

Returns the value of an element's attribute.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

Returns a list of the **inner text** of **all** elements matching the selector.

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

Returns a list of attribute values from multiple elements.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

Selects an option in a `<select>` element.

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## Complete Example

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # Get all products
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # Click on the first product
    driver.click(".product-link:first-child")
```
