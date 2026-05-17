# Быстрый старт

## Менеджер контекста (рекомендуется)

Самый безопасный и удобный способ использования `CDriv`:

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://example.com")

    html = driver.get_page_source()
    print(driver.get_title())
```

Конструкция `with` гарантирует корректный запуск и остановку ChromeDriver,
даже при возникновении исключений.

## Ручное управление

Для полного контроля над жизненным циклом:

```python
from cdriv import CDriv

driver = CDriv()
driver.start()
driver.new_session()
driver.navigate("https://example.com")

# ... ваш код здесь ...

driver.close()
driver.stop()
```

## Конфигурация

### Свой порт

```python
driver = CDriv(port=9516)
```

### Свои пути к бинарным файлам

```python
driver = CDriv(
    chromedriver_path="/usr/bin/chromedriver",
    chromium_path="/usr/bin/chromium-browser",
)
```

## Типичная структура скрипта

1. Создайте экземпляр `CDriv`
2. Запустите сессию с помощью `new_session()`
3. Перейдите на целевой URL
4. Взаимодействуйте со страницей
5. Извлеките необходимые данные
6. Закройте сессию

```python
from cdriv import CDriv

with CDriv() as driver:       # 1. Создание и запуск
    driver.new_session()       # 2. Открытие браузера
    driver.navigate("...")     # 3. Навигация
    driver.fill("#field", "x") # 4. Взаимодействие
    data = driver.get_text("#result")  # 5. Извлечение
    print(data)
# 6. Автоматическая очистка
```
