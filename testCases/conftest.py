from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from utilities import ReadConfigurations
from selenium import webdriver
import pytest

#@pytest.fixture() this code was working
#def setup():
 #   driver=webdriver.Chrome()
  #  return driver
@pytest.fixture(scope="class")
def setup_and_teardown(request):
    browser = ReadConfigurations.read_configuration("basic info", "browser")
    if browser.__eq__("chrome"):
        #driver = webdriver.Chrome()  this is working fine the single line
        c = webdriver.ChromeOptions()
        c.add_argument("--incognito")
        driver = webdriver.Chrome(c)
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    else:
        driver = webdriver.Edge()
    driver.maximize_window()
    driver.implicitly_wait(22)
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    # uname=ReadConfigurations.read_configuration("basic info", "username")
    # driver.find_element(By.ID, "cms-login-userId").send_keys(uname)
    # pswd=ReadConfigurations.read_configuration("basic info", "password")
    # driver.find_element(By.ID, "cms-login-password").send_keys(pswd)
    request.cls.driver = driver # whichever class will request this driver is available to that class
    yield
    driver.quit()

@pytest.fixture(scope="class")
def setupandteardown(request):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://portalval.cms.gov/portal/")
    #driver.get("https://portaldev.cms.gov/portal/")
    request.cls.driver = driver
    yield
    driver.quit()









