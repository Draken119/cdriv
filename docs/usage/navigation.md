# Navegação

Métodos para navegar entre páginas da web.

## `navigate(url)`

Navega para uma URL. Aguarda o carregamento completo da página.

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/produto/123")
```

## `get_current_url()`

Retorna a URL atual da página.

```python
url = driver.get_current_url()
print(f"Você está em: {url}")
```

## `back()`

Volta para a página anterior (como o botão "voltar" do navegador).

```python
driver.navigate("https://site.com/pagina1")
driver.navigate("https://site.com/pagina2")
driver.back()  # Volta para pagina1
```

## `forward()`

Avança para a próxima página (como o botão "avançar").

```python
driver.forward()  # Volta para pagina2
```

## `refresh()`

Recarrega a página atual.

```python
driver.refresh()
```

## Exemplo completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # Simula navegação
    driver.navigate("https://site.com/dashboard")
    driver.back()      # Volta pro login
    driver.forward()   # Volta pro dashboard
    driver.refresh()   # Recarrega o dashboard
```
