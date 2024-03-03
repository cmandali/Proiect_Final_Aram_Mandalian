
**Proiect_Final_Aram_Mandalian**


Project is a Behavior-Driven Development (BDD) test automation framework using the Page Object Model (POM) design pattern. 
It is meant to test a demo shopping web page's functionalities using Python.

Introduction

The purpose of this project is to demonstrate how to use BDD testing, using POM with Python. 
It includes feature files, step definition files, and page files representing classes of different pages of the web page.

The tests cover various functionalities including login, page navigation, and shopping experience features.

How to Enable

To run the tests on your machine, follow these steps:

Clone this repository to your local machine.

Have Python installed on your machine. You can download Python from https://www.python.org/downloads/.

Install the required dependencies typing pip in the terminal: pip install -r requirements.txt (requirments might be libraries, such as behave, selenium, webdriver, html-formatter).
If you are using an IOS system, you might need to type pip3 instead of pip.

Download the appropriate version of Chromedriver for your Chrome browser version. 
Find your chrome browser version by accesing its menu and navigate to About Google Chrome.
You can download Chromedriver from https://chromedriver.chromium.org/downloads.

Place the chromedriver executable in a directory which is in your system's PATH environment variable.

Now open the project in PyCharm.
You may use some other IDE of your preference

In the terminal, you can run the tests by typing this command to generate a HTML report: behave -f html -o report_name.html

You may replace report_name.html with the name for the HTML report file of you.

After running the tests, you can view the results in the HTML file created by opening it in a browser.

You may explore the project's structure.

Requirements

Python

Selenium

Chromedriver

PyCharm or any Python IDE
