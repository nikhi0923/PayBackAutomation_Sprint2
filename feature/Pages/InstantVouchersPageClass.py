import time


from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class InstantVouchersPageClass:

    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.searchBarElement = "//input[@type='search'][1]"
        self.enterText = "//input[@type='search'][1]"
        self.searchLogoElement = "//img[@src='/payback/static/images/search.png'][1]"
        self.searchdropdownElement = "(//*[text()='KFC'])[1]"
        self.chatassistanticon = "//*[@class='chat-icon']"
        self.voucherbutton = "(//*[@class='question-option cus-color'])[1]"
        self.dropdowntextbar = "//*[@class='AutoCompleteText shadow'][1]"
        self.dropdownElement = "//*[@class='AutoCompleteText shadow'][1]"


    def enter_text(self,text):
        entertext = self.driver.find_element(By.XPATH,self.enterText)
        entertext.click()
        time.sleep(3)
        entertext.send_keys(text)
        time.sleep(5)


    def Search_Bar_TextBox(self,vouchername):
       searchBarTextBox = self.driver.find_element(By.XPATH, self.searchBarElement)
       searchBarTextBox.click()


       searchBarTextBox.send_keys(vouchername)

       print("searchTextbox is  working")

    def excel_data(self,text):
        exceldata = self.driver.find_element(By.XPATH,self.enterText)

        exceldata.send_keys(text)
        time.sleep(3)


    def search_icon(self):
        searchIcon = self.driver.find_element(By.XPATH,self.searchLogoElement)
        searchIcon.click()


    def select_text(self):
        selecttext = self.driver.find_element(By.XPATH, self.searchdropdownElement)
        action = ActionChains(self.driver)
        action.move_to_element(selecttext)
        action.perform()
        selecttext.click()

    def drop_down(self):
        selectdropdown = self.driver.find_element(By.XPATH,self.dropdowntextbar)
        selectdropdown.click()


    def select_dropdown_element(self):
        select = self.driver.find_element(By.XPATH,self.dropdownElement)
        select.click()

    def chat_icon(self):
        chaticon = self.driver.find_element(By.XPATH, self.chatassistanticon)
        chaticon.click()


    def click_button(self):
        voucherbutton = self.driver.find_element(By.XPATH,self.voucherbutton)
        voucherbutton.click()




















