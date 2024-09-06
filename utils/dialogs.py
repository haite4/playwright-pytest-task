def handle_consent(page):
    conset_button_selector = page.locator(".fc-primary-button").first
    if conset_button_selector.is_visible():
        conset_button_selector.click()    
