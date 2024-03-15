from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..base.base_class import Base
from ..utilities.logger import Logger

class MainSbis(Base):

    MAIN_URL = 'https://sbis.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # Locators
    CONTACTS = '//a[@href="/contacts"]'
    DOWNLOAD = '//a[@href="/download"]'

    # Getters
    def get_contact_link(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CONTACTS)))
    
    def get_download(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.DOWNLOAD)))
    
    # Actions
    def click_contacts(self):
        self.get_contact_link().click()

    def click_download(self):
        self.driver.execute_script("arguments[0].click();", self.get_download())

    # Methods
    def open_page(self):
        self.driver.get(self.MAIN_URL)
        self.driver.maximize_window()

    def move_to_contacts(self):
        Logger.add_start_step(method='move_to_contacts')
        self.open_page()
        self.click_contacts()
        Logger.add_end_step(url=self.driver.current_url, method='move_to_contacts')

    def move_to_download(self):
        Logger.add_start_step(method='move_to_download')
        self.open_page()
        self.click_download()
        Logger.add_end_step(url=self.driver.current_url, method='move_to_download')