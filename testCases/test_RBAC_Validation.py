import time
import allure
import pytest
import softest
from allure_commons.types import AttachmentType
import os

from pageObjects.FileStatusPage import FileStatusPage
from pageObjects.FileUploadPage import FileUploadPage
from pageObjects.HomePage import HomePage
from pageObjects.RBACValidationPage import RBACValidationPage
#pytest -m "regression" --alluredir=..\Allure_Reports test_RBAC_Validation.py

@pytest.mark.usefixtures("setupandteardown")
class Test_RBACValidation(softest.TestCase):
    @pytest.mark.regression
    def test_ContractorRole(self):
        homePage = HomePage(self.driver)
        RBACPage = RBACValidationPage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        RBACPage.enter_username("CTR_DEV")
        RBACPage.enter_password("Contractor_112723")
        # RBACPage.enter_username("PDCTR_VAL")
        # RBACPage.enter_password("Crowd_val_112723")

        homePage.loadApplication()
        RBACPage.click_OnFileSubmission()
        fileUploadPage.click_OnFileStatusPage()
        fileUploadPage.click_OnSearchbox("FORMQ_NoAccess_JuriCAA.txt")
        RBACPage.isFileuploadOptionExits()
        RBACPage.isAdminOptionExits()
        allure.attach(self.driver.get_screenshot_as_png(),"NOTE:-'File Upload' & 'ADMIN' option not available.", attachment_type=AttachmentType.PNG)
        expected_displayedRecrod = '0 of 0'
        self.soft_assert(self.assertEqual, RBACPage.isRecordDisplayed(), expected_displayedRecrod )
        self.soft_assert(self.assertEqual, RBACPage.isFileuploadOptionExits(), 0)
        self.soft_assert(self.assertEqual, RBACPage.isAdminOptionExits(), 0)
        self.assert_all()

    @pytest.mark.regression
    def test_ContractorPOCRole(self):
        homePage = HomePage(self.driver)
        RBACPage = RBACValidationPage(self.driver)
        fileUploadPage = FileUploadPage(self.driver)
        fileStatusPage = FileStatusPage(self.driver)
        RBACPage.enter_username("POC_DEV")
        RBACPage.enter_password("Contractor_112723")
        #RBACPage.enter_username("PDPOC_VAL")
        #RBACPage.enter_password("Crowd_dev_112723")
        homePage.loadApplication()
        fileUploadPage.click_OnFileUpload()
        fileUploadPage.fileUpload_withAcceptedStatus()
        fileUploadPage.click_OnSubmitButton()
        fileUploadPage.click_OnFileStatusPage()
        time.sleep(5)
        fileStatusPage.click_OnRefreshButton()
        fileStatusPage.click_OnRefreshButton()
        fileStatusPage.click_OnRefreshButton()
        time.sleep(5)
        #fileUploadPage.click_OnSearchbox("Valid_FormQ_2020_Q3.txt")
        fileUploadPage.click_OnSearchbox("Valid_FormS.txt")
        time.sleep(6)
        expected_Status = "ACCEPTED"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_AcceptedMessage(), expected_Status)
        time.sleep(5)

        fileUploadPage.click_OnFileUpload()
        time.sleep(5)
        fileUploadPage.fileUpload_withFailedStatus()
        fileUploadPage.click_OnSubmitButton()
        fileUploadPage.click_OnFileStatusPage()
        fileStatusPage.click_OnRefreshButton()
        fileStatusPage.click_OnRefreshButton()
        time.sleep(8)
        fileUploadPage.click_OnSearchbox("FORMQ_NoAccess_JuriCAA.txt")
        time.sleep(5)
        fileUploadPage.click_OnFAILED()
        allure.attach(self.driver.get_screenshot_as_png(),
                      "NOTE:- Contractor POC can only see file on 'File Status' page according to assign Jurisdiction",
                      attachment_type=AttachmentType.PNG)


        expected_failedStatus = "Status: FAILED"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_failedMessage(), expected_failedStatus)

        expected_prevalidationmsg = "PRE-VALIDATION ERROR(S)"
        self.soft_assert(self.assertEqual, fileUploadPage.verify_preValidationMessage(), expected_prevalidationmsg)

        expected_Note = "Note: The file failed Pre-Validation. Please correct the PRE-VALIDATION ERROR(S) and upload/submit the file again."
        self.soft_assert(self.assertEqual, fileUploadPage.verify_Note(), expected_Note)

        expected_formText = "FORM="
        #formName = fileUploadPage.verify_formName()    formWords = formName.split()   first_word = formWords[0]  # This will give word FORM='' with one letter let say FORM=E
        #word = first_word[:5]  # This will extract the last character of FORM=, it will extract E or any form letter
        #self.soft_assert(self.assertEqual, word, expected_formText)

        self.soft_assert(self.assertTrue, expected_formText in fileUploadPage.verify_formName())

        RBACPage.isAdminOptionExits()
        allure.attach(self.driver.get_screenshot_as_png(), "NOTE:- 'File Upload' option available & 'ADMIN' option not available.", attachment_type=AttachmentType.PNG)
        #self.soft_assert(self.assertEqual, RBACPage.isFileuploadOptionExits(), 1)
        self.soft_assert(self.assertEqual, RBACPage.isAdminOptionExits(), 0)
        self.assert_all()

    @pytest.mark.regression
    def test_GovernmentRole(self):
        homePage = HomePage(self.driver)
        RBACPage = RBACValidationPage(self.driver)
        RBACPage.enter_username("GOV_DEV")
        RBACPage.enter_password("Contractor_112723")
        homePage.loadApplication()
        RBACPage.click_OnFileSubmission()
        RBACPage.isFileuploadOptionExits()
        RBACPage.isAdminOptionExits()
        allure.attach(self.driver.get_screenshot_as_png(), "NOTE:- 'File Upload' & 'ADMIN' options are not available.",
                      attachment_type=AttachmentType.PNG)
        self.soft_assert(self.assertEqual, RBACPage.isFileuploadOptionExits(), 0)
        self.soft_assert(self.assertEqual, RBACPage.isAdminOptionExits(), 0)
        self.assert_all()

    @pytest.mark.regression
    def test_AdminRole(self):
        homePage = HomePage(self.driver)
        RBACPage = RBACValidationPage(self.driver)
        RBACPage.enter_username("ADM_DEV")
        RBACPage.enter_password("Contractor_112723")
        homePage.loadApplication()
        RBACPage.click_OnFileSubmission()
        RBACPage.isFileuploadOptionExits()
        RBACPage.isAdminOptionExits()
        RBACPage.click_OnADMIN()
        allure.attach(self.driver.get_screenshot_as_png(), "NOTE:- 'File Upload' option is not available & 'ADMIN' Option is available",
                      attachment_type=AttachmentType.PNG)
        self.soft_assert(self.assertEqual, RBACPage.isFileuploadOptionExits(), 0)
        self.soft_assert(self.assertEqual, RBACPage.isAdminOptionExits(), 1)
        self.assert_all()

    @pytest.mark.regression
    def test_HelpDeskRole(self):
        homePage = HomePage(self.driver)
        RBACPage = RBACValidationPage(self.driver)
        RBACPage.enter_username("SDHD_001")
        RBACPage.enter_password("Crowd_dev_080923")
        homePage.loadApplication()
        RBACPage.click_OnFileSubmission()
        RBACPage.isFileuploadOptionExits()
        RBACPage.isAdminOptionExits()
        allure.attach(self.driver.get_screenshot_as_png(), "NOTE:- 'File Upload' & 'ADMIN' options are not available.",
                      attachment_type=AttachmentType.PNG)
        self.soft_assert(self.assertEqual, RBACPage.isFileuploadOptionExits(), 0)
        self.soft_assert(self.assertEqual, RBACPage.isAdminOptionExits(), 0)
        self.assert_all()





