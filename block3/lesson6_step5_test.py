import pytest
import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

links = [
    'https://stepik.org/lesson/236895/step/1',
    'https://stepik.org/lesson/236896/step/1',
    # 'https://stepik.org/lesson/236897/step/1',
    # 'https://stepik.org/lesson/236898/step/1',
    # 'https://stepik.org/lesson/236899/step/1',
    # 'https://stepik.org/lesson/236903/step/1',
    # 'https://stepik.org/lesson/236904/step/1',
    # 'https://stepik.org/lesson/236905/step/1',
]


class TestStepikBlock3():
    @pytest.mark.parametrize('link', links)
    def test_guest_should_see_login_link(self, browser, link):
        browser.get(link)
        time.sleep(3)

        math_value = str(math.log(int(time.time())))
        browser.find_element(By.CLASS_NAME, "ember-text-area.ember-view.textarea.string-quiz__textarea").send_keys(math_value)
        time.sleep(3)
        browser.find_element(By.CLASS_NAME, "submit-submission").send_keys(math_value)
        browser.find_element(By.CLASS_NAME, "submit-submission").click()
        time.sleep(1)
        answer = browser.find_element(By.CLASS_NAME, "smart-hints__hint").text
        time.sleep(2)
        assert answer == 'Correct!', f'Ответ должен быть "Correct", получен {answer}'

# python -m pytest -s -v block3/lesson6_step5_test.py