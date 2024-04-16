from selenium import webdriver
import pytest
from pages.order_flow import Zakazat

import settings

class TestZakazat:
    driver = None

    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    def test_check_the_upper_button_zakazat_start_order(self):
        self.driver.get(settings.MAIN_PAGE_URL)
        push_on_zakazat = Zakazat(self.driver)
        assert push_on_zakazat.push_the_upper_button_zakazat_start_order() == settings.MAIN_PAGE_URL + 'order'

    def test_check_the_lower_button_zakazat_start_order(self):
        self.driver.get(settings.MAIN_PAGE_URL)
        push_on_zakazat = Zakazat(self.driver)
        assert push_on_zakazat.push_the_lower_button_zakazat_start_order() == settings.MAIN_PAGE_URL + 'order'

    @pytest.mark.parametrize('name, surname, address, phone, date, comment', [['Тесттт', 'Тестттт', 'Тест 0', '71111111112', '11.11.2025', 'коммент'], ['Тест', 'Тест', 'Тест 1', '79999999991', '11.12.2025', 'комменты']])
    def test_filling_in_all_the_fields_of_the_order(self, name, surname, address, phone, date, comment):
        self.driver.get(settings.MAIN_PAGE_URL + 'order/')
        fill_in = Zakazat(self.driver)
        assert fill_in.fill_the_fields_of_the_order(name, surname, address, phone, date, comment) == 'Самокат на складе'

    @pytest.mark.parametrize('name, surname, address, phone, date, comment',
                             [['Тесттт', 'Тестттт', 'Тест 2', '71111111111', '11.11.2025', 'коммент']])
    def test_push_samokat_button(self, name, surname, address, phone, date, comment):
        self.driver.get(settings.MAIN_PAGE_URL + 'order/')
        push_on_samokat = Zakazat(self.driver)
        assert push_on_samokat.push_samokat_button(name, surname, address, phone, date, comment) == settings.MAIN_PAGE_URL

    def test_push_yandex_button(self):
        self.driver.get('https://qa-scooter.praktikum-services.ru/')
        push_on_yandex = Zakazat(self.driver)
        assert push_on_yandex.push_yandex() == settings.YANDEX

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()

