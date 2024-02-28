from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.open()


@then('The URL of the login page is "https://www.saucedemo.com/"')
def step_impl(context):
    context.login_page.check_url("https://www.saucedemo.com/")


@when('I enter "aramis" in the email input on the login page')
def step_impl(context):
    context.login_page.enter_name("aramis")


@when('I enter a "password1234"')
def step_impl(context):
    context.login_page.enter_name("password1234")


@when("I press the login button")
def step_impl(context):
    context.login_page.click_login()


@when('I enter "{registered_mail}"')
def step_impl(context, registered_mail):
    context.login_page.enter_name(registered_mail)


@when('I enter "{password}" in the password field')
def step_impl(context, password):
    context.login_page.enter_password(password)


@when("I press the login button once more")
def step_impl(context):
    context.login_page.click_login()


@then('The url should be https://www.saucedemo.com/inventory.html')
def step_impl(context):
    context.login_page.check_url("https://www.saucedemo.com/inventory.html")


@when("I click on the Menu to logout")
def step_impl(context):
    context.login_page.log_out()


@then("The log_in fields should be visible")
def step_impl(context):
    context.login_page.check_visibility_of_fields()




