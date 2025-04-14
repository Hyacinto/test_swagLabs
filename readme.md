SwagLabs Test Automation Project
================================

![Tested!](swag_tested.png)

Overview
--------

This project is an automation testing framework developed using Python and Selenium WebDriver. The primary goal of the project is to perform functional and visual regression tests for the **Sauce Demo** application ([https://www.saucedemo.com/](https://www.saucedemo.com/)), a popular web application used for testing and training purposes.
The tests aim to ensure the stability of key functionalities such as login, inventory page rendering, and menu navigation. Additionally, the project implements visual regression testing, ensuring that any UI changes are detected automatically.

Project Structure
-----------------

*   **tests/**: Contains the test scripts for different application pages and features.
*   **pages/**: Houses the page objects for the various components of the Sauce Demo application (e.g., Login, Inventory, etc.).
*   **utilities/**: Includes utility functions for common tasks such as menu navigation and resetting the app state.
*   **.gitignore**: Specifies which files and directories should be ignored by Git.

Built with:
-----------

[![Python](https://img.shields.io/badge/Python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)](https://www.python.org/)
[![Selenium](https://img.shields.io/badge/Selenium-43B02A?style=for-the-badge&logo=selenium&logoColor=white)](https://www.selenium.dev/)
[![Pytest](https://img.shields.io/badge/Pytest-0A0A0A?style=for-the-badge&logo=pytest&logoColor=white)](https://docs.pytest.org/)
[![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
[![Firefox](https://img.shields.io/badge/Firefox-FF7139?style=for-the-badge&logo=firefox-browser&logoColor=white)](https://www.mozilla.org/firefox/)

Features
--------

*   **Functional Testing**: Verifies that critical application features like login, inventory, and user interactions work correctly.
*   **Visual Regression Testing**: Compares screenshots to detect any unexpected changes in the UI, leveraging tools like Applitools.
*   **Headless Mode**: Runs tests in headless mode, ensuring that the tests can run on CI/CD pipelines without a graphical user interface.

Setup Instructions
------------------
1. Clone the repository:
        git clone <repository-url>
        cd test_swagLabs
2. Build the Docker image:
        docker build -t test_swaglabs .
3. Run the Docker container:
        docker run --rm test_swaglabs
This will build the Docker image and run the tests inside the Docker container. The test results and logs will be available at [http://localhost:5050](http://localhost:5050), provided by [![Allure](https://img.shields.io/badge/Allure%20Report-3980F6?style=for-the-badge&logo=allure&logoColor=white)](https://docs.qameta.io/allure/).

