import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options


@pytest.fixture(scope="module")
def browser():
    print("\nstart browser for test..")
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()
