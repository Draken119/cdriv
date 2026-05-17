# データ抽出

ページから情報を抽出するためのメソッドです。

## `get_page_source()`

ページの **完全な** HTML を文字列として返します。

```python
html = driver.get_page_source()

# ファイルに保存
with open("page.html", "w", encoding="utf-8") as f:
    f.write(html)

# BeautifulSoup で解析
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
```

!!! tip "BeautifulSoup はオプションです"
    `cdriv` は BeautifulSoup に依存していません。必要に応じて個別にインストールしてください:
    `pip install beautifulsoup4`

## `get_title()`

ページのタイトル (`<title>` タグの内容) を返します。

```python
title = driver.get_title()
print(f"ページ: {title}")
```

## 例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    title = driver.get_title()

    print(f"タイトル: {title}")
    print(f"HTML サイズ: {len(html)} 文字")
```
