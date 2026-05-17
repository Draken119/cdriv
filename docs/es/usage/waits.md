# Esperas

Espera condiciones específicas en la página antes de continuar.

## `wait_for_element(selector, timeout=10, interval=0.3)`

Espera hasta que un elemento aparezca en el DOM.

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("Elemento encontrado!")
else:
    print("Tiempo de espera agotado — el elemento no apareció")
```

### Uso Típico

```python
driver.navigate("https://site.com/products")

# Esperar a que se cargue la lista
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("La lista de productos no se cargó")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

Espera hasta que un texto específico aparezca en la página.

```python
# Esperar confirmación
if driver.wait_for_text("Order confirmed", timeout=20):
    print("Pedido confirmado exitosamente!")
else:
    print("Tiempo de espera de confirmación agotado")
```

## `wait_for_navigation(timeout=10)`

Espera a que la página termine de cargarse (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("Página cargada!")
```

## `sleep(seconds)`

Pausa durante N segundos. Es lo mismo que `time.sleep()`, pero más legible en el flujo.

```python
driver.sleep(2)  # Esperar 2 segundos
```

## Ejemplo Combinado

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # Esperar a que se cargue el dashboard
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Welcome", timeout=5)
        print("Inicio de sesión exitoso!")
    else:
        driver.screenshot("login_error.png")
        print("Inicio de sesión fallido")
```
