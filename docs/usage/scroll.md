# Scroll

Métodos para rolar a página.

## `scroll_to(x=0, y=0)`

Rola a página para uma posição específica.

```python
driver.scroll_to(0, 500)   # Rola 500px para baixo
driver.scroll_to(0, 0)     # Volta ao topo
driver.scroll_to(200, 300) # 200px direita, 300px baixo
```

## `scroll_to_bottom()`

Rola até o final da página.

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

Rola até que o elemento fique visível (centralizado na tela).

```python
driver.scroll_to_element("#resultados")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#ultimo-link")
```

## Exemplo: paginação infinita

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 scrolls
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.titulo")
    print(f"Posts carregados: {len(posts)}")
```
