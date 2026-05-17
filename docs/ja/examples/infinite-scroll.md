# 無限スクロール

無限スクロール読み込みを行うページのスクレイピング例です。

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # 5回スクロールし、スクロール間でコンテンツの読み込みを待機
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # 新しいコンテンツの読み込みを待機
        print(f"スクロール {i+1}/5 完了")

    # 読み込まれたすべての投稿を抽出
    posts = driver.get_all_texts("article.title")
    print(f"\n読み込まれた投稿の総数: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
