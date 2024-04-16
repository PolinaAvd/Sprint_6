from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class VoprosiOVazhnom:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('Проверяем вопросы')
    def get_text_of_the_question(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        return self.driver.find_element(*locator).text
    @allure.step('Проверяем ответы')
    def check_text_of_the_reply(self, locator, reply):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(locator))
        element.click()
        WebDriverWait(self.driver, 3).until(expected_conditions.visibility_of_element_located(reply))
        return self.driver.find_element(*reply).text







