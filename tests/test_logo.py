import allure

from pages.main_page import MainPage


@allure.feature('Логотипы')
class TestLogo:
    @allure.title('При нажатии на логотип Яндекса в новом окне открывается главная страница Яндекса')
    def test_ya_logo_click_opens_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_accept_cookies_button()
        main_page.click_yandex_logo()
        assert len(driver.window_handles) == 2, 'При нажатии на логотип Яндекса главная страница Яндекса открылась в ' \
                                                'текущем, а не в новом окнне'

    @allure.title('При нажатии на логотип Самоката в текущем окне открывается главная страница Самоката')
    def test_samokat_logo_click_doesnt_open_new_window(self, driver):
        main_page = MainPage(driver)
        main_page.go_to_site()
        main_page.click_accept_cookies_button()
        main_page.click_top_order_button()
        main_page.click_samokat_logo()
        assert driver.current_url == main_page.url, 'При нажатии на логотип Самоката не открылась главная страница ' \
                                                    'Самоката'
        assert len(driver.window_handles) == 1, 'При нажатии на логотип Самоката главная страница Самоката открылась ' \
                                                'в новом, а не в текущем окне'
