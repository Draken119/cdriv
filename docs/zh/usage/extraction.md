# 数据提取

用于从页面提取信息的方法。

## `get_page_source()`

返回页面的**完整** HTML 字符串。

```python
html = driver.get_page_source()

# 保存到文件
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# 使用 BeautifulSoup 解析
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup 是可选的"
    `cdriv` 不依赖 BeautifulSoup。如需使用，请单独安装：`pip install beautifulsoup4`

## `get_title()`

返回页面标题（`<title>` 标签的内容）。

```python
title = driver.get_title()
print(f"页面: {title}")
```

## 示例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"标题: {title}")
    print(f"HTML 大小: {len(html)} 个字符")
```
