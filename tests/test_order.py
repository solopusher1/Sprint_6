import allure
import pytest
from scr.pages.order_second_page import OrderSecondPage
from scr.pages.order_first_page import OrderFirstPage
from scr.pages.main_page import MainPage
from urls import URL
import helpers

class TestMakeOrder:

    @allure.title('Проверка успешного оформления заказа через кнопку "Заказать" в топе')
    @allure.description('Заполняем поля заказа, в конце жмем на подтверждение заказа ')
    @pytest.mark.parametrize('i',[0,1])
    def test_successful_filling_order(self, driver, i):
        main_page = MainPage(driver)
        main_page.click_to_make_order_top_button()

        order_first_page = OrderFirstPage(driver)
        order_first_page.enter_name(helpers.ORDER_DATA[i]['name'])
        order_first_page.enter_secondname(helpers.ORDER_DATA[i]['secondname'])
        order_first_page.enter_address(helpers.ORDER_DATA[i]['address'])
        order_first_page.enter_the_metro_station_field(helpers.ORDER_DATA[i]['metro'])
        order_first_page.enter_phone(helpers.ORDER_DATA[i]['phone'])
        order_first_page.click_next_button()

        order_second_page = OrderSecondPage(driver)
        order_second_page.enter_date()
        order_second_page.enter_the_rental_period(helpers.ORDER_DATA[i]['rental_period'])
        order_second_page.click_to_scooter_color_checkbox()
        order_second_page.enter_the_comment(helpers.ORDER_DATA[i]['comment'])
        order_second_page.click_to_make_order()
        order_second_page.check_confirm_order_is_clickable()
        order_second_page.click_to_confirm_order()

        assert order_second_page.check_show_status_button_is_enabled(), "Сообщение об успешном оформлении заказа отсутствует"

    @allure.title('Проверка кнопки заказать в низу страницы. Должна вести на страницу "для кого самокат')
    @allure.description('Ищем кнопку "Заказать" внизу главной страницы, жмем на нее, проверяем, что открылась страница "для кого самокат"')
    def test_click_to_main_page_order_button_open_order_first_page(self, driver):
        main_page = MainPage(driver)
        main_page.scroll_to_make_order_bot_button()
        main_page.click_to_make_order_bot_button()

        order_first_page = OrderFirstPage(driver)
        current_url = order_first_page.get_current_url()

        assert current_url == URL.ORDER_PAGE, 'нет перехода на страницу "для кого самокат"'