# Utilitários

## `get_user_agent()`

Retorna a string User-Agent do navegador.

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

Retorna o tamanho da janela de visualização como um dicionário `{width, height}`.

```python
size = driver.get_viewport_size()
print(f"Viewport: {size['width']}x{size['height']}")
```
