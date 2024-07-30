from selenium.webdriver.common.by import By


class LocatorsMainPage:

    #  лого на главном экране
    scooter_logo = (By.XPATH, ".//a[contains(@class, 'Scooter')]")
    yandex_logo = (By.XPATH, ".//a[contains(@class, 'Yandex')]")

    #  кнопки заказать на Главном экране
    order_button_on_header = (By.XPATH, ".//div[starts-with(@class, 'Header')]/button[text()='Заказать']")
    order_button_on_home_page = (By.XPATH, ".//div[starts-with(@class, 'Home')]/button[text()='Заказать']")

    # Заголовок "Вопросы о важном"
    question_block_title = (By.XPATH, ".//div[text()='Вопросы о важном']")
    question_section = (By.XPATH, ".//div[@class='accordion__button']")



    @staticmethod
    def get_question_button(reply):
        return (By.XPATH, f".//div[@class='accordion__panel' and @id='accordion__panel-{reply}']/p")

    @staticmethod
    def get_question_id_text(question_id):
        return (By.XPATH, f".//div[@id='accordion__panel-{question_id}' and not(@hidden)]")
