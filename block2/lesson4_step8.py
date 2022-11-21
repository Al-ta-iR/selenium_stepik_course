import math
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, "book").click()

    x_value = browser.find_element(By.ID, "input_value").text

    result = math.log(abs(12*math.sin(int(x_value))))
    browser.find_element(By.ID, "answer").send_keys(str(result))
    WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "solve"))).click()

finally:
    time.sleep(5)
    browser.quit()
