# cdriv

**Controle o Chromium via ChromeDriver no Termux (Android aarch64).**

Uma alternativa direta ao **Playwright** e **Selenium** — que **não funcionam** no Android aarch64. Esta biblioteca se comunica com o ChromeDriver através do protocolo HTTP WebDriver para controlar o Chromium em modo headless, desenvolvida especificamente para o Termux.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Leve e Rápido**

    ---

    Dependência única: `requests`. Sem frameworks pesados, sem contêineres, sem complexidade desnecessária.

-   :material-cellphone:{ .lg .middle } **Feito para o Termux**

    ---

    Roda nativamente no Android aarch64. Instale com `pkg install` e pronto.

-   :material-cookie:{ .lg .middle } **Cookies Prontos para API**

    ---

    Extraia cookies como um dicionário — use diretamente com `requests.Session()`.

-   :material-language-python:{ .lg .middle } **API Intuitiva**

    ---

    Métodos limpos e descritivos. Curva de aprendizado mínima.

</div>

## Instalação Rápida

```bash
pip install cdriv
```

Consulte o [Guia de Instalação](installation.md) para instruções detalhadas.

## Início Rápido

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

## Documentação

| Seção | Descrição |
|---------|-------------|
| [Instalação](installation.md) | Instalação da biblioteca e dependências |
| [Início Rápido](usage/quickstart.md) | Comece por aqui |
| [Exemplos Práticos](examples/login.md) | Casos de uso reais |
| [Referência da API](api/cdriv.md) | Documentação completa da API |
| [Solução de Problemas](troubleshooting.md) | Problemas comuns e soluções |

## Licença

MIT
