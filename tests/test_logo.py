from data.urls import Urls
from pages.main_page import MainPage


class TestLogo:
    def test_ya_logo_click_opens_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_yandex_logo()
        assert len(driver.window_handles) == 2

    def test_samokat_logo_click_doesnt_open_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.click_samokat_logo()
        assert driver.current_url == Urls.main_page
        assert len(driver.window_handles) == 1
