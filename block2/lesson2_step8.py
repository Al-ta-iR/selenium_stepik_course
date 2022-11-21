import time
import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/file_input.html"
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'file.txt')

try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(2)").send_keys('Data')
    browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(4)").send_keys('Data')
    browser.find_element(By.CSS_SELECTOR, "input.form-control:nth-child(6)").send_keys('Data')
    browser.find_element(By.ID, "file").send_keys(file_path)
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()
