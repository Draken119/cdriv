# Monitoramento de Preço

Script de exemplo para monitorar preços de produtos ao longo do tempo.

```python
from cdriv import CDriv
import json
from datetime import datetime

PRODUCT_URL = "https://site.com/product/123"
HISTORY_FILE = "price_history.json"

with CDriv() as driver:
    driver.new_session()
    driver.navigate(PRODUCT_URL)
    driver.wait_for_element(".price", timeout=10)

    # Extrair dados do produto
    name = driver.get_text("h1.product-name")
    price_text = driver.get_text(".current-price")
    stock = driver.get_text(".stock-status")

    # Analisar preço (ex.: "$1,234.56" -> 1234.56)
    price = float(
        price_text.replace("$", "")
        .replace(",", "")
        .strip()
    )

    # Criar registro
    record = {
        "date": datetime.now().isoformat(),
        "product": name,
        "price": price,
        "in_stock": "out of stock" not in stock.lower(),
    }

    print(f"{record['product']}: ${price:.2f}")

    # Salvar histórico
    try:
        with open(HISTORY_FILE) as f:
            history = json.load(f)
    except FileNotFoundError:
        history = []

    history.append(record)
    with open(HISTORY_FILE, "w") as f:
        json.dump(history, f, indent=2)
```
