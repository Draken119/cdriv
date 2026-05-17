# 滚动

用于滚动页面的方法。

## `scroll_to(x=0, y=0)`

将页面滚动到指定位置。

```python
driver.scroll_to(0, 500)   # 向下滚动 500px
driver.scroll_to(0, 0)     # 回到顶部
driver.scroll_to(200, 300) # 向右 200px，向下 300px
```

## `scroll_to_bottom()`

滚动到页面底部。

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

滚动直到元素可见（居中显示在屏幕上）。

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## 示例：无限滚动

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 滚动 5 次
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"已加载文章数：{len(posts)}")
```
