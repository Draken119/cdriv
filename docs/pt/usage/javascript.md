# JavaScript

Execute JavaScript arbitrário na página.

## `execute_script(script, *args)`

Executa JavaScript no contexto da página e retorna o resultado.

```python
# Ler dados
title = driver.execute_script("return document.title")
text = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# Manipular a página
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Com argumentos
driver.execute_script("arguments[0].scrollIntoView()", element)
```

## Casos de Uso Comuns

### Extrair Dados de Tabela

```python
data = driver.execute_script("""
    return Array.from(document.querySelectorAll('table tr')).map(row =>
        Array.from(row.querySelectorAll('td')).map(td => td.innerText)
    )
""")
```

### Manipular Atributos

```python
driver.execute_script("""
    document.querySelectorAll('.hidden').forEach(el =>
        el.style.display = 'block'
    )
""")
```

### Simular Eventos

```python
driver.execute_script("""
    var el = document.querySelector('input#file');
    var event = new MouseEvent('click', {bubbles: true});
    el.dispatchEvent(event);
""")
```

### Monitoramento de Rede (avançado)

```python
driver.execute_script("""
    var logs = [];
    var original = fetch;
    window.fetch = function() {
        logs.push(arguments[0]);
        return original.apply(this, arguments);
    };
""")
```
