# Created by Home at 09.11.2021
Feature: Demo

  Background:
    Given Start wash car
  # Enter feature description here
  Scenario: Wash car
    When I Start first position
    Then I move side motor dir "2"
    Then I move round motor dir "2"
    Then I move main motor dir "1"
    Then I correct main motor dir "1"
    Then I move round motor dir "2"
    Then I move side motor dir "1"
    Then I move round motor dir "2"
    Then I move main motor dir "2"
    Then I correct main motor dir "2"
    Then I move round motor dir "2"
    When I Start first position
    Then I turn on water
    Then I move side motor dir "2"
    Then I move round motor dir "2"
    Then I move main motor dir "1"
    Then I correct main motor dir "1"
    Then I move round motor dir "2"
    Then I move side motor dir "1"
    Then I move round motor dir "2"
    Then I move main motor dir "2"
    Then I correct main motor dir "2"
    Then I move round motor dir "2"
    Then I turn off water
    When I Start first position
    Then I move round motor dir "1"
    Then I turn on hair dryer
    Then I move main motor dir "1"
    Then I correct main motor dir "1"
    Then I move main motor dir "2"
    Then I correct main motor dir "2"
    Then I turn off hair dryer
    Then I move round motor dir "2"