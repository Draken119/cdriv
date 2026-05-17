# Cookies

Manage browser session cookies.

## `get_cookies()`

Returns the raw list of cookies. Each cookie is a dictionary with keys:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(f"{c['name']}: {c['value']} (domain: {c['domain']})")
```

## `get_cookies_dict()`

Returns cookies as a `{name: value}` dictionary — ideal for use with
`requests.Session()`.

```python
cookies = driver.get_cookies_dict()
print(cookies)
# {'sessionid': 'abc123', 'csrftoken': 'xyz789'}
```

### Typical Use Case: Authenticated Requests

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Log in
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")
    driver.wait_for_navigation()

    # Reuse authenticated cookies
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    # Make authenticated requests
    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

## `add_cookie(name, value, domain=None, path="/")`

Adds a cookie manually to the session.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
driver.add_cookie("pref_theme", "dark", path="/")
```

## `delete_all_cookies()`

Removes all cookies from the session.

```python
driver.delete_all_cookies()
```
