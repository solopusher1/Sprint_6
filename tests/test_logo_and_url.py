import allure
from scr.pages.main_page import MainPage
from urls import URL

class TestYandexAndScooterLogo:

    @allure.title('Клик на лого самоката ведет на главную страницу приложения')
    @allure.description('Переходим на страницу заказа, затем кликаем на лого самоката. Проверка что ведет на главную страницу')
    def test_click_to_scooter_open_home_page(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_make_order_top_button()
        main_page.click_to_logo_scooter()

        assert main_page.get_current_url() == URL.MAIN_PAGE, "Урл не совпадает с ожидаемым"

    @allure.title('проверка клика на лого Яндекс. В новом окне должен открыться сайт дзена')
    @allure.description('Кликаем на лого Яндекса в топе.  В урле есть дзен')
    def test_click_to_yandex_logo_open_dzen_page_in_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_to_logo_yandex()
        main_page.switch_to_new_window()
        main_page.check_url_contains_dzen()
        current_url = main_page.get_current_url()
        assert 'dzen.ru' in current_url, "Урл не совпадает с ожидаемым"