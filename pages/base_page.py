from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout
        self.wait = WebDriverWait(driver, self.timeout)

    def navigate_to_url(self, url):
        self.driver.get(url)

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def wait_for_presence_of_all_elements(self, locator):
        return self.wait.until(ec.presence_of_all_elements_located(locator))

    def wait_for_element_clickable(self, locator):
        return self.wait.until(ec.element_to_be_clickable(locator))

    def wait_for_visibility_of_element(self, locator):
        return self.wait.until(ec.visibility_of_element_located(locator))
