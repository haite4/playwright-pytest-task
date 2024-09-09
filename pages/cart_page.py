from playwright.sync_api import Page

class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_items_rows = (
            self.page.locator("#cart_info_table").locator("tbody").locator("tr")
        )
        self.cart_price = self.page.locator(".cart_price")
        self.cart_quantity = self.page.locator(".cart_quantity")
        self.cart_total = self.page.locator(".cart_total")
        self.shopping_cart_text = self.page.get_by_text("Shopping Cart")
        self.proceed_to_checkout_btn = self.page.get_by_text("Proceed To Checkout")
        self.register_login_btn = self.page.get_by_role("link", name="Register / Login")

    def click_proceed_to_checkout_btn(self) -> None:
        self.proceed_to_checkout_btn.click()

    def click_register_login_btn(self) -> None:
        self.register_login_btn.click()

    def products_prices(self) -> list[float]:
        return [
            float(price.inner_text().replace("Rs.", "").strip())
            for price in self.cart_price.all()
        ]

    def products_quantities(self) -> list[int]:
        return [
            int(quantity.inner_text().strip()) for quantity in self.cart_quantity.all()
        ]

    def product_expected_total(self) -> list[float]:
        result = []
        for price in self.products_prices():
            for quantity in self.products_quantities():
                total = price * quantity
            result.append(total)
        return result

    def product_actual_total(self) -> list[float]:
        actual_total = [
            float(total.inner_text().replace("Rs.", "").strip())
            for total in self.cart_total.all()
        ]
        return actual_total
