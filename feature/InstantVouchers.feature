@FunctinoalityTest
Feature: Instant Vouchers Page


  Background:
     Given launch chrome browser and payback application is launched
     When user hovers on earn points and selects instant vouchers link
     Then user is navigated to Instant Vouchers page


 Scenario: To validate user navigation to Instant vouchers page
  # Given launch chrome browser and payback application is launched
   #When user hovers on earn points and selects instant vouchers link
   #Then user is navigated to Instant Vouchers page



 Scenario:To validate user can enter text in the search bar
   And user enters "KFC" in the search bar


  Scenario Outline: To validate user can get relevant result by clicking on search logo
   Then user enters <text> in the search bar
   Then user clicks on search icon
   Then the page is reloaded
    Examples:
      |text|
      |netmeds|
      |Kalyan Gold Coins|

  Scenario Outline: To validate user remains on the same page when enters an invalid text
   Then user enters <text> in the search bar
   Then user clicks on search icon
   And user remains on the same page
    Examples:
      |text|
      |xyz|
      |abc|

  Scenario: to validate the user can select the relevant result which are displayed below the search bar while entering the text
   And user enters "KFC" in the search bar
   Then user selects dropdown text which is displayed


 Scenario: To validate that the chat box has appeared when the user clicks on chat assistant logo
   Then user clicks on chat assistant logo

  Scenario: To validate the user is able to click on any of the displayed options
   Then user clicks on chat assistant logo
    Then user clicks on i have a voucher button











