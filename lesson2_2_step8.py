from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import os

try:
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.NAME, 'firstname')
    input1.send_keys("firstname")
    input2 = browser.find_element(By.NAME, 'lastname')
    input2.send_keys("lastname")
    input3 = browser.find_element(By.NAME, 'email')
    input3.send_keys("email")

    file_path = r'C:\Users\Stanislav\Desktop\B3\selenium_course\text.txt'
    element = browser.find_element(By.XPATH, '//*[@id="file"]')
    element.send_keys(file_path)

    button = browser.find_element(By.CLASS_NAME, "btn")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()