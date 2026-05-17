# Scraping de Múltiplas Páginas

Exemplo de scraping de várias páginas sequencialmente.

```python
from cdriv import CDriv

urls = [
    "https://site.com/pag1",
    "https://site.com/pag2",
    "https://site.com/pag3",
]

with CDriv() as driver:
    driver.new_session()

    for url in urls:
        driver.navigate(url)
        driver.wait_for_element(".conteudo", timeout=10)

        titulo = driver.get_text("h1")
        texto = driver.get_text(".conteudo")
        links = driver.get_all_attributes("a", "href")

        print(f"=== {titulo} ===")
        print(f"Texto: {texto[:100]}...")
        print(f"Links: {len(links)} encontrados")
        print()
```
