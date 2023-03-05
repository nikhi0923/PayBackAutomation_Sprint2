from behave import *
from feature.Pages.InstantVouchersPageClass import InstantVouchersPageClass

from feature.Pages.LandingPageClass import LandingPageClass
import time

from feature.utility.ConfigClass import ConfigClass
from hamcrest import *
from datafiles import ExcelUtils


@when("user enter the {vouchername}  in the search bar")
def step_impl(context,vouchername):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    vouchername = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 2, 1)
    text = InstantVouchersPageClass(context.driver)
    text.excel_data(vouchername)
    time.sleep(3)

@then("user selects the dropdown text which is displayed")
def step_impl(context):
    selectdropdown = InstantVouchersPageClass(context.driver)
    selectdropdown.drop_down()
    time.sleep(3)
    expectedTitle = "Buy Netmeds Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("new page is opened")
    print(actualTitle)

    # Way1
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)




@step("user enter the second {vouchername}  in the search bar")
def step_impl(context,vouchername):
    ExcelUtils.get_row_count(ConfigClass.dataFilePath, "Sheet1")
    vouchername = ExcelUtils.read_data(ConfigClass.dataFilePath, "Sheet1", 3, 1)
    time.sleep(2)
    text = InstantVouchersPageClass(context.driver)
    text.excel_data(vouchername)
    time.sleep(3)


@then("user is redirected to the selected voucher page")
def step_impl(context):
    selectdropdown = InstantVouchersPageClass(context.driver)
    selectdropdown.select_dropdown_element()
    time.sleep(3)
    expectedTitle = "Buy Kalyan Diamond Jewellery Gift Vouchers & Gift Cards | Redeem Payback Points"
    actualTitle = context.driver.title
    print("new page is opened")
    print(actualTitle)

    # Way1
    assert_that(expectedTitle, equal_to(actualTitle))
    time.sleep(3)
