# Esperas

Aguardar condições específicas na página antes de prosseguir.

## `wait_for_element(selector, timeout=10, interval=0.3)`

Aguarda até que um elemento apareça no DOM.

```python
if driver.wait_for_element("#loaded", timeout=15):
    print("Elemento encontrado!")
else:
    print("Timeout — o elemento não apareceu")
```

### Uso Tipico

```python
driver.navigate("https://site.com/products")

# Aguardar a lista carregar
if driver.wait_for_element(".product-item", timeout=10):
    prices = driver.get_all_texts(".product-price")
    print(prices)
else:
    print("A lista de produtos não carregou")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

Aguarda até que um texto específico apareça na página.

```python
# Aguardar confirmação
if driver.wait_for_text("Pedido confirmado", timeout=20):
    print("Pedido confirmado com sucesso!")
else:
    print("Timeout na confirmação")
```

## `wait_for_navigation(timeout=10)`

Aguarda a página terminar de carregar (`document.readyState === 'complete'`).

```python
driver.navigate("https://site.com")
driver.wait_for_navigation(timeout=15)
print("Pagina carregada!")
```

## `sleep(seconds)`

Pausa por N segundos. Equivalente a `time.sleep()`, mas mais legível no fluxo.

```python
driver.sleep(2)  # Aguardar 2 segundos
```

## Exemplo Combinado

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # Aguardar o dashboard carregar
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Bem-vindo", timeout=5)
        print("Login bem-sucedido!")
    else:
        driver.screenshot("login_error.png")
        print("Falha no login")
```
