from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def fill_in_fields_and_click_next(self, person):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(person.name)
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(person.surname)
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(person.address)
        self.driver.find_element(*OrderPageLocators.metro_station_input).send_keys(person.metro_station)
        self.driver.find_element(*OrderPageLocators.metro_station_select_search_result).click()
        self.driver.find_element(*OrderPageLocators.phone_input).send_keys(person.phone_number)
        self.driver.find_element(*OrderPageLocators.next_button).click()
