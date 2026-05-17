# Устранение неполадок

## ChromeDriver не запускается

Проверьте, что необходимые бинарные файлы установлены:

```bash
which chromedriver
which chromium-browser
```

Проверьте версии:

```bash
chromedriver --version
chromium-browser --version
```

Если не установлены:

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## Не удаётся создать сессию

В Termux `chromium-browser` и `chromedriver` **должны быть одной версии**.
Обновите оба:

```bash
pkg upgrade chromium-browser chromedriver
```

## Порт уже занят

Если порт 9515 занят, используйте другой порт:

```python
driver = CDriv(port=9516)
```

## Ошибки прав доступа Sandbox

`CDriv` запускается с флагом `--no-sandbox` по умолчанию, что требуется в Termux
и контейнерах. Если ошибки всё ещё возникают, убедитесь, что chromium установлен правильно.

## 5 частых ошибок

| Ошибка | Причина | Решение |
|--------|---------|---------|
| `ChromeDriver did not start in time` | chromedriver не найден или порт занят | Установите chromedriver, измените порт |
| `No active session` | Забыли вызвать `new_session()` | Вызовите `driver.new_session()` перед навигацией |
| `Failed to create session` | Chromium не найден или несовпадение версий | Установите chromium-browser или укажите путь |
| Timeout | Медленная страница | Увеличьте таймаут или используйте `wait_for_navigation()` |
| Connection error | ChromeDriver не запущен | Вызовите `driver.start()` или используйте `with CDriv()` |

## Отладка

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Сделать скриншот при ошибке
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"Ошибка: {e}")
```
