
from selenium.webdriver.common.by import By
class OrderFlowLocators:

    UPPER_ZAKAZAT = (By.XPATH, ".//button[@class = 'Button_Button__ra12g']") # Кнопка Заказать наверху главной страницы
    LOWER_ZAKAZAT = (By.XPATH, ".//div[@class = 'Home_FinishButton__1_cWm']/button[text() = 'Заказать']") # Кнопка Заказать внизу главной страницы
    ORDER_NAME = (By.XPATH, "//*[@placeholder = '* Имя']") # Поле Имя на первой странице оформления заказа
    ORDER_SURNAME = (By.XPATH, "//*[@placeholder = '* Фамилия']") # Поле Фамилия на первой странице оформления заказа
    ORDER_ADDRESS = (By.XPATH, "//*[@placeholder = '* Адрес: куда привезти заказ']") # Поле Адрес на первой странице оформления заказа
    ORDER_METRO = (By.XPATH, "//*[@placeholder = '* Станция метро']") # Поле Метро на первой странице оформления заказа
    ANY_STATION = (By.XPATH, "//div[text() = 'Бульвар Рокоссовского']") # Станция метро из выпадающего списка
    ORDER_PHONE = (By.XPATH, "//*[@placeholder = '* Телефон: на него позвонит курьер']") # Поле Телефон на первой странице оформления заказа
    DALEE = (By.XPATH, ".//button[text() = 'Далее']") # Кнопка Далее на первой странице оформления заказа
    PRO_ARENDU = (By.XPATH, ".//div[@class = 'Order_Header__BZXOb']") # Заголовок ПРО АРЕНДУ на второй странице оформления заказа
    KOGDA_PRIVEZTI_SAMOKAT = (By.XPATH, "//*[@placeholder = '* Когда привезти самокат']") # Поле Когда привести самокат на второй странице оформления заказа
    SPISOK_SROK_ARENDI = (By.XPATH, "//span[@class = 'Dropdown-arrow']") # Выпадающий список Срок аренды
    ANY_PERIOD = (By.XPATH, "//div[text() = 'двое суток']")  # Период из выпадающего списка Срок аренды
    SROK_ARENDI = (By.XPATH, "//*[@placeholder = '* Срок аренды']") # Поле Срок аренды на второй странице оформления заказа
    BLACK = (By.ID, 'black')  # Черный цвет из списка цветов самоката
    COMMENT_KURIER = (By.XPATH, "//*[@placeholder = 'Комментарий для курьера']") # Поле Комментарйи для курьера на второй странице оформления заказа
    LAST_ZAKAZAT = (By.XPATH,".//div[@class = 'Order_Buttons__1xGrp']/button[text() = 'Заказать']")  # Кнопка Заказать на второй странице
    HOTITE_OFORMIT_ZAKAZ = (By.XPATH, "//div[text() = 'Хотите оформить заказ?']") # Всплывающее окно для подтверждения заказа
    BUTTON_DA = (By.XPATH, ".//button[text() = 'Да']") # Кнопка Да при подтверждении заказа
    NOMER_ZAKAZA = (By.XPATH, ".//div[text() = 'Номер заказа: ']") # Номер заказа
    POSMOTRET_STATUS = (By.XPATH, ".//button[text() = 'Посмотреть статус']") # Кнопка на странице заказа для страницы Посмотреть статус
    BUTTON_SAMOKAT = (By.XPATH, ".//img[@alt = 'Scooter']") # Лого Самокат
    OTMENIT_ZAKAZ = (By.XPATH, ".//button[text() = 'Отменить заказ']") # Кнопка Отменить заказ
    SAMOKAT_NA_SKLADE = (By.XPATH, ".//div[text() = 'Самокат на складе']")  # Статус Самокат на складе
    YANDEX_LOGO = (By.XPATH, ".//img[@alt = 'Yandex']")  # Лого Яндекс
    BUTTON_NAITI = (By.XPATH, ".//button[text() = 'Найти']")  # Кнопка Найти на странице Яндекс

