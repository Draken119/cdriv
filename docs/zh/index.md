# cdriv

**在 Termux (Android aarch64) 上通过 ChromeDriver 控制 Chromium。**

这是 **Playwright** 和 **Selenium** 的直接替代方案——它们在 Android aarch64 上**无法运行**。该库通过 HTTP WebDriver 协议与 ChromeDriver 通信，以无头模式控制 Chromium，专为 Termux 构建。

<div class="grid cards" markdown="1">

-   :material-rocket-launch:{ .lg .middle } **轻量且快速**

---

单一依赖：`requests`。没有沉重框架，没有容器，没有不必要的复杂性。

-   :material-cellphone:{ .lg .middle } **专为 Termux 构建**

---

在 Android aarch64 上原生运行。使用 `pkg install` 安装即可。

-   :material-cookie:{ .lg .middle } **API 就绪的 Cookie**

---

以字典形式提取 Cookie —— 可直接与 `requests.Session()` 一起使用。

-   :material-language-python:{ .lg .middle } **直观的 API**

---

清晰、描述性强的方法。学习曲线极小。

</div>

## 快速安装

```bash
pip install cdriv
```

详细说明请参阅[安装指南](installation.md)。

## 快速开始

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

## 文档

| 章节 | 描述 |
|---------|-------------|
| [安装](installation.md) | 库及依赖安装 |
| [快速入门](usage/quickstart.md) | 从这里开始 |
| [实用示例](examples/login.md) | 真实世界用例 |
| [API 参考](api/cdriv.md) | 完整 API 文档 |
| [故障排除](troubleshooting.md) | 常见问题及解决方案 |

## 许可证

MIT
