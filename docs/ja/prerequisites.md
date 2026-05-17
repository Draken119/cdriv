# 前提条件

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "バージョンの互換性"
    Termux では、`chromium-browser` と `chromedriver` は **同じバージョンである必要があります**。
    常に両方を一緒にアップグレードしてください:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## バイナリの確認

両方のバイナリが利用可能であることを確認します:

```bash
which chromedriver
which chromium-browser
```

バージョンを確認します:

```bash
chromedriver --version
chromium-browser --version
```

## 次のステップ

それでは、[クイックスタートガイド](usage/quickstart.md) に進んで cdriv を使い始めましょう。
