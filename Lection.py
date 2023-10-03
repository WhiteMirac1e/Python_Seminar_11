# # Создайте класс Моя Строка, где:
# # будут доступны все возможности str
# # дополнительно хранятся имя автора строки и время создания
# # (time.time)
from datetime import datetime


class Mystring(str):
    def __new__(cls, value, author):
        instance = super().__new__(cls, value)
        instance.author = author
        instance.value = value
        instance.create_time = datetime.now()
        return instance
    
    def __str__(self):
        return f"{self.value} (Автор: {self.author}, Время создания: {self.create_time})"
    
    def __repl__(self):
        return f'{self.author}'

a = Mystring("Это моя строка", 'Ivan')
my_string = Mystring("Мама мыла раму", "Маршак")

print(a)
print(repr(my_string))
# print(a.author)
# print(a.create_time)

# Создайте класс Архив, который хранит пару свойств.
# Например, число и строку.
# При создании нового экземпляра класса, старые данные из ранее
# созданных экземпляров сохраняются в пару списков архивов
# list-архивы также являются свойствами экземпляра

# class Archive:
#     _instance = None

#     def __new__(cls, number, letter):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             cls._instance.arch = []

#         else:
#             cls._instance.arch.append((cls._instance.number, cls._instance.letter))
#         return cls._instance
    
#     def __init__(self, number, letter):
#         self.number = number
#         self.letter = letter
    
#     def __str__(self):
        # return f'{self.number} {self.letter} | {self.arch}'
    
#     def __repr__(self):
#         return f'{self.number} {self.letter}'
    
# a = Archive(1, "one")
# b = Archive(2, "two")

# print(b._instance)

# Дорабатываем класс прямоугольник из прошлого семинара.
# Добавьте возможность сложения и вычитания.
# При этом должен создаваться новый экземпляр
# прямоугольника.
# Складываем и вычитаем периметры, а не длинну и ширину.
# При вычитании не допускайте отрицательных значений.

# class Rectangle:
#     def __init__(self, len, width = None):
#         self.len = len
#         self.width = width if len else width
    
#     def perimeter(self):
#         return 2* self.len + 2 * self.width

#     def square(self):
#         return self.len * self.width
    
#     def __add__(self, other):
#         return Rectangle(self.data + other.data)

# r1 = Rectangle(7, 15)
# r2 = Rectangle(6, 14)

