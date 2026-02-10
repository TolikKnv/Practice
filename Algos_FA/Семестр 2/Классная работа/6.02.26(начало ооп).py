# Тема 2.1. Знакомство с классами.
# Атрибуты класса. Экземпляр класса. Методы экземпляра класса.
"""Задача 1.Создайте класс фрукты Fruit, хранящий информацию о форме фрукта,
его цвете и вкусе. Форму, цвет и вкус фрукта оформить в виде атрибутов класса.
Создать несколько объектов (экземпляров класса), изменить значения атрибутов
класса для конкретных объектов."""

"""Задача 2. Для класса фрукты Fruit, созданного в предыдущей задаче, создать
атрибуты класса Вес и Количество динамически (не в классе)"""


"""Задача 3. Для класса фрукты Fruit, созданного в задаче номер 1, создать:
- метод подсчета общего веса текущего экземпляра класса.
- метод сравнения общего веса данного экземпляра класса с любым другим.
- метод вывода полной информации об экземпляре класса в виде таблицы."""


"""Задача 6. Реализовать класс - простейший калькулятор, который в качестве методов реализует
арифметические операции.
Программа на вход принимает комбинацию чисел и операций,разделенных пробелами.
Например, 6 - 7 + 4. В качестве операций для работы с числами использовать сложение и вычитание."""


# 1
# class Fruit:
#     def __init__(self, shape, color, tasty):
#         self.shape = shape
#         self.color = color
#         self.tasty = tasty

#     def total_weight(self):
#         return self.weight * self.quantity

#     def chos(self, el):
#         if self.total_weight() > el.total_weight():
#             print("Первый элемент тяжелее")
#         elif self.total_weight() < el.total_weight():
#             print("Второй элемент тяжелее")
#         else:
#             print("Веса равны")

#     def tabl(self):
#         print(' --------------------------')
#         print(f'|{'shape':^12}| {self.shape:^10}  |')
#         print(' --------------------------')
#         print(f'|{'color':^12}| {self.color:^10}  |')
#         print(' --------------------------')
#         print(f'|{'tasty':^12}| {self.tasty:^10}  |')
#         print(' --------------------------')
#         print(f'|{'weight':^12}| {self.weight:^10}  |')
#         print(' --------------------------')
#         print(f'|{'quantity':^12}| {self.quantity:^10}  |')
#         print(' --------------------------')
#         print(f'|{'total_weight':^12}| {self.total_weight():^10}  |')


# apple = Fruit("round", "green", "7/10")
# orange = Fruit("round", "green", "7/10")
# apple.weight = 100
# apple.quantity = 150

# orange.weight = 100
# orange.quantity = 100


# q = apple.total_weight()

# print(apple.quantity, q)
# apple.chos(orange)
# apple.tabl()


"""Задача 4. Создать класс школьник, который хранит  информацию об ученике
(имя, возраст, класс, средний балл). Создать метод изменения среднего балла ученика
и метод получения (вывода на печать) среднего балла ученика. Вывести полную информацию об ученике"""

"""Задача 5. К предыдущей задаче №4 добавить методы изменения имени и возраста ученика."""


# 2
class School:
    def __init__(self, name, age, clas, av_bal):
        self.name = name
        self.age = age
        self.clas = clas
        self.av_bal = av_bal
    def change_av(self):
        a = float(input())
        self.av_bal = a
    def change_name(self):
        a = float(input())
        self.name = a
    def change_age(self):
        a = float(input())
        self.age = a
    def pr_av_bal(self):
        return self.av_bal
    def __repr__(self):
        return f':) {self.name, self.age, self.clas, self.av_bal}'
    def __str__(self):
        return f'{self.name, self.age, self.clas, self.av_bal}'

q = School('qwe', 15, 9, 4.67)
# q.change_av()
# q.pr_av_bal()
print(q)
# print(q.__repr__())

