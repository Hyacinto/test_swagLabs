SwagLabs Test Automation Project
================================
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
2. Install dependencies: Make sure you have Python installed. Then, install the required libraries by running:
        pip install -r requirements.txt
3. Run the tests: You can run the tests using pytest:
        pytest tests/test_inventory.py::test_visual
Current Development Status
--------------------------
This project is currently under active development. Some features may be incomplete or under review. Here are the current points of development:
* Stabilization of the framework: I am improving error handling and test reliability.
* Test coverage expansion: I am adding more test cases to cover additional functionalities of the Sauce Demo app.