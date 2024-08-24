from selenium.webdriver.common.by import By


class Locators:
    # Главная
    # Кнопка "Войти в аккаунт" на главной
    button_login_in_main = By.XPATH, './/button[text() = "Войти в аккаунт"]'

    # Кнопка "Зарегистрироваться"
    button_register = By.XPATH, '//a[text() = "Зарегистрироваться"]'

    # Регистрация аккаунта
    # Поле "Имя"
    fields_name = By.XPATH, '//label[text()="Имя"]/following-sibling::input'

    # Поле Email
    fields_email = By.XPATH, './/label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    fields_password = By.XPATH, './/input[@name="Пароль"]'

    # Кнопка "Зарегистрироваться"
    button_submit = By.XPATH, '//button[text() = "Зарегистрироваться"]'

    # Сообщение об ошибке: пароль не прошел валидацию
    notification_incorrect_password = By.XPATH, '//p[text() = "Некорректный пароль"]'

    # Аутентификация
    # Поле Email
    fields_email_auth = By.XPATH, '//label[text()="Email"]/following-sibling::input'

    # Поле "Пароль"
    fields_password_auth = By.XPATH, '//input[@name = "Пароль"]'

    # Кнопка "Войти"
    button_login = By.XPATH, '//button[text()="Войти"]'

    # Кнопка "Личный кабинет"
    button_personal_account = By.XPATH, '//p[text() = "Личный Кабинет"]'

    # Кнопка "Оформить заказ"
    button_make_the_order = By.XPATH, '//button[text()="Оформить заказ"]'

    # Кнопка "Войти" на форме регистрации
    button_login_in_registration_form = By.XPATH, '//a[text() = "Войти"]'

    # Восстановление пароля
    # Кнопка "Восстановить пароль"
    button_forgot_password = By.XPATH, '//a[text() = "Восстановить пароль"]'

    # Кнопка "Войти" в форме восстановления пароля
    button_login_passwd_recovery_form = By.XPATH, '//a[text() = "Войти"]'
    # Раздел "История заказов"
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'

    # Кнопка "Конструктор" в шапке сайта
    header_of_page_constructor = By.XPATH, '//p[text() = "Конструктор"]'

    # Кликабельный логотип в шапке сайта
    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'

    # Кнопка "Выйти", логаут
    button_logout = By.XPATH, '//button[@type = "button"]'

    # Заголовок раздела "Булки" в меню конструктора
    buns_block = By.XPATH, '//span[text() = "Булки"]'

    # Заголовок раздела "Соусы" в меню конструктора
    sauces_block = By.XPATH, '//span[text() = "Соусы"]'

    # Заголовок раздела "Начинки" в меню конструктора
    fillings_block = By.XPATH, '//span[text() = "Начинки"]'
    # Раздел "Профиль"
    profile = By.XPATH, '//a[@href = "/account/profile"]'

