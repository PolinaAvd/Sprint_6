import allure
from locators.order_flow_locators import OrderFlowLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import settings

class Zakazat(BasePage):

    def __init__(self, driver):
        self.driver = driver


    @allure.step('Проверяем верхнюю кнопку Заказать')
    def push_the_upper_button_zakazat_start_order(self):
        base_page = BasePage(self.driver)
        base_page.open_main_page()
        self.driver.find_element(*OrderFlowLocators.UPPER_ZAKAZAT).click()
        base_page = BasePage(self.driver)
        base_page.visible_dlya_kogo_samokat()
        return self.driver.current_url


    @allure.step('Проверяем нижнюю кнопку Заказать')
    def push_the_lower_button_zakazat_start_order(self):
        base_page = BasePage(self.driver)
        base_page.open_main_page()
        element = self.driver.find_element(*OrderFlowLocators.LOWER_ZAKAZAT)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        self.driver.find_element(*OrderFlowLocators.LOWER_ZAKAZAT).click()
        base_page.visible_dlya_kogo_samokat()
        return self.driver.current_url


    def set_name(self, name):
        self.driver.find_element(*OrderFlowLocators.ORDER_NAME).send_keys(name)


    def set_surname(self, surname):
        self.driver.find_element(*OrderFlowLocators.ORDER_SURNAME).send_keys(surname)


    def set_address(self, address):
        self.driver.find_element(*OrderFlowLocators.ORDER_ADDRESS).send_keys(address)


    def set_metro(self):
        self.driver.find_element(*OrderFlowLocators.ORDER_METRO).click()
        self.driver.find_element(*OrderFlowLocators.ANY_STATION).click()


    def set_phone(self, phone):
        self.driver.find_element(*OrderFlowLocators.ORDER_PHONE).send_keys(phone)


    def click_on_dalee(self):
        self.driver.find_element(*OrderFlowLocators.DALEE).click()


    def set_date(self, date):
        self.driver.find_element(*OrderFlowLocators.KOGDA_PRIVEZTI_SAMOKAT).send_keys(date)


    def set_srok_arendi(self):
        self.driver.find_element(*OrderFlowLocators.SPISOK_SROK_ARENDI).click()
        self.driver.find_element(*OrderFlowLocators.ANY_PERIOD).click()


    def choose_color(self):
        self.driver.find_element(*OrderFlowLocators.BLACK).click()


    def set_comment(self, comment):
        self.driver.find_element(*OrderFlowLocators.COMMENT_KURIER).send_keys(comment)


    def push_zakazat(self):
        self.driver.find_element(*OrderFlowLocators.LAST_ZAKAZAT).click()


    def push_confirm(self):
        self.driver.find_element(*OrderFlowLocators.BUTTON_DA).click()


    def push_posmotret_status(self):
        self.driver.find_element(*OrderFlowLocators.POSMOTRET_STATUS).click()


    @allure.step('Проверяем полный флоу оформления заказа')
    def fill_the_fields_of_the_order(self, name, surname, address, phone, date, comment):
        base_page = BasePage(self.driver)
        base_page.open_order_page()
        self.set_name(name)
        self.set_surname(surname)
        self.set_address(address)
        self.set_metro()
        self.set_phone(phone)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.DALEE))
        self.click_on_dalee()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.PRO_ARENDU))
        self.set_date(date)
        self.set_srok_arendi()
        self.choose_color()
        self.set_comment(comment)
        self.push_zakazat()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.HOTITE_OFORMIT_ZAKAZ))
        self.push_confirm()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.NOMER_ZAKAZA))
        self.push_posmotret_status()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.OTMENIT_ZAKAZ))
        element = self.driver.find_element(*OrderFlowLocators.SAMOKAT_NA_SKLADE)
        return element.text


    @allure.step('Проверяем нажатие на кнопку Самокат')
    def push_samokat_button(self, name, surname, address, phone, date, comment):
        base_page = BasePage(self.driver)
        base_page.open_order_page()
        self.fill_the_fields_of_the_order(name, surname, address, phone, date, comment)
        self.driver.find_element(*OrderFlowLocators.BUTTON_SAMOKAT).click()
        return self.driver.current_url

    @allure.step('Проверяем Переход на страницу яндекс')
    def push_yandex(self):
        base_page = BasePage(self.driver)
        base_page.open_main_page()
        original_window = (self.driver.current_window_handle)
        self.driver.find_element(*OrderFlowLocators.YANDEX_LOGO).click()
        WebDriverWait(self.driver, 3).until(EC.number_of_windows_to_be(2))
        for window_handle in self.driver.window_handles:
            self.driver.switch_to.window(window_handle)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(OrderFlowLocators.BUTTON_NAITI))
        return self.driver.current_url












