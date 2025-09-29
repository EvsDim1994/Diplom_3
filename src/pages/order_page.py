import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage

class OrderPage(BasePage):
    ORDER_NUMBER = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow__3ikwq ')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Проверка появления номера заказа после оформления')
    def check_order_number(self):
        assert self.waiting_visibility_element(self.ORDER_NUMBER)

    