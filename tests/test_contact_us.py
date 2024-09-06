from playwright.sync_api import expect
from pages.home_page import HomePage
from pages.contact_us_page import ContactUsPage
from utils.tools import take_screenshot

def test_contact_us_form(
    home_page: HomePage,
    contact_us_page: ContactUsPage,
    username: str,
    email: str,
    subject: str,
    message: str,
):  
    """
    Verify the functionality of the 'Contact Us' form.
    Ensures that the contact form can be successfully submitted with valid details,
    checks for the appearance of a success message, and confirms navigation back to
    the home page with expected elements visible.
    """
    home_page.verify_home_page_visible()
    home_page.click_contact_us_btn()
    expect(contact_us_page.get_in_touch_text).to_be_visible()
    expect(contact_us_page.get_in_touch_text).to_have_text("Get In Touch")
    contact_us_page.fill_contact_us_form(
        name=username,
        email=email,
        subject=subject,
        message=message,
        file_path="data/txt_files/simple.txt",
    )
    take_screenshot(contact_us_page.page, "contact_us_form")
    contact_us_page.page.on("dialog", lambda dialog: dialog.accept())
    with contact_us_page.page.expect_event("dialog"):
        contact_us_page.click_submit_btn()

    expect(contact_us_page.success_message).to_be_visible()
    expect(contact_us_page.success_message).to_have_text(
        "Success! Your details have been submitted successfully."
    )
    contact_us_page.click_home_btn()
    expect(home_page.page).to_have_url("https://automationexercise.com/")
    expect(home_page.carousel_inner).to_be_visible()
