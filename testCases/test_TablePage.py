import time

import pytest
import softest

from pageObjects.HomePage import HomePage
from pageObjects.TablePage import TablePage


@pytest.mark.usefixtures("setup_and_teardown")
class Test_TablePage(softest.TestCase):

    def test_FileStatusPageTitle(self):
        homePage = HomePage(self.driver)
        tablePage = TablePage(self.driver)
        homePage.loadApplication()
        tablePage.click_OnEachTableLink()

    def test_AsceDescOrderFunctionality(self):
        #Verifying the functionality on Submitted By
        homePage = HomePage(self.driver)
        tablePage = TablePage(self.driver)
        homePage.loadApplication()
        tablePage.click_OnTableOption()
        time.sleep(5)
        #fileStatusPage.clickOnSortingButton()

        originalList = tablePage.original_List()
        # fistPage_Timestamp = fileStatusPage.timeStamp_ofFistPage()


        ascList = tablePage.asce_OrderList()
        # fistPage_Timestamp = fileStatusPage.timeStamp_ofFistPage()

        descList = tablePage.desc_OrederList()