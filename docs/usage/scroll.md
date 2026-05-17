# Scroll

Methods for scrolling the page.

## `scroll_to(x=0, y=0)`

Scrolls the page to a specific position.

```python
driver.scroll_to(0, 500)   # Scroll 500px down
driver.scroll_to(0, 0)     # Back to top
driver.scroll_to(200, 300) # 200px right, 300px down
```

## `scroll_to_bottom()`

Scrolls to the bottom of the page.

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

Scrolls until the element is visible (centered on screen).

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## Example: Infinite Scroll

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 scrolls
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"Posts loaded: {len(posts)}")
```
