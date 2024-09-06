from playwright.sync_api import Page, expect

class HomePage:

    def __init__(self, page: Page):
        self.page = page
        self.signup_login_btn = self.page.get_by_role("link", name=" Signup / Login")
        self.home_btn = self.page.get_by_role("link", name=" Home")
        self.carousel_inner = self.page.locator(".carousel-inner").first
        self.delete_account_btn = self.page.get_by_role("link", name=" Delete Account")
        self.account_deleted_text = self.page.get_by_text("Account Deleted!")
        self.logout_btn = self.page.get_by_role("link", name=" Logout")
        self.contact_us_btn = self.page.get_by_role("link", name=" Contact us")
        self.test_cases_btn = self.page.get_by_role("link", name=" Test Cases")
        self.products_btn = self.page.get_by_role("link", name=" Products")
        self.footer = self.page.locator("#footer")
        self.subscription_text = self.page.get_by_role("heading", name="Subscription")
        self.subscription_email_input = self.page.get_by_placeholder("Your email address")
        self.subscription_submit_btn = self.page.get_by_role("button", name="")
        self.subscription_success_message = self.page.get_by_text("You have been successfully")
        self.cart_btn = self.page.get_by_role("link", name=" Cart")
        self.view_product = self.page.locator(".choose > .nav > li > a")
        
        
    def click_sign_up_login_btn(self) -> None:
        self.signup_login_btn.click()


    def click_delete_account_btn(self) -> None:
        self.delete_account_btn.click()


    def click_logout_btn(self) -> None:
        self.logout_btn.click()
        
        
    def click_home_btn(self) -> None:
        self.home_btn.click()
    
    
    def click_contact_us_btn(self) -> None:
        self.contact_us_btn.click()
    
    
    def click_test_cases_btn(self) -> None:
        self.test_cases_btn.click()
    
    
    def click_products_btn(self) -> None:
        self.products_btn.click()
        
        
    def scroll_down_to_footer(self) -> None:
        self.footer.scroll_into_view_if_needed()
        
        
    def fill_subscription(self, email) -> None:
        self.subscription_email_input.fill(email)
        self.subscription_submit_btn.click()
    
    
    def click_cart_btn(self) -> None:
        self.cart_btn.click()
    
    
    def verify_home_page_visible(self) -> None:
        expect(self.page).to_have_url("https://automationexercise.com/")
        expect(self.signup_login_btn).to_be_visible()
        expect(self.home_btn).to_have_css("color", "rgb(255, 165, 0)")
        expect(self.carousel_inner).to_be_visible()
        
    
    def click_view_product(self) -> None:
        self.view_product.first.click()
        