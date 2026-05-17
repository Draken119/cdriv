# Navegación

Métodos para navegar entre páginas web.

## `navigate(url)`

Navega a una URL. Espera a que la página se cargue completamente.

```python
driver.navigate("https://site.com")
driver.navigate("https://site.com/product/123")
```

## `get_current_url()`

Devuelve la URL de la página actual.

```python
url = driver.get_current_url()
print(f"Estás en: {url}")
```

## `back()`

Vuelve a la página anterior (como el botón de atrás del navegador).

```python
driver.navigate("https://site.com/page1")
driver.navigate("https://site.com/page2")
driver.back()  # Vuelve a page1
```

## `forward()`

Avanza a la página siguiente (como el botón de adelante del navegador).

```python
driver.forward()  # Vuelve a page2
```

## `refresh()`

Recarga la página actual.

```python
driver.refresh()
```

## Ejemplo Completo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()

    driver.navigate("https://site.com/login")
    print(driver.get_current_url())

    # Simular flujo de navegación
    driver.navigate("https://site.com/dashboard")
    driver.back()      # Volver a login
    driver.forward()   # Avanzar a dashboard
    driver.refresh()   # Recargar dashboard
```
