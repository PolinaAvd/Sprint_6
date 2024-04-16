
Для запуска проекта понадобятся также файл с константой URL settings.py и файл c локаторами.

Для проверки вопросов-ответов на главной старанице:
main_page_locators.py - локаторы для главной стараницы
main_page.py - методы для запуска
test_main_page.py - тесты для запуска
	test_check_text_of_question() - проверка корректности самих вопросов
	test_check_the_text_of_the_hidden_fild() - проверка корректности ответов и их соотвествия вопросам

Для проверки flow заказа:
order_flow_locators.py - локаторы для главной стараницы
order_flow.py - методы для запуска
test_order_flow.py - тесты для запуска
	test_check_the_upper_button_zakazat_start_order() - проверка верхней кнопки Заказать
	test_check_the_lower_button_zakazat_start_order() - проверка нижней кнопки Заказать
	test_filling_in_all_the_fields_of_the_order() - заполнение всех полей в заказе
	test_push_samokat_button() - проверка возврата в главное меню по кнопке Самокат
	test_push_yandex_button() - проверка перехода на страницу Яндекс
