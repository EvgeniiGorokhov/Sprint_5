import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from data import UsersTestData
from locators import Locators
from conftest import driver

class TestRegistration:
    # Регистрация аккаунта пользователя с валидными значениями
    def test_registration_new_account_success_submit(self, driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver,5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.fields_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_submit).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        assert driver.find_element(*Locators.button_register).is_displayed()

        # Регистрация аккаунта при пустом поле "Имя"
    def test_for_empty_name(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys('')
        driver.find_element(*Locators.fields_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_submit).click()
        assert driver.find_element(*Locators.button_submit).is_displayed()

        # Создание аккаунта: при вводе недопустимого значения в поле Email отсутствует символ @
    def test_create_account_when_enter_an_invalid_value_in_the_email_field_missing_character(self,driver):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.fields_email).send_keys(UsersTestData.invalid_email)
        driver.find_element(*Locators.fields_password).send_keys(UsersTestData.password)
        driver.find_element(*Locators.button_submit).click()
        assert driver.find_element(*Locators.button_submit).is_displayed()

        # Создание аккаунта при вводе допустимого по длине значения в поле "Пароль"
    @pytest.mark.parametrize('valid_password', ['123456', 'Geirby54-', '90547689732'])
    def test_creating_an_account_by_entering_a_valid_length_value_in_the_password_field(self,driver,valid_password):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.fields_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password).send_keys(valid_password)
        driver.find_element(*Locators.button_submit).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        assert driver.find_element(*Locators.button_register).is_displayed()

        # Создание аккаунта при вводе не допустимого по длине значения в поле "Пароль"
    @pytest.mark.parametrize('invalid_password', ['1', 'Geir', '76'])
    def test_creating_account_when_entering_an_invalid_length_value_in_the_password_field(self,driver,invalid_password):
        driver.find_element(*Locators.button_login_in_main).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_register))
        driver.find_element(*Locators.button_register).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.button_submit))
        driver.find_element(*Locators.fields_name).send_keys(UsersTestData.username)
        driver.find_element(*Locators.fields_email).send_keys(UsersTestData.email)
        driver.find_element(*Locators.fields_password).send_keys(invalid_password)
        driver.find_element(*Locators.button_submit).click()
        assert driver.find_element(*Locators.notification_incorrect_password).text == 'Некорректный пароль'













