Feature: Add to Cart Functionality


  Scenario Outline: Number of products added to shopping basket
    Given I am on all items page
    When I add to cart "<number>" of products
    When I navigate to shopping basket
    When I go to Checkout
    When I fill in the form with "<first_name>", "<last_name>" and "<postal_code>"
    When I continue to checkout
    Then I see "<number>" of products in my basket
    Then I see that total amount equals the summed price of the products
    Examples:
      |number  |first_name |last_name|postal_code|
      | 3| aram |khaciaturian  |234                 |

  Scenario Outline: Remove Items Functionality
    Given I am on all items page again
    When I remove "<number>" of items
    When I proceed to shopping basket
    Then I see "<total_number_of_items>" in my basket
    Examples:
      | number | total_number_of_items |
      | 1| 2                           |

  Scenario Outline: A typical user journey when buying products
    Given I start from all items page
    When I add "<desired_item>" in basket
    When I proceed to final checkout
    When I click on finish
    Then I should received confirmation message for my order
    Examples:
      | desired_item |
      | bike-light   |
