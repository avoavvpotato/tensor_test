import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from ..pages.main_sbis_page import MainSbis
from ..pages.download_sbis_page import DownloadSbisPage

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
#options.add_argument('--headless=new')

DIRECTORY = '/home/darya/main_project_tenz/downloads'
FILE_NAME = 'sbisplugin-setup-web.exe'

options.add_experimental_option("prefs", {
    "download.prompt_for_download": False,
    "download.directory_upgrade": True,
    "safebrowsing.enabled": True,
    "download.default_directory": DIRECTORY
})

def test_third_case(set_up):
    driver = webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install()))

    msb = MainSbis(driver)
    msb.move_to_download()

    dsp = DownloadSbisPage(driver)
    dsp.dowload(DIRECTORY, FILE_NAME)

    driver.quit()