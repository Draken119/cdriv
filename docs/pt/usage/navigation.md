# Navegação

Métodos para navegar entre páginas web.

## `navigate(url)`

Navega para uma URL. Aguarda o carregamento completo da página.

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

Retorna a URL da página atual.

```python
url = driver.get_current_url()
print(f"Você está em: {url}")
```

## `back()`

Volta para a página anterior (como o botão voltar do navegador).

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # Retorna para page1
```

## `forward()`

Avança para a próxima página (como o botão avançar do navegador).

```python
driver.forward()  # Retorna para page2
```

## `refresh()`

Recarrega a página atual.

```python
driver.refresh()
```

## Exemplo Completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # Simular fluxo de navegação
    driver.navigate("https://site.com/dashboard")
    driver.back()      # Voltar para login
    driver.forward()   # Avançar para dashboard
    driver.refresh()   # Recarregar dashboard
```
