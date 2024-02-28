Feature: Sort Items Functionality


  Scenario: Sort price lowest to highest
    Given I start from all items page
    When I sort the product from price low to high
    Then The first product is the one with the lowest price



  Scenario: Sort price highest to lowest
    When I sort the product from price high to low
    Then The first product is the one with the highest price
