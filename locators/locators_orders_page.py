from selenium.webdriver.common.by import By


class LocatorsOrderPage:
    # заголовок страницы
    ORDER_HEADER = (By.XPATH, ".//div[text()='Для кого самокат']")

    # данные заказа
    FIRST_NAME = (By.XPATH, ".//input[@placeholder='* Имя']")
    LAST_NAME = (By.XPATH, ".//input[@placeholder='* Фамилия']")
    ADDRESS = (By.XPATH, ".//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_STATION = (By.CLASS_NAME, "select-search__input")
    PHONE_NUMBER = (By.XPATH, ".//input[@placeholder='* Телефон: на него позвонит курьер']")

    # выбор станции метро
    @staticmethod
    def metro_choice_button(station):
        return (By.XPATH, f".//div[text()='{station}']/parent::button")

    # кнопка Далее
    NEXT_BUTTON = (By.XPATH, ".//button[text()='Далее']")

    # блок Про Аренду
    DELIVERY_TIME = (By.XPATH, ".//input[@placeholder='* Когда привезти самокат']")
    RENT_TIME_PLACEHOLDER = (By.XPATH, ".//div[@class='Dropdown-placeholder']")
    RENT_TIME_DROPDOWN_MENU = (By.XPATH, ".//div[@class='Dropdown-menu']")
    RENT_TIME_DROPDOWN_OPTION = (By.XPATH, ".//div[@class='Dropdown-option']")
    CHOICE_COLOR_SCOOTER = (By.XPATH, ".//label[@for='black']")
    COMMENT_FOR_DELIVERY_MAN = (By.XPATH, ".//input[@placeholder='Комментарий для курьера']")

    # кнопка Назад
    MAKE_ORDER_BUTTON = (By.XPATH, ".//div[@class='Order_Buttons__1xGrp']//button[text()='Заказать']")

    # модалка подтверждения заказа
    APPROVE_MODAL_HEADER = (By.XPATH, ".//div[text()='Хотите оформить заказ?']")
    YES_BUTTON = (By.XPATH, ".//button[text()='Да']")
    NO_BUTTON = (By.XPATH, ".//button[text()='Нет']")

    # модалка с успеха заказа
    SUCCESS_ORDER_STRING = (By.XPATH, ".//div[text()='Заказ оформлен']")
    ORDER_NUMBER = (By.XPATH, ".//div[contains(text(),'Номер заказа')]")
    CHECK_STATUS = (By.XPATH, ".//button[contains(text(),'Посмотреть статус')]")
