from pages.base_page import BasePage
from locators import  MainPageLocators


class MainPage(BasePage):
    def click_order_top_button(self):
        self.click(MainPageLocators.order_top_button)
    def click_order_bottom_button(self):
        self.click(MainPageLocators.order_bottom_button)

    def click_scooter_logo(self):
        self.click(MainPageLocators.scooter_logo)

    def click_yandex_logo(self):
        self.click(MainPageLocators.yandex_logo)