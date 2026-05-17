# Utilitários

## `get_user_agent()`

Retorna o User-Agent do navegador.

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

Retorna o tamanho da viewport como dicionário `{width, height}`.

```python
size = driver.get_viewport_size()
print(f"Viewport: {size['width']}x{size['height']}")
```
