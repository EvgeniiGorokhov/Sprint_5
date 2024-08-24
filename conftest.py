import pytest
from data import UsersTestData
from selenium.webdriver.common.by import By
from selenium import webdriver


# Фикстура для авторизации с валидной парой log/pass перед тестами
@pytest.fixture
def login(driver):
    driver.find_element(By.XPATH, './/button[text() = "Войти в аккаунт"]').click()
    driver.find_element(By.XPATH, './/label[text()="Email"]/following-sibling::input').send_keys(UsersTestData.email)
    driver.find_element(By.XPATH, './/input[@name="Пароль"]').send_keys(UsersTestData.password)
    driver.find_element(By.XPATH, '//button[text()="Войти"]').click()


@pytest.fixture(scope="function")
def driver():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument("--incognito")
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://stellarburgers.nomoreparties.site/")
    yield driver
    driver.quit()

