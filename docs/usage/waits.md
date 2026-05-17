# Waits (Esperas)

Aguarde condições específicas na página antes de prosseguir.

## `wait_for_element(selector, timeout=10, interval=0.3)`

Aguarda até que um elemento apareça no DOM.

```python
if driver.wait_for_element("#carregou", timeout=15):
    print("Elemento encontrado!")
else:
    print("Timeout — elemento não apareceu")
```

### Uso típico

```python
driver.navigate("https://site.com/produtos")

# Aguarda a lista carregar
if driver.wait_for_element(".produto-item", timeout=10):
    precos = driver.get_all_texts(".produto-preco")
    print(precos)
else:
    print("Lista de produtos não carregou")
```

## `wait_for_text(text, timeout=10, interval=0.5)`

Aguarda até que um texto apareça na página.

```python
# Aguarda confirmação
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
print("Página carregada!")
```

## `sleep(seconds)`

Pausa por N segundos. Mesmo que `time.sleep()`, mas mais legível no fluxo.

```python
driver.sleep(2)  # Aguarda 2 segundos
```

## Exemplo combinado

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    driver.fill("input#username", "admin")
    driver.fill("input#password", "123456")
    driver.click("button[type='submit']")

    # Aguarda o dashboard carregar
    if driver.wait_for_element(".dashboard", timeout=10):
        driver.wait_for_text("Bem-vindo", timeout=5)
        print("Login realizado com sucesso!")
    else:
        driver.screenshot("erro_login.png")
        print("Falha no login")
```
