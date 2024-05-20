import random
import time
from telnetlib import EC

import softest
from selenium.common import NoSuchElementException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from Base.base_Driver import BaseDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TablePage(BaseDriver,softest.TestCase):
    btn_Tables_xpath = "//span[@class='list-item-label'][normalize-space()='Tables']"

    # FORM Microstrategye page
    icon_2023_xpath = "//div[contains(@title,'2023')]//img[contains(@class,'mstrTreeViewNodeConnector')]"
    icon_Year_Quarter_xpath = "//*[contains(text(),'YEAR-')]/preceding-sibling::img"
    year_Quarter_xpath = "//*[contains(text(),'2023-')]"
    add_Arrow_xpath = "//div[@id='id_mstr106']//img[@title='Add']"
    run_Document_xpath = "//input[@id='id_mstr249']"

    ##### MSTR Microstrategey page 2
    total_text = "//div[@class='mstrmojo-tabcontainer-tabs']/div/div/div/span"
    frm_version_xpath = "(//div[@class='mstrmojo-DocTextfield-valueNode'][normalize-space()='CROWD (2024.1.0)'])[1]"  # CROWD (2024.1.0)
    form_Name_xpath = "//*[contains(text(), 'FORM')]"
    all_FormHeadings = "//div[@class='mstrmojo-DocTextfield-valueNode']"
    all_FormHeadingsNationalTotals = "//div[@class='mstrmojo-DocTextfield-valueNode']"

    national_Total_xpath = "//div[@class='c']/div/span[2]"

    ##### Ascending, Descending Order Locators
    sortButton_xpath = "//div[@class='tablePresentation']/table/thead/tr/th[1]/div/div/following-sibling::div"
    list_OfFilename_xpath = "//tbody[@class='mdc-data-table__content']/tr/td[1]"


    def __init__(self,
                 driver):  # creating constructor init,and driver is an argument and why we are creating when we create init it will be called whenever object of the class will be created  # and passing argument as driver so same driver can be used in test calss
        super().__init__(driver)
        self.driver = driver

    def click_OnTableOption(self):
        self.driver.find_element(By.XPATH, self.btn_Tables_xpath).click()
    def click_OnEachTableLink(self):   # Working fine.
        self.driver.find_element(By.XPATH, self.btn_Tables_xpath).click()
        time.sleep(2)
        for x in range(1,5):
            tableLink = self.driver.find_element(By.XPATH,"//tbody[@class='mdc-data-table__content']/tr[" + str(x) + "]/td[3]/a")
            maxAttempts =3
            attempt=1
            while(attempt <= maxAttempts):
                try:
                   tableLink.click()
                   break
                except Exception as e:
                    print(e)
            time.sleep(2)
            parent_window_id = self.driver.current_window_handle
            windows = self.driver.window_handles
            for w in windows:
                self.driver.switch_to.window(w)
                time.sleep(2)

           #To run  the document --- for FORM F if logic

            icon_2023 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_2023_xpath)))
            icon_2023.click()
            #self.driver.find_element(By.XPATH, self.icon_2023_xpath).click()

            icon_Year_Quarter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath)))
            icon_Year_Quarter.click()
            #self.driver.find_element(By.XPATH, self.icon_Year_Quarter_xpath).click()

            year_Quarter = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.year_Quarter_xpath)))
            year_Quarter.click()
                    #self.driver.find_element(By.XPATH, self.year_Quarter_xpath).click()
                    #time.sleep(2)
            add_Button = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable(self.driver.find_element(By.XPATH, self.add_Arrow_xpath)))
            add_Button.click()
                #self.driver.find_element(By.XPATH, self.add_Arrow_xpath).click()
            time.sleep(1)
            self.driver.find_element(By.XPATH, self.run_Document_xpath).click()

            total_msg = self.driver.find_element(By.XPATH, self.total_text).text
            print(total_msg)
            print(self.driver.title)

            heading_List= self.driver.find_elements(By.XPATH, self.all_FormHeadings)

            #To pull all Totals heading
            i=1
            for each_Heading in heading_List:
                time.sleep(3)
                data = each_Heading.text
                print(data)
                i += 1
                if (i == 3):
                    break
            print("\n")
            time.sleep(2)
            ## National Total
            self.driver.find_element(By.XPATH, self.national_Total_xpath).click()
            print(self.driver.find_element(By.XPATH, self.national_Total_xpath).text)
            print(self.driver.title)

            self.driver.close()
            self.driver.switch_to.window(parent_window_id)
            self.driver.switch_to.frame(self.driver.find_element(By.XPATH, "//object[@id='obj_crowd_wab_application']"))

        ####################### Ascending and Descending  Functionality of Table Page ###########

    def original_List(self):
        list_elements_b4sort = self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath)
        originalList = []
        for elements_b4 in list_elements_b4sort:
            submittedBy1 = elements_b4.text
            originalList.append(submittedBy1)
        print("Original List:-")
        print(originalList)
        return originalList

    def asce_OrderList(self):
        sortButton = self.driver.find_element(By.XPATH, self.sortButton_xpath)
        self.driver.execute_script("arguments[0].click();", sortButton)
        time.sleep(5)
        list_elements_afterSorting = self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath)
        asc_Sorting_List = []
        for element in list_elements_afterSorting:
            submittedBy = element.text
            asc_Sorting_List.append(submittedBy)
        print("\n")
        print("Ascending Order List:-")
        print(asc_Sorting_List)
        return asc_Sorting_List

    def desc_OrederList(self):
        sortButton = self.driver.find_element(By.XPATH, self.sortButton_xpath)
        self.driver.execute_script("arguments[0].click();", sortButton)
        time.sleep(10)
        list_elements_desc_Sorting = self.driver.find_elements(By.XPATH, self.list_OfFilename_xpath)

        desc_Sorting_List = []
        for element in list_elements_desc_Sorting:
            submittedBy = element.text
            desc_Sorting_List.append(submittedBy)
        print("\n")
        print("Descnding Order List:-")
        print(desc_Sorting_List)
        return desc_Sorting_List

