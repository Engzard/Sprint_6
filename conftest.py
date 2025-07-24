import pytest
from selenium import webdriver
from pages.question_page import QuestionPage




@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def page(driver):
    page = QuestionPage(driver)
    page.open()
    page.scroll_to_question()
    return page
