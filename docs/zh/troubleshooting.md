# 故障排除

## ChromeDriver 无法启动

验证所需的二进制文件是否已安装：

```bash
which chromedriver
which chromium-browser
```

检查版本：

```bash
chromedriver --version
chromium-browser --version
```

如果未安装：

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## 会话创建失败

在 Termux 上，`chromium-browser` 和 `chromedriver` **必须是相同版本**。
请升级两者：

```bash
pkg upgrade chromium-browser chromedriver
```

## 端口已被占用

如果端口 9515 已被占用，请使用其他端口：

```python
driver = CDriv(port=9516)
```

## 沙箱权限错误

`CDriv` 默认以 `--no-sandbox` 参数启动，这在 Termux 和容器中是必需的。
如果仍然遇到错误，请确认 chromium 已正确安装。

## 5 个常见错误

| 错误 | 原因 | 解决方法 |
|-------|-------|----------|
| `ChromeDriver did not start in time` | 找不到 chromedriver 或端口被占用 | 安装 chromedriver，更换端口 |
| `No active session` | 忘记调用 `new_session()` | 在导航前调用 `driver.new_session()` |
| `Failed to create session` | 找不到 Chromium 或版本不匹配 | 安装 chromium-browser 或提供路径 |
| 超时 | 页面加载缓慢 | 增加超时时间或使用 `wait_for_navigation()` |
| 连接错误 | ChromeDriver 未运行 | 调用 `driver.start()` 或使用 `with CDriv()` |

## 调试

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# 在出错时截取屏幕截图
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"错误: {e}")
```
