from data.urls import Urls
from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from pages.order_page import OrderPage


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.navigate_to_url(Urls.main_page)
        self.__click_accept_cookies_button()

    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.yandex_logo).click()

    def click_samokat_logo(self):
        self.driver.find_element(*MainPageLocators.samokat_logo).click()

    def __click_accept_cookies_button(self):
        self.driver.find_element(*MainPageLocators.accept_cookie_button).click()

    def click_top_order_button(self):
        self.driver.find_element(*MainPageLocators.top_order_button).click()
        return OrderPage(self.driver)

    def click_question(self, question_number):
        questions_block = self.driver.find_element(*MainPageLocators.questions_block)
        self.scroll_to_element(questions_block)
        questions = self.wait_for_presence_of_all_elements(MainPageLocators.questions)
        self.wait_for_element_clickable(questions[question_number - 1]).click()

    def get_answer(self, question_number):
        by, path = MainPageLocators.answer
        path = path.format(question_num=question_number - 1)
        return self.wait_for_visibility_of_element((by, path)).text
