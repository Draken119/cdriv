# クイックスタート

## コンテキストマネージャ (推奨)

`CDriv` を使用する最も安全で便利な方法:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

`with` 文は、例外が発生した場合でも、ChromeDriver が正しく起動および停止することを保証します。

## 手動管理

ライフサイクルを完全に制御したい場合:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... ここにコードを記述 ...

driver.close()
driver.stop()
```

## 設定

### カスタムポート

```python
driver = CDriv(port=9516)
```

### カスタムバイナリパス

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## 典型的なスクリプト構成

1. `CDriv` インスタンスを作成する
2. `new_session()` でセッションを開始する
3. 対象の URL に移動する
4. ページと対話する
5. 必要なデータを抽出する
6. セッションを閉じる

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. 作成 & 起動
    driver.new_session()       # 2. ブラウザを開く
    driver.navigate("...")     # 3. 移動
    driver.fill("#field", "x") # 4. 対話
    data = driver.get_text("#result")  # 5. 抽出
    print(data)
# 6. 自動クリーンアップ
```
