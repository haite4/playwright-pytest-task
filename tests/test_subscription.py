from pages.home_page import HomePage
from playwright.sync_api import expect
from utils.tools import take_screenshot

def test_subscription_functionality_on_home_page(home_page: HomePage, email: str):
    """
    Verify that users can successfully subscribe to the newsletter from the home page.
    """
    home_page.verify_home_page_visible()
    home_page.scroll_down_to_footer()
    expect(home_page.subscription_text).to_be_visible()
    take_screenshot(home_page.page, "subscription_home_form")
    expect(home_page.subscription_text).to_have_text("Subscription")
    home_page.fill_subscription(email)
    expect(home_page.subscription_success_message).to_be_visible()
    expect(home_page.subscription_success_message).to_have_text(
        "You have been successfully subscribed!"
    )

def test_subscription_functionality_on_cart_page(home_page: HomePage, email: str):
    """
    Verify that users can successfully subscribe to the newsletter from the cart page.
    """
    home_page.verify_home_page_visible()
    home_page.click_cart_btn()
    home_page.scroll_down_to_footer()
    take_screenshot(home_page.page, "subscription_cart_form")
    expect(home_page.subscription_text).to_be_visible()
    expect(home_page.subscription_text).to_have_text("Subscription")
    home_page.fill_subscription(email)
    expect(home_page.subscription_success_message).to_be_visible()
    expect(home_page.subscription_success_message).to_have_text(
        "You have been successfully subscribed!"
    )
