import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.common.by import By

from utilities import ReadConfigurations


@pytest.fixture(autouse=True)
def setup_and_teardown(request):
    #browser = ReadConfigurations.read_configuration("basic info", "browser")

    # if browser == "chrome":
    #     #driver = webdriver.Chrome()  this is working fine the single line
    #     # c = webdriver.ChromeOptions()
    #     # c.add_argument("--incognito")
    #     driver = webdriver.Chrome()
    # elif browser == "firefox":
    #     driver = webdriver.Firefox()
    # elif browser == "edge":
    #     driver = webdriver.Edge()
    # # app_url = ReadConfigurations.read_configuration("basic info", "url")
    # # driver.get(app_url)
    # driver.maximize_window()
    # driver.get("https://portalval.cms.gov/portal")
    # driver.implicitly_wait(20)
    # # uname=ReadConfigurations.read_configuration("basic info", "username")
    # # driver.find_element(By.ID, "cms-login-userId").send_keys(uname)
    # # pswd=ReadConfigurations.read_configuration("basic info", "password")
    # # driver.find_element(By.ID, "cms-login-password").send_keys(pswd)
    # request.cls.driver = driver # whichever class will request this driver is available to that class
    # yield
    # driver.quit()

    #  pytest -s testCases --name chrome
    E34_URL = "https://selenium.cloud.cms.gov"
    x=request.config.getoption("--browser")
    print(x)
    if x.__eq__('chrome'):
        options = ChromeOptions()
        options.set_capability("browserName", "chrome")
        options.set_capability("browserVersion", "87")
        # options.set_capability("e34:token", "crowd/bHR0NmI3YjY4MGItMzBkNi00ZGJhLWI0ZWQtMzU5NDNlZDE3Zjlm")
        options.set_capability("e34:token", "5ef51158-1dc8-44")
        options.set_capability("e34:video", "false")
        options.set_capability("e34:l_testName", "Test Basic Selenium Remote")
        driver = webdriver.Remote(
            command_executor="https://selenium.cloud.cms.gov/wd/hub",
            options=options)
        #driver.get('http://saucelabs.com/test/guinea-pig')
        print(f"Remote driver session id: %s", driver.session_id)
        #driver.quit()

        app_url = ReadConfigurations.read_configuration("basic info", "url")
        driver.get(app_url)

        uname = ReadConfigurations.read_configuration("basic info", "username")
        driver.find_element(By.ID, "cms-login-userId").send_keys(uname)

        pswd = ReadConfigurations.read_configuration("basic info", "password")
        driver.find_element(By.ID, "cms-login-password").send_keys(pswd)

        request.cls.driver = driver  # whichever class will request this driver is available to that class
        # request.cls.wait =wait
        yield
        driver.quit()

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    #parser.addoption("--url")
    #parser.addoption("--name", action="store")

# def test_basic_selenium_remote(self):
#     options = ChromeOptions()
#     options.set_capability("browserName", "chrome")
#     options.set_capability("browserVersion", "87")
#     # options.set_capability("e34:token", "crowd/bHR0NmI3YjY4MGItMzBkNi00ZGJhLWI0ZWQtMzU5NDNlZDE3Zjlm")
#     options.set_capability("e34:token", "5ef51158-1dc8-44")
#     options.set_capability("e34:video", "false")
#     options.set_capability("e34:l_testName", "Test Basic Selenium Remote")
#     driver = webdriver.Remote(
#         command_executor="https://selenium.cloud.cms.gov/wd/hub",
#         options=options)
#     driver.get('http://saucelabs.com/test/guinea-pig')
#     print(f"Remote driver session id: %s", driver.session_id)
#     driver.quit()

# @pytest.fixture(scope="class", autouse=True)
# def browser(request):
#     return request.config.getoption("--browser")

# @pytest.fixture(scope="class", autouse=True)
# def url(request):
#     return request.config.getoption("--url")


# @pytest.fixture(scope="class", autouse=True)
# def name(pytestconfig):
#     return pytestconfig.getoption('name')

# def pytest_configure(config):
#     x = config.getoption('name')
#     print(x)  # Any logic that uses option value

# options = ChromeOptions()
        # options.browser_version = '123'
        # options.platform_name = 'Windows 11'
        # options.enable_downloads = True
        # options.page_load_strategy = 'normal'
        # options.acceptInsecureCerts = True
        # options.unhandledPromptBehavior = 'accept'
        #
        # #options.timeouts = 30000
        # cloud_options = {}
        # cloud_options['build'] = "build_1"
        # cloud_options['name'] = "test_abc"
        # cloud_options['authorization'] = "bHR0NmI3YjY4MGItMzBkNi00ZGJhLWI0ZWQtMzU5NDNlZDE3Zjlm"
        # options.set_capability('cloud:options', cloud_options)
        # driver = webdriver.Remote(command_executor=E34_URL + "/wd/hub",keep_alive = True,file_detector= None, options=options)




