# Monitoramento de Preços

Exemplo de script para monitorar preços de produtos.

```python
from cdriv import CDriv
import json
from datetime import datetime

URL_PRODUTO = "https://site.com/produto/123"
ARQUIVO_HISTORICO = "historico_precos.json"

with CDriv() as driver:
    driver.new_session()
    driver.navigate(URL_PRODUTO)
    driver.wait_for_element(".preco", timeout=10)

    # Extrai dados do produto
    nome = driver.get_text("h1.produto-nome")
    preco_texto = driver.get_text(".preco-atual")
    disponivel = driver.get_text(".estoque")

    # Converte preço (ex: "R$ 1.234,56" -> 1234.56)
    preco = float(
        preco_texto.replace("R$", "")
        .replace(".", "")
        .replace(",", ".")
        .strip()
    )

    # Registro
    registro = {
        "data": datetime.now().isoformat(),
        "produto": nome,
        "preco": preco,
        "disponivel": "indisponível" not in disponivel.lower(),
    }

    print(f"{registro['produto']}: R$ {preco:.2f}")

    # Salva histórico
    try:
        with open(ARQUIVO_HISTORICO) as f:
            historico = json.load(f)
    except FileNotFoundError:
        historico = []

    historico.append(registro)
    with open(ARQUIVO_HISTORICO, "w") as f:
        json.dump(historico, f, indent=2, ensure_ascii=False)
```
