import pytest
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

env_path = os.path.join('secrets.env')
load_dotenv(env_path)
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")


@pytest.fixture(scope="module")
def browser():
    print("\n► start browser for test..")
    options = Options()
    options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
    browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
    link_url = 'https://stepik.org/catalog?auth=login'
    browser.get(link_url)
    # time.sleep(1)
    WebDriverWait(browser, 10).until(By.ID, "id_login_email").send_keys(EMAIL)
    # WebDriverWait(browser, 5).until(
    #     EC.element_to_be_clickable((By.ID, "verify"))
    # )
    # browser.find_element(By.ID, "id_login_email").send_keys(EMAIL)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sign-form__btn.button_with-loader"))
    ).click()
    # browser.find_element(By.CLASS_NAME, "sign-form__btn.button_with-loader").click()
    yield browser
    print("\n◄ quit browser..")
    time.sleep(3)
    browser.quit()
