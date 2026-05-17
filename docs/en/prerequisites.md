# Prerequisites

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "Version Compatibility"
    On Termux, `chromium-browser` and `chromedriver` **must be the same version**.
    Always upgrade both together:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Verify Binaries

Confirm both binaries are available:

```bash
which chromedriver
which chromium-browser
```

Check versions:

```bash
chromedriver --version
chromium-browser --version
```

## Next Step

Now head over to the [Quickstart Guide](usage/quickstart.md) to start using cdriv.
