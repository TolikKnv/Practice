class Student:
    def __init__(self, name, surname, age):
        self.name = name
        self.surname = surname
        self.age = age

    def __str__(self):
        return f"{self.name} {self.surname}, возраст: {self.age}"

    def check_conditions(self):
        return self.age >= 18

    def get_name(self):
        return self.name

    def get_course(self):
        return None


class Bachelor(Student):
    def __init__(self, name, surname, age, course):
        super().__init__(name, surname, age)
        self.course = course

    def __str__(self):
        return f"{self.name} {self.surname}, возраст: {self.age}, курс: {self.course}"

    def get_course(self):
        return self.course


class Master(Student):
    def __init__(self, name, surname, age, specialization):
        super().__init__(name, surname, age)
        self.specialization = specialization

    def __str__(self):
        return f"{self.name} {self.surname}, возраст: {self.age}, специализация: {self.specialization}"


class Aspirant(Student):
    def __init__(self, name, surname, age, thesis):
        super().__init__(name, surname, age)
        self.thesis = thesis

    def __str__(self):
        return f"{self.name} {self.surname}, возраст: {self.age}, тема диссертации: {self.thesis}"


# список студентов
students = []

students.append(Bachelor("Иван", "Петров", 20, 2))
students.append(Master("Анна", "Смирнова", 24, "AI"))
students.append(Aspirant("Олег", "Иванов", 28, "Нейронные сети"))


print("Все студенты:")
for s in students:
    print(s)


# поиск по имени
name = input("\nВведите имя для поиска: ")

print("Результат поиска:")
for s in students:
    if s.get_name() == name:
        print(s)


# поиск по курсу
course = int(input("\nВведите курс для поиска: "))

print("Результат поиска:")
for s in students:
    if s.get_course() == course:
        print(s)