# cdriv

**Termux (Android aarch64) 上で ChromeDriver 経由で Chromium を制御します。**

**Playwright** や **Selenium** の直接的な代替手段です。これらは Android aarch64 では **動作しません**。このライブラリは HTTP WebDriver プロトコルを通じて ChromeDriver と通信し、Chromium をヘッドレスモードで制御します。Termux 向けに特別に構築されています。

<div class="grid cards" markdown="1">

-   :material-rocket-launch:{ .lg .middle } **軽量 & 高速**

---

単一の依存関係: `requests`。重いフレームワークもコンテナも不要で、余計な複雑さはありません。

-   :material-cellphone:{ .lg .middle } **Termux 向けに構築**

---

Android aarch64 上でネイティブに動作します。`pkg install` でインストールしてすぐに使用できます。

-   :material-cookie:{ .lg .middle } **API 対応クッキー**

---

クッキーを辞書として抽出し、`requests.Session()` で直接使用できます。

-   :material-language-python:{ .lg .middle } **直感的な API**

---

洗練された明確なメソッド。学習曲線は最小限です。

</div>

## クイックインストール

```bash
pip install cdriv
```

詳細な手順については、[インストールガイド](installation.md) を参照してください。

## クイックスタート

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    title = driver.get_title()

    print(title)
```

## ドキュメント

| セクション | 説明 |
|---------|-------------|
| [インストール](installation.md) | ライブラリと依存関係のインストール |
| [クイックスタート](usage/quickstart.md) | ここから始めてください |
| [実践的な例](examples/login.md) | 実際のユースケース |
| [API リファレンス](api/cdriv.md) | 完全な API ドキュメント |
| [トラブルシューティング](troubleshooting.md) | よくある問題と解決策 |

## ライセンス

MIT
