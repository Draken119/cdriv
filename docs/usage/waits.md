# Waits

Wait for specific conditions on the page before proceeding.

## `wait_for_element(selector, timeout=10, interval=0.3)`

Waits until an element appears in the DOM.

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("Element found!")
else:
    print("Timeout — element did not appear")
```

### Typical Usage

```python
driver.navigate("https://site.com/products")

# Wait for the list to load
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("Product list did not load")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

Waits until specific text appears on the page.

```python
# Wait for confirmation
if driver.wait_for_text("Order confirmed", timeout=20):
    print("Order confirmed successfully!")
else:
    print("Confirmation timeout")
```

## `wait_for_navigation(timeout=10)`

Waits for the page to finish loading (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("Page loaded!")
```

## `sleep(seconds)`

Pauses for N seconds. Same as `time.sleep()`, but more readable in flow.

```python
driver.sleep(2)  # Wait 2 seconds
```

## Combined Example

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # Wait for dashboard to load
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Welcome", timeout=5)
        print("Login successful!")
    else:
        driver.screenshot("login_error.png")
        print("Login failed")
```
