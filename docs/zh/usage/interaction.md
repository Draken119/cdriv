# 元素交互

通过 CSS 选择器与页面元素进行交互的方法。

## `click(selector)`

点击一个页面元素。

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

在输入字段中填入值。自动触发 `input` 和 `change` 事件。

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
driver.fill("input[type='search']", "search term")
```

## `get_text(selector)`

返回一个元素的可见文本。

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

返回元素属性的值。

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

返回所有匹配选择器的元素的**内部文本**列表。

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

返回多个元素的属性值列表。

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

在 `<select>` 元素中选择一个选项。

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## 完整示例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # 获取所有产品
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # 点击第一个产品
    driver.click(".product-link:first-child")
```
