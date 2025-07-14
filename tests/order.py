import pytest
import allure
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import OrderLocators, MainPageLocators

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def go_to_site(self, url):
        self.driver.get(url)

    def wait_for_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(
            EC.element_to_be_clickable(locator)
        )

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
        WebDriverWait(self.driver, timeout).until(
            EC.url_contains(text))
    def get_text(self, locator, timeout=10):
        element = self.wait_for_element(locator, timeout)
        return element.text

class MainPage(BasePage):
    def click_order_top_button(self):
        self.click(MainPageLocators.order_top_button)
    def click_order_bottom_button(self):
        self.click(MainPageLocators.order_bottom_button)

    def click_scooter_logo(self):
        self.click(MainPageLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click(MainPageLocators.yandex_logo)


class OrderPage(BasePage):
    def fill_customer_info(self, name, lastname, address, phone, metro_station):
        self.send_keys(OrderLocators.name_input, name)
        self.send_keys(OrderLocators.lastname_input, lastname)
        self.send_keys(OrderLocators.address_input, address)
        self.send_keys(OrderLocators.phone_input, phone)
        self.click(OrderLocators.metro_input)
        self.click(OrderLocators.get_metro_station(metro_station))
        self.click(OrderLocators.next_button)

    def fill_rent_info(self, date, period, color, comment):
        self.clear_and_send_keys(OrderLocators.date_input, date)
        self.click(OrderLocators.rent_period_dropdown)
        self.click(OrderLocators.get_rent_period(period))
        if color == "чёрный жемчуг":
            self.click(OrderLocators.black_color_checkbox)
        else:
            self.click(OrderLocators.grey_color_checkbox)
        self.send_keys(OrderLocators.comment_input, comment)

    def confirm_order(self):
        self.wait_for_element(OrderLocators.order_button)
        self.click(OrderLocators.order_button)
        self.wait_for_element(OrderLocators.confirm_button)
        self.click(OrderLocators.confirm_button)
class TestScooterOrder:

    @pytest.mark.parametrize("customer_data", [
    {
        "name": "Иван",
        "lastname": "Дров",
        "address": "ул. Ленина, 1",
        "phone": "+79191234567",
        "date": "31.07.2025",
        "period": "сутки",
        "color": "чёрный жемчуг",
        "metro": "Сокол",
        "comment": "Позвонить за час до приезда"
    },
    {
        "name": "Мария",
        "lastname": "Киррова",
        "address": "пр. Мира, 10",
        "phone": "+79007654321",
        "date": "20.07.2025",
        "period": "двое суток",
        "color": "серая безысходность",
        "metro": "Красносельская",
        "comment": "Оставить у парадной"
        }
    ])
    @allure.feature("Оформление заказа(верхняя кнопка)")
    def test_order_via_top_button(driver, customer_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        main_page.click_order_top_button()
        with allure.step("Заполняем информацию о клиенте(страница 1)"):
            order_page.fill_customer_info(
                customer_data["name"],
                customer_data["lastname"],
                customer_data["address"],
                customer_data["phone"],
                customer_data["metro"]
            )

        with allure.step("Заполняем информацию о клиенте(страница 2)"):
            order_page.fill_rent_info(
                customer_data["date"],
                customer_data["period"],
                customer_data["color"],
                customer_data["comment"]
            )

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
            success_text = order_page.get_text(OrderLocators.success_message)
            assert success_text == "Заказ оформлен"

    @allure.feature("Оформление заказа(нижняя кнопка)")
    def test_order_via_bottom_button(driver, customer_data):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)

        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        main_page.click_order_bottom_button()

        with allure.step("Заполняем информацию о клиенте(страница 1)"):
            order_page.fill_customer_info(
                customer_data["name"],
                customer_data["lastname"],
                customer_data["address"],
                customer_data["phone"],
                customer_data["metro"]
            )

        with allure.step("Заполняем информацию о клиенте(страница 2)"):
            order_page.fill_rent_info(
                customer_data["date"],
                customer_data["period"],
                customer_data["color"],
                customer_data["comment"]
            )

        with allure.step("Подтверждаем заказ"):
            order_page.confirm_order()
            success_text = order_page.get_text(OrderLocators.success_message)
            assert success_text == "Заказ оформлен"

    @allure.feature("Редирект по логотипу Самоката")
    def test_scooter_logo_redirect(driver):
        main_page = MainPage(driver)

        driver.get("https://qa-scooter.praktikum-services.ru/order")
        main_page.click_scooter_logo()

        assert main_page.get_current_url() == "https://qa-scooter.praktikum-services.ru/"

    @allure.feature("Редирект по логотипу Яндекса")
    def test_yandex_logo_redirect(driver):
        main_page = MainPage(driver)

        main_page.go_to_site("https://qa-scooter.praktikum-services.ru/")
        main_page.click_yandex_logo()
        main_page.wait_for_url_contains("dzen.ru")

        assert driver.current_url == "https://dzen.ru/"
