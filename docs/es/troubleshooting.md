# Solución de Problemas

## ChromeDriver No Inicia

Verifica que los binarios requeridos estén instalados:

```bash
which chromedriver
which chromium-browser
```

Verifica las versiones:

```bash
chromedriver --version
chromium-browser --version
```

Si no están instalados:

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## La Creación de Sesión Falló

En Termux, `chromium-browser` y `chromedriver` **deben tener la misma versión**.
Actualiza ambos:

```bash
pkg upgrade chromium-browser chromedriver
```

## Puerto Ya Está en Uso

Si el puerto 9515 está ocupado, usa un puerto diferente:

```python
driver = CDriv(port=9516)
```

## Errores de Permiso de Sandbox

`CDriv` se inicia con `--no-sandbox` por defecto, lo cual es necesario en Termux
y contenedores. Si aún recibes errores, confirma que chromium fue instalado correctamente.

## 5 Errores Comunes

| Error | Causa | Solución |
|-------|-------|----------|
| `ChromeDriver did not start in time` | chromedriver no encontrado o puerto ocupado | Instala chromedriver, cambia el puerto |
| `No active session` | Olvidaste llamar a `new_session()` | Llama a `driver.new_session()` antes de navegar |
| `Failed to create session` | Chromium no encontrado o versión incorrecta | Instala chromium-browser o proporciona la ruta |
| Timeout | Página lenta | Aumenta el tiempo de espera o usa `wait_for_navigation()` |
| Error de conexión | ChromeDriver no está ejecutándose | Llama a `driver.start()` o usa `with CDriv()` |

## Depuración

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Capturar pantalla en caso de error
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"Error: {e}")
```
