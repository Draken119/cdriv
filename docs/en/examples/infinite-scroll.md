# Infinite Scroll

Example of scraping pages with infinite scroll loading.

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # Scroll 5 times, waiting for content to load between each
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # Wait for new content to load
        print(f"Scroll {i+1}/5 complete")

    # Extract all loaded posts
    posts = driver.get_all_texts("article.title")
    print(f"\nTotal posts loaded: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
