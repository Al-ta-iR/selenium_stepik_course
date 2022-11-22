# 1. Копируем фикстуру браузера из пред. шага
# 2.Создаем фикстуру параметриз('переменная', ["урлы"])
# 3. Создаем класс, название с Test..
# 4. Создаем функцию, название с test...(селф, браузер, переменная с шага 2)
# 5. Создаем переменную = str(math.log(int(time.time())))
# 6. link = переменная 2 шага; браузер гет(link)
# 7. Добавляем ожидание
# 8. Находим поле для ввода ответа и send_keys туда переменную с 5 шага (можно и сразу ввести, не создавая переменную)
# 9. Находим кнопку Отправить через  WebDriverWait...   EC.element_to_be_clickable (так как она не сразу доступна) и нажимаем на нее ( либо после шага 8 - добавьте ожидание)
# 10. Создаем переменную селектора правильности ответа: просто откройте любой урл из списка, введите что угодно в поле и нажмите копку (неважно что неправильный ответ - селектор тот же), после ищите его в коде
# 11. Ассерт 'правильный ответ' in переменная селектора правильности. text
# 12. В конце иф нейм = мейн:
#       пайтест.мейн()

# https://stepik.org


#     открыть страницу 
#     авторизоваться на странице со своим логином и паролем (см. предыдущий шаг)
#     ввести правильный ответ 
#     нажать кнопку "Отправить" 
#     дождаться фидбека о том, что ответ правильный 
#     проверить, что текст в опциональном фидбеке полностью совпадает с "Correct!"
# Опциональный фидбек — это текст в черном поле, как показано на скриншоте: (correct)

# Правильным ответом на задачу в заданных шагах является число:
# import time
# import math
# answer = math.log(int(time.time()))

# Используйте маркировку pytest для параметризации и передайте в тест список ссылок в качестве параметров:
# links = [
#     'https://stepik.org/lesson/236895/step/1',
#     'https://stepik.org/lesson/236896/step/1',
#     'https://stepik.org/lesson/236897/step/1',
#     'https://stepik.org/lesson/236898/step/1',
#     'https://stepik.org/lesson/236899/step/1',
#     'https://stepik.org/lesson/236903/step/1',
#     'https://stepik.org/lesson/236904/step/1',
#     'https://stepik.org/lesson/236905/step/1',
# ]

# Используйте осмысленное сообщение об ошибке в проверке текста, а также настройте нужные ожидания, чтобы тесты работали стабильно. 

# В упавших тестах найдите кусочки послания. Тест должен падать, если текст в опциональном фидбеке не совпадает со строкой "Correct!" Соберите кусочки текста в одно предложение и отправьте в качестве ответа на это задание. 

# Важно! Чтобы пройти это задание, дополнительно убедитесь в том, что у вас установлено правильное локальное время (https://time.is/ru/). Ответ для каждой задачи нужно пересчитывать отдельно, иначе они устаревают. 

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

@pytest.fixture(scope="module")
def login_func(browser):
    link_url = 'https://stepik.org/'
    browser.get(link_url)

    # WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), '100'))
    browser.find_element(By.ID, "ember224").click()


# @pytest.mark.parametrize('language', ["ru", "en-gb"])
def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/ru/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")

