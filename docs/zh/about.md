# 关于

## 什么是 cdriv？

**cdriv** 是一个用于在 **Termux** (Android aarch64) 上通过 ChromeDriver 控制 Chromium 的 Python 库。它的诞生是因为 **Playwright** 和 **Selenium** 在 Android aarch64 上**无法运行**。

与其依赖需要容器或特定运行时的沉重框架，`cdriv` 直接通过 HTTP WebDriver 协议与 ChromeDriver 通信。最终形成了一个只有单一依赖 `requests` 的轻量级库。

## 为什么选择 cdriv？

- :material-cellphone: **可在 Termux 上运行** —— 与 Playwright 和 Selenium 不同
- :material-feather: **轻量级** —— 单一依赖：`requests`
- :material-bolt: **简单** —— 清晰、描述性强的 API
- :material-test-tube: **经过生产测试** —— 在 Termux 上活跃使用

## 许可证

MIT —— 可自由使用、修改和分发。

## 链接

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
