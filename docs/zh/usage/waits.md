# 等待

在继续操作前等待页面上的特定条件。

## `wait_for_element(selector, timeout=10, interval=0.3)`

等待直到元素出现在 DOM 中。

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("找到元素！")
else:
    print("超时 —— 元素未出现")
```

### 典型用法

```python
driver.navigate("https://site.com/products")

# 等待列表加载
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("产品列表未加载")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

等待直到指定文本出现在页面上。

```python
# 等待确认
if driver.wait_for_text("Order confirmed", timeout=20):
    print("订单确认成功！")
else:
    print("确认超时")
```

## `wait_for_navigation(timeout=10)`

等待页面完成加载（`document.readyState === 'complete'`）。

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("页面已加载！")
```

## `sleep(seconds)`

暂停 N 秒。与 `time.sleep()` 功能相同，但在流程中更易读。

```python
driver.sleep(2)  # 等待 2 秒
```

## 组合示例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # 等待仪表盘加载
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Welcome", timeout=5)
        print("登录成功！")
    else:
        driver.screenshot("login_error.png")
        print("登录失败")
```
