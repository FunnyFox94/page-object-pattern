import allure
import pytest

from sprint_6.conftest import driver
from sprint_6.locators.locators_main_page import LocatorsMainPage
from sprint_6.pages.home_page import HomePage
from sprint_6.pages.order_page import OrderPage
from sprint_6.utils.test_literals import ScooterOrderData
import sprint_6.utils.urls as url


@allure.epic('Тестирование Оформление заказа Yandex Самокат')
@allure.parent_suite('Оформление заказа')
@allure.suite('Order')
class TestOrderPage:
    @allure.feature('Заказ самоката')
    @allure.story('При клике на любую кнопку "Заказать" с главной открывается форма заказа')
    @allure.title('Заказ самоката до получения номера заказа')
    @allure.description('Проверка оформления заказа с использованием двух наборов данных')
    @pytest.mark.parametrize('order_button, data_set',
                             [
                                 (LocatorsMainPage.order_button_on_header, 'data_set_1'),
                                 (LocatorsMainPage.order_button_on_header, 'data_set_2'),
                                 (LocatorsMainPage.order_button_on_home_page, 'data_set_1'),
                                 (LocatorsMainPage.order_button_on_home_page, 'data_set_2'),
                             ])
    def test_create_complete_order_header_and_page_order_buttons_positive(self, driver, order_button, data_set):
        order_page = OrderPage(driver)
        home_page = HomePage(driver)
        order_page.go_to_url(url.MAIN_PAGE)

        order_page.scroll_to_element(order_button)
        order_page.click_element(order_button)
        order_page.fill_user_order_data(ScooterOrderData.data_sets[data_set])
        order_page.click_next_button()

        order_page.fill_rent_data(ScooterOrderData.data_sets[data_set])
        order_page.click_final_order_button()

        order_page.click_yes_order_button()
        order_page.click_check_status_button()

        home_page.click_ya_scooter_logo_button()

        assert url.MAIN_PAGE in home_page.get_url()

    @allure.feature('Заказ самоката')
    @allure.story('При клике на любую кнопку "Заказать" с домашней страницы открывается форма заказа')
    @allure.title('Заказ самоката до перехода к заголовку "Про аренду"')
    @allure.description('Проверка оформления заказа с использованием одного набора данных')
    @pytest.mark.parametrize('order_button',
                             [
                                 LocatorsMainPage.order_button_on_header,
                                 LocatorsMainPage.order_button_on_home_page,
                             ])
    def test_create_order_until_order_complete_positive(self, driver, order_button):
        page = OrderPage(driver)
        page.go_to_url(url.MAIN_PAGE)

        page.scroll_to_element(order_button)
        page.click_element(order_button)
        page.fill_user_order_data(ScooterOrderData.data_sets['data_set_1'])
        page.click_next_button()

        page.fill_rent_data(ScooterOrderData.data_sets['data_set_1'])
        page.click_final_order_button()
        assert "Хотите оформить заказ" in page.get_modal_header().text

        page.click_yes_order_button()

        assert "Заказ оформлен" in page.get_order_completed_header().text
