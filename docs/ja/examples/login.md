# ログイン + API

ウェブサイトにログインし、API 呼び出しのためにクッキーを再利用する実践的な例です。

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # ログインフォームに入力
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # リダイレクトを待機
    driver.wait_for_navigation()

    # ログイン成功を確認
    if driver.wait_for_element(".dashboard", timeout=5):
        print("ログイン成功!")

        # クッキーを抽出して認証済みセッションを作成
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # 認証済み API 呼び出しを実行
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("ログイン失敗")
        driver.screenshot("login_error.png")
```
