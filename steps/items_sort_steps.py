from behave import *


@given("I start from all items page")
def step_impl(context):
    context.items_sort_page.all_items_page()


@when("I sort the product from price low to high")
def step_impl(context):
    context.items_sort_page.sort_low_to_high()


@then("The first product is the one with the lowest price")
def step_impl(context):
    context.items_sort_page.verify_sort_low_to_high()


@when("I sort the product from price high to low")
def step_impl(context):
    context.items_sort_page.sort_high_to_low()


@then("The first product is the one with the highest price")
def step_impl(context):
    context.items_sort_page.verify_high_to_low()
