import allure

from pages.about_rent_page import AboutRentOrderPage
from pages.main_page import MainPage
from pages.order_page import OrderPage


@allure.feature('Заказ самоката')
class TestOrderPage:
    @allure.title('После заполнения формы заказа появляется всплывающее окно об успешном создании заказа')
    def test_order(self, driver, person):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_accept_cookies_button()
        main_page.click_top_order_button()
        order_page = OrderPage(driver)
        order_page.fill_in_fields_and_click_next(person)
        about_rent_order_page = AboutRentOrderPage(driver)
        about_rent_order_page.fill_in_fields_and_click_order_button()
        assert about_rent_order_page.get_order_has_been_placed_notification, 'После заполнения формы заказа не ' \
                                                                             'появилось всплывающее окно об успешном ' \
                                                                             'создании заказа'
