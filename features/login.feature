Feature: Login Page


  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the login page is "https://www.saucedemo.com/"

  Scenario Outline: Login with unregistered mail or wrong password
    When I enter "<unregistered_mail>" in the user-name field
    When I enter "<wrong_password>" in the password field
    When I click on Login
    Then I should see the "Username and password do not match any user in this service"
    Examples:
      |  unregistered_mail|wrong_password|
      | aramis@mail.ro| pass1234 |


  Scenario Outline: Reset fields and login successful with a registered email and correct password
    When I click on reset login fields
    When I re-enter "<registered_mail>" in the user-name field
    When I re-enter "<password>" in the password field
    When I press the login button once more
    Then The url should be https://www.saucedemo.com/inventory.html
    Examples:
      |registered_mail  |password|
      | standard_user| secret_sauce |



  Scenario: Logout to main page
    When I click on the Menu to logout
    Then The log_in fields should be visible

