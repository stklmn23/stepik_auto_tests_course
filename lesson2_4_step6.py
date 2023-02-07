from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time
import math

def calc(x):
  return math.log(abs(12*math.sin(x)))

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    current_price = browser.find_element(By.XPATH, '//*[@id="input_value"]').text

    while current_price != '$100':
        print(current_price)
        time.sleep(0.5)
        current_price = browser.find_element(By.XPATH, '//*[@id="price"]').text
    else:
        button = browser.find_element(By.XPATH, '//*[@id="book"]')
        button.click()

    value_x = browser.find_element(By.XPATH, '//*[@id="input_value"]').text
    print(value_x)

    result = calc(int(value_x))
    print(result)

    input2 = browser.find_element(By.ID, 'answer')
    input2.send_keys(result)

    button1 = browser.find_element(By.XPATH, '//*[@id="solve"]')
    button1.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()