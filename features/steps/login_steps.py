from behave import given, when, then
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@given("user is on the login page")
def step_impl(context):
    context.browser.get("https://practicetestautomation.com/practice-test-login/")


@when("the user enters the correct username and password")
def step_impl(context):
    context.browser.find_element("id", "username").send_keys("student")
    context.browser.find_element("id", "password").send_keys("Password123")
    context.browser.find_element("id", "submit").click()


@when('the user enters "{username}" and "{password}"')
def step_impl(context, username, password):
    context.browser.find_element("id", "username").send_keys(username)
    context.browser.find_element("id", "password").send_keys(password)
    context.browser.find_element("id", "submit").click()


@then("the user should be directed to the 'successful login page'")
def step_impl(context):
    expected_url = "https://practicetestautomation.com/logged-in-successfully/"
    assert (
        context.browser.current_url == expected_url
    ), f"Expected URL after login is {expected_url}, but got {context.browser.current_url}"


@then('the user should see an error message "{expected_result}"')
def step_impl(context, expected_result):
    expected_error_message = expected_result.strip(
        "'"
    )  # Remove single quotes for comparison
    # Wait for the error message element to be present and check its text
    error_message_element = WebDriverWait(context.browser, 10).until(
        EC.visibility_of_element_located((By.ID, "error")),
        "Error message element not found.",
    )
    actual_error_message = error_message_element.text
    assert (
        expected_error_message in actual_error_message
    ), f"Expected '{expected_error_message}', but got '{actual_error_message}'"
