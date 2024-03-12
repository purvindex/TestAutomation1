from selenium.webdriver.common.by import By
from selenium.webdriver.support import wait

from utilities import ReadConfigurations
from selenium import webdriver
import pytest

#@pytest.fixture() this code was working
#def setup():
 #   driver=webdriver.Chrome()
  #  return driver

############Commenting out the following code which is running good so far 28th Feb 2024 #####################
## When you want to run Cross Browser Testing  please comment out below code ##########
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
    driver.implicitly_wait(20)
    app_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(app_url)
    # uname=ReadConfigurations.read_configuration("basic info", "username")
    # driver.find_element(By.ID, "cms-login-userId").send_keys(uname)
    # pswd=ReadConfigurations.read_configuration("basic info", "password")
    # driver.find_element(By.ID, "cms-login-password").send_keys(pswd)
    request.cls.driver = driver # whichever class will request this driver is available to that class
    yield
    driver.quit()

##################  above code is working fine #######################################


################ Below Fixture is to run Cross Browser Testing #####################
# @pytest.fixture(autouse=True)
# def setup(request,browser):
#     #browser = ReadConfigurations.read_configuration("basic info", "browser")
#
#     if browser == "chrome":
#         #driver = webdriver.Chrome()  this is working fine the single line
#         # c = webdriver.ChromeOptions()
#         # c.add_argument("--incognito")
#         driver = webdriver.Chrome()
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#     elif browser == "edge":
#         driver = webdriver.Edge()
#     # app_url = ReadConfigurations.read_configuration("basic info", "url")
#     # driver.get(app_url)
#     driver.maximize_window()
#     driver.get("https://portalval.cms.gov/portal")
#     driver.implicitly_wait(20)
#     # uname=ReadConfigurations.read_configuration("basic info", "username")
#     # driver.find_element(By.ID, "cms-login-userId").send_keys(uname)
#     # pswd=ReadConfigurations.read_configuration("basic info", "password")
#     # driver.find_element(By.ID, "cms-login-password").send_keys(pswd)
#     request.cls.driver = driver # whichever class will request this driver is available to that class
#     yield
#     driver.quit()
#
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#     #parser.addoption("--url")
#
# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")

# @pytest.fixture(scope="class", autouse=True)
# def url(request):
#     return request.config.getoption("--url")

#########################Cross Browser testing ends here ##########################################3

############ Below is working fine for Data Driven Testing script ###################
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
#########################################################################










