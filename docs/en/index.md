# cdriv

**Control Chromium via ChromeDriver on Termux (Android aarch64).**

A direct alternative to **Playwright** and **Selenium** — which **do not work** on Android aarch64. This library communicates with ChromeDriver through the HTTP WebDriver protocol to control Chromium in headless mode, built specifically for Termux.

<div class="grid cards" markdown="1">

-   :material-rocket-launch:{ .lg .middle } **Lightweight & Fast**

    ---

    Single dependency: `requests`. No heavy frameworks, no containers, no unnecessary complexity.

-   :material-cellphone:{ .lg .middle } **Built for Termux**

    ---

    Runs natively on Android aarch64. Install with `pkg install` and you're ready.

-   :material-cookie:{ .lg .middle } **API-ready Cookies**

    ---

    Extract cookies as a dictionary — use directly with `requests.Session()`.

-   :material-language-python:{ .lg .middle } **Intuitive API**

    ---

    Clean, descriptive methods. Minimal learning curve.

</div>

## Quick Install

```bash
pip install cdriv
```

See the [Installation Guide](installation.md) for detailed instructions.

## Quick Start

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    title = driver.get_title()

    print(title)
```

## Documentation

| Section | Description |
|---------|-------------|
| [Installation](installation.md) | Library and dependency installation |
| [Quickstart](usage/quickstart.md) | Start here |
| [Practical Examples](examples/login.md) | Real-world use cases |
| [API Reference](api/cdriv.md) | Complete API documentation |
| [Troubleshooting](troubleshooting.md) | Common issues and solutions |

## License

MIT
