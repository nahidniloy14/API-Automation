# Created by lm at 11/18/2022
Feature: Verify ADD books and Delete books using library API
  # Enter feature description here
  @test1
  Scenario: Verify AddBook API functionality
    Given The book details which needs to be added to library
    When We execute post method
    Then Book is suceessfully added
    And status code should be 200
    #reused from githubAPI.feature
  @test2
 #dataset.py
  Scenario Outline: Verify AddBook API functionality
  Given The book details with <isbn> <aisle>
  When  We execute post method
  Then Book is suceessfully added

    Examples:
      |isbn |aisle|
      | book101  | 585   |
      | book 102 |  252 |
