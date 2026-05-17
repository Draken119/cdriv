# Sobre

## O que é cdriv?

**cdriv** é uma biblioteca Python para controlar o Chromium via ChromeDriver no
**Termux** (Android aarch64). Foi criada porque **Playwright** e **Selenium**
simplesmente **não funcionam** no Android aarch64.

Em vez de depender de frameworks pesados que exigem contêineres ou runtimes
específicos, o `cdriv` se comunica diretamente com o ChromeDriver através do
protocolo HTTP WebDriver. O resultado é uma biblioteca leve com uma única
dependência: `requests`.

## Por que cdriv?

- :material-cellphone: **Funciona no Termux** — ao contrário do Playwright e Selenium
- :material-feather: **Leve** — dependência única: `requests`
- :material-bolt: **Simples** — API limpa e descritiva
- :material-test-tube: **Testado em Produção** — usado ativamente no Termux

## Licença

MIT — use, modifique e distribua livremente.

## Links

- :fontawesome-brands-github: [GitHub](https://github.com/Draken119/cdriv)
- :fontawesome-brands-python: [PyPI](https://pypi.org/project/cdriv/)
