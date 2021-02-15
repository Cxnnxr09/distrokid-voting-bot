from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


driver = webdriver.Chrome("D:\webdrivers\chromedriver.exe")
driver.get("https://distrokid.com/spotlight/stacked/vote/")

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="distroListContainer"]/div[3]/div[3]/div[1]/div[1]/div[2]/div[2]/a[1]')))
    time.sleep(1)
    element.click()
    time.sleep(10)
finally:
    driver.quit()

