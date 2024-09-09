from playwright.sync_api import expect
from pages.products_page import ProductsPage
from pages.home_page import HomePage
import re
from utils.tools import take_screenshot

def test_view_all_products_and_product_details(
    home_page: HomePage, products_page: ProductsPage
):
    """
    Test the functionality of viewing all products and product details.
    Verifies that the user can navigate to the 'All Products' page, see the product list,
    and view detailed information for a selected product, including name, price, category,
    availability, condition, and brand.
    """
    home_page.verify_home_page_visible()
    home_page.click_products_btn()
    expect(products_page.page).to_have_url("https://automationexercise.com/products")
    expect(products_page.all_products_text).to_have_text("All Products")
    expect(products_page.products_list_container).to_be_visible()
    products_page.click_product_view_btn()
    take_screenshot(products_page.page, "product_info")
    expect(products_page.product_name).to_be_visible()
    expect(products_page.product_price).to_be_visible()
    expect(products_page.product_category).to_be_visible()
    expect(products_page.product_availability).to_be_visible()
    expect(products_page.product_condition).to_be_visible()
    expect(products_page.product_brand).to_be_visible()

def test_search_product(home_page: HomePage, products_page: ProductsPage):
    """
    Test that verifies the functionality of searching for 'Tshirt' on the products page.
    The test checks that the page loads correctly, displays all products, and confirms that the products listed match the search query 'Tshirt'.
    """
    home_page.verify_home_page_visible()
    home_page.click_products_btn()
    expect(products_page.page).to_have_url("https://automationexercise.com/products")
    expect(products_page.all_products_text).to_have_text("All Products")
    products_page.search_product_by_name("Tshirt")
    take_screenshot(products_page.page, "search_result")
    expect(products_page.searched_product_text).to_be_visible()
    expect(products_page.searched_product_text).to_have_text("Searched Products")

    pattern = re.compile(r"T[ -]?shirt[s]?[ $]*", re.IGNORECASE)
    for product in products_page.products_items_text.all():
        product_text = product.inner_text()

        assert pattern.search(product_text)

    expect(products_page.page).to_have_url(re.compile(r"search=Tshirt"))
