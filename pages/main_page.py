import allure
from pages.base_page import BasePage
import settings
import pytest

class VoprosiOVazhnom(BasePage):


    @allure.step('Проверяем вопросы')
    def get_text_of_the_question(self, locator):
        base_page = BasePage(self.driver)
        base_page.open_main_page()
        base_page.scroll(locator)
        return self.driver.find_element(*locator).text


    @allure.step('Проверяем ответы')
    def check_text_of_the_reply(self, locator, reply):
        base_page = BasePage(self.driver)
        base_page.open_main_page()
        base_page.scroll(locator)
        base_page.visible_locator(locator)
        self.driver.find_element(*locator).click()
        base_page.visible_locator(reply)
        return self.driver.find_element(*reply).text







