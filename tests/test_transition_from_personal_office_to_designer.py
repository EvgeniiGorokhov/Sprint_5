from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver, login

class TestTransitionFromPersonalOfficeToDesigner:

    # Переход из личного кабинета в конструктор
    def test_go_by_click_to_constructor(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.header_of_page_constructor).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

        # Переход из личного кабинета на логотип Stellar Burgers
    def test_go_by_click_to_logo_Stellar_Burgers(self, driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.profile))
        driver.find_element(*Locators.logo).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()




