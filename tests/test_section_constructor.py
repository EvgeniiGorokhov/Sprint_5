from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import Locators
from conftest import driver, login

class TestSectionConstructor:
    # Проверка перехода из раздела "Булки" в раздел "Соусы"
    def test_transition_from_the_section_bun_to_the_section_sauces(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.sauces_block).click()
        assert driver.find_element(*Locators.sauces_block).text == 'Соусы'

    # Проверка перехода из раздела "Булки" в раздел "Соусы" авторизованый
    def test_transition_from_the_section_bun_to_the_section_sauces_authorization(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.sauces_block).click()
        assert driver.find_element(*Locators.sauces_block).text == 'Соусы'

    # Проверка перехода из раздела "Булки" в раздел "Начинки"
    def test_transition_from_bun_section_to_filling_section(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.fillings_block).click()
        assert driver.find_element(*Locators.fillings_block).text == 'Начинки'

        # Проверка перехода из раздела "Булки" в раздел "Начинки" авторизованый
    def test_transition_from_bun_section_to_filling_section_authorization(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.buns_block))
        driver.find_element(*Locators.fillings_block).click()
        assert driver.find_element(*Locators.fillings_block).text == 'Начинки'

    # Проверка перехода из раздела "Соусы" в раздел "Начинки"
    def test_transition_from_the_sauces_section_to_the_toppings_section(self,driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        driver.find_element(*Locators.fillings_block).click()
        assert driver.find_element(*Locators.fillings_block).text == 'Начинки'

    # Проверка перехода из раздела "Соусы" в раздел "Начинки" авторизованый
    def test_transition_from_the_sauces_section_to_the_toppings_section_authorization(self, driver, login):
            WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
            driver.find_element(*Locators.sauces_block).click()
            driver.find_element(*Locators.fillings_block).click()
            assert driver.find_element(*Locators.fillings_block).text == 'Начинки'

    # Проверка перехода из раздела "Соусы" в раздел "Булки"
    def test_transition_from_the_sauces_section_to_the_bun_section(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        driver.find_element(*Locators.buns_block).click()
        assert driver.find_element(*Locators.buns_block).text == 'Булки'

    # Проверка перехода из раздела "Соусы" в раздел "Булки" авторизованый
    def test_transition_from_the_sauces_section_to_the_bun_section_authorization(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.sauces_block))
        driver.find_element(*Locators.sauces_block).click()
        driver.find_element(*Locators.buns_block).click()
        assert driver.find_element(*Locators.buns_block).text == 'Булки'

    # Проверка перехода из раздела "Начинки" в раздел "Соусы"
    def test_checking_the_transition_from_the_fillings_section_to_the_sauces_section(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        driver.find_element(*Locators.sauces_block).click()
        assert driver.find_element(*Locators.sauces_block).text == 'Соусы'

    # Проверка перехода из раздела "Начинки" в раздел "Соусы" авторизованый
    def test_checking_the_transition_from_the_fillings_section_to_the_sauces_section_authorization(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        driver.find_element(*Locators.sauces_block).click()
        assert driver.find_element(*Locators.sauces_block).text == 'Соусы'


    # Проверка перехода из раздела "Начинки" в раздел "Булки"
    def test_checking_transition_from_filling_section_to_bun_section(self, driver):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        driver.find_element(*Locators.buns_block).click()
        assert driver.find_element(*Locators.buns_block).text == 'Булки'

    # Проверка перехода из раздела "Начинки" в раздел "Булки" авторизованый
    def test_checking_transition_from_filling_section_to_bun_section_authorization(self, driver, login):
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(Locators.fillings_block))
        driver.find_element(*Locators.fillings_block).click()
        driver.find_element(*Locators.buns_block).click()
        assert driver.find_element(*Locators.buns_block).text == 'Булки'











