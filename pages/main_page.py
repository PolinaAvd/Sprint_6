import allure
from pages.base_page import BasePage


class VoprosiOVazhnom(BasePage):


    @allure.step('Проверяем вопросы')
    def get_text_of_the_question(self, locator):
        self.open_main_page()
        self.scroll(locator)
        return self.driver.find_element(*locator).text
    @allure.step('Проверяем вопросы')
    def a_get_text_of_the_question(self, locator):
        self.open_main_page()
        self.scroll(locator)
        return self.driver.find_element(*locator).text


    @allure.step('Проверяем ответы')
    def check_text_of_the_reply(self, locator, reply):
        self.open_main_page()
        self.scroll(locator)
        self.visible_locator(locator)
        self.driver.find_element(*locator).click()
        self.visible_locator(reply)
        return self.driver.find_element(*reply).text







