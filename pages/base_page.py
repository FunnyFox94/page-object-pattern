import allure
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, timeout=10):
        self.driver = driver
        self.timeout = timeout

    def find_element(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_element_located(locator))

    def find_elements(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.presence_of_all_elements_located(locator))

    def click_element(self, locator):
        element = self.find_element(locator)
        return element.click()

    def send_text(self, locator, text):
        element = self.find_element(locator)
        return element.send_keys(text)

    def element_is_visible(self, locator):
        return WebDriverWait(self.driver, self.timeout).until(EC.visibility_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step('Получить URL страницы')
    def get_url(self):
        return self.driver.current_url

    @allure.step('Перейти на страницу')
    def go_to_url(self, page_url):
        return self.driver.get(page_url)

    @allure.step('Тап Далее')
    def tap_enter_button(self, locator):
        self.find_element(locator).send_keys(Keys.ENTER)

    @allure.step('Переключить вкладку по номеру')
    def switch_to(self, window_number: int = 1):
        self.driver.switch_to.window(self.driver.window_handles[window_number])

    @allure.step('Закрыть вкладку')
    def close_page(self):
        self.driver.close()

    @allure.step('Дождаться отображения URL страницы')
    def wait_for_url(self):
        WebDriverWait(self.driver, self.timeout).until_not(EC.url_matches("about:blank"))
