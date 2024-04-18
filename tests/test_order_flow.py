from selenium import webdriver
import pytest
from pages.order_flow import Zakazat
import settings



class TestZakazat:


    def test_check_the_upper_button_zakazat_start_order(self, driver):
        push_on_zakazat = Zakazat(driver)
        assert push_on_zakazat.push_the_upper_button_zakazat_start_order() == settings.ORDER_PAGE


    def test_check_the_lower_button_zakazat_start_order(self, driver):
        push_on_zakazat = Zakazat(driver)
        assert push_on_zakazat.push_the_lower_button_zakazat_start_order() == settings.ORDER_PAGE


    @pytest.mark.parametrize('name, surname, address, phone, date, comment', [['Тесттт', 'Тестттт', 'Тест 0', '71111111112', '11.11.2025', 'коммент'], ['Тест', 'Тест', 'Тест 1', '79999999991', '11.12.2025', 'комменты']])
    def test_filling_in_all_the_fields_of_the_order(self, driver, name, surname, address, phone, date, comment):
        fill_in = Zakazat(driver)
        assert fill_in.fill_the_fields_of_the_order(name, surname, address, phone, date, comment) == 'Самокат на складе'


    @pytest.mark.parametrize('name, surname, address, phone, date, comment',
                             [['Тесттт', 'Тестттт', 'Тест 2', '71111111111', '11.11.2025', 'коммент']])
    def test_push_samokat_button(self, driver, name, surname, address, phone, date, comment):
        push_on_samokat = Zakazat(driver)
        assert push_on_samokat.push_samokat_button(name, surname, address, phone, date, comment) == settings.MAIN_PAGE_URL


    def test_push_yandex_button(self, driver):
        push_on_yandex = Zakazat(driver)
        assert push_on_yandex.push_yandex() == settings.YANDEX


