Feature: Verifying registration functionality


Scenario: Registration with valid data
  Given User is on Registration page
  When user enters username
  And user enters password
  And user clicks on Signup button
  Then validate user logged in successfully