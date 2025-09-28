import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from src.pages.base_page import BasePage
from src.pages.personal_account_page import PersonalAccountPage
from src.pages.recovery_page import RecoveryPage

class AuthorizationPage (BasePage):
    RECOVERY_PASSWORD = (By.XPATH, ".//a[text()='Восстановить пароль']")
    EMAIL_FIELD = (By.XPATH, ".//input[@name='name']")
    PASSWORD_FIELD = (By.XPATH, ".//input[@name='Пароль']")
    EXIT_BUTTON = (By.XPATH, ".//button[text()='Войти']")

    def __init__(self, driver: WebDriver):
        self.driver = driver

    @allure.step('Нажать на кнопку Восстановить пароль')
    def click_recovery_password(self):
        self.waiting_visibility_element(self.RECOVERY_PASSWORD)
        self.click(self.RECOVERY_PASSWORD)
        return RecoveryPage(self.driver)

    @allure.step('Ввод email')
    def input_email(self, email):
        self.input_text(self.EMAIL_FIELD, email)
        
    @allure.step('Ввод password')
    def input_password(self, password):
        self.input_text(self.PASSWORD_FIELD, password)

    @allure.step('Нажать на кнопку Войти')
    def click_exit_button(self):
        self.waiting_clickable(self.EXIT_BUTTON)
        self.click(self.EXIT_BUTTON)
        return PersonalAccountPage(self.driver)
    