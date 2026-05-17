# 要素との対話

CSS セレクタを使用してページ要素と対話するためのメソッドです。

## `click(selector)`

ページ要素をクリックします。

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

入力フィールドに値を入力します。`input` イベントと `change` イベントを自動的に発火します。

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
driver.fill("input[type='search']", "search term")
```

## `get_text(selector)`

要素の visible なテキストを返します。

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

要素の属性の値を返します。

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

セレクタに一致する **すべての** 要素の **内部テキスト** のリストを返します。

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

複数の要素から属性値のリストを返します。

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

`<select>` 要素のオプションを選択します。

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## 完全な例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # すべての商品を取得
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # 最初の商品をクリック
    driver.click(".product-link:first-child")
```
