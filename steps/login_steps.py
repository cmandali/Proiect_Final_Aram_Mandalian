from behave import *


@given("I am on the login page")
def step_impl(context):
    context.login_page.open()


@then('The URL of the login page is "https://www.saucedemo.com/"')
def step_impl(context):
    context.login_page.check_url("https://www.saucedemo.com/")


@given('I start from login page')
def step_impl(context):
    context.login_page.open()


@when('I enter "{unregistered_mail}" in the user-name field')
def step_impl(context, unregistered_mail):
    context.login_page.enter_name(unregistered_mail)


@when('I enter "{wrong_password}" in the password field')
def step_impl(context, wrong_password):
    context.login_page.enter_password(wrong_password)


@when("I click on Login")
def step_impl(context):
    context.login_page.click_login()


@then('I should see the "{login_error_text}"')
def step_impl(context, login_error_text):
    context.login_page.check_error_text(login_error_text)


@given('I enter wrong user-name & password an click login')
def step_impl(context):
    context.login_page.enter_name('Aram')
    context.login_page.enter_password("strong1234")
    context.login_page.click_login()


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


@then('The url should be "{correct_url}"')
def step_impl(context, correct_url):
    context.login_page.check_url(correct_url)


@given('I successfully logged in into all items page')
def step_impl(context):
    context.add_to_cart_page.all_items_page()


@when("I click on the Menu to logout")
def step_impl(context):
    context.login_page.access_menu()
    context.login_page.log_out()


@then("The log_in fields should be visible")
def step_impl(context):
    context.login_page.check_visibility_of_fields()


@given('I begin from all items page')
def step_impl(context):
    context.add_to_cart_page.all_items_page()


@when('I click on the 3 lines menu')
def step_impl(context):
    context.login_page.access_menu()


@when('I click About')
def step_impl(context):
    context.login_page.about_information()


@then('I should be re-directed to saucelabs.com official web app')
def step_impl(context):
    context.login_page.check_url("https://saucelabs.com/")

