# マルチページスクレイピング

複数のページを順番にスクレイピングする例です。

```python
from cdriv import CDriv

urls = [
    "https://site.com/page1",
    "https://site.com/page2",
    "https://site.com/page3",
]

with CDriv() as driver:
    driver.new_session()

    for url in urls:
        driver.navigate(url)
        driver.wait_for_element(".content", timeout=10)

        title = driver.get_text("h1")
        text = driver.get_text(".content")
        links = driver.get_all_attributes("a", "href")

        print(f"=== {title} ===")
        print(f"テキスト: {text[:100]}...")
        print(f"リンク: {len(links)} 個見つかりました")
        print()
```
