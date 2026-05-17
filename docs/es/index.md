# cdriv

**Controla Chromium mediante ChromeDriver en Termux (Android aarch64).**

Una alternativa directa a **Playwright** y **Selenium** — que **no funcionan** en Android aarch64. Esta librería se comunica con ChromeDriver a través del protocolo HTTP WebDriver para controlar Chromium en modo headless, construida específicamente para Termux.

<div class="grid cards" markdown="1">

-   :material-rocket-launch:{ .lg .middle } **Ligero y Rápido**

    ---

    Una sola dependencia: `requests`. Sin frameworks pesados, sin contenedores, sin complejidad innecesaria.

-   :material-cellphone:{ .lg .middle } **Construido para Termux**

    ---

    Funciona de forma nativa en Android aarch64. Instala con `pkg install` y ya estás listo.

-   :material-cookie:{ .lg .middle } **Cookies listas para API**

    ---

    Extrae cookies como diccionario — úsalas directamente con `requests.Session()`.

-   :material-language-python:{ .lg .middle } **API Intuitiva**

    ---

    Métodos limpios y descriptivos. Curva de aprendizaje mínima.

</div>

## Instalación Rápida

```bash
pip install cdriv
```

Consulta la [Guía de Instalación](installation.md) para instrucciones detalladas.

## Inicio Rápido

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

## Documentación

| Sección | Descripción |
|---------|-------------|
| [Instalación](installation.md) | Instalación de la librería y dependencias |
| [Inicio Rápido](usage/quickstart.md) | Empieza aquí |
| [Ejemplos Prácticos](examples/login.md) | Casos de uso reales |
| [Referencia de API](api/cdriv.md) | Documentación completa de la API |
| [Solución de Problemas](troubleshooting.md) | Problemas comunes y soluciones |

## Licencia

MIT
