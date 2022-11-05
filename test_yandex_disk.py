import random
import string

from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.disk_page import DiskPage


'''Тест создания нового файла в приложении Яндекс Диск'''
class TestYandex:

    NAME_FOLDER = ''.join(random.sample(string.ascii_lowercase, 8))
    NAME_FILE = ''.join(random.sample(string.ascii_lowercase, 8))

    def test_new_yandex_disk(self, browser):
        link = "http://ya.ru"
        main_page = MainPage(browser, link)
        main_page.open()
        main_page.go_to_login_page()
        login_page = LoginPage(browser, browser.current_url)
        login_page.login()
        main_page = MainPage(browser, browser.current_url)
        window_one = browser.window_handles[0]
        main_page.go_to_disk()
        window_two = browser.window_handles[1]
        browser.switch_to.window(window_two)
        disk_page = DiskPage(browser, browser.current_url)
        disk_page.create_new_folder(self.NAME_FOLDER)
        disk_page.open_folder(self.NAME_FOLDER)
        disk_page = DiskPage(browser, browser.current_url)
        disk_page.create_new_file(self.NAME_FILE)
        disk_page.should_be_add_new_file(self.NAME_FILE)
        window_three = browser.window_handles[2]
        browser.switch_to.window(window_three)
        disk_page.should_be_name_new_file(self.NAME_FILE)
        browser.close()
        browser.switch_to.window(window_one)
        main_page.logout()
