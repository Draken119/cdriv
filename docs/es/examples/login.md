# Inicio de Sesión + API

Ejemplo real de inicio de sesión en un sitio web y reutilización de cookies para llamadas a la API.

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Rellenar formulario de inicio de sesión
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Esperar la redirección
    driver.wait_for_navigation()

    # Verificar que el inicio de sesión fue exitoso
    if driver.wait_for_element(".dashboard", timeout=5):
        print("Inicio de sesión exitoso!")

        # Extraer cookies y crear sesión autenticada
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # Hacer llamadas autenticadas a la API
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("Inicio de sesión fallido")
        driver.screenshot("login_error.png")
```
