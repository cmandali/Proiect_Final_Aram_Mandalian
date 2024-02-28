from browser import Browser


class BasePage(Browser):

    def find(self, locator):
        return self.driver.find_element(*locator)

    def find_more_than_one(self, locator):
        return self.driver.find_elements(*locator)

    def type(self, locator, text_to_type):
        self.find(locator).send_keys(text_to_type)

    def get_text(self, locator):
        return self.find(locator).text

    def is_url_correct(self, expected_url):
        return self.driver.current_url == expected_url

