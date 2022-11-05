import pytest

from .base_page import BasePage
from .locators import DiskPageLocators
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By


'''Страница Яндекс Диск'''
class DiskPage(BasePage):
    
    locators = DiskPageLocators()

    '''Создание новой папки'''
    def create_new_folder(self, name_folder):
        locator = (By.CSS_SELECTOR, ".rename-dialog__rename-error")
        self.element_is_visible(self.locators.CREATE).click()
        self.element_is_visible(self.locators.FOLDER).click()
        input_name = self.element_is_visible(self.locators.INPUT_NAME)
        input_name.click()
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(name_folder)
        self.element_is_clickable(self.locators.SAVE).click()
        if self.element_is_visible(locator).text:
                pytest.skip(f"Папка с именем «{name_folder}» уже существует")

    '''Открытие папки'''
    def open_folder(self, name_folder):
        locator = (By.XPATH, f"//div[./div[@aria-label='{name_folder}']]")
        folder = self.element_is_visible(locator)
        ActionChains(self.browser).double_click(folder).perform()
    
    '''Создание нового файла (в данном случае .docx)'''
    def create_new_file(self, name_file):
        self.element_is_visible(self.locators.CREATE).click()
        self.element_is_visible(self.locators.FILE).click()
        input_name = self.element_is_visible(self.locators.INPUT_NAME)
        input_name.click()
        input_name.send_keys(Keys.CONTROL + "a")
        input_name.send_keys(Keys.DELETE)
        input_name.send_keys(name_file)
        self.element_is_clickable(self.locators.SAVE).click()

    '''Проверка на создание нового файла'''
    def should_be_add_new_file(self, name_file):
        locator = (By.XPATH, f"//*[text()='{name_file}.docx']")
        assert len(self.elements_are_visible(locator)) > 0, "Новый файл не создан"

    '''Проверка на соответствие имени'''
    def should_be_name_new_file(self, name_file):
        name_new_file = self.browser.title[:-24]
        assert name_new_file == name_file, "Имя файла не соответствует"
        