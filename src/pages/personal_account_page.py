import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage
from src.pages.ingredient_form import IngredientPage
from src.pages.order_page import OrderPage

class PersonalAccountPage(BasePage):
    ORDER_HISTORY = (By.XPATH, ".//a[text()='История заказов']")
    ACCOUNT = (By.XPATH, ".//p[text()='Личный Кабинет']")
    ORDER_MAKE_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")
    CONSTRUCTOR_TEXT = (By.XPATH, ".//h1[text()='Соберите бургер']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//p[text()='Конструктор']")
    LIST_ORDER_TEXT = (By.XPATH, ".//h1[text()='Лента заказов']")
    LIST_ORDER_BUTTON = (By.XPATH, ".//p[text()='Лента Заказов']")
    BUN = (By.XPATH, ".//p[text()='Флюоресцентная булка R2-D3' and contains(@class, 'BurgerIngredient_ingredient__text__yp3dH')]")
    BASKET = (By.XPATH, ".//span[text()='Перетяните булочку сюда (верх)']")
    COUNT_BUN = (By.XPATH, ".//p[text()='2']")
    MAKE_ORDER_BUTTON = (By.XPATH, ".//button[text()='Оформить заказ']")


    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на Личный кабинет')
    def click_personal_account(self):
        self.waiting_clickable(self.ACCOUNT)
        self.click(self.ACCOUNT)

    @allure.step('Нажать на История заказов')
    def click_order_history(self):
        self.waiting_clickable(self.ORDER_HISTORY)
        self.click(self.ORDER_HISTORY)

    @allure.step('Ожидание появления кнопки оформить заказ')
    def check_order_button(self):
        self.waiting_visibility_element(self.ORDER_MAKE_BUTTON)

    @allure.step('Проверка перехода на страницу https://stellarburgers.nomoreparties.site/account/order-history')
    def check_order_history_page(self):
        self.waiting_url("https://stellarburgers.nomoreparties.site/account/order-history")
        print(self.driver.current_url)
        assert self.driver.current_url == "https://stellarburgers.nomoreparties.site/account/order-history"

    @allure.step('Ожидание появления текста Соберите бургер')
    def check_constructor_text(self):
        assert self.waiting_text_in_element(self.CONSTRUCTOR_TEXT, "Соберите бургер")

    @allure.step('Нажать на Конструктор')
    def click_constructor_button(self):
        self.waiting_clickable(self.CONSTRUCTOR_BUTTON)
        self.click(self.CONSTRUCTOR_BUTTON)

    @allure.step('Ожидание появления текста Лента заказов')
    def check_list_order_text(self):
        assert self.waiting_text_in_element(self.LIST_ORDER_TEXT, "Лента заказов")

    @allure.step('Нажать на Лента заказов')
    def click_list_order_button(self):
        self.waiting_clickable(self.LIST_ORDER_BUTTON)
        self.click(self.LIST_ORDER_BUTTON)

    @allure.step('Нажать на Флюоресцентная булка R2-D3')
    def select_ingredient(self):
        self.waiting_clickable(self.BUN)
        self.click(self.BUN)
        return IngredientPage(self.driver)
    
    @allure.step('Добавить Флюоресцентная булка R2-D3 в заказ')
    def drag_to_element(self):
        self.drag_to_locator(self.BUN, self.BASKET)

    @allure.step('Проверка изменения количества у Флюоресцентная булка R2-D3')
    def check_count_buns(self):
        assert self.waiting_text_in_element(self.COUNT_BUN, "2")

    @allure.step('Нажать на кнопку оформления заказа')
    def click_order_button(self):
        self.waiting_clickable(self.ORDER_MAKE_BUTTON)
        self.click(self.ORDER_MAKE_BUTTON)
        return OrderPage(self.driver)
    

