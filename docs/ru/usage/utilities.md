# Утилиты

## `get_user_agent()`

Возвращает строку User-Agent браузера.

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

Возвращает размер области просмотра в виде словаря `{width, height}`.

```python
size = driver.get_viewport_size()
print(f"Область просмотра: {size['width']}x{size['height']}")
```
