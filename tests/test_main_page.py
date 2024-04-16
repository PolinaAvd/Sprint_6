from selenium import webdriver
import pytest
from pages.main_page import VoprosiOVazhnom
import settings
from locators.main_page_locators import MainLocators

class TestVoprosiOVazhnom:
    driver = None
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Firefox()

    @pytest.mark.parametrize('text_of_question, locator', [('Сколько это стоит? И как оплатить?',
                                                            MainLocators.PERVIY_VOPROS),
                                                           ('Хочу сразу несколько самокатов! Так можно?',
                                                            MainLocators.VTOROI_VOPROS),
                                                            ('Как рассчитывается время аренды?',
                                                             MainLocators.TRETIY_VOPROS),
                                                            ('Можно ли заказать самокат прямо на сегодня?',
                                                             MainLocators.CHETVERTIY_VOPROS),
                                                           ('Можно ли продлить заказ или вернуть самокат раньше?',
                                                            MainLocators.PIATIY_VOPROS),
                                                           ('Вы привозите зарядку вместе с самокатом?',
                                                            MainLocators.SHESTOY_VOPROS),
                                                           ('Можно ли отменить заказ?',
                                                            MainLocators.SEDMOY_VOPROS),
                                                           ('Я жизу за МКАДом, привезёте?',
                                                            MainLocators.VOSMOY_VOPROS)
                                                           ])

    def test_check_text_of_question(self, text_of_question, locator):
        self.driver.get(settings.MAIN_PAGE_URL)
        question_text = VoprosiOVazhnom(self.driver)
        assert question_text.get_text_of_the_question(locator) == text_of_question
    @pytest.mark.parametrize('text_of_reply, locator, reply', [('Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                                                            MainLocators.PERVIY_VOPROS, MainLocators.PERVIY_OTVET),
                                                               ('Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                                                               MainLocators.VTOROI_VOPROS, MainLocators.VTOROI_OTVET),
                                                               ('Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                                                               MainLocators.TRETIY_VOPROS, MainLocators.TRETIY_OTVET),
                                                               ('Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                                                               MainLocators.CHETVERTIY_VOPROS, MainLocators.CHETVERTIY_OTVET),
                                                               ('Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                                                               MainLocators.PIATIY_VOPROS, MainLocators.PIATIY_OTVET),
                                                               ('Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                                                               MainLocators.SHESTOY_VOPROS, MainLocators.SHESTOY_OTVET),
                                                               ('Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                                                               MainLocators.SEDMOY_VOPROS, MainLocators.SEDMOY_OTVET),
                                                               ('Да, обязательно. Всем самокатов! И Москве, и Московской области.',
                                                               MainLocators.VOSMOY_VOPROS, MainLocators.VOSMOY_OTVET)])
    def test_check_the_text_of_the_hidden_fild(self, text_of_reply, locator, reply):
        self.driver.get(settings.MAIN_PAGE_URL)
        first_question_opens = VoprosiOVazhnom(self.driver)
        assert first_question_opens.check_text_of_the_reply(locator, reply) == text_of_reply
    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
