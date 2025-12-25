from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import unittest
import time


class BookStoreTest(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--ignore-ssl-errors')
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.get("https://demoqa.com/books")
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def test_01_element_not_found_exception(self):
        try:
            element = self.driver.find_element(By.ID, "non_existent_element")
            self.fail("Expected NoSuchElementException but element was found")
        except NoSuchElementException:
            print("Test 1: NoSuchElementException caught")

    def test_02_timeout_exception(self):
        try:
            element = self.wait.until(
                EC.presence_of_element_located((By.ID, "element_that_never_appears"))
            )
            self.fail("Expected TimeoutException but element appeared")
        except TimeoutException:
            print("Test 2: TimeoutException caught")

    def test_03_element_not_interactable_exception(self):
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "searchBox"))
            )
            search_box.send_keys("Git")
            hidden_element = self.driver.find_element(By.CLASS_NAME, "hidden-element")
            hidden_element.click()
            self.fail("Expected ElementNotInteractableException")
        except (ElementNotInteractableException, NoSuchElementException):
            print("Test 3: ElementNotInteractableException caught")

    def test_04_stale_element_reference_exception(self):
        try:
            books = self.driver.find_elements(By.CLASS_NAME, "rt-tr-group")
            if books:
                self.driver.refresh()
                books[0].click()
                self.fail("Expected StaleElementReferenceException")
        except StaleElementReferenceException:
            print("Test 4: StaleElementReferenceException caught")

    def test_05_javascript_exception(self):
        try:
            self.driver.execute_script("invalidJavaScriptCode();")
            self.fail("Expected JavascriptException")
        except JavascriptException:
            print("Test 5: JavascriptException caught")

    def test_06_no_such_frame_exception(self):
        try:
            self.driver.switch_to.frame("non_existent_frame")
            self.fail("Expected NoSuchFrameException")
        except NoSuchFrameException:
            print("Test 6: NoSuchFrameException caught")
            self.driver.switch_to.default_content()

    def test_07_no_such_window_exception(self):
        try:
            self.driver.switch_to.window("non_existent_window")
            self.fail("Expected NoSuchWindowException")
        except NoSuchWindowException:
            print("Test 7: NoSuchWindowException caught")

    def test_08_no_alert_present_exception(self):
        try:
            alert = self.driver.switch_to.alert
            alert.accept()
            self.fail("Expected NoAlertPresentException")
        except NoAlertPresentException:
            print("Test 8: NoAlertPresentException caught")

    def test_09_invalid_selector_exception(self):
        try:
            self.driver.find_element(By.XPATH, "//invalid[xpath]")
            self.fail("Expected InvalidSelectorException")
        except InvalidSelectorException:
            print("Test 9: InvalidSelectorException caught")

    def test_10_invalid_element_state_exception(self):
        try:
            search_box = self.wait.until(
                EC.presence_of_element_located((By.ID, "searchBox"))
            )
            self.driver.execute_script("arguments[0].disabled = true;", search_box)
            search_box.send_keys("Test")
            self.fail("Expected InvalidElementStateException")
        except InvalidElementStateException:
            print("Test 10: InvalidElementStateException caught")

    def test_11_move_target_out_of_bounds_exception(self):
        try:
            from selenium.webdriver.common.action_chains import ActionChains
            actions = ActionChains(self.driver)
            actions.move_by_offset(10000, 10000).perform()
            print("Test 11: Mouse movement successful")
        except MoveTargetOutOfBoundsException:
            print("Test 11: MoveTargetOutOfBoundsException caught")

    def test_12_combined_exceptions(self):
        exceptions_caught = []
        try:
            self.driver.find_element(By.ID, "ghost_element")
        except NoSuchElementException:
            exceptions_caught.append("NoSuchElementException")

        try:
            self.wait.until(
                EC.element_to_be_clickable((By.ID, "never_clickable"))
            )
        except TimeoutException:
            exceptions_caught.append("TimeoutException")

        try:
            self.driver.switch_to.alert
        except NoAlertPresentException:
            exceptions_caught.append("NoAlertPresentException")

        print(f"Test 12: Exceptions caught: {exceptions_caught}")
        self.assertGreaterEqual(len(exceptions_caught), 2)

    def test_13_normal_operation(self):
        try:
            search_box = self.wait.until(
                EC.element_to_be_clickable((By.ID, "searchBox"))
            )
            search_box.clear()
            search_box.send_keys("JavaScript")
            time.sleep(2)
            books = self.driver.find_elements(By.CLASS_NAME, "rt-tr-group")
            self.assertGreater(len(books), 0)
            print("Test 13: Normal operation successful")
        except Exception as e:
            self.fail(f"Normal operation failed: {str(e)}")

    def test_14_navigation_exceptions(self):
        try:
            current_url = self.driver.current_url
            self.driver.get("https://invalid-url-that-does-not-exist.xyz")
            self.driver.back()
            self.assertEqual(self.driver.current_url, current_url)
            print("Test 14: Navigation successful")
        except (WebDriverException, InvalidArgumentException):
            print("Test 14: WebDriverException caught")


def main():
    test_suite = unittest.TestLoader().loadTestsFromTestCase(BookStoreTest)
    runner = unittest.TextTestRunner(verbosity=2)

    print("=" * 60)
    print("Starting Book Store Automated Tests")
    print("=" * 60)

    result = runner.run(test_suite)

    print("=" * 60)
    print("Test Results:")
    print(f"Tests run: {result.testsRun}")
    print(f"Errors: {len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print("=" * 60)

    return result


if __name__ == "__main__":
    result = main()
    exit_code = 0 if len(result.errors) == 0 and len(result.failures) == 0 else 1
    exit(exit_code)