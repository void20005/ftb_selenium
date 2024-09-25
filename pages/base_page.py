import logging
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

class BasePage:
    def __init__(self, driver, url=None):
        self.driver = driver
        self.url = url
        self.logger = logging.getLogger(self.__class__.__name__)

    def open(self):
        if self.url:
            self.logger.info(f"Opening URL: {self.url}")
            self.driver.get(self.url)

    def wait_for_element_visible(self, locator, timeout=5):
        self.logger.info(f"Waiting for element {locator} to be visible")
        return Wait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_element_clickable(self, locator, timeout=5):
        self.logger.info(f"Waiting for element {locator} to be clickable")
        return Wait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def wait_for_element_present(self, locator, timeout=5):
        self.logger.info(f"Waiting for element {locator} to be present")
        return Wait(self.driver, timeout).until(EC.presence_of_element_located(locator))

    def wait_for_element_invisible(self, locator, timeout=5):
        self.logger.info(f"Waiting for element {locator} to be invisible")
        return Wait(self.driver, timeout).until(EC.invisibility_of_element(locator))

    def click_element(self, locator, timeout=5):
        self.logger.info(f"Clicking on element {locator}")
        element = self.wait_for_element_clickable(locator, timeout)
        element.click()

    def enter_text(self, locator, text, timeout=5):
        self.logger.info(f"Entering text into element {locator}: {text}")
        element = self.wait_for_element_visible(locator, timeout)
        element.clear()
        element.send_keys(text)

    def is_element_present(self, locator, timeout=5):
        try:
            self.logger.info(f"Checking if element {locator} is present")
            self.wait_for_element_present(locator, timeout)
            return True
        except:
            self.logger.warning(f"Element {locator} not found")
            return False

    def select_by_value(self, locator, value, timeout=5):
        self.logger.info(f"Selecting value {value} from dropdown {locator}")
        select_element = Select(self.wait_for_element_visible(locator, timeout))
        select_element.select_by_value(value)

    def select_by_text(self, locator, text, timeout=5):
        self.logger.info(f"Selecting text {text} from dropdown {locator}")
        select_element = Select(self.wait_for_element_visible(locator, timeout))
        select_element.select_by_visible_text(text)

    def select_by_index(self, locator, index, timeout=5):
        self.logger.info(f"Selecting index {index} from dropdown {locator}")
        select_element = Select(self.wait_for_element_visible(locator, timeout))
        select_element.select_by_index(index)
