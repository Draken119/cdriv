# 工具方法

## `get_user_agent()`

返回浏览器的 User-Agent 字符串。

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

以 `{width, height}` 字典形式返回视口大小。

```python
size = driver.get_viewport_size()
print(f"视口: {size['width']}x{size['height']}")
```
