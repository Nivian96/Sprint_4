import pytest
from selenium import webdriver
from data.person import Person


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()


@pytest.fixture
def person():
    person = Person('Виктория', 'Васюкова', 'Москва', 'Киевская', '89167771122')
    return person
