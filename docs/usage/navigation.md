# Navigation

Methods for navigating between web pages.

## `navigate(url)`

Navigates to a URL. Waits for the page to load completely.

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

Returns the current page URL.

```python
url = driver.get_current_url()
print(f"You are at: {url}")
```

## `back()`

Goes back to the previous page (like the browser's back button).

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # Returns to page1
```

## `forward()`

Goes forward to the next page (like the browser's forward button).

```python
driver.forward()  # Returns to page2
```

## `refresh()`

Reloads the current page.

```python
driver.refresh()
```

## Complete Example

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # Simulate navigation flow
    driver.navigate("https://site.com/dashboard")
    driver.back()      # Back to login
    driver.forward()   # Forward to dashboard
    driver.refresh()   # Reload dashboard
```
