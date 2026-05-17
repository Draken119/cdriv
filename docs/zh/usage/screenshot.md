# 截图

捕获当前页面的屏幕截图。

## `screenshot(filepath="screenshot.png")`

截取页面截图并保存到文件。返回文件路径。

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### 使用截图进行调试

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("找到错误元素！")
    except:
        driver.screenshot("error.png")
        print("截图已保存为 error.png")
```

## `screenshot_as_base64()`

以 base64 字符串形式返回截图（不保存到文件）。

```python
img_b64 = driver.screenshot_as_base64()

# 发送到 API
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# 在 HTML 中显示
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
