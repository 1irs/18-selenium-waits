from time import time, sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, element_to_be_clickable, \
    invisibility_of_element
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
driver.get('https://angular.io/')
driver.maximize_window()

start_time = time()

search_box = driver.find_element(By.CSS_SELECTOR, "[placeholder=Search]")

search_box.send_keys('module\n')

# Обнаружены симптомы проблем синхронизации:
# 2. Тест проходит под дебаггером по шагам, а без дебаггера не проходит.
# 3. Элемент управления есть на странице, а скрипт его не находит.
# Скорее всего, предыдущая операция АСИНХРОННАЯ, требует синхронизации.
# При простом поиске элемента поможет неявная синхронизация (driver.implicitly_wait)

# sleep(1)

first_section_header = driver.find_element(By.CLASS_NAME, 'search-section-header')

actual = first_section_header.text

expected = 'API (43)'

assert expected == actual

print('✅ First test success')

search_box.clear()
search_box.send_keys('filter\n')


# Перед тем как искать элемент, нужно убедиться, что исчез старый результат поиска.

WebDriverWait(driver, timeout=2).until(invisibility_of_element(first_section_header))

# sleep(1)

first_section_header = driver.find_element(By.CLASS_NAME, 'search-section-header')

actual = first_section_header.text


expected = 'API (2)'

assert expected == actual

print('✅ Second test success')

end_time = time()

print('done in', end_time-start_time, 'seconds')

# sleep: 2.4 on average
# WebDriverWait: 1.8 on average.
