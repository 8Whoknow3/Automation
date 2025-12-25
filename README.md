# Selenium Automation Tests Repository

This repository contains two Python scripts demonstrating Selenium WebDriver usage for automated web testing, focusing on handling common exceptions and performing practical test cases.

## Files

### 1. `book_store_test.py`
A comprehensive **unittest-based** test suite that runs on the [DEMOQA Book Store](https://demoqa.com/books) application.

The purpose of this script is to **demonstrate and verify proper handling of various Selenium exceptions** in a structured testing framework.

#### Tests Included:
- `test_01_element_not_found_exception` → NoSuchElementException
- `test_02_timeout_exception` → TimeoutException
- `test_03_element_not_interactable_exception` → ElementNotInteractableException
- `test_04_stale_element_reference_exception` → StaleElementReferenceException
- `test_05_javascript_exception` → JavascriptException
- `test_06_no_such_frame_exception` → NoSuchFrameException
- `test_07_no_such_window_exception` → NoSuchWindowException
- `test_08_no_alert_present_exception` → NoAlertPresentException
- `test_09_invalid_selector_exception` → InvalidSelectorException
- `test_10_invalid_element_state_exception` → InvalidElementStateException (disabled element)
- `test_11_move_target_out_of_bounds_exception` → MoveTargetOutOfBoundsException
- `test_12_combined_exceptions` → Multiple exception handling in one test
- `test_13_normal_operation` → Successful search for "JavaScript" books
- `test_14_navigation_exceptions` → Handling invalid URL navigation

The script uses `unittest.TextTestRunner` to run all tests and provides a clear summary at the end.

### 2. `Login Test.py`
A simple **procedural script** that performs multiple login attempts on the popular [Herokuapp Login Page](https://the-internet.herokuapp.com/login).

It demonstrates both **positive and negative test cases** for a login form, including edge cases and exception handling.

#### Test Cases Included:
- TC1: Valid credentials (expected success)
- TC2–TC9: Various invalid inputs (wrong username/password, empty fields, long inputs, special characters)
- TC10: Attempt to access unreachable URL → WebDriverException
- TC11: Searching for non-existent element → NoSuchElementException

Each case prints a clear result message.

## Prerequisites

- Python 3.6+
- Google Chrome browser installed
- ChromeDriver compatible with your Chrome version (managed automatically if using `webdriver-manager`, or place in PATH)

## Installation

```bash
git clone https://github.com/your-username/selenium-exception-tests.git
cd selenium-exception-tests

# Recommended: Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install selenium
```

> Optional (recommended for automatic ChromeDriver management):
> ```bash
> pip install webdriver-manager
> ```
> Then modify the driver initialization to use `WebDriverManager` (not included in current scripts).

## Running the Tests

### Run the Book Store unittest suite:
```bash
python book_store_test.py
```

You will see detailed output for each test, followed by a summary of runs, failures, and errors.

### Run the Login test script:
```bash
python "Login Test.py"
```

Output will show results for each test case (TC1–TC11).

## Notes

- Both scripts use explicit `time.sleep()` in some places — in production tests, prefer `WebDriverWait` for better reliability.
- The Book Store tests intentionally trigger exceptions to verify they are caught correctly.
- These scripts are excellent for learning Selenium exception handling and basic automation patterns.



