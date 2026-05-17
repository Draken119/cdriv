# Pré-requisitos

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "Versões compatíveis"
    No Termux, é essencial que `chromium-browser` e `chromedriver` sejam da **mesma versão**.
    Sempre atualize ambos juntos:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Verificar instalação

Confirme que os binários estão disponíveis:

```bash
which chromedriver
which chromium-browser
```

Verifique as versões:

```bash
chromedriver --version
chromium-browser --version
```

## Próximo passo

Agora veja os [Primeiros Passos](usage/quickstart.md) para começar a usar.
