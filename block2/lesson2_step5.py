import time
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


link = "https://SunInJuly.github.io/execute_script.html"
try:
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    browser.get(link)

    button = browser.find_element(By.TAG_NAME, "button")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)  # прокрутка вниз до кнопки
    browser.execute_script("window.scrollBy(0, 100);")  # или можно скролл вниз
    button.click()

finally:
    time.sleep(5)
    browser.quit()
