# ナビゲーション

ウェブページ間を移動するためのメソッドです。

## `navigate(url)`

URL に移動します。ページが完全に読み込まれるまで待機します。

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

現在のページの URL を返します。

```python
url = driver.get_current_url()
print(f"現在のURL: {url}")
```

## `back()`

前のページに戻ります (ブラウザの戻るボタンと同様)。

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # page1 に戻る
```

## `forward()`

次のページに進みます (ブラウザの進むボタンと同様)。

```python
driver.forward()  # page2 に進む
```

## `refresh()`

現在のページを再読み込みします。

```python
driver.refresh()
```

## 完全な例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # ナビゲーションフローのシミュレーション
    driver.navigate("https://site.com/dashboard")
    driver.back()      # ログインページに戻る
    driver.forward()   # ダッシュボードに進む
    driver.refresh()   # ダッシュボードを再読み込み
```
