import time

import pytest
import softest

from pageObjects.FileStatusPage import FileStatusPage
from pageObjects.FormPage import FormPage
from pageObjects.HomePage import HomePage


#@pytest.mark.usefixtures("setup_and_teardown",scope="class")
@pytest.mark.usefixtures("setup_and_teardown")
class Test_FormPage(softest.TestCase):

    def test_verifyEachForm(self):
        #Verifying the functionality on Submitted By
        hp = HomePage(self.driver)
        #fs = FileStatusPage(self.driver)
        formPage = FormPage(self.driver)
        hp.loadApplication()
        formPage.click_OnEachForm()

    def test_verifyExportFunctionalirty(self):
        #Verifying the functionality on Submitted By
        hp = HomePage(self.driver)
        #fs = FileStatusPage(self.driver)
        formPage = FormPage(self.driver)
        hp.loadApplication()
        actual_result =formPage.verify_ExportFunctionality()
        expected_result="Pass"

        self.soft_assert(self.assertEqual, actual_result, expected_result)
        self.assert_all()
