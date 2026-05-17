# О проекте

## Что такое cdriv?

**cdriv** — это Python-библиотека для управления Chromium через ChromeDriver на
**Termux** (Android aarch64). Она была создана потому, что **Playwright** и
**Selenium** просто **не работают** на Android aarch64.

Вместо использования тяжелых фреймворков, требующих контейнеров или специальных
сред выполнения, `cdriv` взаимодействует напрямую с ChromeDriver через HTTP-протокол
WebDriver. Результат — легковесная библиотека с единственной
зависимостью: `requests`.

## Почему cdriv?

- :material-cellphone: **Работает на Termux** — в отличие от Playwright и Selenium
- :material-feather: **Легковесный** — единственная зависимость: `requests`
- :material-bolt: **Простой** — чистый, понятный API
- :material-test-tube: **Проверен в работе** — активно используется на Termux

## Лицензия

MIT — используйте, изменяйте и распространяйте свободно.

## Ссылки

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
