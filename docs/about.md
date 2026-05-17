# Sobre

## O que é?

**cdriv** é uma biblioteca Python para controlar o Chromium via ChromeDriver
no **Termux** (Android aarch64). Ela foi criada porque o **Playwright** e
**Selenium** simplesmente **não funcionam** em Android/aarch64.

Em vez de depender de frameworks pesados que exigem contêineres ou runtime
específicos, o `cdriv` se comunica diretamente com o ChromeDriver via
protocolo HTTP WebDriver. O resultado é uma lib leve, que depende apenas do
pacote `requests`.

## Por que cdriv?

- :material-cellphone: **Funciona no Termux** — ao contrário de Playwright e Selenium
- :material-feather: **Leve** — única dependência: `requests`
- :material-bolt: **Simples** — API em português, métodos diretos
- :material-test-tube: **Testado** — usado em produção no Termux

## Licença

MIT — use, modifique, distribua à vontade.

## Links

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
