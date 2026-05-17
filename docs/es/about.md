# Acerca de

## ¿Qué es cdriv?

**cdriv** es una librería de Python para controlar Chromium mediante ChromeDriver en
**Termux** (Android aarch64). Fue creada porque **Playwright** y
**Selenium** simplemente **no funcionan** en Android aarch64.

En lugar de depender de frameworks pesados que requieren contenedores o entornos
de ejecución específicos, `cdriv` se comunica directamente con ChromeDriver a través del
protocolo HTTP WebDriver. El resultado es una librería ligera con una sola
dependencia: `requests`.

## ¿Por qué cdriv?

- :material-cellphone: **Funciona en Termux** — a diferencia de Playwright y Selenium
- :material-feather: **Ligero** — una sola dependencia: `requests`
- :material-bolt: **Simple** — API limpia y descriptiva
- :material-test-tube: **Probado en producción** — usado activamente en Termux

## Licencia

MIT — úsalo, modifícalo y distribúyelo libremente.

## Enlaces

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
