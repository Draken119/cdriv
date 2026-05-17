# 导航

用于在网页之间导航的方法。

## `navigate(url)`

导航到指定 URL。等待页面完全加载。

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

返回当前页面的 URL。

```python
url = driver.get_current_url()
print(f"您当前在: {url}")
```

## `back()`

返回上一个页面（类似于浏览器的后退按钮）。

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # 回到 page1
```

## `forward()`

前进到下一个页面（类似于浏览器的前进按钮）。

```python
driver.forward()  # 回到 page2
```

## `refresh()`

重新加载当前页面。

```python
driver.refresh()
```

## 完整示例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # 模拟导航流程
    driver.navigate("https://site.com/dashboard")
    driver.back()      # 回到登录页
    driver.forward()   # 前进到仪表盘
    driver.refresh()   # 重新加载仪表盘
```
