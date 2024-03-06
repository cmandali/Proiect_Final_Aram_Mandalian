from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.open()


@then('The URL of the login page is "https://www.saucedemo.com/"')
def step_impl(context):
    context.login_page.check_url("https://www.saucedemo.com/")


@when('I enter "{unregistered_mail}" in the user-name field')
def step_impl(context, unregistered_mail):
    context.login_page.enter_name(unregistered_mail)


@when('I enter "{wrong_password}" in the password field')
def step_impl(context, wrong_password):
    context.login_page.enter_password(wrong_password)


@when("I click on Login")
def step_impl(context):
    context.login_page.click_login()


@then('I should see the "Username and password do not match any user in this service"')
def step_impl(context):
    context.login_page.check_error_text("Username and password do not match any user in this service")


@when('I click on reset login fields')
def step_impl(context):
    context.login_page.reset_login_fields()


@when('I re-enter "{registered_mail}" in the user-name field')
def step_impl(context, registered_mail):
    context.login_page.enter_name(registered_mail)


@when('I re-enter "{password}" in the password field')
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
