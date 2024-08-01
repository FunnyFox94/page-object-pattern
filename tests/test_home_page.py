import allure
import pytest

from sprint_6.locators.locators_main_page import LocatorsMainPage
from sprint_6.pages.home_page import HomePage
from sprint_6.utils.test_literals import ImportantQuestions
import sprint_6.utils.urls as url


@allure.epic('Тестирование главной Самоката')
@allure.parent_suite('Домашняя страница')
@allure.suite('Home')
class TestHomePage:
    @allure.feature('Клик на "Вопросы о важном"')
    @allure.story('При клике на вопрос в разделе "Вопросы о важном" выпадает текст с ответом')
    @allure.title('Выпадение ответа при нажатии')
    @allure.description('Проверка раскрытия всех кнопок с вопросами')
    @pytest.mark.parametrize(
        "question_id, expected_reply",
        [
            (0, ImportantQuestions.text0),
            (1, ImportantQuestions.text1),
            (2, ImportantQuestions.text2),
            (3, ImportantQuestions.text3),
            (4, ImportantQuestions.text4),
            (5, ImportantQuestions.text5),
            (6, ImportantQuestions.text6),
            (7, ImportantQuestions.text7),
        ]
    )
    def test_click_on_all_questions_about_important(self, driver, question_id, expected_reply):
        page = HomePage(driver)
        page.go_to_url(url.MAIN_PAGE)

        page.scroll_to_question_about_important_section()
        page.click_question_buttons(question_id)
        result = page.get_question_button_text(question_id)

        assert result.is_displayed() and result.text == expected_reply

    @allure.feature('Переход на страницу Order')
    @allure.story('При клике "Заказать" осуществляется переход на страницу Order')
    @allure.title('Переход на страницу Order')
    @allure.description('Проверка коррекнтного перехода на страницу Order из header')
    @pytest.mark.parametrize('order_button',
                             [
                                 LocatorsMainPage.ORDER_BUTTON_ON_HEADER,
                                 LocatorsMainPage.ORDER_BUTTON_ON_MAIN_PAGE
                             ]
                             )
    def test_click_on_order_button_from_header_and_home_sections(self, driver, order_button):
        page = HomePage(driver)
        page.go_to_url(url.MAIN_PAGE)

        page.scroll_to_order_button(order_button)
        page.click_order_button(order_button)
        page.wait_for_order_header_text()

        assert page.get_url() == url.ORDER_PAGE

    @allure.feature('Клик на лого Самокат')
    @allure.story('При клике на лого "Самокат" URL не меняется')
    @allure.title('Остаемся на домашней странице')
    @allure.description('Проверка тапа по лого Самоката, когда мы нахоодимся на главной странице')
    def test_click_on_ya_scooter_logo_from_home_page(self, driver):
        page = HomePage(driver)
        page.go_to_url(url.MAIN_PAGE)
        page.click_ya_scooter_logo_button()

        assert url.MAIN_PAGE in page.get_url()

    @allure.feature('Клик на лого Самокат со страницы Order')
    @allure.story('При клике на лого "Самокат" переход на главную')
    @allure.title('Открытие главной страницы')
    @allure.description('Проверка перехода со страницы order на главную через тап по лого Самоката')
    def test_click_on_ya_scooter_logo_from_order_page(self, driver):
        page = HomePage(driver)
        page.go_to_url(url.ORDER_PAGE)
        page.click_ya_scooter_logo_button()

        assert url.MAIN_PAGE in page.get_url()

    @allure.feature('Клик на лого "Yandex" со страницы Order')
    @allure.story('При клике на лого "Yandex" переход на dzen.ru')
    @allure.title('Открытие вкладки /order')
    @allure.description('Проверка перехода со страницы order в dzen.ru через клик по лого Яндекса')
    def test_click_on_yandex_logo_from_order_page(self, driver):
        page = HomePage(driver)
        page.go_to_url(url.ORDER_PAGE)
        page.click_yandex_logo_button()
        page.switch_to_new_tab()
        page.wait_for_redirect_to_dzen()

        assert url.DZEN_HOME_PAGE in page.get_url()
