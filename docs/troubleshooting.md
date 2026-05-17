# Solução de Problemas

## ChromeDriver não inicia

Verifique se os binários estão instalados:

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

## Sessão não cria / navegador não abre

No Termux, é essencial que os pacotes `chromium-browser` e `chromedriver` sejam
da **mesma versão**. Atualize ambos:

```bash
pkg upgrade chromium-browser chromedriver
```

## Porta ocupada

Se a porta 9515 estiver ocupada, use uma porta diferente:

```python
driver = CDriv(port=9516)
```

## Erro de permissão (sandbox)

O `CDriv` já inicia com `--no-sandbox` por padrão, que é necessário no Termux
e em containers. Se ainda assim tiver erro, confirme que o chromium foi
instalado corretamente.

## Timeout ao navegar

Páginas muito lentas podem exceder o timeout padrão. Aumente o timeout
explicitamente ou use `wait_for_navigation()`.

## 5 erros comuns

| Erro | Causa | Solução |
|------|-------|---------|
| `ChromeDriver não iniciou a tempo` | chromedriver não encontrado ou porta ocupada | Instale o chromedriver, troque a porta |
| `Nenhuma sessão ativa` | Esqueceu de chamar `new_session()` | Chame `driver.new_session()` antes de navegar |
| `Failed to create session` | Chromium não encontrado ou versão incompatível | Instale chromium-browser ou informe o caminho |
| Timeout | Página lenta | Aumente timeout ou use `wait_for_navigation()` |
| Erro de conexão | ChromeDriver não está rodando | Chame `driver.start()` ou use `with CDriv()` |

## Logs e depuração

```python
import logging
logging.basicConfig(level=logging.DEBUG)

# Capture screenshot em caso de erro
try:
    driver.navigate("https://site.com")
except Exception as e:
    driver.screenshot("erro.png")
    print(f"Erro: {e}")
```
