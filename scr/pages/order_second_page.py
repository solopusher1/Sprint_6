import allure
from scr.locators.order_page_locators import SecondPageOrderLocators
from scr.locators.order_page_locators import OrderConfirmLocators
from scr.pages.base_page import BasePage
import random, datetime

class OrderSecondPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Рандомный выбор даты для поля "Когда привезти самокат"')
    def choose_date(self):
        today = datetime.date.today()
        tomorrow = today + datetime.timedelta(days=1)
        date = random.choice((today, tomorrow))
        return date.strftime('%d.%m.%Y')

    @allure.step('заполняем поле "Когда привезти самокат"')
    def enter_date(self):
        self.filling_the_field(SecondPageOrderLocators.DELIVERY_DATE, self.choose_date())

    @allure.step('клик по сроку аренды')
    def click_to_rental_period(self):
        self.click_to_element(SecondPageOrderLocators.RENT_PERIOD)

    @allure.step('Клик по нужному периоду аренды из писка')
    def choose_rental_period(self, period_name):
        if period_name == 'сутки':
            self.click_to_element(SecondPageOrderLocators.RENT_PERIOD_DAY)
        else:
            self.click_to_element(SecondPageOrderLocators.RENT_PERIOD_FIVE_DAYS)

    @allure.step('заполнение срока аренды')
    def enter_the_rental_period(self, period_name):
        self.click_to_rental_period()
        self.choose_rental_period(period_name)

    @allure.step('клик по  выбора цвета')
    def click_to_scooter_color_checkbox(self):
        locator = random.choice((SecondPageOrderLocators.COLOR_BLACK_CHECKBOX, SecondPageOrderLocators.COLOR_GREY_CHECKBOX))
        self.click_to_element(locator)

    @allure.step('заполнение комментария')
    def enter_the_comment(self, comment):
        self.filling_the_field(SecondPageOrderLocators.COMMENT_FIELD, comment)

    @allure.step('клик по "Заказать"')
    def click_to_make_order(self):
        self.click_to_element(SecondPageOrderLocators.ORDER_BUTTON)

    @allure.step('да - кликабельная')
    def check_confirm_order_is_clickable(self):
        self.wait_for_element_to_be_clickable(OrderConfirmLocators.CONFIRMATION_BUTTON)

    @allure.step('Клик по "да"')
    def click_to_confirm_order(self):
        self.click_to_element(OrderConfirmLocators.CONFIRMATION_BUTTON)

    @allure.step('кнопка "Посмотреть статус" доступна')
    def check_show_status_button_is_enabled(self):
        return self.check_element_is_enabled(OrderConfirmLocators.STATUS_BUTTON)