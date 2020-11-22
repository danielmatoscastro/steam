from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time

APP_ID = 730
BASE_URL = 'https://steamdb.info/app/'

profile = webdriver.FirefoxProfile()
profile.set_preference("general.useragent.override", "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:83.0) Gecko/20100101 Firefox/83.0")
profile.set_preference("javascript.enabled", True)
profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

firefox = webdriver.Firefox(profile)
firefox.get(f'{BASE_URL}{APP_ID}/')
time.sleep(2)
br = firefox.find_element_by_id('js-price-history')
br.click()
time.sleep(2)
#export_btn = firefox.find_element_by_css_selector('.highcharts-button')
#export_btn.click()
WebDriverWait(firefox, 2).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".highcharts-button-symbol"))).click()
time.sleep(2)
csv = firefox.find_element_by_css_selector('div.highcharts-contextmenu > ul > li:nth-child(1)')
csv.click()
#firefox.quit()
