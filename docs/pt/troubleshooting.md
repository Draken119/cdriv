# Solução de Problemas

## ChromeDriver Não Inicia

Verifique se os binários necessários estão instalados:

```bash
which chromedriver
which chromium-browser
```

Verifique as versões:

```bash
chromedriver --version
chromium-browser --version
```

Se não estiverem instalados:

=== "Termux"
    ```bash
    pkg install chromium-browser chromedriver
    ```
=== "Ubuntu/Debian"
    ```bash
    sudo apt install chromium-browser chromium-chromedriver
    ```

## Criação de Sessão Falha

No Termux, `chromium-browser` e `chromedriver` **devem ser da mesma versão**.
Atualize ambos:

```bash
pkg upgrade chromium-browser chromedriver
```

## Porta já em Uso

Se a porta 9515 estiver ocupada, use uma porta diferente:

```python
driver = CDriv(port=9516)
```

## Erros de Permissão Sandbox

O `CDriv` inicia com `--no-sandbox` por padrão, o que é necessário no Termux
e em contêineres. Se ainda assim receber erros, confirme se o chromium foi instalado corretamente.

## 5 Erros Comuns

| Erro | Causa | Solução |
|-------|-------|----------|
| `ChromeDriver did not start in time` | chromedriver não encontrado ou porta ocupada | Instale o chromedriver, altere a porta |
| `No active session` | Esqueceu de chamar `new_session()` | Chame `driver.new_session()` antes de navegar |
| `Failed to create session` | Chromium não encontrado ou incompatibilidade de versão | Instale o chromium-browser ou forneça o caminho |
| Timeout | Página lenta | Aumente o timeout ou use `wait_for_navigation()` |
| Erro de conexão | ChromeDriver não está rodando | Chame `driver.start()` ou use `with CDriv()` |

## Depuração

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Capturar screenshot em caso de erro
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("error.png")
    print(f"Erro: {e}")
```
