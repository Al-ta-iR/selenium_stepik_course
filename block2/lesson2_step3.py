import time
import math
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = 'http://suninjuly.github.io/selects1.html'
try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    x_flag = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y_flag = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum = str(int(x_flag) + int(y_flag))
    print(sum)

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(sum)   

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
