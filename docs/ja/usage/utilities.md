# ユーティリティ

## `get_user_agent()`

ブラウザの User-Agent 文字列を返します。

```python
ua = driver.get_user_agent()
print(f"User-Agent: {ua}")
```

## `get_viewport_size()`

ビューポートサイズを `{width, height}` 辞書として返します。

```python
size = driver.get_viewport_size()
print(f"ビューポート: {size['width']}x{size['height']}")
```
