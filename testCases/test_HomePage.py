import time
import pytest
from pageObjects.HomePage import HomePage
from selenium.webdriver.common.by import By

@pytest.mark.usefixtures("setup_and_teardown",scope="class")
class Test_HomePage:
   
    def test_homePage(self):
        hp = HomePage(self.driver)
        time.sleep(5)
        hp.loadApplication()
