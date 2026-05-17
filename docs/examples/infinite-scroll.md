# Paginação Infinita (Scroll)

Exemplo de scraping de páginas com carregamento infinito via scroll.

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # Rola 5 vezes, aguardando carregar entre cada scroll
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # Aguarda novos conteúdos carregarem
        print(f"Scroll {i+1}/5 concluído")

    # Extrai todos os posts carregados
    posts = driver.get_all_texts("article.titulo")
    print(f"\nTotal de posts carregados: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
