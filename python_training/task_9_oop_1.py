# Создайте класс Input, принимающий 1 аргумент при инициализации (Loc)
# Создайте объект search (экземпляр класса Input)
# Выведите в консоль значение аргумента Loc объекта search

class Input:
    def __init__(self, loc):
        self.loc = loc

search = Input('input#search')

print(search.loc)


# Добавьте к классу Input атрибут объекта text
# В этом же файле создайте: классы Button, Title, Link
# Для каждого класса пропишите атрибуты text и loc
# Создайте каждому из 4 классов объекты с любыми данными
# Выведите в консоль text и loc каждого класса

from task_9_checks import Checks

class Input(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

enter_email = Input('Электронная почта', 'input#email')

print(enter_email.text, enter_email.loc)


class Button(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

main_page = Button('Главная страница', 'button#main')

print(main_page.text, main_page.loc)


class Title(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

item_title = Title('Наименование', 'title#item')

print(item_title.text, item_title.loc)


class Link(Checks):

    def __init__(self, text, loc):
        super().__init__(loc)
        self.text = text
        self.loc = loc

source_link = Link('Ссылка на источник', 'link#source')

print(source_link.text, source_link.loc)

print(enter_email.check_text())
print(main_page.check_text())
print(item_title.check_text())
print(source_link.check_text())