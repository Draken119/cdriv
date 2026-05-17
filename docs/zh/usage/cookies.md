# Cookies

管理浏览器会话 Cookie。

## `get_cookies()`

返回原始的 Cookie 列表。每个 Cookie 是一个包含以下键的字典：`name`、`value`、`domain`、`path`、`secure`、`httpOnly` 等。

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (域名: {c['domain']})")
```

## `get_cookies_dict()`

以 `{name: value}` 字典形式返回 Cookie —— 非常适合与 `requests.Session()` 一起使用。

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### 典型用例：认证请求

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # 登录
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # 重用已认证的 Cookie
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # 发起已认证的请求
    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

手动向会话添加一个 Cookie。

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

删除会话中的所有 Cookie。

```python
driver.delete_all_cookies()
```
