from pages.checkout_page import CheckoutPage
from pages.home_page import HomePage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.auth_page import AuthPage
from pages.payment_page import PaymentPage
from playwright.sync_api import expect
import re
from utils.tools import take_screenshot

def test_register_while_checkout(
    home_page: HomePage,
    checkout_page: CheckoutPage,
    products_page: ProductsPage,
    cart_page: CartPage,
    auth_page: AuthPage,
    payment_page: PaymentPage,
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
    message: str,
    card_number: str,
    cvc_code: str,
    expiration_date: str,
):
    """This test verifies the functionality of registering a new user during the checkout process.
    It includes adding a product to the cart, proceeding to checkout, registering a new user,
    filling in account and address details, placing the order, and confirming the order and payment.
    The test also ensures the user account is deleted after the purchase.
    """
    home_page.verify_home_page_visible()
    products_page.click_add_to_cart_btn_first()
    products_page.click_continue_shopping_btn()
    home_page.click_cart_btn()
    expect(cart_page.shopping_cart_text).to_have_text("Shopping Cart")
    expect(cart_page.page).to_have_url("https://automationexercise.com/view_cart")
    cart_page.click_proceed_to_checkout_btn()
    cart_page.click_register_login_btn()
    auth_page.signUp(username, email)
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
    expect(auth_page.account_created).to_be_visible()
    expect(auth_page.account_created).to_have_text("Account Created!")
    auth_page.click_continue_btn()
    expect(auth_page.get_logged_in_as_username(username)).to_be_visible()
    expect(auth_page.get_logged_in_as_username(username)).to_have_text(
        f"Logged in as {username}"
    )
    home_page.click_cart_btn()
    cart_page.click_proceed_to_checkout_btn()
    expect(checkout_page.first_name_last_name).to_have_text(
        re.compile(f"{first_name} {last_name}")
    )
    expect(checkout_page.company_name).to_have_text(company_name)
    expect(checkout_page.address).to_have_text(address)
    expect(checkout_page.address2).to_have_text(address2)
    expect(checkout_page.phone_number).to_have_text(mobile_number)
    take_screenshot(checkout_page.page, "checkout_details")
    assert len(cart_page.products_prices()) == len(cart_page.products_quantities())
    assert cart_page.product_expected_total() == cart_page.product_actual_total()
    assert cart_page.products_quantities()[0] == 1
    checkout_page.enter_comment_and_click_place_order_btn(comment=message)
    payment_page.fill_payment_details(
        card_name=f"{first_name} {last_name}",
        card_number=card_number,
        cvc_code=cvc_code,
        expiration_date_month=expiration_date["month"],
        expiration_date_year=expiration_date["year"],
    )
    take_screenshot(payment_page.page, "payment_cart_details")
    expect(payment_page.payment_success_message).to_have_text(
        "Congratulations! Your order has been confirmed!"
    )
    home_page.click_delete_account_btn()
    expect(home_page.account_deleted_text).to_have_text("Account Deleted!")
    auth_page.click_continue_btn()


def test_register_before_checkout(
    home_page: HomePage,
    checkout_page: CheckoutPage,
    products_page: ProductsPage,
    cart_page: CartPage,
    auth_page: AuthPage,
    payment_page: PaymentPage,
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
    message: str,
    card_number: str,
    cvc_code: str,
    expiration_date: str,
):
    """
    This test verifies the registration of a new user before starting the checkout process.
    It includes registering a user, adding a product to the cart, verifying account details at checkout,
    placing an order, confirming payment, and deleting the user account after the purchase.
    """
    home_page.verify_home_page_visible()
    home_page.click_sign_up_login_btn()
    auth_page.signUp(username, email)
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
    expect(auth_page.account_created).to_be_visible()
    expect(auth_page.account_created).to_have_text("Account Created!")
    auth_page.click_continue_btn()
    expect(auth_page.get_logged_in_as_username(username)).to_be_visible()
    expect(auth_page.get_logged_in_as_username(username)).to_have_text(
        f"Logged in as {username}"
    )
    products_page.click_add_to_cart_btn_first()
    products_page.click_view_cart_btn()
    expect(cart_page.shopping_cart_text).to_have_text("Shopping Cart")
    expect(cart_page.page).to_have_url("https://automationexercise.com/view_cart")
    cart_page.click_proceed_to_checkout_btn()
    expect(checkout_page.first_name_last_name).to_have_text(
        re.compile(f"{first_name} {last_name}")
    )
    expect(checkout_page.company_name).to_have_text(company_name)
    expect(checkout_page.address).to_have_text(address)
    expect(checkout_page.address2).to_have_text(address2)
    expect(checkout_page.phone_number).to_have_text(mobile_number)
    take_screenshot(checkout_page.page, "checkout_delivery_details")
    assert len(cart_page.products_prices()) == len(cart_page.products_quantities())
    assert cart_page.product_expected_total() == cart_page.product_actual_total()
    assert cart_page.products_quantities()[0] == 1
    checkout_page.enter_comment_and_click_place_order_btn(comment=message)
    payment_page.fill_payment_details(
        card_name=f"{first_name} {last_name}",
        card_number=card_number,
        cvc_code=cvc_code,
        expiration_date_month=expiration_date["month"],
        expiration_date_year=expiration_date["year"],
    )
    expect(payment_page.payment_success_message).to_have_text(
        "Congratulations! Your order has been confirmed!"
    )
    home_page.click_delete_account_btn()
    expect(home_page.account_deleted_text).to_have_text("Account Deleted!")
    auth_page.click_continue_btn()
