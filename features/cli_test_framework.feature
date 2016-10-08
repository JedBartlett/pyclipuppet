Feature: Testing the Test Framework

  Scenario: Get version of Python
    Given A Windows Command Line Interface
    When the command "python --version" is issued
    Then "Python" should be found in the output
