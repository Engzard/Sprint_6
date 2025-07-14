from selenium.webdriver.common.by import By
class AccordionLocators:
    first_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Сколько это стоит? И как оплатить?']")
    second_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Хочу сразу несколько самокатов! Так можно?']")
    third_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Как рассчитывается время аренды?']")
    fourth_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Можно ли заказать самокат прямо на сегодня?']")
    fifth_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Можно ли продлить заказ или вернуть самокат раньше?']")
    sixth_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Вы привозите зарядку вместе с самокатом?']")
    seventh_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Можно ли отменить заказ?']")
    eighth_question = (By.XPATH, "//div[contains(@class, 'accordion__button') and text()='Я живу за МКАДом, привезёте?']")

    first_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and text()='Сутки — 400 рублей. Оплата курьеру — наличными или картой.']")
    second_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Пока что у нас так: один заказ — один самокат.')]")
    third_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Допустим, вы оформляете заказ на 8 мая.')]")
    fourth_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and text()='Только начиная с завтрашнего дня. Но скоро станем расторопнее.']")
    fifth_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Пока что нет!')]")
    sixth_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Самокат приезжает к вам с полной зарядкой.')]")
    seventh_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and contains(., 'Да, пока самокат не привезли.')]")
    eighth_answer = (By.XPATH, "//div[contains(@class, 'accordion__panel') and text()='Да, обязательно. Всем самокатов! И Москве, и Московской области.']")
class MainPageLocators:
    order_top_button = (By.CLASS_NAME, 'Button_Button__ra12g')
    order_bottom_button = (By.CLASS_NAME, 'Button_Button__ra12g Button_Middle__1CSJM')
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
class OrderLocators:
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")
    lastname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")
    address_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_input = (By.XPATH, "//input[@placeholder='* Станция метро']")
    phone_input = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.XPATH, "//button[text()='Далее']")
    date_input = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    rent_period_dropdown = (By.CLASS_NAME, "Dropdown-placeholder")
    black_color_checkbox = (By.ID, "black")
    grey_color_checkbox = (By.ID, "grey")
    comment_input = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    order_button = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Заказать'])")
    confirm_button = (By.XPATH, "(//button[contains(@class, 'Button_Button__ra12g Button_Middle__1CSJM') and text()='Да']")
    success_message = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
    @staticmethod
    def get_metro_station(name):
        return (By.XPATH, f"//div[contains(@class, 'select-search__row') and text()='{name}']")
    @staticmethod
    def get_rent_period(period):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{period}']")
