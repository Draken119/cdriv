# Desplazamiento Infinito

Ejemplo de extracción de datos de páginas con carga mediante desplazamiento infinito.

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # Desplazarse 5 veces, esperando que el contenido se cargue entre cada una
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # Esperar a que se cargue nuevo contenido
        print(f"Desplazamiento {i+1}/5 completado")

    # Extraer todas las publicaciones cargadas
    posts = driver.get_all_texts("article.title")
    print(f"\nTotal de publicaciones cargadas: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
