from selenium.webdriver.common.by import By


class AboutRentPageLocators:
    date_input = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')
    date_picker = (
        By.XPATH,
        "//div[contains(@class, 'react-datepicker__day--selected')]",
    )
    dropdown_control = (By.CLASS_NAME, "Dropdown-control")
    dropdown_option = (By.CLASS_NAME, "Dropdown-option")
    black_checkbox = (By.ID, "black")
    order_button = (
        By.XPATH,
        "//button[contains(text(), 'Заказать') and contains(@class, 'Button_Middle__1CSJM')]",
    )
    yes_button = (
        By.XPATH,
        "//button[contains(text(), 'Да') and contains(@class, 'Button_Middle__1CSJM')]",
    )
    order_complete = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
