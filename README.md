
**Proiect_Final_Aram_Mandalian**


The project is a Behavior-Driven Development (BDD) test automation framework using the Page Object Model (POM) design pattern. 
It is meant to test a demo shopping web page's functionalities using Python.

**Introduction**:


The purpose of this project is to demonstrate how to use BDD testing, using POM with Python. 
It includes feature files, step definition files, and page files representing classes of different pages of the web page.


**How it works**:


Step definition files which are in the folder named "steps" will implement every scenario that is scrapped from feature files.

Implementation will be done by using objects and functions created in the files from the folder "pages". 
Each feature file has a corresponding file in the 2 mentioned folders above, named similar (example: 'items_sort.feature', 'items_sort_page.py', items_sort.steps')


The tests cover various functionalities including login, page navigation, and shopping experience features.


**How to Enable**



To run the tests on your machine, follow these steps:

Clone this repository to your local machine.

Have Python installed on your machine. You can download Python from https://www.python.org/downloads/.

Install the required dependencies typing pip in the terminal: pip install -r requirements.txt (requirments might be libraries, such as behave, selenium, webdriver, html-formatter).
If you are using an IOS system, you might need to type pip3 instead of pip.

Download the appropriate version of Chromedriver for your Chrome browser version. 
Find your chrome browser version by accessing its menu and navigate to About Google Chrome.
You can download Chromedriver from https://chromedriver.chromium.org/downloads.

Place the chromedriver executable in a directory which is in your system's PATH environment variable.

Now open the project in PyCharm.
You may use some other IDE of your preference

In the features files, when you come across a Scenario Outline, feel free to replace the desired value in the Example fields:

 |  unregistered_mail | wrong_password |
 
      | aramis@mail.ro | pass1234 | - replace this values with the desired values
      

In the terminal, you can run the tests by typing this command to generate a HTML report: _behave -f html -o report_name.html_

You may replace _report_name.html_ with the name for the HTML report file of you.

After running the tests, you can view the results in the HTML file created by opening it in a browser.


You may want to print the test only on your terminal, or may want to run some scenarios or feature files and exclude other. Here is what you need to type in your terminal:

_behave_ - results will be printed in the terminal, no html file will be updated or created.

_behave -n name_of_the_scenario_ - testing a specific scenario.

_behave -i name_of_feature_file_ - testing a specific feature file.

_behave -e name_of_feature_file_ - exclusion of a specific feature file from testing.



**You may explore the project's structure.**


**Requirements**

- Python

- Selenium

- Chromedriver

- PyCharm or any Python IDE
