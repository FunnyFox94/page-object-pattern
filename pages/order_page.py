import allure

from sprint_6.locators.locators_orders_page import LocatorsOrderPage
from sprint_6.pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Ввести имя')
    def enter_name(self, name):
        self.send_text(LocatorsOrderPage.FIRST_NAME, name)

    @allure.step('Ввести фамилию')
    def enter_surname(self, last_name):
        self.send_text(LocatorsOrderPage.LAST_NAME, last_name)

    @allure.step('Ввести адресс')
    def enter_address(self, address):
        self.send_text(LocatorsOrderPage.ADDRESS, address)

    @allure.step('Ввести станцию метро')
    def enter_subway_station(self, station):
        self.find_element(LocatorsOrderPage.METRO_STATION).click()
        return self.find_element(LocatorsOrderPage.metro_choice_button(station)).click()

    @allure.step('Ввести номер телефона')
    def enter_phone_number(self, phone):
        self.send_text(LocatorsOrderPage.PHONE_NUMBER, phone)

    @allure.step('Ввести дату')
    def enter_date(self, date):
        self.send_text(LocatorsOrderPage.DELIVERY_TIME, date)
        self.tap_enter_button(LocatorsOrderPage.DELIVERY_TIME)

    @allure.step('Ввести время аренды')
    def enter_rent_time(self, rent_time):
        self.click_element(LocatorsOrderPage.RENT_TIME_PLACEHOLDER)
        self.element_is_visible(LocatorsOrderPage.RENT_TIME_DROPDOWN_MENU)
        self.find_elements(LocatorsOrderPage.RENT_TIME_DROPDOWN_OPTION)[rent_time].click()

    @allure.step('Выбрать цвет')
    def enter_color(self):
        self.click_element(LocatorsOrderPage.CHOICE_COLOR_SCOOTER)

    @allure.step('Ввести комментарий к заказу')
    def enter_comment_for_deliveryman(self, comment):
        self.send_text(LocatorsOrderPage.COMMENT_FOR_DELIVERY_MAN, comment)

    @allure.step('Заполнить данные заказа')
    def fill_user_order_data(self, data_set: dict):
        self.enter_name(data_set['name'])
        self.enter_surname(data_set['surname'])
        self.enter_address(data_set['address'])
        self.enter_subway_station(data_set['station'])
        self.enter_phone_number(data_set['phone_number'])

    @allure.step('Клик "Далее" при оформлении заказа')
    def click_next_button(self):
        self.scroll_to_element(LocatorsOrderPage.NEXT_BUTTON)
        self.click_element(LocatorsOrderPage.NEXT_BUTTON)

    @allure.step('Заполнить данные об аренде')
    def fill_rent_data(self, data_set: dict):
        self.enter_date(data_set['date'])
        self.enter_rent_time(data_set['rent_time'])
        self.enter_color()
        self.enter_comment_for_deliveryman(data_set['comment_for_courier'])

    @allure.step('Клик Заказать')
    def click_final_order_button(self):
        self.click_element(LocatorsOrderPage.MAKE_ORDER_BUTTON)

    @allure.step('Клик Да при оформлении заказа')
    def click_yes_order_button(self):
        self.click_element(LocatorsOrderPage.YES_BUTTON)

    @allure.step('Нажать кнопку "Посмотреть статус" после оформления заказа')
    def click_check_status_button(self):
        self.click_element(LocatorsOrderPage.CHECK_STATUS)

    def get_modal_header(self):
        return self.element_is_visible(LocatorsOrderPage.APPROVE_MODAL_HEADER)

    def get_order_completed_header(self):
        return self.element_is_visible(LocatorsOrderPage.SUCCESS_ORDER_STRING)
