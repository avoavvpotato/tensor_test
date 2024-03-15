from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains

from ..base.base_class import Base
from ..utilities.logger import Logger

class AboutTensorPage(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # Locators
    IMAGES_SECTION_WORK = '//img[@class="tensor_ru-About__block3-image new_lazy loaded"]'
    SECTION_WORK = '//h2[contains(text(), "Работаем")]'
    HEIGHT = 0
    WIDTH = 0

    def get_section_work(self):
        return self.driver.find_element(By.XPATH, self.SECTION_WORK)
    
    def move_to_section_work(self):
        self.action.move_to_element(self.get_section_work()).perform()

    def get_images_section_work(self):
        return WebDriverWait(self.driver, 30).until(EC.presence_of_all_elements_located((By.XPATH, self.IMAGES_SECTION_WORK)))
    
    def get_size_image(self):
        first_image = self.get_images_section_work()[0].size
        self.HEIGHT = first_image['height']
        self.WIDTH = first_image['width']


    def check_images_section_work(self):
        Logger.add_start_step(method='check_images_section_work')
        self.move_to_section_work()
        self.get_size_image()
        self.check_size_images(self.get_images_section_work(), self.HEIGHT, self.WIDTH)
        Logger.add_end_step(url=self.driver.current_url, method='check_images_section_work')