# Quickstart

## Context Manager (recommended)

The safest and most convenient way to use `CDriv`:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

The `with` statement guarantees the ChromeDriver starts and stops correctly,
even when exceptions occur.

## Manual Management

For full control over the lifecycle:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... your code here ...

driver.close()
driver.stop()
```

## Configuration

### Custom Port

```python
driver = CDriv(port=9516)
```

### Custom Binary Paths

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## Typical Script Structure

1. Create a `CDriv` instance
2. Start a session with `new_session()`
3. Navigate to the target URL
4. Interact with the page
5. Extract required data
6. Close the session

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. Create & start
    driver.new_session()       # 2. Open browser
    driver.navigate("...")     # 3. Navigate
    driver.fill("#field", "x") # 4. Interact
    data = driver.get_text("#result")  # 5. Extract
    print(data)
# 6. Auto-cleanup
```
