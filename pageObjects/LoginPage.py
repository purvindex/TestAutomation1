import time


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

class TestingHomepage():
    def testing_page(self):
        driver = webdriver.Chrome()
        driver.get("https://portaldev.cms.gov/portal")
        driver.maximize_window()
        driver.implicitly_wait(20)
        driver.find_element(By.ID, "cms-login-userId").send_keys("PDPOC_01")
        driver.find_element(By.ID, "cms-login-password").send_keys("Crowd_dev_112723")
        driver.find_element(By.ID, "cms-label-tc").click()
        driver.find_element(By.ID, "cms-login-submit").click()
        time.sleep(7)
        # self.wait.until(EC.element_to_be_clickable(By.ID,"cms-send-push-phone" )).click()
        driver.find_element(By.ID, "cms-send-push-phone").click()
        time.sleep(30)

        # # Click on CROWD
        # driver.find_element(By.XPATH, "//div[@class='ng-star-inserted']").click()
        # time.sleep(7)
        # driver.find_element(By.LINK_TEXT, "Application").click()
        # time.sleep(10)
        #
        # # Verify Title
        # actual_Title = "CMS Enterprise Portal - My Portal"
        # expected_Title = self.driver.title
        # self.log.info("Verifying Title CMS Enterprise Portal - My Portal")
        # if actual_Title == expected_Title:
        #     assert True
        #     self.log.info("Assertion Passed")
        # else:
        #     assert False

        driver.get("https://www.google.com/gmail/about")
        time.sleep(5)

        driver.find_element(By.ID, "//a[normalize-space()='Sign in']").click()
        driver.find_element(By.ID, "//input[@id='identifierId']").send_keys("dh.purvi@gmail.com")
        driver.find_element(By.XPATH, "//span[normalize-space()='Next'])[1]").click()
        driver.find_element(By.XPATH, "//input[@name='Passwd']").send_keys("county040671")
        driver.find_element(By.XPATH, "(//div[@class='VfPpkd-RLmnJb'])[2]").click()






        # This solution did not work
        # driver.switch_to.frame(driver.find_element(By.XPATH,"//objectx0020data[@id='obj_crowd_wab_application']"))
        # print(driver.title)
        # Type Error ,str object is not callable
        # str=driver.find_element(By.XPATH("//object[@id='obj_crowd_wab_application']")).find_element(By.XPATH, "//h1[@id='focus-main-content']").text
        # print(str)
        #Overstock
        # welcome = driver.find_element(By.XPATH, "//h1[@id='focus-main-content']")
        # driver.find_element(By.XPATH("//object[@id='obj_crowd_wab_application']")).get_attribute(welcome)

        # reportLink = driver.find_element(By.XPATH, "//span[normalize-space()='Reports']")
        # driver.execute_script("arguments[0].click();", reportLink)
        time.sleep(20)
        reportLink = driver.find_element(By.XPATH,
                                              "//span[@class='mat-list-item-content'][normalize-space()='Reports']")
        driver.execute_script("arguments[0].click();", reportLink)
        time.sleep(30)







        # # parent_handle= self.driver.current_window_handle
        # # print(parent_handle)
        #
        # #Click on Application
        # self.driver.find_element(By.LINK_TEXT, "Application").click()
        # print("click on CROWD")
        # print(driver.title)
        # time.sleep(30)
        #
        # # child_hanlde = self.driver.current_window_handle
        # # print(child_hanlde)
        #
        #
        # driver.get("https://portaldev.cms.gov/myportal/wps/myportal/cmsportal/crowd/verticalRedirect/application")
        # time.sleep(10)

        # str1 =driver.find_element(By.XPATH, "//main[@id='main-home']/div/h1").text # //div[@class='ng-star-inserted']   //div[@id='homeTitleRow']/h1
        # print(str1)


        #str1= self.driver.find_element(By.XPATH, "//div[@id='homeTitleRow']/h1")

        # print(str1)
        # if str1 == "Welcome to CROWD":
        #     assert True
        # else:
        #     assert False

