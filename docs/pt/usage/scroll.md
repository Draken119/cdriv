# Rolagem

Métodos para rolar a página.

## `scroll_to(x=0, y=0)`

Rola a página para uma posição específica.

```python
driver.scroll_to(0, 500)   # Rolar 500px para baixo
driver.scroll_to(0, 0)     # Voltar ao topo
driver.scroll_to(200, 300) # 200px para direita, 300px para baixo
```

## `scroll_to_bottom()`

Rola até o final da página.

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

Rola até que o elemento fique visível (centralizado na tela).

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## Exemplo: Rolagem Infinita

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 rolagens
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"Posts carregados: {len(posts)}")
```
