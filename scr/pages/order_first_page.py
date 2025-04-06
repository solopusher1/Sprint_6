import allure
from scr.locators.order_page_locators import OrderPageLocators
from scr.pages.base_page import BasePage

class OrderFirstPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('ввод имени')
    def enter_name(self, name):
        self.filling_the_field(OrderPageLocators.FIRST_NAME, name)

    @allure.step('ввод фамилии')
    def enter_secondname(self, secondname):
        self.filling_the_field(OrderPageLocators.SECOND_NAME, secondname)

    @allure.step('ввод адресса"')
    def enter_address(self, address):
        self.filling_the_field(OrderPageLocators.ADDRESS, address)

    @allure.step('ввод номера"')
    def enter_phone(self, phone):
        self.filling_the_field(OrderPageLocators.PHONE, phone)

    @allure.step('ввод метро"')
    def enter_data_metro_station(self, metro):
        self.filling_the_field(OrderPageLocators.METRO, metro)

    @allure.step('клик по нужной станции метро из списка')
    def click_to_metro_station(self, station_name):
        if station_name == 'Аэропорт':
            self.click_to_element(OrderPageLocators.STATION_AEROPORT)
        else:
            self.click_to_element(OrderPageLocators.STATION_DOMODEDOVSKAYA)

    @allure.step('заполняем поле метро из ввода и клика"')
    def enter_the_metro_station_field(self, station_name):
        self.enter_data_metro_station(station_name)
        self.click_to_metro_station(station_name)

    @allure.step('клик по кнопке "Далее"')
    def click_next_button(self):
        self.click_to_element(OrderPageLocators.NEXT_BUTTON)
