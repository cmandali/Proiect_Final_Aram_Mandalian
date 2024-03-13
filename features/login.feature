Feature: Login Page


  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the login page is "https://www.saucedemo.com/"
    
  Scenario Outline: Login with unregistered mail or wrong password
    Given I start from login page
    When I enter "<unregistered_mail>" in the user-name field
    When I enter "<wrong_password>" in the password field
    When I click on Login
    Then I should see the "<login_error_text>"
    Examples:
      |  unregistered_mail|wrong_password|login_error_text |
      | aramis@mail.ro| pass1234      | Username and password do not match any user in this service |
    
  Scenario Outline: Reset fields and login successful with a registered email and correct password
    Given I enter wrong user-name & password an click login
    When I click on reset login fields
    When I re-enter "<registered_mail>" in the user-name field
    When I re-enter "<password>" in the password field
    When I press the login button once more
    Then The url should be "<correct_url>"
    Examples:
      |registered_mail  |password| correct_url |
      | standard_user| secret_sauce | https://www.saucedemo.com/inventory.html|
    
  Scenario: Logout to main page
    Given I successfully logged in into all items page
    When I click on the Menu to logout
    Then The log_in fields should be visible
    
  Scenario: Surf to saucelabs official web app
    Given I begin from all items page
    When I click on the 3 lines menu
    When I click About
    Then I should be re-directed to saucelabs.com official web app

