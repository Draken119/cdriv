# Primeiros Passos

## Context Manager (recomendado)

A forma mais segura e prática de usar o `CDriv`:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://exemplo.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

O `with` garante que o ChromeDriver será iniciado automaticamente e finalizado
corretamente, mesmo em caso de erro.

## Gerenciamento manual

Se prefere controle total sobre o ciclo de vida:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://exemplo.com")

# ... seu código aqui ...

driver.close()
driver.stop()
```

## Configuração básica

### Porta personalizada

```python
driver = CDriv(port=9516)
```

### Caminhos manuais

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## Estrutura típica de um script

1. Criar instância do `CDriv`
2. Iniciar sessão com `new_session()`
3. Navegar para a URL desejada
4. Interagir com a página
5. Extrair dados necessários
6. Encerrar a sessão

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. Cria e inicia
    driver.new_session()       # 2. Abre o navegador
    driver.navigate("...")     # 3. Navega
    driver.fill("#campo", "x") # 4. Interage
    dados = driver.get_text("#resultado")  # 5. Extrai
    print(dados)
# 6. Encerra automaticamente
```
