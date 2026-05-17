# 快速入门

## 上下文管理器（推荐）

使用 `CDriv` 最安全、最便捷的方式：

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

`with` 语句保证了 ChromeDriver 正确启动和停止，即使发生异常也是如此。

## 手动管理

如需完全控制生命周期：

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... 你的代码在这里 ...

driver.close()
driver.stop()
```

## 配置

### 自定义端口

```python
driver = CDriv(port=9516)
```

### 自定义二进制路径

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## 典型脚本结构

1. 创建 `CDriv` 实例
2. 使用 `new_session()` 启动会话
3. 导航到目标 URL
4. 与页面交互
5. 提取所需数据
6. 关闭会话

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. 创建并启动
    driver.new_session()       # 2. 打开浏览器
    driver.navigate("...")     # 3. 导航
    driver.fill("#field", "x") # 4. 交互
    data = driver.get_text("#result")  # 5. 提取
    print(data)
# 6. 自动清理
```
