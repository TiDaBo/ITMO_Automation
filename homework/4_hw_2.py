# Доп*
# 4. В отдельном файле напишите программу с классом Car.
# a. Создайте конструктор класса Car. Создайте атрибуты класса Car — color (цвет), type (тип), year (год).
# b. Напишите пять методов.
# i. Первый — запуск автомобиля, при его вызове выводится сообщение «Автомобиль заведен».
# ii. Второй — отключение автомобиля — выводит сообщение «Автомобиль заглушен».
# iii. Третий — присвоение автомобилю года выпуска.
# iv. Четвертый метод — присвоение автомобилю типа.
# v. Пятый — присвоение автомобилю цвета.

class Car:

    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print('Автомобиль заведен')

    def stop(self):
        print('Автомобиль заглушен')

    def year_of(self):
        print(f'Автомобиль { self.year } года выпуска')

    def car_type(self):
        print(f'Тип автомобиля: { self.type}')

    def car_color(self):
        print(f'Цвет автомобиля: {self.color}')


buick_8 = Car('синий', 'седан', 1954)

buick_8.start()
buick_8.stop()
buick_8.year_of()
buick_8.car_type()
buick_8.car_color()




