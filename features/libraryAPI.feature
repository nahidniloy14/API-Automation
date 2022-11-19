# Created by lm at 11/18/2022
Feature: Verify ADD books and Delete books using library API
  # Enter feature description here

  Scenario: Verify AddBook API functionality
    Given The book details which needs to be added to library
    When We execute post method
    Then Book is suceessfully added