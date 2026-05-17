# トラブルシューティング

## ChromeDriver が起動しない

必要なバイナリがインストールされていることを確認します:

```bash
which chromedriver
which chromium-browser
```

バージョンを確認します:

```bash
chromedriver --version
chromium-browser --version
```

インストールされていない場合:

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## セッションの作成に失敗する

Termux では、`chromium-browser` と `chromedriver` は **同じバージョンである必要があります**。
両方をアップグレードしてください:

```bash
pkg upgrade chromium-browser chromedriver
```

## ポートが既に使用されている

ポート 9515 が占有されている場合は、別のポートを使用します:

```python
driver = CDriv(port=9516)
```

## サンドボックスの権限エラー

`CDriv` はデフォルトで `--no-sandbox` を指定して起動します。これは Termux およびコンテナ環境で必要です。
それでもエラーが発生する場合は、chromium が正しくインストールされていることを確認してください。

## 5 つのよくあるエラー

| エラー | 原因 | 解決策 |
|-------|-------|----------|
| `ChromeDriver did not start in time` | chromedriver が見つからない、またはポートがビジー状態 | chromedriver をインストールする、ポートを変更する |
| `No active session` | `new_session()` の呼び出し忘れ | ナビゲーション前に `driver.new_session()` を呼び出す |
| `Failed to create session` | Chromium が見つからない、またはバージョンの不一致 | chromium-browser をインストールする、またはパスを指定する |
| タイムアウト | ページの読み込みが遅い | タイムアウトを増やす、または `wait_for_navigation()` を使用する |
| 接続エラー | ChromeDriver が実行されていない | `driver.start()` を呼び出す、または `with CDriv()` を使用する |

## デバッグ

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# エラー時にスクリーンショットを撮影
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"Error: {e}")
```
