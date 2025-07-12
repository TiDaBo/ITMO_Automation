# Создайте функцию которая
# a. переходит на страницу https://www.saucedemo.com/
# b. находит элементы:
# i. текстовое поле username
# ii. текстовое поле password
# iii. кнопку submit
# c. Создайте условие, если элементы найдены - вывести в консоль текст “Элементы найдены”


from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome() #./chromedriver
driver.get("https://www.saucedemo.com/")


text_field_username = driver.find_element(By.CSS_SELECTOR, '#user-name')
if text_field_username is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


text_field_pass = driver.find_element(By.CSS_SELECTOR, '#password')
if text_field_pass is None:
    print('Элемент не найден')
else:
    print('Элемент найден')


submit_button = driver.find_element(By.CSS_SELECTOR, '*.submit-button')
if text_field_pass is None:
    print('Элемент не найден')
else:
    print('Элемент найден')