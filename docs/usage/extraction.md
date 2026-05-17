# Extração de Dados

Métodos para extrair informações da página.

## `get_page_source()`

Retorna o HTML **completo** da página como string.

```python
html = driver.get_page_source()

# Salvar em arquivo
with open("pagina.html", "w", encoding="utf-8") as f:
    f.write(html)

# Buscar com BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup é opcional"
    O `cdriv` não depende do BeautifulSoup. Instale separadamente se precisar:
    `pip install beautifulsoup4`

## `get_title()`

Retorna o título da página (conteúdo da tag `<title>`).

```python
titulo = driver.get_title()
print(f"Página: {titulo}")
```

## Exemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://exemplo.com")

    html = driver.get_page_source()
    titulo = driver.get_title()

    print(f"Título: {titulo}")
    print(f"Tamanho do HTML: {len(html)} caracteres")
```
