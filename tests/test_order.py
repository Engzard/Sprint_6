import pytest
import allure
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
    @allure.title("Оформление заказа(верхняя кнопка)")
    def test_order_via_top_button(self, customer_data):
        main_page = MainPage(self)
        order_page = OrderPage(self)

        with allure.step('Открытие главной страницы'):
            main_page.open()
        with allure.step('Нажатие верхней кнопки заказа'):
            main_page.click_order_top_button()
        with allure.step("Заполнение первой страницы заказа"):
            order_page.fill_customer_info(
                customer_data["name"],
                customer_data["lastname"],
                customer_data["address"],
                customer_data["phone"],
                customer_data["metro"]
            )

        with allure.step('Заполнение второй страницы заказа'):
            order_page.fill_rent_info(
                customer_data["date"],
                customer_data["period"],
                customer_data["color"],
                customer_data["comment"]
            )

        with allure.step('Подтверждение заказа'):
            order_page.confirm_order()
            assert order_page.is_order_successful()

    @allure.title("Оформление заказа(нижняя кнопка)")
    def test_order_via_bottom_button(self, customer_data):
        main_page = MainPage(self)
        order_page = OrderPage(self)
        with allure.step('Открытие главной страницы'):
            main_page.open()
        with allure.step('Нажатие нижней кнопки заказа'):
            main_page.click_order_bottom_button()
        with allure.step("Заполнение первой страницы заказа"):
            order_page.fill_customer_info(
                customer_data["name"],
                customer_data["lastname"],
                customer_data["address"],
                customer_data["phone"],
                customer_data["metro"]
            )

        with allure.step('Заполнение второй страницы заказа'):
            order_page.fill_rent_info(
                customer_data["date"],
                customer_data["period"],
                customer_data["color"],
                customer_data["comment"]
            )

        with allure.step('Подтверждение заказа'):
            order_page.confirm_order()
            assert order_page.is_order_successful()
    @allure.title("Редирект по логотипу Самоката")
    def test_scooter_logo_redirect(self):
        main_page = MainPage(self)
        with allure.step('Открытие главной страницы'):
            main_page.open()
        with allure.step('Нажатие лого самоката'):
            main_page.click_scooter_logo()
        assert main_page.main_page_chek()

    @allure.title("Редирект по логотипу Яндекса")
    def test_yandex_logo_redirect(self):
        main_page = MainPage(self)
        with allure.step('Открытие главной страницы'):
            main_page.open()
        with allure.step('Нажатие лого Яндекс'):
            main_page.click_yandex_logo()
        main_page.wait_for_url_contains("dzen.ru")
        assert main_page.dzen_page_chek()
