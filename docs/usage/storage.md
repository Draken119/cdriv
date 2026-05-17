# Storage (localStorage / sessionStorage)

Access and manipulate browser local storage.

## `get_local_storage(key=None)`

Returns a value from `localStorage`. If `key=None`, returns everything.

```python
# Specific value
token = driver.get_local_storage("token")
print(token)

# Everything
all_data = driver.get_local_storage()
```

## `set_local_storage(key, value)`

Sets a value in `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
driver.set_local_storage("prefs", '{"lang": "en-US"}')
```

## `get_session_storage(key=None)`

Returns a value from `sessionStorage`. If `key=None`, returns everything.

```python
# Specific value
session_id = driver.get_session_storage("session_id")

# Everything
all_data = driver.get_session_storage()
```

## Example

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com")

    # Read auth token from localStorage
    token = driver.get_local_storage("auth_token")

    if token:
        print(f"Token found: {token[:20]}...")
    else:
        print("User not authenticated")
        driver.set_local_storage("auth_token", "new_token")
```
