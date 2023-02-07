from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math

try: 
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    value_1 = browser.find_element(By.ID, 'num1').text
    print(value_1)
    value_2 = browser.find_element(By.ID, 'num2').text
    print(value_2)
    result = int(value_1) + int(value_2)
    print(result)
    browser.find_element(By.CSS_SELECTOR, "[value='{}']".format(result)).click()

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(20)
    # закрываем браузер после всех манипуляций
    browser.quit()