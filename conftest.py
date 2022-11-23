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
    link_url = 'https://stepik.org/lesson/236895/step/1'
    browser.get(link_url)
    time.sleep(2)
    browser.find_element(By.ID, "ember32").click()
    browser.find_element(By.ID, "id_login_email").send_keys('************')
    browser.find_element(By.ID, "id_login_password").send_keys('************')
    browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    time.sleep(2)
    yield browser
    print("\nquit browser..")
    time.sleep(3)
    browser.quit()
