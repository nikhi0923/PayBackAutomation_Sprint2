Feature: Instant Vouchers Page DDF

   Scenario: To validate the user can select the relevant result which are displayed below the search bar while entering the text
   Given launch chrome browser and payback application is launched
   When user hovers on earn points and selects instant vouchers link
   Then user is navigated to Instant Vouchers page
   When user enter the <vouchername>  in the search bar
   Then user selects the dropdown text which is displayed
    And user enter the second <vouchername>  in the search bar
    Then user is redirected to the selected voucher page



