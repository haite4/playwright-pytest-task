from playwright.sync_api import Page

class PaymentPage:

    def __init__(self, page: Page):
        self.page = page
        self.card_name = self.page.locator('input[name="name_on_card"]')
        self.card_number = self.page.locator('input[name="card_number"]')
        self.cvc_code = self.page.get_by_placeholder("ex.")
        self.expiration_date_month = self.page.get_by_placeholder("MM")
        self.expiration_date_year = self.page.get_by_placeholder("YYYY")
        self.pay_confirm_order_btn = self.page.get_by_role(
            "button", name="Pay and Confirm Order"
        )
        self.payment_success_message = self.page.get_by_text("Congratulations! Your order")


    def fill_payment_details(
        self,
        card_name,
        card_number,
        cvc_code,
        expiration_date_month,
        expiration_date_year,
    ) -> None:
        self.card_name.fill(card_name)
        self.card_number.fill(card_number)
        self.cvc_code.fill(cvc_code)
        self.expiration_date_month.fill(expiration_date_month)
        self.expiration_date_year.fill(expiration_date_year)
        self.pay_confirm_order_btn.click()
