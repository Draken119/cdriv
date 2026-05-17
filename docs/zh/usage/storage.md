# 存储（localStorage / sessionStorage）

访问和操作浏览器本地存储。

## `get_local_storage(key=None)`

从 `localStorage` 中返回一个值。如果 `key=None`，则返回全部内容。

```python
# 特定值
token = driver.get_local_storage("token")
print(token)

# 全部内容
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

在 `localStorage` 中设置一个值。

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "en-US"}')
```

## `get_session_storage(key=None)`

从 `sessionStorage` 中返回一个值。如果 `key=None`，则返回全部内容。

```python
# 特定值
session_id = driver.get_session_storage("session_id")

# 全部内容
all_data = driver.get_session_storage()
```

## 示例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # 从 localStorage 读取认证令牌
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"找到令牌：{token[:20]}...")
    else:
        print("用户未认证")
        driver.set_local_storage("auth_token", "new_token")
```
