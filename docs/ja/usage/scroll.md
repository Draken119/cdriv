# スクロール

ページをスクロールするためのメソッドです。

## `scroll_to(x=0, y=0)`

ページを特定の位置にスクロールします。

```python
driver.scroll_to(0, 500)   # 500px 下にスクロール
driver.scroll_to(0, 0)     # 先頭に戻る
driver.scroll_to(200, 300) # 200px 右、300px 下
```

## `scroll_to_bottom()`

ページの一番下までスクロールします。

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

要素が表示されるまでスクロールします (画面中央に配置)。

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## 例: 無限スクロール

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5回スクロール
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"読み込まれた投稿数: {len(posts)}")
```
