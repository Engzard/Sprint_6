import allure
from pages.base_page import BasePage
from locators import OrderLocators

class OrderPage(BasePage):
    @allure.step('Открытие главной страницы')
    def open(self):
        self.go_to_site(self.url)

    @allure.step('Заполнение первой страницы заказа')
    def fill_customer_info(self, name, lastname, address, phone, metro_station):
        self.send_keys(OrderLocators.name_input, name)
        self.send_keys(OrderLocators.lastname_input, lastname)
        self.send_keys(OrderLocators.address_input, address)
        self.send_keys(OrderLocators.phone_input, phone)
        self.click(OrderLocators.metro_input)
        self.click(OrderLocators.get_metro_station(metro_station))
        self.click(OrderLocators.next_button)
    @allure.step('Заполнение второй страницы заказа')
    def fill_rent_info(self, date, period, color, comment):
        self.clear_and_send_keys(OrderLocators.date_input, date)
        self.click(OrderLocators.rent_period_dropdown)
        self.click(OrderLocators.get_rent_period(period))
        if color == "чёрный жемчуг":
            self.click(OrderLocators.black_color_checkbox)
        else:
            self.click(OrderLocators.grey_color_checkbox)
        self.send_keys(OrderLocators.comment_input, comment)
    @allure.step('Подтверждение заказа')
    def confirm_order(self):
        self.wait_for_element(OrderLocators.order_button)
        self.click(OrderLocators.order_button)
        self.wait_for_element(OrderLocators.confirm_button)
        self.click(OrderLocators.confirm_button)
    @allure.step("Проверить успешность оформления заказа")
    def is_order_successful(self):
        success_text = self.get_text(OrderLocators.success_message)
        return success_text == "Заказ оформлен"
