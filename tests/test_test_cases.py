from pages.home_page import HomePage
from pages.test_cases_page import TCasesPage
from playwright.sync_api import expect
from utils.tools import take_screenshot

def test_verify_test_cases_page(home_page: HomePage, test_cases_page: TCasesPage):
    """
    Verify that the Test Cases Page loads correctly.
    Checks that the Test Cases Page is accessible, displays the correct title,
    and contains the expected introductory text.
    """
    home_page.verify_home_page_visible()
    home_page.click_test_cases_btn()
    take_screenshot(test_cases_page.page, "test_cases_page")
    expect(test_cases_page.test_cases_title).to_be_visible()
    expect(test_cases_page.page).to_have_url(
        "https://automationexercise.com/test_cases"
    )
    expect(test_cases_page.list_of_test_message).to_have_text(
        "Below is the list of  test Cases for you to practice the Automation. Click on the scenario for detailed Test Steps:"
    )
