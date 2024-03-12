import pytest
from selenium import webdriver
@pytest.fixture(autouse=True)
def setup(request,browser):
    #browser = ReadConfigurations.read_configuration("basic info", "browser")

    if browser == "chrome":
        #driver = webdriver.Chrome()  this is working fine the single line
        # c = webdriver.ChromeOptions()
        # c.add_argument("--incognito")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "edge":
        driver = webdriver.Edge()
    # app_url = ReadConfigurations.read_configuration("basic info", "url")
    # driver.get(app_url)
    driver.maximize_window()
    driver.get("https://portalval.cms.gov/portal")
    driver.implicitly_wait(20)
    # uname=ReadConfigurations.read_configuration("basic info", "username")
    # driver.find_element(By.ID, "cms-login-userId").send_keys(uname)
    # pswd=ReadConfigurations.read_configuration("basic info", "password")
    # driver.find_element(By.ID, "cms-login-password").send_keys(pswd)
    request.cls.driver = driver # whichever class will request this driver is available to that class
    yield
    driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser")
    #parser.addoption("--url")

@pytest.fixture(scope="class", autouse=True)
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture(scope="class", autouse=True)
def url(request):
    return request.config.getoption("--url")
