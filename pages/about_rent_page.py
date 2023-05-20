from locators.about_rent_page_locators import AboutRentPageLocators
from pages.base_page import BasePage
from datetime import date


class AboutRentOrderPage(BasePage):
    def fill_in_fields_and_click_order_button(self):
        self.driver.find_element(*AboutRentPageLocators.date_input).send_keys(str(date.today()))
        self.driver.find_element(*AboutRentPageLocators.date_picker).click()
        self.driver.find_element(*AboutRentPageLocators.dropdown_control).click()
        self.driver.find_elements(*AboutRentPageLocators.dropdown_option)[6].click()
        self.driver.find_element(*AboutRentPageLocators.black_checkbox).click()
        self.driver.find_element(*AboutRentPageLocators.order_button).click()
        self.driver.find_element(*AboutRentPageLocators.yes_button).click()

    def get_order_has_been_placed_notification(self):
        return self.wait_for_visibility_of_element(AboutRentPageLocators.order_complete)
