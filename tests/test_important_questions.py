import allure
import pytest
from pages.question_page import QuestionPage
from data import questions_data
@allure.feature("Тесты Важных вопросов")
class TestAccordion(QuestionPage):

    @allure.title("Проверка ответов на вопросы")
    @pytest.mark.parametrize("question_locator, answer_locator, expected_text", questions_data)
    def test_question_answer(self, question_locator, answer_locator, expected_text):
        question_page = QuestionPage(self)
        with allure.step('Открытие главной страницы'):
            question_page.open()
        with allure.step('Прокрутка к полю вопросов'):
            question_page.scroll_to_question()
        with allure.step('Нажатие на вопрос'):
            question_page.click_question(question_locator)
        actual_text = self.get_answer_text(answer_locator)
        assert expected_text in actual_text
