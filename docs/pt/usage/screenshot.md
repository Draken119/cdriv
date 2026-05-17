# Screenshot

Capturar screenshots da página atual.

## `screenshot(filepath="screenshot.png")`

Tira um screenshot da página e salva em um arquivo. Retorna o caminho do arquivo.

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### Depuração com Screenshots

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("Elemento de erro encontrado!")
    except:
        driver.screenshot("error.png")
        print("Screenshot salvo como error.png")
```

## `screenshot_as_base64()`

Retorna o screenshot como uma string base64 (sem salvar em arquivo).

```python
img_b64 = driver.screenshot_as_base64()

# Enviar para API
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# Exibir em HTML
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
