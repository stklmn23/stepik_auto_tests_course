from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    value_x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    print(value_x)

    result = calc(int(value_x))
    print(result)

    input = browser.find_element(By.ID, 'answer')
    input.send_keys(result)

    button2 = browser.find_element(By.CLASS_NAME, "btn")
    button2.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()