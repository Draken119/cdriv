# Form Automation

Example of filling out and submitting forms automatically.

```python
from cdriv import CDriv

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/register")

    # Wait for the form to load
    driver.wait_for_element("form#registration", timeout=10)

    # Fill in fields
    driver.fill("input#name", "John Doe")
    driver.fill("input#email", "john@email.com")
    driver.fill("input#phone", "+1 (555) 123-4567")
    driver.fill("textarea#message", "Hello, I would like more information.")

    # Select options
    driver.select_option("select#country", "US")
    driver.select_option("select#category", "support")

    # Check terms
    driver.click("input#accept-terms")

    # Submit the form
    driver.click("button[type='submit']")

    # Wait for confirmation
    if driver.wait_for_text("Registration successful", timeout=15):
        print("Form submitted successfully!")
        print(driver.get_text(".success-message"))
    else:
        print("Error submitting form")
        driver.screenshot("form_error.png")
```
