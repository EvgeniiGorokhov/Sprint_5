from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UsersTestData
from locators import Locators
from conftest import driver

class TestAuthorization:

    # вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_login_to_account_on_home(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        driver.find_element(*Locators.fields_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

        # вход через кнопку «Личный кабинет
    def test_login_via_button_personal_office(self,driver):
        driver.find_element(*Locators.button_personal_account).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        driver.find_element(*Locators.fields_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

        # вход через кнопку в форме регистрации
    def test_login_via_button_in_registration_form(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_in_registration_form))
        driver.find_element(*Locators.button_login_in_registration_form).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        driver.find_element(*Locators.fields_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()

        #вход через кнопку в форме восстановления пароля
    def test_login_via_button_in_password_recovery_form(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_forgot_password))
        driver.find_element(*Locators.button_forgot_password).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login_passwd_recovery_form))
        driver.find_element(*Locators.button_login_passwd_recovery_form).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_login))
        driver.find_element(*Locators.fields_email_auth).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password_auth).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_login).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_make_the_order))
        assert driver.find_element(*Locators.button_make_the_order).is_displayed()














