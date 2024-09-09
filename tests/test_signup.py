from playwright.sync_api import expect
from pages.auth_page import AuthPage
from pages.home_page import HomePage
from utils.tools import take_screenshot

def test_register_user(
    home_page: HomePage,
    auth_page: AuthPage,
    username: str,
    email: str,
    password: str,
    first_name: str,
    last_name: str,
    company_name: str,
    address: str,
    address2: str,
    state: str,
    city: str,
    zipcode: str,
    mobile_number: str,
):
    """Test to verify the user registration process.
    This test simulates the user registration process on the Automation Exercise website.
    It verifies each step from navigating the homepage to filling in registration details,
    creating an account, and finally deleting the account.
    """
    home_page.verify_home_page_visible()
    home_page.click_sign_up_login_btn()
    expect(auth_page.new_user_signup).to_be_visible()
    auth_page.signUp(username, email)
    expect(auth_page.title).to_be_visible()
    auth_page.fill_account_info(password)
    auth_page.fill_adress_info(
        first_name=first_name,
        last_name=last_name,
        company=company_name,
        address=address,
        address2=address2,
        state=state,
        city=city,
        zipcode=zipcode,
        mobile_number=mobile_number,
    )
    take_screenshot(auth_page.page, "signup_form")
    expect(auth_page.account_created).to_be_visible()
    auth_page.click_continue_btn()
    expect(auth_page.get_logged_in_as_username(username)).to_be_visible()
    home_page.click_delete_account_btn()
    expect(home_page.account_deleted_text).to_be_visible()
    auth_page.continue_btn.click()

def test_register_user_with_existing_email(
    auth_page: AuthPage, home_page: HomePage, valid_login_creds: dict, username: str
):
    """
    Test registration with an already used email address.
    Verifies that attempting to register a new user with an existing email
    shows an appropriate error message indicating that the email address already exists.
    """
    home_page.verify_home_page_visible()
    home_page.click_sign_up_login_btn()
    expect(auth_page.new_user_signup).to_be_visible()
    auth_page.signUp(username, valid_login_creds["email"])
    expect(auth_page.email_already_exist).to_be_visible()
    expect(auth_page.email_already_exist).to_have_text("Email Address already exist!")
    take_screenshot(auth_page.page, "signup_error")
