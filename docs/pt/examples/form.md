# Automação de Formulários

Exemplo de preenchimento e envio de formulários automaticamente.

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # Aguardar o formulário carregar
    driver.wait_for_element("form#registration", timeout=10)

    # Preencher campos
    driver.fill("input#name", "João Silva")
    driver.fill("input#email", "joao@email.com")
    driver.fill("input#phone", "+55 (11) 99999-8888")
    driver.fill("textarea#message", "Olá, gostaria de mais informações.")

    # Selecionar opções
    driver.select_option("select#country", "BR")
    driver.select_option("select#category", "support")

    # Aceitar termos
    driver.click("input#accept-terms")

    # Enviar o formulário
    driver.click("button[type='submit']")

    # Aguardar confirmação
    if driver.wait_for_text("Cadastro realizado com sucesso", timeout=15):
        print("Formulário enviado com sucesso!")
        print(driver.get_text(".success-message"))
    else:
        print("Erro ao enviar formulário")
        driver.screenshot("form_error.png")
```
