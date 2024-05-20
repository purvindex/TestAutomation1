import os
import time
import softest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from Base.base_Driver import BaseDriver
class RBACValidationPage(BaseDriver):

    inputbox_userName_id="cms-login-userId"
    inputbox_password_id ="cms-login-password"
    btnFileSubmission_xpath = "//span[normalize-space()='File Submission']"
    btnfileStatus_xpath = "//a[normalize-space()='File Status']"
    option_Fileupload_xpath = "//*[contains(text(),'File Upload')]"
    option_AdminText_xpath = "//*[contains(text(),'Admin')]"
    option_AdminOption_xpath ="//span[normalize-space()='Admin']"
    fileBrowse_xpath = "//input[@type='file']"
    searchResult_xpath = "//div[@aria-label='Displaying records']"

    def __init__(self,
                 driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, username):
        return self.driver.find_element(By.ID, self.inputbox_userName_id).send_keys(username)
    def enter_password(self, password):
        return self.driver.find_element(By.ID, self.inputbox_password_id).send_keys(password)

    def click_OnFileSubmission(self):
        time.sleep(6)
        # fileSubmission = WebDriverWait(self.driver, 15).until(
        #     EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath)))
        # fileSubmission.click()
        self.driver.find_element(By.XPATH, self.btnFileSubmission_xpath).click()
        time.sleep(7)


    def isFileuploadOptionExits(self):
        fileUploadOptions= self.driver.find_elements(By.XPATH,self.option_Fileupload_xpath)
        x = len(fileUploadOptions)
        #print(x)
        return x

    def isAdminOptionExits(self):
        adminOptions= self.driver.find_elements(By.XPATH,self.option_AdminText_xpath)
        y = len(adminOptions)
        #print(y)
        return y
    def isRecordDisplayed(self):
        searchResult= self.driver.find_element(By.XPATH,self.searchResult_xpath).text
        print("Contractor can not see the file on 'File Status' page as has no JE Jurisdction")
        print(searchResult)
        return searchResult


    def click_OnADMIN(self):
        return self.driver.find_element(By.XPATH, self.option_AdminOption_xpath).click()



