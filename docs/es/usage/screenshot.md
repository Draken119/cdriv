# Captura de Pantalla

Captura pantallas de la página actual.

## `screenshot(filepath="screenshot.png")`

Toma una captura de pantalla de la página y la guarda en un archivo. Devuelve la ruta del archivo.

```python
driver.screenshot("page.png")
driver.screenshot(f"/sdcard/screenshots/{timestamp}.png")
```

### Depuración con Capturas de Pantalla

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    try:
        driver.navigate("https://site.com")
        driver.wait_for_element("#error", timeout=5)
        print("Elemento de error encontrado!")
    except:
        driver.screenshot("error.png")
        print("Captura guardada como error.png")
```

## `screenshot_as_base64()`

Devuelve la captura de pantalla como una cadena base64 (sin guardar en un archivo).

```python
img_b64 = driver.screenshot_as_base64()

# Enviar a una API
import requests
requests.post("https://api.example.com/upload", json={"image": img_b64})

# Mostrar en HTML
html = f'<img src="data:image/png;base64,{img_b64}" />'
```
