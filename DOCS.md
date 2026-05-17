# cdriv Documentation

Python library for controlling Chromium via ChromeDriver on **Termux** (Android aarch64).
A direct alternative to Playwright and Selenium, which **do not work** on Android/aarch64.

## Index

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Complete API](#complete-api)
  - [ChromeDriver Management](#chromedriver-management)
  - [Browser Session](#browser-session)
  - [Navigation](#navigation)
  - [Data Extraction](#data-extraction)
  - [Cookies](#cookies)
  - [JavaScript](#javascript)
  - [Element Interaction](#element-interaction)
  - [Scroll](#scroll)
  - [Waits](#waits)
  - [Screenshot](#screenshot)
  - [Storage (localStorage / sessionStorage)](#storage-localstorage--sessionstorage)
  - [Utilities](#utilities)
- [Practical Examples](#practical-examples)
- [Troubleshooting](#troubleshooting)

---

## Installation

```bash
pip install cdriv
```

### Prerequisites (Termux)

```bash
pkg update
pkg install chromium-browser chromedriver
```

### Prerequisites (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

---

## Quick Start

### Context Manager (recommended)

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")
    html = driver.get_page_source()
    print(driver.get_title())
```

### Manual Management

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")
# ... do what you need ...
driver.close()
driver.stop()
```

---

## Complete API

### ChromeDriver Management

#### `CDriv(port=9515, chromedriver_path=None, chromium_path=None)`

Constructor. Initializes the controller.

| Parameter | Default | Description |
|-----------|---------|-------------|
| `port` | `9515` | ChromeDriver HTTP port |
| `chromedriver_path` | `None` (auto-detect) | Path to chromedriver binary |
| `chromium_path` | `None` (auto-detect) | Path to chromium-browser binary |

```python
driver = CDriv(port=9515)
driver = CDriv(chromedriver_path="/usr/bin/chromedriver")
```

#### `start()`

Starts the ChromeDriver process. Waits until it responds on the configured port.
Returns `self` for method chaining.

```python
driver.start()
```

#### `stop()`

Stops the ChromeDriver process. Unregisters the `atexit` handler.

```python
driver.stop()
```

#### `restart()`

Restarts the ChromeDriver (stop + start).

```python
driver.restart()
```

---

### Browser Session

#### `new_session()`

Opens a new Chromium window (creates a WebDriver session). Returns the `sessionId`.

The browser starts in **headless** mode with the following automatic settings:
- Window size: 1920x1080
- User-Agent: Chrome 146 (Linux x86_64)
- Automation detection disabled
- No-sandbox, disable-dev-shm-usage (required for Termux/containers)

```python
session_id = driver.new_session()
```

#### `close()`

Closes the current session (closes the browser).

```python
driver.close()
```

---

### Navigation

| Method | Description |
|--------|-------------|
| `navigate(url)` | Navigate to a URL |
| `get_current_url()` | Return the current URL |
| `back()` | Go to previous page |
| `forward()` | Go to next page |
| `refresh()` | Reload the current page |

```python
driver.navigate("https://site.com")
print(driver.get_current_url())
driver.back()
driver.forward()
driver.refresh()
```

---

### Data Extraction

#### `get_page_source()`

Returns the **full** page HTML as a string.

```python
html = driver.get_page_source()
```

#### `get_title()`

Returns the page title (content of the `<title>` tag).

```python
title = driver.get_title()
```

---

### Cookies

#### `get_cookies()`

Returns the raw list of cookies. Each cookie is a dictionary with keys:
`name`, `value`, `domain`, `path`, `secure`, `httpOnly`, etc.

```python
cookies = driver.get_cookies()
for c in cookies:
    print(c['name'], c['value'])
```

#### `get_cookies_dict()`

Returns cookies as `{name: value}` dictionary — ideal for use with `requests.Session()`.

```python
import requests

session = requests.Session()
session.cookies.update(driver.get_cookies_dict())
resp = session.get("https://site.com/api/data")
print(resp.json())
```

#### `add_cookie(name, value, domain=None, path="/")`

Adds a cookie manually to the session.

```python
driver.add_cookie("token", "abc123", domain=".site.com")
```

#### `delete_all_cookies()`

Removes all cookies from the session.

```python
driver.delete_all_cookies()
```

---

### JavaScript

#### `execute_script(script, *args)`

Executes JavaScript on the page and returns the result.

```python
# Read data
title = driver.execute_script("return document.title")
text = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# Manipulate the page
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# With arguments
driver.execute_script("arguments[0].scrollIntoView()", element)
```

---

### Element Interaction

#### `click(selector)`

Clicks an element via CSS selector.

```python
driver.click("button#submit")
driver.click("a.login-link")
driver.click(".btn-primary")
```

#### `fill(selector, value)`

Fills an input field. Fires `input` and `change` events.

```python
driver.fill("input#email", "user@email.com")
driver.fill("textarea#message", "Hello, world!")
```

#### `get_text(selector)`

Returns the visible text of an element.

```python
name = driver.get_text("h1.title")
price = driver.get_text(".product-price")
```

#### `get_attribute(selector, attr)`

Returns the value of an element attribute.

```python
href = driver.get_attribute("a.link", "href")
src = driver.get_attribute("img#photo", "src")
```

#### `get_all_texts(selector)`

Returns a list of the inner text of **all** elements matching the selector.

```python
items = driver.get_all_texts("li.item")
# ["Item 1", "Item 2", "Item 3"]
```

#### `get_all_attributes(selector, attr)`

Returns a list of attribute values from multiple elements.

```python
links = driver.get_all_attributes("a", "href")
# ["https://...", "https://...", ...]
images = driver.get_all_attributes("img", "src")
```

#### `select_option(selector, value)`

Selects an option in a `<select>` element.

```python
driver.select_option("select#country", "BR")
driver.select_option("select#category", "technology")
```

---

### Scroll

#### `scroll_to(x=0, y=0)`

Scrolls the page to a specific position.

```python
driver.scroll_to(0, 500)  # Scroll 500px down
```

#### `scroll_to_bottom()`

Scrolls to the bottom of the page.

```python
driver.scroll_to_bottom()
```

#### `scroll_to_element(selector)`

Scrolls until the element is visible (centered on screen).

```python
driver.scroll_to_element("#results")
```

---

### Waits

#### `wait_for_element(selector, timeout=10, interval=0.3)`

Waits until an element appears in the DOM. Returns `True` if found, `False` on timeout.

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("Element found!")
else:
    print("Timeout — element did not appear")
```

#### `wait_for_text(text, timeout=10, interval=0.5)`

Waits until text appears on the page.

```python
if driver.wait_for_text("Order confirmed", timeout=20):
    print("Order confirmed!")
```

#### `wait_for_navigation(timeout=10)`

Waits for the page to finish loading (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
```

#### `sleep(seconds)`

Pauses for N seconds. Same as `time.sleep()`, but more readable in context.

```python
driver.sleep(2)  # Wait 2 seconds
```

---

### Screenshot

#### `screenshot(filepath="screenshot.png")`

Takes a page screenshot and saves it to a file. Returns the file path.

```python
driver.screenshot("page.png")
```

#### `screenshot_as_base64()`

Returns the screenshot as a base64 string (without saving to a file).

```python
img_b64 = driver.screenshot_as_base64()
```

---

### Storage (localStorage / sessionStorage)

#### `get_local_storage(key=None)`

Returns a value from `localStorage`. If `key=None`, returns everything as a JSON string.

```python
driver.get_local_storage("token")       # specific value
driver.get_local_storage()              # everything
```

#### `set_local_storage(key, value)`

Sets a value in `localStorage`.

```python
driver.set_local_storage("theme", "dark")
driver.set_local_storage("token", "abc123")
```

#### `get_session_storage(key=None)`

Returns a value from `sessionStorage`. If `key=None`, returns everything.

```python
driver.get_session_storage("session_id")
driver.get_session_storage()
```

---

### Utilities

#### `get_user_agent()`

Returns the browser's User-Agent string.

```python
ua = driver.get_user_agent()
```

#### `get_viewport_size()`

Returns the viewport size as `{width, height}` dictionary.

```python
size = driver.get_viewport_size()
print(f"{size['width']}x{size['height']}")
```

---

## Practical Examples

### 1. Login + Extract Cookies for API

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Fill in form
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Wait for redirect
    driver.wait_for_navigation()

    # Get cookies and make authenticated request
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    data = session.get("https://site.com/api/data").json()
    print(data)
```

### 2. Multi-page Scraping

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    for url in ["https://site.com/page1", "https://site.com/page2", "https://site.com/page3"]:
        driver.navigate(url)
        driver.wait_for_element(".content", timeout=10)

        title = driver.get_text("h1")
        text = driver.get_text(".content")
        links = driver.get_all_attributes("a", "href")

        print(f"=== {title} ===")
        print(f"Links: {len(links)} found")
```

### 3. Infinite Scroll (Paginated Loading)

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 scrolls
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"Posts loaded: {len(posts)}")
```

### 4. Screenshots for Debugging

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

---

## Troubleshooting

### ChromeDriver Won't Start

```bash
# Check if binaries are installed
which chromedriver
which chromium-browser

# Check versions
chromedriver --version
chromium-browser --version
```

If not installed:
```bash
pkg install chromium-browser chromedriver
```

### Session Won't Create / Browser Won't Open

On Termux, `chromium-browser` and `chromedriver` must be the **same version**. Upgrade both:

```bash
pkg upgrade chromium-browser chromedriver
```

### Port Already in Use

If port 9515 is occupied, use a different port:

```python
driver = CDriv(port=9516)
```

### Sandbox Permission Errors

`CDriv` starts with `--no-sandbox` by default, which is required on Termux
and containers. If you still get errors, confirm chromium was installed correctly.
