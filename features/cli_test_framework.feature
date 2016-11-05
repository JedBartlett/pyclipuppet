Feature: Testing the Test Framework

  Scenario: Get version of Python
    Given A Windows Command Line Interface
    When the command "python --version" is issued
    Then "Python" can be found in the output
    And the error level returned is: "0"

  Scenario: Run illegal command and check for %errorcode%
    Given A Windows Command Line Interface
    When the command "thisisabadcommand" is issued
    Then "not recognized as an internal or external command" can be found in the output
    And the error level returned is: "9009"