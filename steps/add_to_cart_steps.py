from behave import *


@given("I am on all items page")
def step_impl(context):
    context.add_to_cart_page.all_items_page()


@when('I add to cart "{number}" of products')
def step_impl(context, number):
    context.add_to_cart_page.add_to_cart(number)


@when('I navigate to shopping basket')
def step_impl(context):
    context.add_to_cart_page.navigate_to_shopping_basket()


@when('I go to Checkout')
def step_impl(context):
    context.add_to_cart_page.proceed_to_checkout()


@when('I fill in the form with "{first_name}", "{last_name}" and "{postal_code}"')
def step_impl(context, first_name, last_name, postal_code):
    context.add_to_cart_page.complete_form(first_name, last_name, postal_code)


@when('I continue to checkout')
def step_impl(context):
    context.add_to_cart_page.continue_to_checkout()


@then('I see "{number}" of products in my basket')
def step_impl(context, number):
    context.add_to_cart_page.check_number_of_products(number)


@then("I see that total amount equals the summed price of the products")
def step_impl(context):
    context.add_to_cart_page.get_the_prices()
    context.add_to_cart_page.verify_total_amount()


@given("I am on all items page again")
def step_impl(context):
    context.add_to_cart_page.navigate_to_all_items_page()


@when('I remove "{number}" of items')
def step_impl(context, number):
    context.add_to_cart_page.remove_items(number)


@when('I proceed to shopping basket')
def step_impl(context):
    context.add_to_cart_page.navigate_to_shopping_basket()


@Then('I see "{total_number_of_items}" in my basket')
def step_impl(context, total_number_of_items):
    context.add_to_cart_page.check_number_of_products(total_number_of_items)

