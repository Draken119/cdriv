# Utilidades

## `get_user_agent()`

Devuelve la cadena User-Agent del navegador.

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

Devuelve el tamaño del viewport como un diccionario `{width, height}`.

```python
size = driver.get_viewport_size()
print(f"Viewport: {size['width']}x{size['height']}")
```
