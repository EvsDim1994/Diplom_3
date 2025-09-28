import pytest

from src.config import Config
from src.helpers.faker import fake_user
from src.helpers.reqistration_user import register_new_user_and_return_token
from src.requests.requests import Request
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver


@pytest.fixture(scope='class')
def create_fake_user():
    return fake_user()

@pytest.fixture(scope='class')
def register_user(create_fake_user):
    return register_new_user_and_return_token(create_fake_user)

@pytest.fixture(scope='session')
def client():
    return Request(Config.URL)

@pytest.fixture(scope='function')
def driver():
    options = webdriver.FirefoxOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Firefox(options=options)
    driver.implicitly_wait(10)
    yield driver
    # закрытие драйвера
    driver.quit()

@pytest.fixture(scope='function')
def main_page(driver: WebDriver):
    # открыть главную страницу
    driver.get(Config.URL)