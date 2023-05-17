from pages.main_page import MainPage


class TestOrderPage:
    def test_order(self, driver):
        main_page = MainPage(driver)
        order_page = main_page.click_top_order_button()
        about_rent_order_page = order_page.fill_in_fields_and_click_next()
        about_rent_order_page.fill_in_fields_and_click_order_button()
        assert about_rent_order_page.get_order_has_been_placed_notification
