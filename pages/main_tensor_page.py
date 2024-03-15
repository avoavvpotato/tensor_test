from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from ..base.base_class import Base
from ..utilities.logger import Logger

class MainTensorPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

# Perform the move action

    # Locators
    SECTION_STRENGTH = '//p[contains(text(), "Сила в людях")]'
    LINK_ABOUT = '//a[@href="/about"]'
    URL_ABOUT = 'https://tensor.ru/about'

    # Getters
    def get_container_strength(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.SECTION_STRENGTH)))
    
    def get_link_about(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.LINK_ABOUT)))
    
    # Actions
    def click_link_about(self):
        self.get_link_about().click()

    # Methods
    def link_about_tensor(self):
        Logger.add_start_step(method='link_about_tensor')
        self.assert_word(self.get_container_strength(), 'Сила в людях')
        self.click_link_about()
        self.assert_url(self.URL_ABOUT)
        Logger.add_end_step(url=self.driver.current_url, method='link_about_tensor')
        