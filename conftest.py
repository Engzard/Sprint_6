import pytest
from selenium import webdriver

@pytest.fixture
def scroll_to_question(driver):
    def _scroll(element):
        driver.execute_script("arguments[0].scrollIntoView();", element)
    return _scroll

@pytest.fixture(scope="class")
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope="class")
def page(driver):
    page = MainPage(driver)
    page.open()
    return page
