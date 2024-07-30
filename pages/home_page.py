import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from sprint_6.locators.locators_main_page import LocatorsMainPage
from sprint_6.locators.locators_orders_page import LocatorsOrderPage
from sprint_6.pages.base_page import BasePage


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('Скролл до блока с вопросами')
    def scroll_to_question_about_important_section(self):
        self.scroll_to_element(LocatorsMainPage.question_block_title)
        self.element_is_visible(LocatorsMainPage.question_block_title)

    @allure.step('Тап по секции с вопросами')
    def click_question_buttons(self, question_id):
        elements = self.find_elements(LocatorsMainPage.question_section)
        elements[question_id].click()
        self.element_is_visible(LocatorsMainPage.get_question_id_text(question_id))

    @allure.step('Тап по лого Яндекс')
    def click_yandex_logo_button(self):
        self.click_element(LocatorsMainPage.yandex_logo)

    @allure.step('Тап по лого Самокат')
    def click_ya_scooter_logo_button(self):
        self.click_element(LocatorsMainPage.scooter_logo)

    def get_question_button_text(self, question_id):
        return self.find_element(LocatorsMainPage.get_question_button(question_id))

    def scroll_to_order_button(self, order_button):
        self.scroll_to_element(order_button)

    def click_order_button(self, order_button):
        self.click_element(order_button)

    def wait_for_order_header_text(self):
        self.element_is_visible(LocatorsOrderPage.order_header)

    def wait_for_redirect_to_dzen(self):
        self.wait_for_url()

    @allure.step('Переключиться на другую вкладку')
    def switch_to_new_tab(self):
        WebDriverWait(self.driver, self.timeout).until(EC.number_of_windows_to_be(2))
        new_tab = self.driver.window_handles[1]
        self.driver.switch_to.window(new_tab)
