# クッキー

ブラウザセッションのクッキーを管理します。

## `get_cookies()`

クッキーの生のリストを返します。各クッキーは以下のキーを持つ辞書です:
`name`、`value`、`domain`、`path`、`secure`、`httpOnly` など。

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (domain: {c['domain']})")
```

## `get_cookies_dict()`

クッキーを `{name: value}` 辞書として返します — `requests.Session()` との使用に最適です。

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### 典型的なユースケース: 認証済みリクエスト

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # ログイン
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # 認証済みクッキーを再利用
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # 認証済みリクエストを実行
    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

手動でクッキーをセッションに追加します。

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

セッションからすべてのクッキーを削除します。

```python
driver.delete_all_cookies()
```
