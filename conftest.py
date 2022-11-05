import pytest
from selenium import webdriver


'''Фикстура для открытия Chrome в начале теста и закрытие по завершению теста'''
@pytest.fixture(scope="class")
def browser(): 
    print("\nstart chrome browser for test..")
    browser = webdriver.Chrome()
    yield browser
    print("\nquit browser..")
    browser.quit()
    