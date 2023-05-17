from data.person import Person
from data.urls import Urls
from locators.order_page_locators import OrderPageLocators
from pages.about_rent_page import AboutRentOrderPage
from pages.base_page import BasePage


class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate_to_url(Urls.order_page)

    def fill_in_fields_and_click_next(self):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(Person.name)
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(
            Person.surname
        )
        self.driver.find_element(*OrderPageLocators.address_input).send_keys(
            Person.address
        )
        self.driver.find_element(*OrderPageLocators.metro_station_input).send_keys(
            Person.metro_station
        )
        self.driver.find_element(
            *OrderPageLocators.metro_station_select_search_result
        ).click()
        self.driver.find_element(*OrderPageLocators.phone_input).send_keys(
            Person.phone_number
        )
        self.driver.find_element(*OrderPageLocators.next_button).click()
        return AboutRentOrderPage(self.driver)
