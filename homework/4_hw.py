# 1. создайте класс прямоугольника.
# a. атрибуты - прямоугольнику можно задать ширину и высоту
# b. методы - реализуйте 2 метода:
# i. расчет площади прямоугольника
# ii. расчет периметра прямоугольника
# c. создайте 3 объекта, рассчитайте площадь и периметр для каждого. Результаты выводить в консоль.

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

rec1 = Rectangle(3, 4)
rec2 = Rectangle(1, 10)
rec3 = Rectangle(7, 2.5)

print(rec1.square())
print(rec1.perimeter())

print(rec2.square())
print(rec2.perimeter())

print(rec3.square())
print(rec3.perimeter())


# 2. Создайте класс Math.
# a. Создайте два атрибута — a и b.
# b. Напишите методы
# i. addition — сложение,
# ii. multiplication — умножение,
# iii. division — деление,
# iv. subtraction — вычитание.
# При передаче в методы параметров a и b с ними нужно производить соответствующие действия и печатать ответ.

class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        print(self.a + self.b)

    def multiplication(self):
        print(self.a * self.b)

    def division(self):
        print(self.a / self.b)

    def subtraction(self):
        print(self.a - self.b)

Math(2, 8).addition()
Math(5, 4).multiplication()
Math(13, 2).division()
Math(25, 87).subtraction()


# 3. откройте страницу https://demoqa.com/text-box
# На странице присутствует сайдбар (меню слева)
# a. Создайте объекты для каждой кнопки 2-го уровня вложенности (“Text Box” и т.п.)
# Для этого опишите класс.
# Каждый объект должен содержать в себе:
# - текст кнопки (пример: “Text Box”)
# - тип - одинаковый для всех “Кнопка”
# - локатор - не заполнять, сделать по умолчанию пустой строкой
# Также на кнопку можно нажать - реализуйте метод. Метод возвращает текст “Клик по кнопке { ТЕКСТ КНОПКИ }”
# b. выведите текст для каждой кнопки
# c. вызовите “Клик” для каждой кнопки

class Sidebar:

    def __init__(self, text, type, loc):
        self.text = text
        self.type = type
        self.loc = loc

    def click(self):
        print(f'Клик по кнопке { self.text }')


text_box_button = Sidebar('Text Box', 'Кнопка', '')
check_box_button = Sidebar('Check Box', 'Кнопка', '')
radio_button = Sidebar('Radio Button', 'Кнопка', '')
web_tables_button = Sidebar('Web Tables', 'Кнопка', '')
buttons_button = Sidebar('Buttons', 'Кнопка', '')
links_button = Sidebar('Links', 'Кнопка', '')
broken_links_button = Sidebar('Broken Links - Images', 'Кнопка', '')
up_and_download_button = Sidebar('Upload and Download', 'Кнопка', '')
dyn_prop_button = Sidebar('Dynamic Properties', 'Кнопка', '')


print(text_box_button.text)
print(check_box_button.text)
print(radio_button.text)
print(web_tables_button.text)
print(buttons_button.text)
print(links_button.text)
print(broken_links_button.text)
print(up_and_download_button.text)
print(dyn_prop_button.text)


text_box_button.click()
check_box_button.click()
radio_button.click()
web_tables_button.click()
buttons_button.click()
links_button.click()
broken_links_button.click()
up_and_download_button.click()
dyn_prop_button.click()
