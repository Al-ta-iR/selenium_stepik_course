import math
import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "http://suninjuly.github.io/execute_script.html"
try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    x_value = browser.find_element(By.ID, "input_value").text
    result = math.log(abs(12*math.sin(int(x_value))))
    browser.find_element(By.ID, "answer").send_keys(str(result))
    browser.find_element(By.ID, "robotCheckbox").click()
    radio_button = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio_button)
    radio_button.click()
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()

finally:
    time.sleep(5)
    browser.quit()
