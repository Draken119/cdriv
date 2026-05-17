# Screenshot

Capture screenshots of the current page.

## `screenshot(filepath="screenshot.png")`

Takes a screenshot of the page and saves it to a file. Returns the file path.

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### Debugging with Screenshots

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("Error element found!")
    except:
        driver.screenshot("error.png")
        print("Screenshot saved as error.png")
```

## `screenshot_as_base64()`

Returns the screenshot as a base64 string (without saving to a file).

```python
img_b64 = driver.screenshot_as_base64()

# Send to API
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# Display in HTML
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
