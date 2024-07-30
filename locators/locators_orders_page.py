from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    # заголовок страницы
    order_header = (By.XPATH, ".//div[text()='Для кого самокат']")

    # данные заказа
    first_name = (By.XPATH, ".//input[@placeholder='* Имя']")
    last_name = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    address = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    metro_station = (By.CLASS_NAME, "select-search__input")
    phone_number = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    # выбор станции метро
    @staticmethod
    def metro_choice_button(station):
        return (By.XPATH, f".//div[text()='{station}']/parent::button")

    # кнопка Далее
    next_button = (By.XPATH, ".//button[text()='Далее']")

    # блок Про Аренду
    delivery_time = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    rent_time_placeholder = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    rent_time_dropdown_menu = (By.XPATH, ".//div[@class='Dropdown-menu']")
    rent_time_dropdown_option = (By.XPATH, ".//div[@class='Dropdown-option']")
    choice_color_scooter = (By.XPATH, ".//label[@for='black']")
    comment_for_deliveryman = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    # datepicker при выборе времени доставки
    datepicker = (By.CLASS_NAME, 'react-datepicker')

    # кнопка Назад
    back_button = (By.XPATH, ".//button[contains(text(), 'Назад')]")
    make_order_button = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

    # модалка подтверждения заказа
    approve_modal_header = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    yes_button = (By.XPATH, ".//button[text()='Да']")
    no_button = (By.XPATH, ".//button[text()='Нет']")

    # модалка с успеха заказа
    succsess_order_string = (By.XPATH, ".//div[text()='Заказ оформлен']")
    order_number = (By.XPATH, ".//div[contains(text(),'Номер заказа')]")
    check_status = (By.XPATH, ".//button[contains(text(),'Посмотреть статус')]")
