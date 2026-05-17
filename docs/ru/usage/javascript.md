# JavaScript

Выполнение произвольного JavaScript-кода на странице.

## `execute_script(script, *args)`

Выполняет JavaScript в контексте страницы и возвращает результат.

```python
# Чтение данных
title = driver.execute_script("return document.title")
text = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# Манипуляция страницей
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# С аргументами
driver.execute_script("arguments[0].scrollIntoView()", element)
```

## Часто используемые сценарии

### Извлечение данных из таблицы

```python
data = driver.execute_script("""
    return Array.from(document.querySelectorAll('table tr')).map(row =>
        Array.from(row.querySelectorAll('td')).map(td => td.innerText)
    )
""")
```

### Манипуляция атрибутами

```python
driver.execute_script("""
    document.querySelectorAll('.hidden').forEach(el =>
        el.style.display = 'block'
    )
""")
```

### Симуляция событий

```python
driver.execute_script("""
    var el = document.querySelector('input#file');
    var event = new MouseEvent('click', {bubbles: true});
    el.dispatchEvent(event);
""")
```

### Мониторинг сетевых запросов (продвинутый)

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
