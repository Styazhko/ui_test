from .base_page import BasePage
from .locators import LoginPageLocators
from ..settings import login, password

'''Страница авторизации'''
class LoginPage(BasePage):

    locators = LoginPageLocators()

    '''Данные для входа'''
    LOGIN = login
    PASSWORD = password

    '''Вход в профиль'''
    def login(self):
        self.element_is_clickable(self.locators.MAIL).click()
        login = self.element_is_visible(self.locators.LOGIN)
        login.send_keys(self.LOGIN)
        self.element_is_visible(self.locators.BUTTON).click()
        password = self.element_is_visible(self.locators.PASSWORD)
        password.send_keys(self.PASSWORD)
        self.element_is_visible(self.locators.BUTTON).click()
        