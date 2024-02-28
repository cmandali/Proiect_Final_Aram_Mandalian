from browser import Browser
from pages.login_page import LoginPage
from pages.add_to_cart_page import Add_to_Cart
from pages.items_sort_page import SortItems


def before_all(context):
    context.browser = Browser()
    context.login_page = LoginPage()
    context.add_to_cart_page = Add_to_Cart()
    context.items_sort_page = SortItems()


def after_all(context):
    context.browser.close()
