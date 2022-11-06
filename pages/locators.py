from selenium.webdriver.common.by import By


class MainPageLocators:
    LOGIN_LINK = (By.CSS_SELECTOR, "div.headline__personal > a:nth-child(1)")
    LOGOUT_LINK = (By.XPATH, "//*[text()='Выход']")
    MORE = (By.CSS_SELECTOR, "div.services-pinned__content > a")
    DISK_LINK = (By.XPATH, "//*[text()='Диск']")
    PROFILE = (By.CSS_SELECTOR, "span.avatar__image-wrapper")
    

class LoginPageLocators:
    TELEPHONE = (By.CSS_SELECTOR, "#passp-field-phone")
    MAIL = (By.CSS_SELECTOR, ".AuthLoginInputToggle-type > button")
    LOGIN = (By.CSS_SELECTOR, "#passp-field-login")
    PASSWORD = (By.CSS_SELECTOR, "#passp-field-passwd")
    BUTTON = (By.CSS_SELECTOR, ".passp-button.passp-sign-in-button > button")


class DiskPageLocators:
    CREATE = (By.CSS_SELECTOR, ".Button2.Button2_view_raised.Button2_size_m.Button2_width_max")
    FOLDER = (By.XPATH, "//*[text()='Папку']")
    FILE = (By.XPATH, "//*[text()='Текстовый документ']")
    INPUT_NAME = (By.CSS_SELECTOR, ".Textinput.Textinput_view_default.Textinput_size_m > input")
    SAVE = (By.CSS_SELECTOR, ".confirmation-dialog__footer > button")
    # NAME_FOLDER = (By.XPATH, "//div[./div[@aria-label='NewFolder']]")
    # NAME_FILE = (By.XPATH, "//*[text()='NewFile.docx']")
     