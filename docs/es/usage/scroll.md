# Desplazamiento

Métodos para desplazarse por la página.

## `scroll_to(x=0, y=0)`

Desplaza la página a una posición específica.

```python
driver.scroll_to(0, 500)   # Desplazar 500px hacia abajo
driver.scroll_to(0, 0)     # Volver al inicio
driver.scroll_to(200, 300) # 200px a la derecha, 300px hacia abajo
```

## `scroll_to_bottom()`

Desplaza hasta el final de la página.

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

Desplaza hasta que el elemento sea visible (centrado en la pantalla).

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## Ejemplo: Desplazamiento Infinito

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 desplazamientos
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"Publicaciones cargadas: {len(posts)}")
```
