# Requisitos Previos

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "Compatibilidad de Versiones"
    En Termux, `chromium-browser` y `chromedriver` **deben tener la misma versión**.
    Actualiza siempre ambos juntos:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Verificar los Binarios

Confirma que ambos binarios estén disponibles:

```bash
which chromedriver
which chromium-browser
```

Verifica las versiones:

```bash
chromedriver --version
chromium-browser --version
```

## Siguiente Paso

Ahora dirígete a la [Guía de Inicio Rápido](usage/quickstart.md) para empezar a usar cdriv.
