from .locators import MainPageLocators
from .base_page import BasePage


'''Главная страница'''
class MainPage(BasePage):
    
    locators = MainPageLocators()
    
    '''Переход к странице авторизации'''
    def go_to_login_page(self):
        self.element_is_visible(self.locators.LOGIN_LINK).click()

    '''Переход к странице Яндекс Диск'''
    def go_to_disk(self):
        self.element_is_visible(self.locators.MORE).click()
        self.element_is_visible(self.locators.DISK_LINK).click()
    
    '''Выход из профиля'''
    def logout(self):
        self.element_is_visible(self.locators.PROFILE).click()
        self.element_is_visible(self.locators.LOGOUT_LINK).click()
