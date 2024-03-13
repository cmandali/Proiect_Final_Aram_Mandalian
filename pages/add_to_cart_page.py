import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage


class Add_to_Cart(LoginPage):
    ADD_TO_CART_BUTTONS = (By.CLASS_NAME, "btn")
    SHOPPING_BASKET_BUTTONS = (By.ID, "shopping_cart_container")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POSTAL_CODE_INPUT = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    ITEMS_IN_BASKET = (By.CLASS_NAME, "inventory_item_price")
    TAX_VALUE = (By.CLASS_NAME, "summary_tax_label")
    TOTAL_AMOUNT_INCL_TAXES = (By.CLASS_NAME, "summary_total_label")
    ALL_ITEMS_BUTTON = (By.ID, "inventory_sidebar_link")
    REMOVE_ITEMS = (By.XPATH, '//div/button[text()="Remove"]')

    def all_items_page(self):
        self.open()
        self.enter_name("standard_user")
        self.enter_password("secret_sauce")
        self.click_login()
        time.sleep(1)

# adding the desired quantity of items in your shooping cart
    def add_to_cart(self, number_of_products):
        items = self.find_more_than_one(self.ADD_TO_CART_BUTTONS)
        for btn in items:
            if btn in items[0:int(number_of_products)]:
                btn.click()
            else:
                pass

    def navigate_to_shopping_basket(self):
        self.find(self.SHOPPING_BASKET_BUTTONS).click()

    def proceed_to_checkout(self):
        checkout = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CHECKOUT_BUTTON))
        checkout.click()

    def complete_form(self, first_name, last_name, postal_code):
        self.type(self.FIRST_NAME_INPUT, first_name)
        self.type(self.LAST_NAME_INPUT, last_name)
        self.type(self.POSTAL_CODE_INPUT, postal_code)

    def continue_to_checkout(self):
        proceed = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.CONTINUE_BUTTON))
        proceed.click()

    def check_number_of_products(self, number):
        items_in_basket = self.find_more_than_one(self.ITEMS_IN_BASKET)
        assert len(items_in_basket) == int(number), "Unmatching number of products"

    # below function will get all the prices of the products similar to: "19.99 $" in a list and then will return a list of floats
    def get_the_prices(self):
        items_in_basket = self.find_more_than_one(self.ITEMS_IN_BASKET)
        items_text = []
        for item in items_in_basket:
            items_text.append(item.text)

        # replacing characters that are not digits
        items_prices = []
        for prices in items_text:
            items_prices.append(prices.replace("$", ""))

        # casting all elements to floats to return a newly created list which contains only floats
        items_prices_floats = []
        for price_value in items_prices:
            items_prices_floats.append(float(price_value))

        return items_prices_floats

    def verify_total_amount(self):
        items_prices_floats = self.get_the_prices()
        tax = self.find(self.TAX_VALUE).text
        tax_value = float(tax.replace("Tax: $", ""))
        total_items_value = sum(items_prices_floats)
        total_amount = self.find(self.TOTAL_AMOUNT_INCL_TAXES).text
        total_amount_value = float(total_amount.replace("Total: $", ""))
        assert tax_value + total_items_value == total_amount_value, "Total not correct"

    def navigate_to_all_items_page(self):
        self.find(self.MENU_BUTTON).click()
        self.find(self.ALL_ITEMS_BUTTON).click()

# remove the desired quantity of items from your shooping cart    
    def remove_items(self, item_removed):
        items_removed = self.find_more_than_one(self.REMOVE_ITEMS)
        for btn_remove in items_removed:
            if btn_remove in items_removed[0:int(item_removed)]:
                btn_remove.click()
            else:
                pass

        def add_desired_items(self, desired_item):
        items = self.find_more_than_one(self.ALL_ITEMS)
        for item in items:
            if desired_item.replace("-", " ").lower() in item.text.replace("-", " ").lower():
                add_to_cart_button = item.find_element(By.XPATH, "//button[contains(text(),'Add to cart')]")
                add_to_cart_button.click()

    def confirm_order(self):
        self.find(self.FINISH_BUTTON).click()

    def check_confirmation(self):
        assert "Thank you for your order" in self.find(self.CONFIRMATION_TEXT).text
