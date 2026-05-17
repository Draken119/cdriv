# Utilities

## `get_user_agent()`

Returns the browser's User-Agent string.

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

Returns the viewport size as a `{width, height}` dictionary.

```python
size = driver.get_viewport_size()
print(f"Viewport: {size['width']}x{size['height']}")
```
