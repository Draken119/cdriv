# JavaScript

Execute JavaScript arbitrário na página.

## `execute_script(script, *args)`

Executa JavaScript na página e retorna o resultado.

```python
# Ler dados
titulo = driver.execute_script("return document.title")
texto = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# Manipular a página
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# Com argumentos
driver.execute_script("arguments[0].scrollIntoView()", elemento)
```

## Casos de uso comuns

### Extrair dados de uma tabela

```python
dados = driver.execute_script("""
    return Array.from(document.querySelectorAll('table tr')).map(row =>
        Array.from(row.querySelectorAll('td')).map(td => td.innerText)
    )
""")
```

### Manipular atributos

```python
driver.execute_script("""
    document.querySelectorAll('.hidden').forEach(el =>
        el.style.display = 'block'
    )
""")
```

### Simular eventos

```python
driver.execute_script("""
    var el = document.querySelector('input#file');
    var event = new MouseEvent('click', {bubbles: true});
    el.dispatchEvent(event);
""")
```

### Monitorar rede (avançado)

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
