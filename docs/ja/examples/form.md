# フォーム自動化

フォームに自動的に入力して送信する例です。

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # フォームの読み込みを待機
    driver.wait_for_element("form#registration", timeout=10)

    # フィールドに入力
    driver.fill("input#name", "John Doe")
    driver.fill("input#email", "john@email.com")
    driver.fill("input#phone", "+1 (555) 123-4567")
    driver.fill("textarea#message", "Hello, I would like more information.")

    # オプションを選択
    driver.select_option("select#country", "US")
    driver.select_option("select#category", "support")

    # 利用規約にチェック
    driver.click("input#accept-terms")

    # フォームを送信
    driver.click("button[type='submit']")

    # 確認を待機
    if driver.wait_for_text("Registration successful", timeout=15):
        print("フォームが正常に送信されました!")
        print(driver.get_text(".success-message"))
    else:
        print("フォーム送信エラー")
        driver.screenshot("form_error.png")
```
