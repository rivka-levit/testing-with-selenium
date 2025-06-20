# Test Automation with Selenium and Python – Course Solutions

### 📚 Overview

This repository contains my completed exercises and solutions from the course
["Test Automation with Selenium and Python"](https://stepik.org/course/575/syllabus). The course focuses on automating 
web application testing using the Selenium WebDriver with Python, covering 
fundamental to intermediate concepts of UI test automation.

### 🚀 What You’ll Find Here

- ✅ Solutions to hands-on exercises and assignments from the course
- 🧪 Automated test scripts using Selenium WebDriver
- 🛠️ Usage of test frameworks like unittest and pytest
- 🔧 Setup and teardown strategies for test environments
- 📄 Page Object Model (POM) implementation for scalable test design
- 🧱 Handling dynamic elements, waits, and browser interactions
- 📦 Dependency management with requirements.txt

### 🔧 Setup Instructions

1. Clone the repository
    ```
    git clone https://github.com/rivka-levit/testing-with-selenium.git
    cd selenium_testing
    ```
2. Create and activate a virtual environment
    ```
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
3. Install dependencies
    ```
    pip install -r requirements.txt
    ```
4. Download the appropriate WebDriver
   - For Chrome: https://sites.google.com/chromium.org/driver/
   - For Firefox: https://github.com/mozilla/geckodriver/releases

Make sure the driver is added to your system’s PATH or placed in the drivers/ folder.

### ▶️ Running Tests

#### To run tests with unittest:
```
python -m unittest discover tests/
```
#### To run tests with pytest:
```
pytest tests/
```

### 🧰 Tools & Technologies Used

- 🐍 Python 3.x
- 🌐 Selenium WebDriver
- 🧪 unittest & pytest
- 📄 Page Object Model (POM)
- 🧼 pytest fixtures & test setup
- ⏱️ Implicit and explicit waits
- 🌍 ChromeDriver / GeckoDriver

### 📌 Course Topics Covered

- Setting up Selenium WebDriver with Python
- Locating elements with XPath, CSS selectors, and other strategies
- Interacting with input fields, buttons, checkboxes, dropdowns
- Waiting for elements using explicit/implicit waits
- Creating reusable page objects with POM
- Test case structuring with unittest and pytest
- Debugging and troubleshooting test failures
- Organizing test suites and generating reports

### 🙌 Acknowledgments

This repository is based on the exercises from the "Test Automation with 
Selenium and Python" course. Special thanks to the course instructor for 
the clear explanations and practical examples.