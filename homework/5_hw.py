# Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”


from selenium import webdriver
from selenium.webdriver.common.by import By

def find_saucedemo_elements():

    driver = webdriver.Chrome() #./chromedriver
    driver.get("https://www.saucedemo.com/")

    text_field_username = driver.find_elements(By.CSS_SELECTOR, '#user-name')
    text_field_pass = driver.find_elements(By.CSS_SELECTOR, '#password')
    submit_button = driver.find_elements(By.CSS_SELECTOR, '#login-button')

    if text_field_username and text_field_pass and submit_button:
        print('Элементы найдены')
    else:
        print('Элементы не найдены')
