# Automatización de Formularios

Ejemplo de cómo rellenar y enviar formularios automáticamente.

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # Esperar a que se cargue el formulario
    driver.wait_for_element("form#registration", timeout=10)

    # Rellenar campos
    driver.fill("input#name", "John Doe")
    driver.fill("input#email", "john@email.com")
    driver.fill("input#phone", "+1 (555) 123-4567")
    driver.fill("textarea#message", "Hello, I would like more information.")

    # Seleccionar opciones
    driver.select_option("select#country", "US")
    driver.select_option("select#category", "support")

    # Aceptar términos
    driver.click("input#accept-terms")

    # Enviar el formulario
    driver.click("button[type='submit']")

    # Esperar confirmación
    if driver.wait_for_text("Registration successful", timeout=15):
        print("Formulario enviado exitosamente!")
        print(driver.get_text(".success-message"))
    else:
        print("Error al enviar el formulario")
        driver.screenshot("form_error.png")
```
