from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import os

# Global timestamp
timestamp = None

# Install the ChromeDriver if not already installed and get the executable path
driver_path = ChromeDriverManager().install()

# Create a Service object with the executable path
service = Service(executable_path=driver_path)


def before_all(context):
    global timestamp
    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")
    context.browser = webdriver.Chrome(service=service)
    context.browser.implicitly_wait(
        10
    )  # Wait up to 10 seconds for elements to become available


def after_all(context):
    if hasattr(context, "browser"):
        context.browser.quit()  # Close browser when tests are completed


def after_scenario(context, scenario):
    global timestamp
    if not os.path.exists(f"reports/screenshots_{timestamp}"):
        os.makedirs(f"reports/screenshots_{timestamp}")
    screenshot_name = f"reports/screenshots_{timestamp}/screenshot_{scenario.name}.png"
    context.browser.save_screenshot(screenshot_name)
    print(f"Screenshot saved as '{screenshot_name}'")
