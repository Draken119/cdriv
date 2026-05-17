# Login + API

Exemplo real de login em um site e reutilização dos cookies para chamadas de API.

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Preenche formulário de login
    driver.fill("input#username", "meu_login")
    driver.fill("input#password", "minha_senha")
    driver.click("button[type='submit']")

    # Aguarda redirecionamento
    driver.wait_for_navigation()

    # Verifica se login foi bem-sucedido
    if driver.wait_for_element(".dashboard", timeout=5):
        print("Login realizado!")

        # Extrai cookies e cria sessão autenticada
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # Faz chamadas autenticadas
        dados = session.get("https://site.com/api/dados").json()
        print(dados)
    else:
        print("Falha no login")
        driver.screenshot("erro_login.png")
```
