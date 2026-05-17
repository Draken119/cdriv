# Login + API

Real-world example of logging into a website and reusing cookies for API calls.

```python
from cdriv import CDriv
import requests

with CDriv() as driver:
    driver.new_session()
    driver.navigate("https://site.com/login")

    # Fill in login form
    driver.fill("input#username", "my_user")
    driver.fill("input#password", "my_password")
    driver.click("button[type='submit']")

    # Wait for redirect
    driver.wait_for_navigation()

    # Verify login was successful
    if driver.wait_for_element(".dashboard", timeout=5):
        print("Login successful!")

        # Extract cookies and create authenticated session
        session = requests.Session()
        session.cookies.update(driver.get_cookies_dict())

        # Make authenticated API calls
        data = session.get("https://site.com/api/data").json()
        print(data)
    else:
        print("Login failed")
        driver.screenshot("login_error.png")
```
