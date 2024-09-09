from playwright.sync_api import Page

class ContactUsPage:

    def __init__(self, page: Page):
        self.page = page
        self.get_in_touch_text = self.page.get_by_role("heading", name="Get In Touch")
        self.name_input = self.page.get_by_placeholder("Name")
        self.email_input = self.page.get_by_placeholder("Email", exact=True)
        self.subject_input = self.page.get_by_placeholder("Subject")
        self.text_area_input = self.page.get_by_placeholder("Your Message Here")
        self.upload_file_input = self.page.locator('input[name="upload_file"]')
        self.submit_btn = self.page.get_by_role("button", name="Submit")
        self.success_message = self.page.locator("#contact-page").get_by_text("Success! Your details have")
        self.home_btn = self.page.get_by_role("link", name=" Home")
          
    def fill_contact_us_form(self, name, email, subject, message, file_path) -> None:
        self.name_input.fill(name)
        self.email_input.fill(email)
        self.subject_input.fill(subject)
        self.text_area_input.fill(message)
        self.upload_file_input.set_input_files(file_path)
        
    def click_submit_btn(self) -> None:
        self.submit_btn.click()

    def click_home_btn(self) -> None:
        self.home_btn.click()
        
        