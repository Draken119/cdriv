# Automação de Formulário

Exemplo de preenchimento e envio automático de formulários.

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/cadastro")

    # Aguarda o formulário carregar
    driver.wait_for_element("form#cadastro", timeout=10)

    # Preenche campos
    driver.fill("input#nome", "João Silva")
    driver.fill("input#email", "joao@email.com")
    driver.fill("input#telefone", "(11) 99999-8888")
    driver.fill("textarea#mensagem", "Olá, gostaria de mais informações.")

    # Seleciona opções
    driver.select_option("select#pais", "BR")
    driver.select_option("select#categoria", "suporte")

    # Marca checkbox
    driver.click("input#aceito-termos")

    # Envia o formulário
    driver.click("button[type='submit']")

    # Aguarda confirmação
    if driver.wait_for_text("Cadastro realizado", timeout=15):
        print("Formulário enviado com sucesso!")
        print(driver.get_text(".mensagem-sucesso"))
    else:
        print("Erro ao enviar formulário")
        driver.screenshot("erro_form.png")
```
