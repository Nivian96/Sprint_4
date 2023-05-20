from selenium.webdriver.common.by import By


class MainPageLocators:
    yandex_logo = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]')
    samokat_logo = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]')
    top_order_button = (By.XPATH, '//button[@class="Button_Button__ra12g"]')
    central_big_order_button = (
        By.XPATH,
        '//button[@class="Button_Button__ra12g Button_UltraBig__UU3Lp"]',
    )
    accept_cookie_button = (By.XPATH, '//button[@class="App_CookieButton__3cvqF"]')
    questions_block = (By.XPATH, '//div[@data-accordion-component="Accordion"]')
    questions = (By.XPATH, '//div[@data-accordion-component="AccordionItem"]')
    answer = (
        By.CSS_SELECTOR,
        "#accordion__panel-{question_num}",
    )
