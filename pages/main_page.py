import allure

from pages.base_page import BasePage
from locators import  MainPageLocators


class MainPage(BasePage):
    @allure.step('Открытие главной страницы')
    def open(self):
        self.go_to_site(self.url)
    @allure.step('Нажатие верхней кнопки заказа')
    def click_order_top_button(self):
        self.click(MainPageLocators.order_top_button)
    @allure.step('Нажатие нижней кнопки заказа')
    def click_order_bottom_button(self):
        self.click(MainPageLocators.order_bottom_button)
    @allure.step('Нажатие лого самоката')
    def click_scooter_logo(self):
        self.click(MainPageLocators.scooter_logo)
    @allure.step('Нажатие лого Яндекс')
    def click_yandex_logo(self):
        self.click(MainPageLocators.yandex_logo)
    def main_page_chek(self):
        return self.get_current_url() == "https://qa-scooter.praktikum-services.ru/"
    def dzen_page_chek(self):
        return self.get_current_url() == "https://dzen.ru/"