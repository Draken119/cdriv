# About

## What is cdriv?

**cdriv** is a Python library for controlling Chromium via ChromeDriver on
**Termux** (Android aarch64). It was created because **Playwright** and
**Selenium** simply **do not work** on Android aarch64.

Instead of relying on heavy frameworks that require containers or specific
runtimes, `cdriv` communicates directly with ChromeDriver through the HTTP
WebDriver protocol. The result is a lightweight library with a single
dependency: `requests`.

## Why cdriv?

- :material-cellphone: **Works on Termux** — unlike Playwright and Selenium
- :material-feather: **Lightweight** — single dependency: `requests`
- :material-bolt: **Simple** — clean, descriptive API
- :material-test-tube: **Production-tested** — actively used on Termux

## License

MIT — use, modify, and distribute freely.

## Links

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
