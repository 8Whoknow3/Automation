from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, WebDriverException
import time

driver = webdriver.Chrome()
driver.maximize_window()

def login_test(username, password, test_name):
    try:
        driver.get("https://the-internet.herokuapp.com/login")
        time.sleep(1)

        user = driver.find_element(By.ID, "username")
        pwd = driver.find_element(By.ID, "password")
        btn = driver.find_element(By.CSS_SELECTOR, "button.radius")

        user.clear()
        pwd.clear()

        user.send_keys(username)
        pwd.send_keys(password)
        btn.click()

        time.sleep(1)
        message = driver.find_element(By.ID, "flash").text
        print(f"{test_name} → {message}")

    except NoSuchElementException:
        print(f"{test_name} → ❌ NoSuchElementException")
    except Exception as e:
        print(f"{test_name} → ❌ Exception: {e}")

# ✅ TC1: Login correct
login_test("tomsmith", "SuperSecretPassword!", "TC1 Correct Login")

# ❌ TC2: Wrong username
login_test("wronguser", "SuperSecretPassword!", "TC2 Wrong Username")

# ❌ TC3: Wrong password
login_test("tomsmith", "123456", "TC3 Wrong Password")

# ❌ TC4: Empty username
login_test("", "SuperSecretPassword!", "TC4 Empty Username")

# ❌ TC5: Empty password
login_test("tomsmith", "", "TC5 Empty Password")

# ❌ TC6: Empty fields
login_test("", "", "TC6 Both Empty")

# ❌ TC7: Long username
login_test("a"*100, "SuperSecretPassword!", "TC7 Long Username")

# ❌ TC8: Long password
login_test("tomsmith", "a"*100, "TC8 Long Password")

# ❌ TC9: Special characters
login_test("!@#$%", "!@#$%", "TC9 Special Characters")

# ❌ TC10: Website unreachable (Exception)
try:
    driver.get("http://wrong-url-test.com")
except WebDriverException:
    print("TC10 → ❌ WebDriverException (Site unreachable)")

# ❌ TC11: Element not found
try:
    driver.find_element(By.ID, "not_exist")
except NoSuchElementException:
    print("TC11 → ❌ NoSuchElementException (Element not found)")

driver.quit()
