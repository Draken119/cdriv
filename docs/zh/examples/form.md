# 表单自动化

自动填写和提交表单的示例。

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # 等待表单加载
    driver.wait_for_element("form#registration", timeout=10)

    # 填写字段
    driver.fill("input#name", "John Doe")
    driver.fill("input#email", "john@email.com")
    driver.fill("input#phone", "+1 (555) 123-4567")
    driver.fill("textarea#message", "Hello, I would like more information.")

    # 选择选项
    driver.select_option("select#country", "US")
    driver.select_option("select#category", "support")

    # 勾选条款
    driver.click("input#accept-terms")

    # 提交表单
    driver.click("button[type='submit']")

    # 等待确认
    if driver.wait_for_text("Registration successful", timeout=15):
        print("表单提交成功！")
        print(driver.get_text(".success-message"))
    else:
        print("表单提交出错")
        driver.screenshot("form_error.png")
```
