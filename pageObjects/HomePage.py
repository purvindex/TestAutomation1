import time

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Base.base_Driver import BaseDriver


class HomePage(BaseDriver):
    def __init__(self, driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created
        super().__init__(driver)
        self.driver = driver   #and passing argument as driver so same driver can be used in test calss

    checkLbl_xpath = "//label[@id='cms-label-tc']"
    btnLogin_xpath = "//button[@id='cms-login-submit']"
    #btnCROWD_xpath = "//div[@class='ng-star-inserted']" changed on 18th April for ADMIN role
    btnCROWD_xpath ="//a[@id='cms-tile-a-hs-crowd']"
    btnApplication_linkText= "Application"
    btnApplication_xpath="//a[@id='mp_crowd_verticalRedirect/application']"
    switchingFrame_xpath = "//object[@id='obj_crowd_wab_application']"

    def loadApplication (self):

        time.sleep(3)
        self.driver.find_element(By.XPATH, self.checkLbl_xpath).click()
        # time.sleep(7)  # self.driver.find_element(By.XPATH, self.btnLogin_xpath).click()

        btnLogin = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnLogin_xpath)))
        self.driver.execute_script("arguments[0].click();", btnLogin)

        # time.sleep(7) # self.driver.find_element(By.XPATH, self.btnCROWD_xpath).click()
        btnCROWD = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnCROWD_xpath)))
        self.driver.execute_script("arguments[0].click();", btnCROWD)

        # time.sleep(7)  #self.driver.find_element(By.XPATH, self.btnApplication_xpath).click()
        btnApplication = WebDriverWait(self.driver, 20).until(
            EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.btnApplication_xpath)))
        self.driver.execute_script("arguments[0].click();", btnApplication)

        time.sleep(5)
        self.driver.switch_to.frame(self.driver.find_element(By.XPATH, self.switchingFrame_xpath))


