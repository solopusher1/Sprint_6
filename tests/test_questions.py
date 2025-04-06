import allure
import pytest
from scr.pages.main_page import MainPage
from helpers import ANSWERS_DATA

class TestQuestions:

    @allure.title('Соответствие вопросов и ответов')
    @allure.description('Скроллим до вопроса. Кликаем. Сверяем результаты')
    @pytest.mark.parametrize('question_id',range(8))
    def test_click_to_question_check_answers(self, driver, question_id):
        main_page = MainPage(driver)
        main_page.scroll_to_question(question_id)
        main_page.wait_to_question_button(question_id) #убирает оверлей от самоката из за которого иногда вопрос не был кликабельным
        main_page.click_to_question_button(question_id)
        main_page.check_answer_is_visible(question_id)
        actual_answer_text = main_page.get_answer_text(question_id)
        expected_answer_text = ANSWERS_DATA[question_id]

        assert actual_answer_text == expected_answer_text, "Текст ответа не соответствует ОР"