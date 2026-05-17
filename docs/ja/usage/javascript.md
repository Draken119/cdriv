# JavaScript

ページ上で任意の JavaScript を実行します。

## `execute_script(script, *args)`

ページコンテキストで JavaScript を実行し、結果を返します。

```python
# データの読み取り
title = driver.execute_script("return document.title")
text = driver.execute_script("return document.querySelector('.x').innerText")
token = driver.execute_script("return localStorage.getItem('token')")

# ページの操作
driver.execute_script("document.querySelector('#btn').click()")
driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

# 引数付き
driver.execute_script("arguments[0].scrollIntoView()", element)
```

## よくあるユースケース

### テーブルデータの抽出

```python
data = driver.execute_script("""
    return Array.from(document.querySelectorAll('table tr')).map(row =>
        Array.from(row.querySelectorAll('td')).map(td => td.innerText)
    )
""")
```

### 属性の操作

```python
driver.execute_script("""
    document.querySelectorAll('.hidden').forEach(el =>
        el.style.display = 'block'
    )
""")
```

### イベントのシミュレーション

```python
driver.execute_script("""
    var el = document.querySelector('input#file');
    var event = new MouseEvent('click', {bubbles: true});
    el.dispatchEvent(event);
""")
```

### ネットワーク監視 (高度)

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
