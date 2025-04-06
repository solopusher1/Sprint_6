from selenium.webdriver.common.by import By

class MainPageLocators:
    ORDER_BUTTON_TOP = (By.XPATH, './/button[text()="Заказать"]') #верхняя кнопка заказать
    ORDER_BUTTON_BOTTOM = (By.XPATH, './/div[@class="Home_FinishButton__1_cWm"]/button[text()="Заказать"]')  # нижняя кнопка заказать
    LOGO_YANDEX = (By.XPATH, './/img[@alt="Yandex"]')  #лого Яндекс
    LOGO_SCOOTER = (By.XPATH, './/img[@alt="Scooter"]') # Лого скутер
    QUESTIONS_TITLE = (By.XPATH, './/div[text()="Вопросы о важном"]')  # вопросы о важном посреди страницы
