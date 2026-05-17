# JavaScript

在页面上执行任意 JavaScript。

## `execute_script(script, *args)`

在页面上下文中执行 JavaScript 并返回结果。

```python
# 读取数据
title = driver.execute_script("return document.title")
text = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# 操作页面
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 带参数
driver.execute_script("arguments[0].scrollIntoView()", element)
```

## 常见用例

### 提取表格数据

```python
data = driver.execute_script("""
    return Array.from(document.querySelectorAll('table tr')).map(row =>
        Array.from(row.querySelectorAll('td')).map(td => td.innerText)
    )
""")
```

### 操作属性

```python
driver.execute_script("""
    document.querySelectorAll('.hidden').forEach(el =>
        el.style.display = 'block'
    )
""")
```

### 模拟事件

```python
driver.execute_script("""
    var el = document.querySelector('input#file');
    var event = new MouseEvent('click', {bubbles: true});
    el.dispatchEvent(event);
""")
```

### 网络监控（高级）

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
