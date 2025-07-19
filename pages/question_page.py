from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage

class QuestionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = "https://qa-scooter.praktikum-services.ru/"
        self.driver = driver
        self.subheader_locator = (By.CLASS_NAME, "Home_SubHeader__zwi_E")

    def open(self):
        self.go_to_site(self.url)

    def scroll_to_question(self):
        subheader = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.subheader_locator)
        )
        self.driver.execute_script("arguments[0].scrollIntoView();", subheader)

    def click_question(self, locator):
        self.click(locator)

    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)