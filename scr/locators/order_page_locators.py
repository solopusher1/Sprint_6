from selenium.webdriver.common.by import By

class OrderPageLocators:

    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']") #имя
    SECOND_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']") #фамилия
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']") #адрес
    METRO = (By.XPATH, ".//input[@placeholder='* Станция метро']") #станция метро
    STATION_AEROPORT = (By.XPATH, './/*[text()="Аэропорт"]')  # Аэропорт в списке станций
    STATION_DOMODEDOVSKAYA = (By.XPATH, './/*[text()="Домодедовская"]')  # Домодедовская в списке станций
    PHONE = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']") #телефон
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']") #кнопка "далее"

class SecondPageOrderLocators:

    DELIVERY_DATE = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']") #дата доставки
    RENT_PERIOD = (By.XPATH, ".//div[@class='Dropdown-arrow-wrapper']/span[@class='Dropdown-arrow']")
    RENT_PERIOD_DAY = (By.XPATH, './/div[@class="Dropdown-option" and text()="сутки"]') # период аренды "сутки"
    RENT_PERIOD_FIVE_DAYS = (By.XPATH, './/div[@class="Dropdown-option" and text()="пятеро суток"]')  # период аренды "сутки"
    COLOR_BLACK_CHECKBOX = (By.XPATH, './/input[@id="black"]') #черный самокат
    COLOR_GREY_CHECKBOX = ([By.XPATH, './/input[@id="grey"]']) #серый самокат
    COMMENT_FIELD = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']") #коммент
    ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']/button[text()='Заказать']") # заказать на странице заказа

class OrderConfirmLocators:

    CONFIRMATION_BUTTON = (By.XPATH, ".//button[text()='Да']") #да на странице подтверждения
    STATUS_BUTTON = (By.XPATH, ".//button[text()='Посмотреть статус']") #посмотреть статус
