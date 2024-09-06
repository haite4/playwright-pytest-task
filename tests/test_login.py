from playwright.sync_api import expect
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from utils.tools import take_screenshot

def test_user_login_with_valid_credentials(
    home_page: HomePage, auth_page: AuthPage, valid_login_creds: dict
):
    """
    Test the login functionality with valid credentials.
    Verifies that a user can log in, check for successful login confirmation,
    and then delete the account on the Automation Exercise website.
    """
    home_page.verify_home_page_visible()
    home_page.click_sign_up_login_btn()
    expect(auth_page.login_to_your_account).to_be_visible()
    auth_page.login(
        email=valid_login_creds["email"], password=valid_login_creds["password"]
    )
    expect(
        auth_page.get_logged_in_as_username(valid_login_creds["username"])
    ).to_be_visible()
    take_screenshot(home_page.page, "logged_as_username")
    home_page.click_delete_account_btn()
    expect(home_page.account_deleted_text).to_be_visible()


def test_user_login_with_incorrect_credentials(
    home_page: HomePage, auth_page: AuthPage, email: str, password: str
):
    """
    Test login with incorrect credentials.

    Verifies that an error message is shown when attempting to log in with invalid email and  password.
    """
    home_page.verify_home_page_visible()
    home_page.click_sign_up_login_btn()
    expect(auth_page.login_to_your_account).to_be_visible()
    auth_page.login(email=email, password=password)
    expect(auth_page.error_message).to_be_visible()
    expect(auth_page.error_message).to_have_text("Your email or password is incorrect!")
    take_screenshot(auth_page.page, "login_error_message")