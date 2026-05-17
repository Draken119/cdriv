# cdriv について

## cdriv とは?

**cdriv** は、**Termux** (Android aarch64) 上で ChromeDriver 経由で Chromium を制御するための Python ライブラリです。**Playwright** や **Selenium** が Android aarch64 では **動作しない** ために作成されました。

コンテナや特定のランタイムを必要とする重いフレームワークに頼る代わりに、`cdriv` は HTTP WebDriver プロトコルを通じて ChromeDriver と直接通信します。その結果、単一の依存関係 `requests` を持つ軽量なライブラリが実現しました。

## cdriv を選ぶ理由

- :material-cellphone: **Termux で動作** — Playwright や Selenium とは異なります
- :material-feather: **軽量** — 単一の依存関係: `requests`
- :material-bolt: **シンプル** — 洗練されたわかりやすい API
- :material-test-tube: **本番環境でテスト済み** — Termux で積極的に使用されています

## ライセンス

MIT — 自由に使用、修正、配布できます。

## リンク

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
