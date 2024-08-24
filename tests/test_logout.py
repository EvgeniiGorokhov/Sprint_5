from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver, login

class TestLogout:
    # Проверь выход по кнопке «Выйти» в личном кабинете
    def test_exit_by_the_exit_button_in_your_personal_office(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.button_logout).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        assert driver.find_element(*Locators.button_login).is_displayed()


