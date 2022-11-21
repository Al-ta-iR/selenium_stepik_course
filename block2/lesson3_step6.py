import math
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/redirect_accept.html"

try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    browser.find_element(By.CLASS_NAME, "trollface.btn.btn-primary").click()

    time.sleep(2)
    window_new = browser.window_handles[1]
    browser.switch_to.window(window_new)
    x_value = browser.find_element(By.ID, "input_value").text

    result = math.log(abs(12*math.sin(int(x_value))))
    browser.find_element(By.ID, "answer").send_keys(str(result))
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()
