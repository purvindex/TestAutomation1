import time

import pytest
import softest

from pageObjects.FileUploadPage import FileUploadPage
from pageObjects.FormPage import FormPage
from pageObjects.HomePage import HomePage

@pytest.mark.usefixtures("setup_and_teardown")
class Test_FileUploadPage(softest.TestCase):

    def test_AcceptedOverride(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        formPage = FormPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileSubmission()
        fileUploadPage.click_OnFileStatusPage()
        time.sleep(8)
        fileUploadPage.click_OnSearchbox("ACCEPTED (WITH OVERRIDE)")
        fileUploadPage.click_OnAcceptedWithOverrideButton()
        first_Seriouserror= formPage.seriousError()

        ### Working fine
        formName_WN_Year= formPage.formName_WN_Year_BSI()
        time.sleep(3)
        formPage.click_OnAcceptedOverrideForm(formName_WN_Year)
        time.sleep(2)
        formPage.switch_ToWindow()
        time.sleep(2)
        formPage.select_YearMonth(formName_WN_Year)
        formPage.verify_LineColumnValue(first_Seriouserror)




