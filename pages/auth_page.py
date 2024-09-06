from playwright.sync_api import Page, Locator
import random

class AuthPage:

    def __init__(self, page: Page):
        self.page = page
        self.new_user_signup = self.page.get_by_role("heading", name="New User Signup!")
        self.input_signup_name = self.page.get_by_placeholder("Name")
        self.input_signup_email = (
            self.page.locator("form")
            .filter(has_text="Signup")
            .get_by_placeholder("Email Address")
        )
        self.sign_up_btn = self.page.get_by_role("button", name="Signup")
        self.title = self.page.get_by_text("Enter Account Information")
        self.title_checkbox = self.page.get_by_label("Mr.")
        self.input_signup_password = self.page.get_by_label("Password *")
        self.select_days = self.page.locator("#days")
        self.select_months = self.page.locator("#months")
        self.select_years = self.page.locator("#years")
        self.datelist = [self.select_days, self.select_months, self.select_years]
        self.new_sletter_checkbox = self.page.get_by_label(
            "Sign up for our newsletter!"
        )
        self.special_offers_checkbox = self.page.get_by_label(
            "Receive special offers from"
        )
        self.first_name_input = self.page.get_by_label("First name *")
        self.last_name_input = self.page.get_by_label("Last name *")
        self.company_input = self.page.get_by_label("Company", exact=True)
        self.address_input = self.page.get_by_label("Address * (Street address, P.")
        self.address2_input = self.page.get_by_label("Address 2")
        self.select_country = self.page.get_by_label("Country *")
        self.state_input = self.page.get_by_label("State *")
        self.city_input = self.page.get_by_label("City *")
        self.zipcode_input = self.page.locator("#zipcode")
        self.mobile_number_input = self.page.get_by_label("Mobile Number *")
        self.create_account_btn = self.page.get_by_role("button", name="Create Account")
        self.account_created = self.page.get_by_text("Account Created!")
        self.continue_btn = self.page.get_by_role("link", name="Continue")
        self.login_to_your_account = self.page.get_by_role("heading", name="Login to your account")
        self.input_login_email = self.page.locator("form").filter(has_text="Login").get_by_placeholder("Email Address")
        self.input_login_password = self.page.get_by_placeholder("Password")
        self.login_btn = self.page.get_by_role("button", name="Login")
        self.error_message = self.page.get_by_text("Your email or password is")
        self.email_already_exist = self.page.get_by_text("Email Address already exist!")

        
    def click_continue_btn(self) -> None:
        self.continue_btn.click()


    def get_logged_in_as_username(self, username: str) -> Locator:
        return self.page.get_by_text(f"Logged in as {username}")


    def signUp(self, username, email) -> None:
        self.input_signup_name.fill(username)
        self.input_signup_email.fill(email)
        self.sign_up_btn.click()
        
        
    def login(self, email, password) -> None:
         self.input_login_email.fill(email)
         self.input_login_password.fill(password)
         self.login_btn.click()
        

    def fill_account_info(self, password) -> None:
        self.title_checkbox.wait_for(state='visible')
        self.title_checkbox.check()
        self.input_signup_password.fill(password)
        self.select_random_option(self.datelist)
        self.new_sletter_checkbox.check()
        self.special_offers_checkbox.check()


    def fill_adress_info(
        self,
        first_name,
        last_name,
        company,
        address,
        address2,
        state,
        city,
        zipcode,
        mobile_number,
    ) -> None:
        self.first_name_input.fill(first_name)
        self.last_name_input.fill(last_name)
        self.company_input.fill(company)
        self.address_input.fill(address)
        self.address2_input.fill(address2)
        self.select_random_option(self.select_country)
        self.state_input.fill(state)
        self.city_input.fill(city)
        self.zipcode_input.fill(zipcode)
        self.mobile_number_input.fill(mobile_number)
        self.create_account_btn.click()


    def select_random_option(self, locatorList) -> None:
        if isinstance(locatorList, list):     
            for dropdown in locatorList:
                options_number = dropdown.locator("option").count()
                index = self.get_random_index(options_number)
                dropdown.select_option(index=index)
        else:
            single_locator = locatorList
            options_number = single_locator.locator("option").count()
            index = self.get_random_index(options_number)
            single_locator.select_option(index=index)
            
        
    def get_random_index(self, number_of_options: int) -> int:
        return random.randint(1, number_of_options - 1)

    