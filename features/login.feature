Feature: Login Page


  Scenario: Check that the URL is correct
    Given I am on the login page
    Then The URL of the login page is "https://www.saucedemo.com/"


  Scenario Outline: Login successful with a registered email and password
    When I enter "<registered_mail>"
    When I enter "<password>" in the password field
    When I press the login button once more
    Then The url should be https://www.saucedemo.com/inventory.html
    Examples:
      |registered_mail  |password|
      | standard_user| secret_sauce |



  Scenario: Logout to main page
    When I click on the Menu to logout
    Then The log_in fields should be visible

