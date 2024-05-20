
from selenium.webdriver.support import expected_conditions as EC, wait


class BaseDriver:

    def __init__(self,driver):
        self.driver=driver

    def page_scroll(self,direction):
        pass
    def wait_for_presence_of_all_elements(self,locator_type, locator):
        list_of_elements = self.wait.until(EC.presence_of_all_elements_located((locator_type,locator)))
        return list_of_elements

    def wait_until_element_is_clickable(self,locator_type,locator):
        element = self.wait.until(EC.element_to_be_clickable((locator_type,locator)))
        return element




