from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input = (By.XPATH, '//input[@placeholder="* Имя"]')
    surname_input = (By.XPATH, '//input[@placeholder="* Фамилия"]')
    address_input = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')
    metro_station_input = (By.XPATH, '//input[@placeholder="* Станция метро"]')
    metro_station_select_search_result = (
        By.XPATH,
        '//li[@class = "select-search__row"][1]',
    )
    phone_input = (
        By.XPATH,
        '//input[@placeholder="* Телефон: на него позвонит курьер"]',
    )
    next_button = (By.XPATH, "//button[contains(text(), 'Далее')]")
