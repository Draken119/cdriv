# Interacción con Elementos

Métodos para interactuar con elementos de la página mediante selectores CSS.

## `click(selector)`

Hace clic en un elemento de la página.

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

Rellena un campo de entrada con un valor. Dispara los eventos `input` y `change` automáticamente.

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
driver.fill("input[type='search']", "search term")
```

## `get_text(selector)`

Devuelve el texto visible de un elemento.

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

Devuelve el valor de un atributo de un elemento.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

Devuelve una lista del **texto interno** de **todos** los elementos que coinciden con el selector.

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

Devuelve una lista de valores de atributos de múltiples elementos.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

Selecciona una opción en un elemento `<select>`.

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## Ejemplo Completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # Obtener todos los productos
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # Hacer clic en el primer producto
    driver.click(".product-link:first-child")
```
