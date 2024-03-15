from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..pages.main_sbis_page import MainSbis
from ..pages.contacts_sbis_page import ContactsSbisPage
from ..pages.main_tensor_page import MainTensorPage
from ..pages.about_tensor_page import AboutTensorPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument('--headless=new')

def test_first_case(set_up):
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    msb = MainSbis(driver)
    msb.move_to_contacts()

    csp = ContactsSbisPage(driver)
    csp.move_tensor()

    mtp = MainTensorPage(driver)
    mtp.link_about_tensor()

    atp = AboutTensorPage(driver)
    atp.check_images_section_work()

    driver.quit()