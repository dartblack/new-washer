# Created by Home at 09.11.2021
Feature: Demo

  Background:
    Given Start wash car
  # Enter feature description here
  Scenario: Wash Car
    When I Start first position
    Then I move side motor dir "1"
    Then I move round motor dir "1"
    Then I move main motor dir "1"
    Then I move round motor dir "1"
    Then I move side motor dir "2"
    Then I move round motor dir "1"
    Then I move main motor dir "2"
    Then I move side motor dir "1"