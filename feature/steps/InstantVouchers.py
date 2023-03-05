from behave import *
from feature.Pages.InstantVouchersPageClass import InstantVouchersPageClass

from feature.Pages.LandingPageClass import LandingPageClass
import time
from hamcrest import *




@given("launch chrome browser and payback application is launched")
def step_impl(context):
    expectedTitle = "Largest Multi-brand Loyalty Program in India - PAYBACK"
    actualTitle = context.driver.title
    print(actualTitle)
    # Way1
    assert expectedTitle == actualTitle




@when("user hovers on earn points and selects instant vouchers link")
def step_impl(context):

    landingpage = LandingPageClass(context.driver)
    landingpage.mouse_hover()


    landingpage.click_Instant_Vouchers()

@then("user is navigated to Instant Vouchers page")
def step_impl(context):

    expectedTitle = "Redeem Payback Points for Instant Free Gift cards | PAYBACK Voucher World"
    actualTitle = context.driver.title
    print(actualTitle)
    # Way1
    assert_that(expectedTitle,equal_to(actualTitle))

#####################################################


@step('user enters "{text}" in the search bar')
def step_impl(context,text):

    entertext = InstantVouchersPageClass(context.driver)
    entertext.enter_text(text)
    time.sleep(3)



@then("user enters {text} in the search bar")
def step_impl(context, text):

    entertext = InstantVouchersPageClass(context.driver)
    entertext.Search_Bar_TextBox(text)
    time.sleep(3)


@then("user clicks on search icon")
def step_impl(context):
    searchicon = InstantVouchersPageClass(context.driver)
    searchicon.search_icon()

@then("the page is reloaded")
def step_impl(context):
    time.sleep(2)
    expectedTitle = "Redeem Payback Points for Instant Free Gift cards | PAYBACK Voucher World"
    actualTitle = context.driver.title
    print(actualTitle)
    # Way1
    assert_that(expectedTitle, equal_to(actualTitle))


#Scenario 4


@step("user remains on the same page")
def step_impl(context):

    expectedTitle = "Redeem Payback Points for Instant Free Gift cards | PAYBACK Voucher World"
    actualTitle = context.driver.title
    print("by entering invalid text user remains on the same page")
    print(actualTitle)
    # Way1
    assert_that(expectedTitle, equal_to(actualTitle))
    print("user remains on the same page")




@then("user selects dropdown text which is displayed")
def step_impl(context):
    selecttext = InstantVouchersPageClass(context.driver)
    selecttext.select_text()
    time.sleep(4)
    expectedTitle = "Buy KFC Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("new page is opened")
    print(actualTitle)

    # Way1
    assert_that(expectedTitle, equal_to(actualTitle))



@then("user clicks on chat assistant logo")
def step_impl(context):
    time.sleep(3)
    chaticon = InstantVouchersPageClass(context.driver)
    chaticon.chat_icon()
    time.sleep(5)




@then("user clicks on i have a voucher button")
def step_impl(context):
    time.sleep(4)
    voucherbutton = InstantVouchersPageClass(context.driver)
    voucherbutton.click_button()
    time.sleep(5)



