from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver, login

class TestGoToYourPersonalAccount:

    # Проверь переход по клику на «Личный кабинет

    def test_go_from_the_main_page_to_your_personal_account(self,driver, login):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.profile))
        assert driver.find_element(*Locators.order_history).is_displayed()





