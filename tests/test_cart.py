from pages.home_page import HomePage
from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from utils.tools import take_screenshot
import re

def test_add_product_in_cart(
    home_page: HomePage, products_page: ProductsPage, cart_page: CartPage
):
    """
    Test case to verify that adding two products to the cart reflects the correct prices, quantities, and total amounts.
    """
    home_page.verify_home_page_visible()
    home_page.click_products_btn()
    products_page.click_add_to_cart_btn_first()
    products_page.click_continue_shopping_btn()
    products_page.click_add_to_cart_btn_second()
    products_page.click_view_cart_btn()
    take_screenshot(products_page.page, "cart_items")
    expect(cart_page.cart_items_rows).to_have_count(2)
    assert len(cart_page.products_prices()) == len(cart_page.products_quantities())
    assert cart_page.product_expected_total() == cart_page.product_actual_total()

def test_product_quantity_in_cart(
    home_page: HomePage, cart_page: CartPage, products_page: ProductsPage
):
    """
    Verifies that the product quantity is updated to 4 in the cart after adding the product.
    """
    home_page.verify_home_page_visible()
    home_page.click_view_product()
    expect(products_page.page).to_have_url(re.compile(r"product_details"))
    products_page.increase_product_quantity("4")
    products_page.click_add_to_cart_btn()
    products_page.click_view_cart_btn()
    take_screenshot(products_page.page, "cart_quantity")
    assert cart_page.products_quantities()[0] == 4
