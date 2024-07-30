import allure

from sprint_6.locators.locators_orders_page import LocatorsOrderPage
from sprint_6.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввести имя')
    def enter_name(self, name):
        self.send_text(LocatorsOrderPage.first_name, name)

    @allure.step('Ввести фамилию')
    def enter_surname(self, last_name):
        self.send_text(LocatorsOrderPage.last_name, last_name)

    @allure.step('Ввести адресс')
    def enter_address(self, address):
        self.send_text(LocatorsOrderPage.address, address)

    @allure.step('Ввести станцию метро')
    def enter_subway_station(self, station):
        self.find_element(LocatorsOrderPage.metro_station).click()
        return self.find_element(LocatorsOrderPage.metro_choice_button(station)).click()

    @allure.step('Ввести номер телефона')
    def enter_phone_number(self, phone):
        self.send_text(LocatorsOrderPage.phone_number, phone)

    @allure.step('Ввести дату')
    def enter_date(self, date):
        self.send_text(LocatorsOrderPage.delivery_time, date)
        self.tap_enter_button(LocatorsOrderPage.delivery_time)

    @allure.step('Ввести время аренды')
    def enter_rent_time(self, rent_time):
        self.click_element(LocatorsOrderPage.rent_time_placeholder)
        self.element_is_visible(LocatorsOrderPage.rent_time_dropdown_menu)
        self.find_elements(LocatorsOrderPage.rent_time_dropdown_option)[rent_time].click()

    @allure.step('Выбрать цвет')
    def enter_color(self):
        self.click_element(LocatorsOrderPage.choice_color_scooter)

    @allure.step('Ввести комментарий к заказу')
    def enter_comment_for_deliveryman(self, comment):
        self.send_text(LocatorsOrderPage.comment_for_deliveryman, comment)

    @allure.step('Заполнить данные заказа')
    def fill_user_order_data(self, data_set: dict):
        self.enter_name(data_set['name'])
        self.enter_surname(data_set['surname'])
        self.enter_address(data_set['address'])
        self.enter_subway_station(data_set['station'])
        self.enter_phone_number(data_set['phone_number'])

    @allure.step('Клик "Далее" при оформлении заказа')
    def click_next_button(self):
        self.scroll_to_element(LocatorsOrderPage.next_button)
        self.click_element(LocatorsOrderPage.next_button)

    @allure.step('Заполнить данные об аренде')
    def fill_rent_data(self, data_set: dict):
        self.enter_date(data_set['date'])
        self.enter_rent_time(data_set['rent_time'])
        self.enter_color()
        self.enter_comment_for_deliveryman(data_set['comment_for_courier'])

    @allure.step('Клик Заказать')
    def click_final_order_button(self):
        self.click_element(LocatorsOrderPage.make_order_button)

    @allure.step('Клик Да при оформлении заказа')
    def click_yes_order_button(self):
        self.click_element(LocatorsOrderPage.yes_button)

    @allure.step('Нажать кнопку "Посмотреть статус" после оформления заказа')
    def click_check_status_button(self):
        self.click_element(LocatorsOrderPage.check_status)

    def get_modal_header(self):
        return self.element_is_visible(LocatorsOrderPage.approve_modal_header)

    def get_order_completed_header(self):
        return self.element_is_visible(LocatorsOrderPage.succsess_order_string)
