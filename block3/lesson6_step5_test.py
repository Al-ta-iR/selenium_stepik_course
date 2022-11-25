import pytest
import math
import time
import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

env_path = os.path.join('secrets.env')
load_dotenv(env_path)
EMAIL = os.getenv("EMAIL")
PASSWORD = os.getenv("PASSWORD")

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    'https://stepik.org/lesson/236897/step/1',
    'https://stepik.org/lesson/236898/step/1',
    'https://stepik.org/lesson/236899/step/1',
    'https://stepik.org/lesson/236903/step/1',
    'https://stepik.org/lesson/236904/step/1',
    'https://stepik.org/lesson/236905/step/1',
]


@pytest.fixture(autouse=True, scope="module")
def login_func(browser):
    link_url = 'https://stepik.org/catalog?auth=login'
    browser.get(link_url)
    WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.ID, "id_login_email"))
    ).send_keys(EMAIL)
    browser.find_element(By.ID, "id_login_password").send_keys(PASSWORD)
    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "sign-form__btn.button_with-loader"))
    ).click()
    time.sleep(3)


@pytest.mark.parametrize('link', links)
def test_guest_should_see_login_link(browser, link):
    browser.get(link)
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "again-btn.white"))
        ).click()
    except:
        pass
    math_value = str(math.log(int(time.time())))
    WebDriverWait(browser, 15).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea"))
    ).send_keys(math_value)

    WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))
    ).click()
    answer = WebDriverWait(browser, 5).until(
        EC.visibility_of_element_located((By.CLASS_NAME, "smart-hints__hint"))
    ).text
    assert answer == 'Correct!', f'Ответ должен быть "Correct", получен {answer}'

# python -m pytest -s -v block3/lesson6_step5_test.py
