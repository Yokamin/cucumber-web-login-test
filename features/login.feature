Feature: Login functionality

  Scenario: Successful login
    Given user is on the login page
    When the user enters the correct username and password
    Then the user should be directed to the 'successful login page'

  Scenario Outline: Login attempts
    Given user is on the login page
    When the user enters "<username>" and "<password>"
    Then the user should see an error message "<expected_result>"

    Examples:
      | username      | password          | expected_result             |
      | incorrectUser | Password123       | 'Your username is invalid!' |
      | student       | incorrectPassword | 'Your password is invalid!' |