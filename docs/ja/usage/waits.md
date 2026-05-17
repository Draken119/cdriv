# 待機

処理を進める前にページ上の特定の条件を待機します。

## `wait_for_element(selector, timeout=10, interval=0.3)`

要素が DOM に現れるまで待機します。

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("要素が見つかりました!")
else:
    print("タイムアウト — 要素が現れませんでした")
```

### 典型的な使用法

```python
driver.navigate("https://site.com/products")

# リストの読み込みを待機
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("商品リストが読み込まれませんでした")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

特定のテキストがページに現れるまで待機します。

```python
# 確認を待機
if driver.wait_for_text("Order confirmed", timeout=20):
    print("注文が正常に確認されました!")
else:
    print("確認のタイムアウト")
```

## `wait_for_navigation(timeout=10)`

ページの読み込みが完了するまで待機します (`document.readyState === 'complete'`)。

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("ページが読み込まれました!")
```

## `sleep(seconds)`

N 秒間一時停止します。`time.sleep()` と同じですが、フロー内でより読みやすくなっています。

```python
driver.sleep(2)  # 2秒待機
```

## 組み合わせ例

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # ダッシュボードの読み込みを待機
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Welcome", timeout=5)
        print("ログイン成功!")
    else:
        driver.screenshot("login_error.png")
        print("ログイン失敗")
```
