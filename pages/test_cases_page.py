from playwright.sync_api import Page

class TCasesPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.test_cases_title = self.page.get_by_role("heading", name="Test Cases", exact=True)
        self.list_of_test_message = self.page.get_by_text("Below is the list of test")
    
