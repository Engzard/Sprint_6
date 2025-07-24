from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://qa-scooter.praktikum-services.ru/"

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def go_to_site(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def click(self, locator):
        self.wait_for_clickable(locator).click()

    def send_keys(self, locator, text):
        self.wait_for_element(locator).send_keys(text)

    def clear_and_send_keys(self, locator, text):
        element = self.wait_for_element(locator)
        element.clear()
        element.send_keys(text)

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url_contains(self, text, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.url_contains(text))

    def wait_for_visible(self, locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text
    def wait_for_element_presence(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))