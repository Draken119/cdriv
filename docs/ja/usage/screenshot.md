# スクリーンショット

現在のページのスクリーンショットを撮影します。

## `screenshot(filepath="screenshot.png")`

ページのスクリーンショットを撮影してファイルに保存します。ファイルパスを返します。

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### スクリーンショットを使ったデバッグ

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("エラー要素が見つかりました!")
    except:
        driver.screenshot("error.png")
        print("スクリーンショットを error.png として保存しました")
```

## `screenshot_as_base64()`

スクリーンショットを base64 文字列として返します (ファイルに保存せずに)。

```python
img_b64 = driver.screenshot_as_base64()

# API に送信
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# HTML で表示
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
