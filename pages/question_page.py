import allure
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class QuestionPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.subheader_locator = (By.CLASS_NAME, "Home_SubHeader__zwi_E")
    @allure.step('Открытие главной страницы')
    def open(self):
        self.go_to_site(self.url)
    @allure.step('Прокрутка к полю вопросов')
    def scroll_to_question(self):
        subheader = self.wait_for_element_presence(self.subheader_locator)
        self.scroll_to_element(subheader)
    @allure.step('Нажатие на вопрос')
    def click_question(self, locator):
        self.click(locator)

    def get_answer_text(self, answer_locator):
        return self.get_text(answer_locator)