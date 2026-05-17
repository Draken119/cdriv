# Interação com Elementos

Métodos para interagir com elementos da página via seletores CSS.

## `click(selector)`

Clica em um elemento da página.

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

Preenche um campo de entrada com um valor. Dispara os eventos `input` e `change` automaticamente.

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Ola, mundo!")
driver.fill("input[type='search']", "termo de busca")
```

## `get_text(selector)`

Retorna o texto visível de um elemento.

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
description = driver.get_text("#description")
```

## `get_attribute(selector, attr)`

Retorna o valor de um atributo de um elemento.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

Retorna uma lista do **texto interno** de **todos** os elementos que correspondem ao seletor.

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

prices = driver.get_all_texts(".product-price")
# ["$10.00", "$25.50", "$99.90"]
```

## `get_all_attributes(selector, attr)`

Retorna uma lista de valores de atributos de múltiplos elementos.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

images = driver.get_all_attributes("img", "src")
# ["photo1.jpg", "photo2.jpg", ...]
```

## `select_option(selector, value)`

Seleciona uma opção em um elemento `<select>`.

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

## Exemplo Completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/products")

    # Obter todos os produtos
    names = driver.get_all_texts(".product-name")
    prices = driver.get_all_texts(".product-price")
    links = driver.get_all_attributes(".product-link", "href")

    for name, price, link in zip(names, prices, links):
        print(f"{name}: {price} -> {link}")

    # Clicar no primeiro produto
    driver.click(".product-link:first-child")
```
