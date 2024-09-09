from playwright.sync_api import Page

class ProductsPage:
    
    def __init__(self, page: Page):
        self.page = page
        self.all_products_text = self.page.get_by_role("heading", name="All Products")
        self.products_list_container = self.page.get_by_text("All Products  Added! Your")
        self.product_view_btn = self.page.locator(".choose > .nav > li > a").first
        self.product_name = self.page.get_by_role("heading", name="Blue Top")
        self.product_category = self.page.get_by_text("Category: Women > Tops")
        self.product_price = self.page.get_by_text("Rs.")
        self.product_availability = self.page.get_by_text("Availability: In Stock")
        self.product_condition = self.page.get_by_text("Condition: New")
        self.product_brand = self.page.get_by_text("Brand: Polo")
        self.search_input = self.page.get_by_placeholder("Search Product")
        self.submit_search_btn = self.page.get_by_role("button", name="")
        self.searched_product_text = self.page.get_by_role("heading", name="Searched Products")
        self.products_items_text = self.page.locator(".overlay-content p")
        self.product_info_btn = self.page.locator(".productinfo > .btn")
        self.continue_shopping_btn = self.page.get_by_role("button", name="Continue Shopping")
        self.view_cart_btn = self.page.get_by_role("link", name="View Cart")
        self.add_to_cart_overlay = self.page.locator(".overlay-content > .btn")
        self.product_quantity = self.page.locator("#quantity")
        self.add_to_cart_btn = self.page.get_by_role("button", name=" Add to cart")
        
    def click_product_view_btn(self) -> None:
        self.product_view_btn.click()
        
    def search_product_by_name(self, product_name: str) -> None:
        self.search_input.fill(product_name)
        self.submit_search_btn.click()
    
    def click_add_to_cart_btn_first(self) -> None:
        first_product = self.product_info_btn.nth(0)
        first_product.hover()
        add_to_cart_button_first = self.add_to_cart_overlay.nth(0)
        add_to_cart_button_first.wait_for(state='visible') 
        add_to_cart_button_first.click()
    
    def click_add_to_cart_btn_second(self) -> None:
        second_product = self.product_info_btn.nth(1)
        second_product.hover()
        add_to_cart_button_second = self.add_to_cart_overlay.nth(1)
        add_to_cart_button_second.wait_for(state='visible') 
        add_to_cart_button_second.click()
        
    def click_continue_shopping_btn(self) -> None:
        self.continue_shopping_btn.click()
   
    def click_view_cart_btn(self) -> None:
        self.view_cart_btn.click()
    
    def increase_product_quantity(self, quantity: str):
        self.product_quantity.fill(quantity)
    
    def click_add_to_cart_btn(self):
        self.add_to_cart_btn.click()