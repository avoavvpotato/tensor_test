from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from ..base.base_class import Base
from ..utilities.logger import Logger

class ContactsSbisPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
    
    # Locators
    TENSOR_BANNER = '//a[@title="tensor.ru"]'
    TENSOR_URL = 'https://tensor.ru/'
    REGION = '//div[@class="sbis_ru-container sbisru-Contacts__relative"]//span/span'
    CITY = '//div[@id="city-id-2"]'
    PARTNERS = '//div[@class="sbisru-Contacts-List__col-1"]'
    NAME_PARTNER = ''


    # Getters
    def get_tensor_banner(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.TENSOR_BANNER)))
    
    def get_region(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.REGION)))
    
    def get_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.CITY)))
    
    def get_selected_region(self, selected_region):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, f'//span[@title="{selected_region}"]')))
    
    def get_list_patners(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.PARTNERS)))

    # Actions
    def click_tensor_banner(self):
        self.get_tensor_banner().click()

    def click_region(self):
        self.get_region().click()

    def click_new_region(self, selected_region):
        self.get_selected_region(selected_region).click()
    
    # Methods
    def check_if_partners_exist(self):
        Logger.add_start_step(method='check_if_partners_exist')
        list_partners = self.get_list_patners()
        self.NAME_PARTNER = list_partners[0].text
        assert len(list_partners) > 0
        Logger.add_end_step(url=self.driver.current_url ,method='check_if_partners_exist')

    def move_tensor(self):
        Logger.add_start_step(method='move_tensor')
        self.click_tensor_banner()
        self.driver.switch_to.window(self.driver.window_handles[1])
        self.assert_url(self.TENSOR_URL)
        Logger.add_end_step(url=self.driver.current_url, method='move_tensor')

    def check_city(self, check_region, check_city):
        Logger.add_start_step(method='check_city')
        self.assert_word(self.get_region(), check_region)
        self.assert_word(self.get_city(), check_city)
        Logger.add_end_step(url=self.driver.current_url, method='check_city')

    def check_patner_changed(self):
        Logger.add_start_step(method='check_patner_changed')
        list_partners = self.get_list_patners()
        assert self.NAME_PARTNER != list_partners[0].text
        self.NAME_PARTNER = list_partners[0].text
        Logger.add_end_step(url=self.driver.current_url, method='check_patner_changed')

    def switch_to_another_region(self, new_region, new_city, url):
        Logger.add_start_step(method='switch_to_another_region')
        new_url = f'https://sbis.ru/contacts/{url}?tab=clients'
        self.click_region()
        self.click_new_region(new_region)
        self.driver.implicitly_wait(10)
        self.driver.get(new_url)
        self.assert_url(new_url)
        self.assert_title(new_region)
        self.check_city(new_region, new_city)
        self.check_patner_changed()
        Logger.add_end_step(url=self.driver.current_url, method='switch_to_another_region')