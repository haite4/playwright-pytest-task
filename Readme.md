# Playwright + pytest + github actions

## Introduction
This repository contains automated tests using Playwright and pytest, written specifically for the website [Automation Exercise](https://www.automationexercise.com/). It includes 15 test cases for login, registration, cart functionality, checkout, payment, and more. Tests are run across different browsers and managed via GitHub Actions, with results available on GitHub Pages.

## Requirements
- **Python**: Version 3.11 or higher
- **Dependencies**:
  - `faker`: Version 28.1.0  or higher
  - `allure-pytest`: Version 2.13.5 or higher
  - `pytest-xdist`: Version 3.6.1 or higher
  
  - `allure-python-commons`: Version 2.13.5 or higher
  
   - `pipenv`: version 2024.0.1
  

## Steps to Install
1. Install Python:

    [Python](https://www.python.org/downloads/)

2. Clone the repository:
    ```sh
    https://github.com/haite4/playwright-pytest-task
    ```
3. Navigate to the project directory:
    ```sh 
    cd playwright-pytest-task
    ```
4. Install Pipenv:
    ```sh
    pip install pipenv
    ```

5. Install dependencies:
    ```sh
    pipenv install --system
    ``` 
6. Install chromium browser:
    ```sh
    playwright install chromium
    ```

## Steps to Launch

1. **Run all tests on Chrome:**:
    ```sh
    pytest --browser_name chromium
    ```
2. **Run all tests on Firefox:**
    ```sh
    pytest --browser_name firefox
    ```
3. **Run all tests on Webkit:**
    ```sh
    pytest --browser_name webkit
    ```
4. **Run all tests on Firefox in parallel:**
    ```sh
    pytest -n 3 --browser_name firefox
    ```

5. **Run all tests on Chrome in parallel:**
    ```sh
    pytest -n 3 --browser_name chromium
    ```
8. **Run all tests on Webkit in parallel:**
    ```sh
    pytest -n 3 --browser_name webkit
    ```
9. **Run all signup tests**
    ```sh 
    pytest -k test_signup
    ```
10. **Run all subscription tests**
    ```sh 
    pytest -k test_subscription
    ```

11. **Run all test cases tests**
    ```sh 
    pytest -k test_test_cases
    ```
12. **Run all products tests**
    ```sh 
    pytest -k test_products
    ```  

12. **Run all place order tests**
    ```sh 
    pytest -k test_place_order
    ```
13. **Run all logout tests**
    ```sh 
    pytest -k test_logout
    ```
14. **Run all login tests**
    ```sh 
    pytest -k test_login
    ```
15. **Run all contact us tests**
    ```sh 
    pytest -k test_contact_us
    ```
16. **Run all cart  tests**
    ```sh 
    pytest -k test_cart
    ```

## Generate Allure Report: 

1. **Test report generated automatically after each test run overriding the previous report. Use this command to see the report:**
    ```sh
    allure serve allure-results
    ```


## GitHub Actions Integration

The GitHub Actions workflow is set up to automatically run the Playwright + pytest test suite for a Python web automation project. After running the tests, the results are published using Allure Reports and deployed to GitHub Pages. The workflow also sends notifications via Slack about the test status. You can view the test results at the following link:

[View Test Results](https://haite4.github.io/playwright-pytest-task/8/index.html)

### Summary
- **Test Coverage:**: The project includes 15 test cases covering login, registration, shopping cart, checkout, payment, and other functionalities.
- **GitHub Actions Workflow:**: The workflow installs dependencies, runs Playwright tests on Chromium, generates Allure reports, and deploys the report to GitHub Pages.
- **Result Publication:**: Test results are automatically published to GitHub Pages for easy access to detailed insights and reports.