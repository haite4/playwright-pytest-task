from playwright.sync_api import Page

class CheckoutPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.first_name_last_name = self.page.locator('//*[@id="address_delivery"]/li[2]')
        self.company_name = self.page.locator('//*[@id="address_delivery"]/li[3]')
        self.address = self.page.locator('//*[@id="address_delivery"]/li[4]')
        self.address2 = self.page.locator('//*[@id="address_delivery"]/li[5]')
        self.country = self.page.locator('//*[@id="address_delivery"]/li[7]')
        self.phone_number = self.page.locator('//*[@id="address_delivery"]/li[8]')
        self.comment_text_area = self.page.locator("textarea[name=\"message\"]")
        self.place_order_btn = self.page.get_by_role("link", name="Place Order")
        
        
    def enter_comment_and_click_place_order_btn(self, comment: str) -> None:
        self.comment_text_area.fill(comment)
        self.place_order_btn.click()
        