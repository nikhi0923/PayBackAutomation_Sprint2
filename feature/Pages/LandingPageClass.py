from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

class LandingPageClass:

    def __init__(self, driver):
        self.driver = driver

        # Element Locators Values
        self.earnPointsLinkElement ="//ul[@class='nav navbar-nav pb-main-menu']/li[1]"
        self.instantVouchersLinkElement = "(//*[@href='https://www.gyftr.com/payback/singlesign?token=TEMPXYZ786'])[1]"



    # Creating Element Methods
    def mouse_hover(self):

        hoverElement = self.driver.find_element(By.XPATH, self.earnPointsLinkElement)

        action = ActionChains(self.driver)
        action.move_to_element(hoverElement)
        action.perform()




    def click_Instant_Vouchers(self):
        instantVouchersLink = self.driver.find_element(By.XPATH,self.instantVouchersLinkElement)
        instantVouchersLink.click()

        parentWindow = self.driver.current_window_handle
        allWindows = self.driver.window_handles
        for childWindow in allWindows:
            if(parentWindow != childWindow):
                self.driver.switch_to.window(childWindow)















