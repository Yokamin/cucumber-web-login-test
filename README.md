# Cucumber Web Login Test
My first Cucumber project for learning - testing login page of 'practicetestautomation.com'
This project demonstrates how to perform automated web login tests using Cucumber, Selenium, and Behave in Python.

## Requirements

- Python 3.12.1
- Google Chrome
- ChromeDriver

## Installation

1. **Clone the repository:**
   ```bash
   git clone git@github.com:Yokamin/cucumber-web-login-test.git
   ```
2. **Create and activate a virtual environment _(optional but recommended)_:**
    - Windows: `python -m venv venv && .\venv\Scripts\activate`
    - macOS/Linux: `python3 -m venv venv && source venv/bin/activate`
3. **Install dependencies:**
   ```bash
    cd cucumber-web-login-test
    pip install -r requirements.txt
    ```
4. **Install ChromeDriver _(if not already installed)_:**\
    You can install ChromeDriver manually or use the WebDriver Manager to automatically download and manage it.

    **Manual Installation:** Download ChromeDriver from the [ChromeDriver downloads page](https://sites.google.com/chromium.org/driver/) and place the executable in a directory included in your system's PATH.

    **Using WebDriver Manager:** This project already includes the webdriver_manager package in the requirements.txt file. ChromeDriver will be automatically managed by this package during test execution.

## Running Tests

Execute the following command to run the tests:

```bash
behave
```

This command will run all feature files (`*.feature`) in the `features` directory.

## Structure

- `environment.py`: Contains the Behave hooks and setup for WebDriver.
- `login.feature`: Defines the Gherkin scenarios for login functionality.
- `login_steps.py`: Implements the step definitions for the login scenarios.
- `reports/`: Directory to store test reports and screenshots.

## Author

[Joakim Aagedal](https://github.com/Yokamin/)

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details.