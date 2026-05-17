# Extracción de Datos

Métodos para extraer información de la página.

## `get_page_source()`

Devuelve el HTML **completo** de la página como una cadena.

```python
html = driver.get_page_source()

# Guardar en archivo
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# Analizar con BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup es opcional"
    `cdriv` no depende de BeautifulSoup. Instálalo por separado si es necesario:
    `pip install beautifulsoup4`

## `get_title()`

Devuelve el título de la página (contenido de la etiqueta `<title>`).

```python
title = driver.get_title()
print(f"Página: {title}")
```

## Ejemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"Título: {title}")
    print(f"Tamaño del HTML: {len(html)} caracteres")
```
