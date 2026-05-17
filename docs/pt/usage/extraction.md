# Extração de Dados

Métodos para extrair informações da página.

## `get_page_source()`

Retorna o HTML **completo** da página como uma string.

```python
html = driver.get_page_source()

# Salvar em arquivo
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# Analisar com BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup é opcional"
    O `cdriv` não depende do BeautifulSoup. Instale separadamente se necessário:
    `pip install beautifulsoup4`

## `get_title()`

Retorna o título da página (conteúdo da tag `<title>`).

```python
title = driver.get_title()
print(f"Pagina: {title}")
```

## Exemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"Titulo: {title}")
    print(f"Tamanho do HTML: {len(html)} caracteres")
```
