# Login + API

Exemplo real de login em um site e reutilização de cookies para chamadas de API.

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Preencher formulário de login
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Aguardar redirecionamento
    driver.wait_for_navigation()

    # Verificar se o login foi bem-sucedido
    if driver.wait_for_element(".dashboard", timeout=5):
        print("Login bem-sucedido!")

        # Extrair cookies e criar sessão autenticada
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # Fazer chamadas de API autenticadas
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("Falha no login")
        driver.screenshot("login_error.png")
```
