from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators
import settings
import pytest

class BasePage:

    def __init__(self, driver):
        self.driver = driver


    def open_main_page(self):
        self.driver.get(settings.MAIN_PAGE_URL)


    def open_order_page(self):
        self.driver.get(settings.ORDER_PAGE + '/')


    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)


    def visible_locator(self, locator):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))


    def visible_reply(self, reply):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(reply))


    def visible_dlya_kogo_samokat(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(BasePageLocators.DLYA_KOGO_SAMOKAT))