from time import sleep, time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element, element_to_be_clickable
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get('https://dineshvelhal.github.io/testautomation-playground/expected_conditions.html')
driver.maximize_window()

start_time = time()

visibility_trigger = driver.find_element(By.ID, 'visibility_trigger')
visibility_trigger.click()

invisible_button = driver.find_element(By.ID, 'visibility_target')

# Т. к. после клика по кнопке Trigger, кнопка Click Me появляется не мгновенно, а с задержкой
# то нам нужно вставить явное ожидание.

# ❌ sleep — нельзя! Плохая практика!
# ❌ sleep(5)

# An Expectation for checking an element is visible and enabled such that you can click it.
# Ожидаем событие, когда элемент стал видимым и кликабельным.
WebDriverWait(driver, timeout=5).until(element_to_be_clickable(invisible_button))
invisible_button.click()

popover = driver.find_element(By.CLASS_NAME, 'arrow')

assert popover


end_time = time()
print('✅ Success! Done in', end_time-start_time, 'seconds.')
