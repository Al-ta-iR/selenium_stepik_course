import time
import unittest

from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By


link_1 = 'http://suninjuly.github.io/registration1.html'
link_2 = 'http://suninjuly.github.io/registration2.html'

class TestAbs(unittest.TestCase):
    def test_link_1(self):
        try:
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
            browser.get(link_1)

            # first_block
            # required=''

            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.first_class > .form-control.first')
            input1.send_keys("Data")
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.second_class > .form-control.second')
            input1.send_keys("Data")
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.third_class > .form-control.third')
            input1.send_keys("Data")
            # elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
            # for element in elements:
            #     element.send_keys("Data")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!", welcome_text)


        finally:
            time.sleep(2)
            browser.quit()

            
    def test_link_2(self):
        try:
            options = Options()
            options.binary_location = r'C:\Program Files\Mozilla Firefox\firefox.exe'
            browser = webdriver.Firefox(executable_path=r'C:\WebDrivers\geckodriver.exe', options=options)
            browser.get(link_2)

            # first_block
            # required=''

            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.first_class > .form-control.first')
            input1.send_keys("Data")
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.second_class > .form-control.second')
            input1.send_keys("Data")
            input1 = browser.find_element(By.CSS_SELECTOR, '.first_block > .form-group.third_class > .form-control.third')
            input1.send_keys("Data")
            # elements = browser.find_elements(By.CSS_SELECTOR, "input:required")
            # for element in elements:
            #     element.send_keys("Data")

            button = browser.find_element(By.CSS_SELECTOR, "button.btn")
            button.click()

            time.sleep(1)

            welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
            welcome_text = welcome_text_elt.text
            self.assertEqual("Congratulations! You have successfully registered!" == welcome_text)


        finally:
            time.sleep(2)
            browser.quit()

if __name__ == "__main__":
    unittest.main()
