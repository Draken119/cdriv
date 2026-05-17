# Rolagem Infinita

Exemplo de raspagem de páginas com carregamento por rolagem infinita.

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # Rolar 5 vezes, aguardando o carregamento do conteúdo entre cada
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # Aguardar novo conteúdo carregar
        print(f"Rolagem {i+1}/5 concluida")

    # Extrair todos os posts carregados
    posts = driver.get_all_texts("article.title")
    print(f"\nTotal de posts carregados: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
