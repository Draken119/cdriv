# Pré-requisitos

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "Compatibilidade de Versão"
    No Termux, `chromium-browser` e `chromedriver` **devem ser da mesma versão**.
    Sempre atualize ambos juntos:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Verificar Binários

Confirme que ambos os binários estão disponíveis:

```bash
which chromedriver
which chromium-browser
```

Verifique as versões:

```bash
chromedriver --version
chromium-browser --version
```

## Proximo Passo

Agora vá para o [Guia de Inicio Rapido](usage/quickstart.md) para começar a usar o cdriv.
