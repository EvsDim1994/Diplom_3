import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage


class ListOrderPage(BasePage):
    LIST_ORDER_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")
    ALL_ORDERS = (By.XPATH, ".//div[p[text()='Выполнено за все время:'] and p[contains(@class, 'OrderFeed_number__2MbrQ')]]")
    ORDER_TODAY = (By.XPATH, ".//div[p[text()='Выполнено за сегодня:'] and p[contains(@class, 'OrderFeed_number__2MbrQ')]]")
    IN_WORK_ORDER = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[contains(@class, 'text_type_digits-default')]")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Ожидание появления текста Лента заказов')
    def check_list_order_text(self):
        assert self.waiting_text_in_element(self.LIST_ORDER_TEXT, "Лента заказов")

    @allure.step('Получение всех заказов до оформления')
    def get_all_orders(self):
        return self.find_element(self.ALL_ORDERS).text
    
    @allure.step('Получение всех заказов за сегодня до оформления')
    def get_all_orders_today(self):
        return self.find_element(self.ORDER_TODAY).text
    
    @allure.step('Получение заказа в работе')
    def get_all_order_in_work(self):
        return self.find_element(self.IN_WORK_ORDER).text
    
    @allure.step('Проверка изменения счетчика всех заказов')
    def check_all_order(self, orders):
        def get_number(text):
            return int(''.join(filter(str.isdigit, text)))
    
        current = get_number(orders)
        expected = current + 1
        actual = get_number(self.get_all_orders())
    
        assert actual == expected, f"Счетчик заказов: ожидалось {expected}, но получили {actual}"

    @allure.step('Проверка изменения счетчика всех заказов')
    def check_all_order_today(self, orders):
        def get_number(text):
            return int(''.join(filter(str.isdigit, text)))
    
        current = get_number(orders)
        expected = current + 1
        actual = get_number(self.get_all_orders_today())
    
        assert actual == expected, f"Счетчик заказов: ожидалось {expected}, но получили {actual}"

    @allure.step('Проверка номера заказа в работе')
    def check_order_in_work(self, number):
        number_in_work = self.get_all_order_in_work()
        number_in_work = f'#{number_in_work}'
        assert number == number_in_work
    