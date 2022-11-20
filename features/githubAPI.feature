# Created by lm at 11/19/2022
Feature: Github API Validation
  # Enter feature description here
  @github
  Scenario: Session management check
    Given I have github auth credentials
    When I hit the getRepo API of github
    Then status code should be 200

    #reused in library API