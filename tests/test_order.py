import pytest
import allure
from locators import OrderLocators
from pages.main_page import MainPage
from pages.order_page import OrderPage

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
