from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..pages.main_sbis_page import MainSbis
from ..pages.contacts_sbis_page import ContactsSbisPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument('--headless=new')

def test_second_case(set_up):
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    msb = MainSbis(driver)
    msb.move_to_contacts()

    REGION_1 = 'Новосибирская обл.'
    CITY_1 = 'Новосибирск'
    REGION_2 = 'Камчатский край'
    CITY_2 = 'Петропавловск-Камчатский'
    URL = '41-kamchatskij-kraj'

    cp = ContactsSbisPage(driver)
    cp.check_city(REGION_1, CITY_1)
    cp.check_if_partners_exist()
    cp.switch_to_another_region(REGION_2, CITY_2, URL)

    driver.quit()