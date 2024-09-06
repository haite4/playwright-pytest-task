from playwright.sync_api import expect
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from utils.tools import take_screenshot

def test_logout_user(auth_page: AuthPage, home_page: HomePage, valid_login_creds: dict):
    """
    Verify that a user can log out and is redirected to the login page.
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
    home_page.click_logout_btn()
    take_screenshot(home_page.page, "logout_btn_click")
    expect(auth_page.page).to_have_url("https://automationexercise.com/login")
    
