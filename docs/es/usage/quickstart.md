# Inicio Rápido

## Gestor de Contexto (recomendado)

La forma más segura y conveniente de usar `CDriv`:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

La declaración `with` garantiza que ChromeDriver se inicie y detenga correctamente,
incluso cuando ocurren excepciones.

## Gestión Manual

Para tener control total sobre el ciclo de vida:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... tu código aquí ...

driver.close()
driver.stop()
```

## Configuración

### Puerto Personalizado

```python
driver = CDriv(port=9516)
```

### Rutas de Binarios Personalizadas

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## Estructura Típica de un Script

1. Crear una instancia de `CDriv`
2. Iniciar una sesión con `new_session()`
3. Navegar a la URL de destino
4. Interactuar con la página
5. Extraer los datos requeridos
6. Cerrar la sesión

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. Crear e iniciar
    driver.new_session()       # 2. Abrir navegador
    driver.navigate("...")     # 3. Navegar
    driver.fill("#field", "x") # 4. Interactuar
    data = driver.get_text("#result")  # 5. Extraer
    print(data)
# 6. Limpieza automática
```
