# ストレージ (localStorage / sessionStorage)

ブラウザのローカルストレージにアクセスして操作します。

## `get_local_storage(key=None)`

`localStorage` から値を返します。`key=None` の場合はすべてを返します。

```python
# 特定の値
token = driver.get_local_storage("token")
print(token)

# すべて
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

`localStorage` に値を設定します。

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "en-US"}')
```

## `get_session_storage(key=None)`

`sessionStorage` から値を返します。`key=None` の場合はすべてを返します。

```python
# 特定の値
session_id = driver.get_session_storage("session_id")

# すべて
all_data = driver.get_session_storage()
```

## 例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # localStorage から認証トークンを読み取り
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"トークンが見つかりました: {token[:20]}...")
    else:
        print("ユーザーは認証されていません")
        driver.set_local_storage("auth_token", "new_token")
```
