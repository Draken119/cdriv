# Бесконечная прокрутка

Пример парсинга страниц с бесконечной прокруткой.

```python
from cdriv import CDriv
import time

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/feed")

    # Прокрутить 5 раз, ожидая загрузки контента между каждой
    for i in range(5):
        driver.scroll_to_bottom()
        time.sleep(2)  # Ожидание загрузки нового контента
        print(f"Прокрутка {i+1}/5 завершена")

    # Извлечение всех загруженных постов
    posts = driver.get_all_texts("article.title")
    print(f"\nВсего загружено постов: {len(posts)}")
    for post in posts:
        print(f"- {post}")
```
