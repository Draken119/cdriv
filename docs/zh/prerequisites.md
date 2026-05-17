# 先决条件

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "版本兼容性"
    在 Termux 上，`chromium-browser` 和 `chromedriver` **必须是相同版本**。
    请始终同时升级两者：

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## 验证二进制文件

确认两个二进制文件都可用：

```bash
which chromedriver
which chromium-browser
```

检查版本：

```bash
chromedriver --version
chromium-browser --version
```

## 下一步

现在请前往[快速入门指南](usage/quickstart.md)开始使用 cdriv。
