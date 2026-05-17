# Troubleshooting

## ChromeDriver Won't Start

Verify that the required binaries are installed:

```bash
which chromedriver
which chromium-browser
```

Check versions:

```bash
chromedriver --version
chromium-browser --version
```

If not installed:

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## Session Creation Fails

On Termux, `chromium-browser` and `chromedriver` **must be the same version**.
Upgrade both:

```bash
pkg upgrade chromium-browser chromedriver
```

## Port Already in Use

If port 9515 is occupied, use a different port:

```python
driver = CDriv(port=9516)
```

## Sandbox Permission Errors

`CDriv` starts with `--no-sandbox` by default, which is required on Termux
and containers. If you still get errors, confirm chromium was installed correctly.

## 5 Common Errors

| Error | Cause | Solution |
|-------|-------|----------|
| `ChromeDriver did not start in time` | chromedriver not found or port busy | Install chromedriver, change port |
| `No active session` | Forgot to call `new_session()` | Call `driver.new_session()` before navigating |
| `Failed to create session` | Chromium not found or version mismatch | Install chromium-browser or provide the path |
| Timeout | Slow page | Increase timeout or use `wait_for_navigation()` |
| Connection error | ChromeDriver not running | Call `driver.start()` or use `with CDriv()` |

## Debugging

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Capture screenshot on error
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"Error: {e}")
```
