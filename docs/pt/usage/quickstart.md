# Início Rápido

## Gerenciador de Contexto (recomendado)

A forma mais segura e conveniente de usar o `CDriv`:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

A declaração `with` garante que o ChromeDriver inicie e pare corretamente,
mesmo quando ocorrem exceções.

## Gerenciamento Manual

Para controle total sobre o ciclo de vida:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... seu código aqui ...

driver.close()
driver.stop()
```

## Configuração

### Porta Personalizada

```python
driver = CDriv(port=9516)
```

### Caminhos de Binários Personalizados

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## Estrutura Típica de Script

1. Criar uma instância de `CDriv`
2. Iniciar uma sessão com `new_session()`
3. Navegar para a URL alvo
4. Interagir com a página
5. Extrair os dados necessários
6. Fechar a sessão

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. Criar e iniciar
    driver.new_session()       # 2. Abrir navegador
    driver.navigate("...")     # 3. Navegar
    driver.fill("#field", "x") # 4. Interagir
    data = driver.get_text("#result")  # 5. Extrair
    print(data)
# 6. Limpeza automática
```
