# Interação com Elementos

Métodos para interagir com elementos da página via seletores CSS.

## `click(selector)`

Clica em um elemento da página.

```python
driver.click("button#enviar")
driver.click("a.link-login")
driver.click(".btn-primary")
driver.click("#menu > li:first-child a")
```

## `fill(selector, value)`

Preenche um campo de input com um valor. Dispara eventos `input` e `change`
automaticamente.

```python
driver.fill("input#email", "usuario@email.com")
driver.fill("textarea#mensagem", "Olá, mundo!")
driver.fill("input[type='search']", "termo de busca")
```

## `get_text(selector)`

Retorna o texto visível de um elemento.

```python
nome = driver.get_text("h1.titulo")
preco = driver.get_text(".produto-preco")
descricao = driver.get_text("#descricao")
```

## `get_attribute(selector, attr)`

Retorna o valor de um atributo de um elemento.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#foto", "src")
alt = driver.get_attribute("img.logo", "alt")
```

## `get_all_texts(selector)`

Retorna uma lista com o texto de **todos** os elementos que correspondem ao seletor.

```python
itens = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]

precos = driver.get_all_texts(".produto-preco")
# ["R$ 10,00", "R$ 25,50", "R$ 99,90"]
```

## `get_all_attributes(selector, attr)`

Retorna uma lista com valores de atributos de múltiplos elementos.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]

imgs = driver.get_all_attributes("img", "src")
# ["foto1.jpg", "foto2.jpg", ...]
```

## `select_option(selector, value)`

Seleciona uma opção em um elemento `<select>`.

```python
driver.select_option("select#pais", "BR")
driver.select_option("select#categoria", "tecnologia")
```

## Exemplo completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/produtos")

    # Pega todos os produtos
    nomes = driver.get_all_texts(".produto-nome")
    precos = driver.get_all_texts(".produto-preco")
    links = driver.get_all_attributes(".produto-link", "href")

    for nome, preco, link in zip(nomes, precos, links):
        print(f"{nome}: {preco} -> {link}")

    # Clica no primeiro produto
    driver.click(".produto-link:first-child")
```
