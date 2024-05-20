

from selenium import webdriver

import pytest

from selenium.webdriver.chrome.options import Options as ChromeOptions

#parser = argparse.ArgumentParser(description='Process some integers.')

class SampleTest:


    # E34_TEST_NAME = "Sample Test"
    # E34_WAIT_TIME = 60000
    # PAUSE_TIME = 5000

#mvn clean test - Durl = [target_url] - Dtoken = [sbox_token] - Dbrowser = [chrome | firefox] - Dvideo = [true | false]
#$ pytest -q -s --name Brian test_param.py
#  pytest -s tests/my_test_module.py --name abc
#mvn clean test - Durl = https: // www.google.com - Dtoken = xxxxxxxx - xxxx - xx - Dbrowser = firefox - Dvideo = true
    @pytest.fixture(scope="session")
    def name(pytestconfig):
        return pytestconfig.getoption("name")

    def test_print_name(name):
        print(f"\ncommand line param (name): {name}")

    def test_print_name_2(pytestconfig):
        print(f"test_print_name_2(name): {pytestconfig.getoption('name')}")

    # def pytest_generate_tests(metafunc):
    #     # This is called for every test. Only get/set command line arguments
    #     # if the argument is specified in the list of test "fixturenames".
    #     option_value = metafunc.config.option.name
    #     if 'name' in metafunc.fixturenames and option_value is not None:
    #         metafunc.parametrize("name", [option_value])

        # TARGET_URL = pytestconfig.getoption('url')
        # E34_BROWSER = pytestconfig.getoption("browser")
        # E34_TOKEN = pytestconfig.getoption("token")
        # E34_VIDEO = pytestconfig.getoption("video")
        E34_URL = "https://selenium.cloud.cms.gov"
#@ Test(threadPoolSize=5, invocationCount=1)

        if {pytestconfig.getoption('name')}.__eq__('chrome') :
            options = ChromeOptions()
            options.browser_version = '123'
            options.platform_name = 'Windows 10'
            options.timeouts = '60000'
            cloud_options = {}
            cloud_options['build'] = "build_1"
            cloud_options['name'] = "test_abc"
            options.set_capability('cloud:options', cloud_options)
            driver = webdriver.Remote(command_executor = E34_URL + "/wd/hub", options=options)


#     RemoteWebDriver
# driver = null;
# DesiredCapabilities
# Options = new
# DesiredCapabilities();
#
# Options.setCapability("browserName", E34_BROWSER);
# Options.setCapability("e34:token", E34_TOKEN);
# Options.setCapability("e34:video", E34_VIDEO);
# Options.setCapability("e34:l_testName", E34_TEST_NAME);
# // Options.setCapability("browserVersion", E34_BROWSER_VER);
#
# System.out.println("Test Name: " + E34_TEST_NAME);
# System.out.println("Wait Time: " + E34_WAIT_TIME);
# System.out.println("Selenium Webdriver testing initiated");
# System.out.println("    Thread ID: " + Thread.currentThread().getId());
# System.out.println("    Video recording: " + E34_VIDEO);
# System.out.println("    Test Grid: " + E34_URL);
# System.out.println("    Test Browser: " + E34_BROWSER);
# // System.out.println("    Test Browser Version: " + E34_BROWSER_VER);
# System.out.println("    Test Target: " + TARGET_URL);
#
# driver = new
# RemoteWebDriver(new
# URL(E34_URL + "/wd/hub"), Options);
#
# WebDriverWait
# wait = new
# WebDriverWait(driver, E34_WAIT_TIME);
#
# try {
#
# driver.get(TARGET_URL);
# System.out.println("Status: BEGIN");
#
# // TEST BEGIN
# // TIP: Copy
# codes
# exported
# from Selenium IDE
#
# for (int cntr = 1; cntr <= 3; cntr = cntr + 1) {
#     driver.navigate().refresh();
# System.out.println("  Refresh Count : " + cntr);
# Thread.sleep(PAUSE_TIME);
# }
#
# // TEST END
#
# driver.close();
# System.out.println("Status: SUCCESS");
#
# } catch (Exception e) {
# File tmp = driver.getScreenshotAs(OutputType.FILE);
# File dest = new File("x-exception-" + driver.getSessionId().toString() + ".png");
# tmp.renameTo(dest);
# System.out.println(dest.getAbsolutePath());
# throw e;
# } finally {
# driver.quit();
#
# }
# }
# }