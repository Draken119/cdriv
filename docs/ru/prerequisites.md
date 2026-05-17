# Необходимые компоненты

## Termux (Android)

```bash
pkg update
pkg install chromium-browser chromedriver
```

!!! tip "Совместимость версий"
    В Termux `chromium-browser` и `chromedriver` **должны быть одной версии**.
    Всегда обновляйте их вместе:

    ```bash
    pkg upgrade chromium-browser chromedriver
    ```

## Linux (Ubuntu/Debian)

```bash
sudo apt update
sudo apt install chromium-browser chromium-chromedriver
```

## Проверка бинарных файлов

Убедитесь, что оба бинарных файла доступны:

```bash
which chromedriver
which chromium-browser
```

Проверьте версии:

```bash
chromedriver --version
chromium-browser --version
```

## Следующий шаг

Теперь переходите к [Руководству по быстрому старту](usage/quickstart.md), чтобы начать использовать cdriv.
