import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC




@pytest.fixture(scope="module")
def browser():
    print("\n► start browser for test..")
    browser = webdriver.Firefox()
    yield browser
    print("\n◄ quit browser..")
    browser.quit()
