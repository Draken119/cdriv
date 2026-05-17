<div align="center">

# cdriv

**Control Chromium via ChromeDriver on Termux (Android aarch64).**

[![PyPI version](https://img.shields.io/pypi/v/cdriv?color=teal&style=flat-square)](https://pypi.org/project/cdriv/)
[![PyPI downloads](https://img.shields.io/pypi/dm/cdriv?color=teal&style=flat-square)](https://pypi.org/project/cdriv/)
[![Python versions](https://img.shields.io/pypi/pyversions/cdriv?color=teal&style=flat-square)](https://pypi.org/project/cdriv/)
[![License](https://img.shields.io/github/license/Draken119/cdriv?color=teal&style=flat-square)](LICENSE)
[![Documentation](https://img.shields.io/badge/docs-GitHub%20Pages-teal?style=flat-square)](https://draken119.github.io/cdriv/)
[![GitHub stars](https://img.shields.io/github/stars/Draken119/cdriv?style=flat-square&color=teal)](https://github.com/Draken119/cdriv/stargazers)

</div>

---

A direct alternative to **Playwright** and **Selenium** — which **do not work** on Android aarch64. `cdriv` communicates with ChromeDriver through the HTTP WebDriver protocol to control Chromium in headless mode, designed and tested specifically for **Termux**.

No containers, no heavy frameworks, no runtime dependencies. Just Python, HTTP, and a running ChromeDriver.

---

## Features

| | Feature | Description |
|---|---|---|
| :rocket: | **Lightweight** | Single dependency: `requests`. No Playwright, no Selenium, no containers. |
| :iphone: | **Termux-native** | Works on Android aarch64 where Playwright/Selenium fail. |
| :cookie: | **Cookie extraction** | Get cookies as a plain dict — ready for `requests.Session()`. |
| :camera: | **Screenshots** | Capture page screenshots, including as base64. |
| :mouse: | **Element interaction** | Click, fill, select — all via CSS selectors. |
| :scroll: | **JavaScript execution** | Run arbitrary JS and get results back. |
| :arrows_counterclockwise: | **Navigation control** | Navigate, back, forward, refresh. |
| :mag: | **Waits** | Wait for elements, text, or page load. |
| :floppy_disk: | **Storage access** | Read/write localStorage and sessionStorage. |

---

## Installation

```bash
pip install cdriv
```

### Prerequisites (Termux)

```bash
pkg update && pkg install chromium-browser chromedriver
```

### Prerequisites (Linux)

```bash
sudo apt update && sudo apt install chromium-browser chromium-chromedriver
```

---

## Quick Start

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    title = driver.get_title()

    print(f"Title: {title}")
```

### Authenticated Requests

```python
import requests
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Reuse authenticated cookies
    session = requests.Session()
    session.cookies.update(driver.get_cookies_dict())

    resp = session.get("https://site.com/api/data")
    print(resp.json())
```

---

## API Overview

| Method | Description |
|--------|-------------|
| `start()` / `stop()` | Start/stop the ChromeDriver process |
| `new_session()` / `close()` | Open/close a Chromium window |
| `navigate(url)` | Navigate to a URL |
| `get_page_source()` | Get the full page HTML |
| `get_cookies_dict()` | Get cookies as `{name: value}` dict |
| `execute_script(js)` | Execute JavaScript on the page |
| `click(selector)` | Click an element by CSS selector |
| `fill(selector, value)` | Fill an input field |
| `get_text(selector)` | Get the visible text of an element |
| `get_attribute(selector, attr)` | Get an element attribute |
| `screenshot(path)` | Take a page screenshot |
| `wait_for_element(selector)` | Wait for an element to appear |
| `scroll_to_bottom()` | Scroll to the bottom of the page |

---

## Documentation

Full documentation is available at **[draken119.github.io/cdriv](https://draken119.github.io/cdriv/)** with:

- :book: Complete [API Reference](https://draken119.github.io/cdriv/api/cdriv/)
- :bulb: [Practical Examples](https://draken119.github.io/cdriv/examples/login/) (login, scraping, price monitoring, forms)
- :wrench: [Troubleshooting Guide](https://draken119.github.io/cdriv/troubleshooting/)
- :memo: [Installation & Prerequisites](https://draken119.github.io/cdriv/installation/)

---

<div align="center">

## License

[MIT](LICENSE) &copy; 2026 Draken119

[![Documentation](https://img.shields.io/badge/docs-draken119.github.io/cdriv-0d0d0d?style=for-the-badge&logo=materialformkdocs&logoColor=white)](https://draken119.github.io/cdriv/)
[![PyPI](https://img.shields.io/badge/PyPI-cdriv-0d0d0d?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/cdriv/)
[![GitHub](https://img.shields.io/badge/source-Draken119/cdriv-0d0d0d?style=for-the-badge&logo=github&logoColor=white)](https://github.com/Draken119/cdriv)

</div>
