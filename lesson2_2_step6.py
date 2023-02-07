from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    value_x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    print(value_x)

    result = calc(int(value_x))
    print(result)

    browser.execute_script("window.scrollBy(0, 100);")

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)

    option = browser.find_element(By.ID, "robotCheckbox")
    option.click()

    option2 = browser.find_element(By.ID, "robotsRule")
    option2.click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()