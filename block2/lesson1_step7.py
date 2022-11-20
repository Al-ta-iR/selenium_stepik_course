import time
import math
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    flag = browser.find_element(By.ID, "treasure")
    x = flag.get_attribute("valuex")
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.ID, "robotCheckbox")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    button.click()
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()
