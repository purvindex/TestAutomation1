import time
import pytest
import softest
from selenium.webdriver.common.by import By

from pageObjects.FileUploadPage import FileUploadPage
from pageObjects.FormPage import FormPage
from pageObjects.HomePage import HomePage
from pageObjects.FileStatusPage import FileStatusPage
# pytest --html=..\Reports\report.html test_dataDrivenTesting_TestEnv.py
#pytest --alluredir=..\Allure_Reports test_dataDrivenTesting_TestEnv.py

#@pytest.mark.usefixtures("setup_and_teardown",scope="class")
@pytest.mark.usefixtures("setup_and_teardown")
class Test_FileUploadPage(softest.TestCase):
    @pytest.mark.smoke
    def test_FileUploadPageTitle(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileUpload()
        time.sleep(6)
        expected_Title = "File Upload"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_titleOfFileUploadPage(), expected_Title)
        self.assert_all()

    @pytest.mark.regression
    def test_FileUpload_withACCEPTED_Status(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileUpload()
        fileUploadPage.fileUpload_withAcceptedStatus()
        #fileUploadPage.enterComment()
        fileUploadPage.click_OnSubmitButton()
        fileUploadPage.click_OnFileStatusPage()
        fileUploadPage.click_OnSearchbox("Valid_FormQ_2020_Q3.txt")
        time.sleep(3)
        expected_Status = "ACCEPTED"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_AcceptedMessage(), expected_Status)
        self.assert_all()

    @pytest.mark.regression
    def test_FileUpload_withFAILED_Status(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileUpload()
        fileUploadPage.fileUpload_withFailedStatus()
        #fileUploadPage.enterComment()
        fileUploadPage.click_OnSubmitButton()
        fileUploadPage.click_OnFileStatusPage()
        fileUploadPage.click_OnSearchbox("FORMQ_NoAccess_JuriCAA.txt") # --N/A case
        time.sleep(4)
        fileUploadPage.click_OnFAILED()
        time.sleep(5)

        expected_failedStatus = "Status: FAILED"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_failedMessage(), expected_failedStatus)

        expected_prevalidationmsg = "PRE-VALIDATION ERROR(S)"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_preValidationMessage(), expected_prevalidationmsg)

        expected_Note = "Note: The file failed Pre-Validation. Please correct the PRE-VALIDATION ERROR(S) and upload/submit the file again."
        self.soft_assert(self.assertEqual, fileUploadPage.verify_Note(), expected_Note)

        expected_formText = "FORM="
        formName = fileUploadPage.verify_formName()
        formWords = formName.split()
        first_word =  formWords[0] # This will give word FORM='' with one letter let say FORM=E
        word =first_word[:5] # This will extract the last character of FORM=, it will extract E or any form letter

        #self.soft_assert(self.assertTrue(formName.contains(expected_formText)))
        #assert fileUploadPage.verify_formName().__contains__(expected_formText)
        self.soft_assert(self.assertEqual, word, expected_formText)

        self.assert_all()

    @pytest.mark.regression
    def test_FileUpload_withREJECTED_Status(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileUpload()
        fileUploadPage.fileUpload_withRejectedStatus()
        fileUploadPage.enterComment()
        fileUploadPage.click_OnSubmitButton()
        fileUploadPage.click_OnFileStatusPage()
        #fileUploadPage.click_OnSearchbox("B_invalid_multiple.txt") # Dev Environment with option 1 button
        #fileUploadPage.click_OnSearchbox("VALIDATION_BAD_L2_C1_FORM_Q.txt")
        fileUploadPage.click_OnSearchbox("FORMQ.txt")
        time.sleep(4)
        fileUploadPage.click_OnREJECTED()
        time.sleep(5)

        expected_rejectedStatus = "Status: REJECTED"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_rejectedMessage(), expected_rejectedStatus)

        expected_seriouserrormsg = "SERIOUS ERROR(S)"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_seriousErrorMessage(), expected_seriouserrormsg)

        expected_formText = "FORM=Q"
        self.soft_assert(self.assertEqual, expected_formText, fileUploadPage.verify_formName())

        expected_rejected_note = "Note: The deadline to request an override for the file is"
        noEleigible_expected_note = "Note: The file is no longer eligible for an override request."
        totalButtons = self.driver.find_elements(By.XPATH, "//span[@class='mdc-button__label']")
        tot_Buttons= len(totalButtons)
        if(tot_Buttons==1):
            self.soft_assert(self.assertTrue,noEleigible_expected_note in fileUploadPage.verify_noEleigible_rejectedNote())
        else:
            self.soft_assert(self.assertTrue, expected_rejected_note in fileUploadPage.verify_rejectedNote())

        self.assert_all()

    @pytest.mark.regression
    def test_verify_AcceptedOverride(self):
        homePage = HomePage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        formPage = FormPage(self.driver)
        homePage.loadApplication()
        fileUploadPage.click_OnFileSubmission()
        fileUploadPage.click_OnFileStatusPage()
        time.sleep(8)
        fileUploadPage.click_OnSearchbox("ACCEPTED (WITH OVERRIDE)")
        fileUploadPage.click_OnAcceptedWithOverride()
        # fileUploadPage.verify_formName()
        time.sleep(6)
       # formPage.click_OnForm()
        formPage.click_OnFormpage()
        #formPage.click_OnForm()
        #formPage.switch_ToWindow()
        formPage.select_YearMonth()
        time.sleep(5)








