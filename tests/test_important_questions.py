import allure
import pytest
from pages.base_page import BasePage
from locators import AccordionLocators

@allure.feature("Тесты Важных вопросов")
class TestAccordion(BasePage):
    questions_data = [
        (AccordionLocators.first_question, AccordionLocators.first_answer,
         'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'),
        (AccordionLocators.second_question, AccordionLocators.second_answer,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'),
        (AccordionLocators.third_question, AccordionLocators.third_answer,
         'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        (AccordionLocators.fourth_question, AccordionLocators.fourth_answer,
         'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'),
        (AccordionLocators.fifth_question, AccordionLocators.fifth_answer,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'),
        (AccordionLocators.sixth_question, AccordionLocators.sixth_answer,
         'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'),
        (AccordionLocators.seventh_question, AccordionLocators.seventh_answer,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'),
        (AccordionLocators.eighth_question, AccordionLocators.eighth_answer,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
    ]

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", questions_data)
    def test_question_answer(self, question_locator, answer_locator, expected_text):
        self.wait_for_clickable(question_locator).click()
        actual_text = self.wait_for_visible(answer_locator).text
        assert expected_text in actual_text
