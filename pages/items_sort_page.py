from selenium.webdriver.common.by import By
from pages.add_to_cart_page import Add_to_Cart


class SortItems(Add_to_Cart):
    SORT_BUTTON = (By.CSS_SELECTOR, 'select[data-test="product_sort_container"]')
    PRICES_LO_HI_BUTTON = (By.CSS_SELECTOR, 'option[value="lohi"]')
    PRICES_HI_LO_BUTTON = (By.CSS_SELECTOR, 'option[value="hilo"]')

    def sort_low_to_high(self):
        self.find(self.SORT_BUTTON).click()
        self.find(self.PRICES_LO_HI_BUTTON).click()

    def sort_high_to_low(self):
        self.find(self.SORT_BUTTON).click()
        self.find(self.PRICES_HI_LO_BUTTON).click()

    def verify_sort_low_to_high(self):
        prices_list = self.get_the_prices()
        assert prices_list[0] == min(prices_list), "Items not sorted low to high"

    def verify_high_to_low(self):
        prices_list = self.get_the_prices()
        assert prices_list[0] == max(prices_list), "Items not sorted high to low"
