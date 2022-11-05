from .base_page import BasePage
from .locators import LoginPageLocators


'''Страница авторизации'''
class LoginPage(BasePage):

    locators = LoginPageLocators()

    '''Данные для входа'''
    LOGIN = "testui.test"
    PASSWORD = "Test2022"

    '''Вход в профиль'''
    def login(self):
        login = self.element_is_visible(self.locators.LOGIN)
        login.send_keys(self.LOGIN)
        self.element_is_visible(self.locators.BUTTON).click()
        password = self.element_is_visible(self.locators.PASSWORD)
        password.send_keys(self.PASSWORD)
        self.element_is_visible(self.locators.BUTTON).click()
        