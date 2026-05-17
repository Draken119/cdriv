# Data Extraction

Methods for extracting information from the page.

## `get_page_source()`

Returns the **full** page HTML as a string.

```python
html = driver.get_page_source()

# Save to file
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# Parse with BeautifulSoup
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup is optional"
    `cdriv` does not depend on BeautifulSoup. Install separately if needed:
    `pip install beautifulsoup4`

## `get_title()`

Returns the page title (content of the `<title>` tag).

```python
title = driver.get_title()
print(f"Page: {title}")
```

## Example

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"Title: {title}")
    print(f"HTML size: {len(html)} characters")
```
