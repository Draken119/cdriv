# Прокрутка

Методы для прокрутки страницы.

## `scroll_to(x=0, y=0)`

Прокручивает страницу до указанной позиции.

```python
driver.scroll_to(0, 500)   # Прокрутка на 500px вниз
driver.scroll_to(0, 0)     # Наверх
driver.scroll_to(200, 300) # 200px вправо, 300px вниз
```

## `scroll_to_bottom()`

Прокручивает вниз страницы.

```python
driver.scroll_to_bottom()
```

## `scroll_to_element(selector)`

Прокручивает до тех пор, пока элемент не станет видимым (по центру экрана).

```python
driver.scroll_to_element("#results")
driver.scroll_to_element(".footer")
driver.scroll_to_element("a#last-link")
```

## Пример: бесконечная прокрутка

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    for i in range(5):  # 5 прокруток
        driver.scroll_to_bottom()
        time.sleep(2)

    posts = driver.get_all_texts("article.title")
    print(f"Загружено постов: {len(posts)}")
```
