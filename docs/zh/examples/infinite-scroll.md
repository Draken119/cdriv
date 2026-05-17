# 无限滚动

抓取具有无限滚动加载功能的页面的示例。

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # 滚动 5 次，每次等待内容加载
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # 等待新内容加载
        print(f"滚动 {i+1}/5 完成")

    # 提取所有已加载的文章
    posts = driver.get_all_texts("article.title")
    print(f"\n总共加载文章数：{len(posts)}")
    for post in posts:
        print(f"- {post}")
```
