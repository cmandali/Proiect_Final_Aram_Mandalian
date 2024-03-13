from selenium.webdriver.support import expected_conditions as EC


class LoginPage(BasePage):
    LOGIN_PAGE_URL = "https://www.saucedemo.com/"
    USER_NAME_BOX = (By.ID, "user-name")
    PASSWORD_BOX = (By.ID, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "input[name='login-button']")
    RESET_FIELDS = (By.CSS_SELECTOR, 'svg[data-icon="times"]')
    ERROR_TEXT = (By.XPATH, '//h3[text()="Epic sadface: Username and password do not match any user in this service"]')
    PASSWORD_REQUIRED_TEXT = (By.XPATH, '//h3[text()="Epic sadface: Password is required"]')
    MENU_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_BUTTON = (By.ID, "logout_sidebar_link")
    ABOUT_BUTTON = (By.ID, 'about_sidebar_link')

    def open(self):
        self.driver.get(self.LOGIN_PAGE_URL)

    def check_url(self, expected_url):
        time.sleep(1)
        actual_url = self.driver.current_url
        assert actual_url == expected_url, "Not the correct URL"

    def enter_name(self, user_name):
        if self.find(self.USER_NAME_BOX).get_attribute("value"):
            self.find(self.USER_NAME_BOX).clear()
            self.type(self.USER_NAME_BOX, user_name)
        else:
            self.type(self.USER_NAME_BOX, user_name)

    def enter_password(self, password):
        if self.find(self.PASSWORD_BOX).get_attribute("value"):
            self.find(self.PASSWORD_BOX).clear()
            self.type(self.PASSWORD_BOX, password)
        else:
            self.type(self.PASSWORD_BOX, password)
        time.sleep(2)

    def click_login(self):
        login = WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(self.LOGIN_BUTTON))
        login.click()
        time.sleep(2)

    def check_error_text(self, expected_text):
        error_text = self.find(self.ERROR_TEXT).text
        assert expected_text in error_text

    def reset_login_fields(self):
        self.find(self.RESET_FIELDS).click()

    def access_menu(self):
        self.find(self.MENU_BUTTON).click()

    def log_out(self):
        self.find(self.LOGOUT_BUTTON).click()

    def about_information(self):
        self.find(self.ABOUT_BUTTON).click()

    def check_visibility_of_fields(self):
        assert self.find(self.USER_NAME_BOX).is_displayed(), "Fields are not visible"
