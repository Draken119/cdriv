# Скриншот

Создание снимков экрана текущей страницы.

## `screenshot(filepath="screenshot.png")`

Делает скриншот страницы и сохраняет его в файл. Возвращает путь к файлу.

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### Отладка с помощью скриншотов

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("Элемент ошибки найден!")
    except:
        driver.screenshot("error.png")
        print("Скриншот сохранён как error.png")
```

## `screenshot_as_base64()`

Возвращает скриншот в виде base64-строки (без сохранения в файл).

```python
img_b64 = driver.screenshot_as_base64()

# Отправка в API
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# Отображение в HTML
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
