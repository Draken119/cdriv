# 登录 + API

登录网站并重用 Cookie 进行 API 调用的真实示例。

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # 填写登录表单
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # 等待重定向
    driver.wait_for_navigation()

    # 验证登录是否成功
    if driver.wait_for_element(".dashboard", timeout=5):
        print("登录成功！")

        # 提取 Cookie 并创建认证会话
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # 发起认证 API 调用
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("登录失败")
        driver.screenshot("login_error.png")
```
