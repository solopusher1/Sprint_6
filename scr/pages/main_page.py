import allure
from selenium.webdriver.common.by import By
from scr.pages.base_page import BasePage
from scr.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Клик по кнопке "Заказать" в топе страницы')
    def click_to_make_order_top_button(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_TOP)

    @allure.step('Клик по лого "Самокат" в топе')
    def click_to_logo_scooter(self):
        self.click_to_element(MainPageLocators.LOGO_SCOOTER)

    @allure.step('Клик по лого "Яндекс" в топе')
    def click_to_logo_yandex(self):
        self.click_to_element(MainPageLocators.LOGO_YANDEX)

    @allure.step('Проверяем что в урле есть "https://dzen.ru"')
    def check_url_contains_dzen(self):
        self.check_url_contains_value("https://dzen.ru")

    @allure.step('Скролл до вопроса')
    def scroll_to_question(self, question_id):
        self.scroll_to_element((By.ID, "accordion__heading-" + str(question_id)))

    @allure.step('Клик по вопросу')
    def click_to_question_button(self, question_id):
        self.click_to_element((By.ID, "accordion__heading-" + str(question_id)))

    @allure.step('Проверка что есть ответ на вопрос')
    def check_answer_is_visible(self, question_id):
        self.wait_for_visibility_of_element((By.ID, "accordion__panel-" + str(question_id)))

    @allure.step('Получаем текст ответа на вопрос')
    def get_answer_text(self, question_id):
        return self.get_text_of_the_element((By.ID, "accordion__panel-" + str(question_id)))

    @allure.step('Скролл до кнопки "Заказать" в боте страницы')
    def scroll_to_make_order_bot_button(self):
        self.scroll_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Нажатие на кнопку "Заказать" в боте страницы')
    def click_to_make_order_bot_button(self):
        self.click_to_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    @allure.step('Ждать пока вопрос будет кликабельным')
    def wait_to_question_button(self, question_id):
        self.wait_for_element_to_be_clickable((By.ID, "accordion__heading-" + str(question_id)))
