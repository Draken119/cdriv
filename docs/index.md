# cdriv

**Controle o Chromium via ChromeDriver no Termux (Android aarch64).**

Alternativa direta ao **Playwright** e **Selenium** — que **não funcionam** em Android/aarch64. Esta lib usa o protocolo WebDriver via HTTP para controlar o Chromium em modo headless, especificamente desenvolvida para rodar no Termux.

<div class="grid cards" markdown>

-   :material-rocket-launch:{ .lg .middle } **Leve e rápido**

    ---

    Depende apenas de `requests`. Sem frameworks pesados, sem contêineres, sem complexidade desnecessária.

-   :material-cellphone:{ .lg .middle } **Feito pro Termux**

    ---

    Funciona nativamente em Android aarch64. Instala com `pkg install` e já era.

-   :material-cookie:{ .lg .middle } **Cookies prontos pra API**

    ---

    Extrai cookies como dicionário — usa direto com `requests.Session()`.

-   :material-language-python:{ .lg .middle } **API intuitiva**

    ---

    Métodos diretos e descritivos. Em português. Curva de aprendizado mínima.

</div>

## Instalação rápida

```bash
pip install cdriv
```

Veja o [Guia de Instalação](installation.md) completo.

## Primeiro exemplo

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://exemplo.com")

    html = driver.get_page_source()
    cookies = driver.get_cookies_dict()
    titulo = driver.get_title()

    print(titulo)
```

## Documentação

| Seção | Descrição |
|-------|-----------|
| [Instalação](installation.md) | Instalação da lib e dependências |
| [Primeiros Passos](usage/quickstart.md) | Comece por aqui |
| [Exemplos Práticos](examples/login.md) | Exemplos reais de uso |
| [API Reference](api/cdriv.md) | Documentação completa da API |
| [Solução de Problemas](troubleshooting.md) | Problemas comuns e soluções |

## Licença

MIT
