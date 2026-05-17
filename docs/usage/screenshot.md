# Screenshot

Capture screenshots da página atual.

## `screenshot(filepath="screenshot.png")`

Tira um screenshot da página e salva em arquivo. Retorna o caminho do arquivo.

```python
driver.screenshot("pagina.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### Uso para depuração

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#erro", timeout=5)
        print("Elemento de erro encontrado!")
    except:
        driver.screenshot("erro.png")
        print("Screenshot salvo como erro.png")
```

## `screenshot_as_base64()`

Retorna o screenshot como string base64 (sem salvar em arquivo).

```python
img_b64 = driver.screenshot_as_base64()

# Enviar para API
import requests
requests.post("https://api.exemplo.com/upload", json={"image": img_b64})

# Exibir em HTML
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
