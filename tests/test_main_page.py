
import pytest
from pages.main_page import VoprosiOVazhnom
import settings
from locators.main_page_locators import MainLocators


class TestVoprosiOVazhnom:


    @pytest.mark.parametrize('text_of_question, locator', [(settings.text_of_question_1,
                                                            MainLocators.PERVIY_VOPROS),
                                                           (settings.text_of_question_2,
                                                            MainLocators.VTOROI_VOPROS),
                                                            (settings.text_of_question_3,
                                                             MainLocators.TRETIY_VOPROS),
                                                            (settings.text_of_question_4,
                                                             MainLocators.CHETVERTIY_VOPROS),
                                                           (settings.text_of_question_5,
                                                            MainLocators.PIATIY_VOPROS),
                                                           (settings.text_of_question_6,
                                                            MainLocators.SHESTOY_VOPROS),
                                                           (settings.text_of_question_7,
                                                            MainLocators.SEDMOY_VOPROS),
                                                           (settings.text_of_question_8,
                                                            MainLocators.VOSMOY_VOPROS)])
    def test_check_text_of_question(self, driver, text_of_question, locator):
        question_text = VoprosiOVazhnom(driver)
        assert question_text.get_text_of_the_question(locator) == text_of_question


    @pytest.mark.parametrize('text_of_reply, locator, reply', [(settings.text_of_reply_1,
                                                                MainLocators.PERVIY_VOPROS, MainLocators.PERVIY_OTVET),
                                                               (settings.text_of_reply_2,
                                                               MainLocators.VTOROI_VOPROS, MainLocators.VTOROI_OTVET),
                                                               (settings.text_of_reply_3,
                                                               MainLocators.TRETIY_VOPROS, MainLocators.TRETIY_OTVET),
                                                               (settings.text_of_reply_4,
                                                               MainLocators.CHETVERTIY_VOPROS, MainLocators.CHETVERTIY_OTVET),
                                                               (settings.text_of_reply_5,
                                                               MainLocators.PIATIY_VOPROS, MainLocators.PIATIY_OTVET),
                                                               (settings.text_of_reply_6,
                                                               MainLocators.SHESTOY_VOPROS, MainLocators.SHESTOY_OTVET),
                                                               (settings.text_of_reply_7,
                                                               MainLocators.SEDMOY_VOPROS, MainLocators.SEDMOY_OTVET),
                                                               (settings.text_of_reply_8,
                                                               MainLocators.VOSMOY_VOPROS, MainLocators.VOSMOY_OTVET)])
    def test_check_the_text_of_the_hidden_fild(self, driver, text_of_reply, locator, reply):
        first_question_opens = VoprosiOVazhnom(driver)
        assert first_question_opens.check_text_of_the_reply(locator, reply) == text_of_reply


