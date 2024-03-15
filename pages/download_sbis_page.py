import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from ..base.base_class import Base
from ..utilities.logger import Logger

class DownloadSbisPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    URL_TAB = 'https://sbis.ru/download?tab=ereport&innerTab=ereport25'

    # Locators
    PLAGIN = '//div[@class="controls-TabButton__caption"][contains(text(), "Плагин")]'
    FILE_TO_DOWNLOAD = '//a[@href="https://update.sbis.ru/Sbis3Plugin/master/win32/sbisplugin-setup-web.exe"]'

    def get_plagin(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.PLAGIN)))
    
    def get_file_to_download(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FILE_TO_DOWNLOAD)))
    
    def click_plagin(self):
        self.driver.execute_script("arguments[0].click();", self.get_plagin())

    def click_file_to_dowload(self):
        self.get_file_to_download().click()
    
    def wait_for_url(self):
        return WebDriverWait(self.driver, 30).until(lambda driver: self.driver.current_url == self.URL_TAB)

    def size_file(self):
        text_size = WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.FILE_TO_DOWNLOAD))).text
        return text_size.split()[2]
        
    def wait_for_dowload(self, directory, file_name):
        while True:
            try:
                open(os.path.join(directory, file_name))
                break
            except:
                time.sleep(.1)

    def dowload(self, directory, file_name):
        Logger.add_start_step(method='dowload')
        self.wait_for_url()
        self.click_plagin()
        self.click_file_to_dowload()
        self.wait_for_dowload(directory, file_name)
        #self.assert_file_download(directory, file_name)
        self.assert_file_size(os.path.join(directory, file_name), self.size_file(), 'MB')
        self.clear_directory(directory)
        Logger.add_end_step(url=self.driver.current_url, method='dowload')

    