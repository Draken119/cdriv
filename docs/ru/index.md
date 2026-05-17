# cdriv

**Управляйте Chromium через ChromeDriver на Termux (Android aarch64).**

Прямая альтернатива **Playwright** и **Selenium** — которые **не работают** на Android aarch64. Эта библиотека взаимодействует с ChromeDriver через HTTP-протокол WebDriver для управления Chromium в headless-режиме, создана специально для Termux.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Легковесный и быстрый**

    ---

    Единственная зависимость: `requests`. Никаких тяжелых фреймворков, контейнеров или излишней сложности.

-   :material-cellphone:{ .lg .middle } **Создан для Termux**

    ---

    Работает нативно на Android aarch64. Установите с помощью `pkg install` и вы готовы к работе.

-   :material-cookie:{ .lg .middle } **Cookies для API**

    ---

    Извлекайте cookies в виде словаря — используйте напрямую с `requests.Session()`.

-   :material-language-python:{ .lg .middle } **Интуитивный API**

    ---

    Чистые, понятные методы. Минимальный порог входа.

</div>

## Быстрая установка

```bash
pip install cdriv
```

Подробные инструкции см. в [Руководстве по установке](installation.md).

## Быстрый старт

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    title = driver.get_title()

    print(title)
```

## Документация

| Раздел | Описание |
|--------|----------|
| [Установка](installation.md) | Установка библиотеки и зависимостей |
| [Быстрый старт](usage/quickstart.md) | Начните здесь |
| [Практические примеры](examples/login.md) | Примеры использования из реальной жизни |
| [Справочник API](api/cdriv.md) | Полная документация API |
| [Устранение неполадок](troubleshooting.md) | Частые проблемы и их решения |

## Лицензия

MIT
