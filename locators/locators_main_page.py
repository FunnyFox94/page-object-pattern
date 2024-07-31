from selenium.webdriver.common.by import By


class LocatorsMainPage:
    #  лого на главном экране
    SCOOTER_LOGO = (By.XPATH, ".//a[contains(@class, 'Scooter')]")
    YANDEX_LOGO = (By.XPATH, ".//a[contains(@class, 'Yandex')]")

    #  кнопки заказать на Главном экране
    ORDER_BUTTON_ON_HEADER = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    ORDER_BUTTON_ON_MAIN_PAGE = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")

    # Заголовок "Вопросы о важном"
    QUESTION_BLOCK_TITLE = (By.XPATH, ".//div[text()='Вопросы о важном']")
    QUESTION_SECTION = (By.XPATH, ".//div[@class='accordion__button']")

    @staticmethod
    def get_question_button(reply):
        return (By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{reply}']/p")

    @staticmethod
    def get_question_id_text(question_id):
        return (By.XPATH, f".//div[@id='accordion__panel-{question_id}' and not(@hidden)]")
