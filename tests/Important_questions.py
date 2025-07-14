import pytest
import allure
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import AccordionLocators

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.subheader_locator = (By.CLASS_NAME, "Home_SubHeader__zwi_E")

    def open(self):
        self.driver.get("https://qa-scooter.praktikum-services.ru/")
    def scroll_to_question(self):
        subheader = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(self.subheader_locator))
        self.driver.execute_script("arguments[0].scrollIntoView();", subheader)

class TestAccordion:
    @allure.feature("Тесты Важных вопросов")
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.page = MainPage(cls.driver)
        cls.page.open()
        cls.page.scroll_to_question()

    @allure.story("Проверка первого вопроса")
    def test_first_question_click(self,scroll_to_question):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.first_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.first_answer)).text
        expected_text = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'
        assert expected_text in actual_text

    @allure.story("Проверка второго вопроса")
    def test_second_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.second_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.second_answer)).text
        expected_text = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'
        assert expected_text in actual_text

    @allure.story("Проверка третьего вопроса")
    def test_third_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.third_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.third_answer)).text
        expected_text = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'
        assert expected_text in actual_text

    @allure.story("Проверка четвёртого вопроса")
    def test_fourth_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.fourth_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.fourth_answer)).text
        expected_text = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'
        assert expected_text in actual_text

    @allure.story("Проверка пятого вопроса")
    def test_fifth_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.fifth_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.fifth_answer)).text
        expected_text = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'
        assert expected_text in actual_text

    @allure.story("Проверка шестого вопроса")
    def test_sixth_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.sixth_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.sixth_answer)).text
        expected_text = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'
        assert expected_text in actual_text

    @allure.story("Проверка седьмого вопроса")
    def test_seventh_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.seventh_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.seventh_answer)).text
        expected_text = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'
        assert expected_text in actual_text

    @allure.story("Проверка восьмого вопроса")
    def test_eighth_question_click(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(AccordionLocators.eighth_question)).click()
        actual_text = WebDriverWait(self.driver.scroll_to_question, 10).until(EC.visibility_of_element_located(AccordionLocators.eighth_answer)).text
        expected_text = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'
        assert expected_text in actual_text

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
