class Car:

    def __init__(self, mark, model, year):
        self.mark = mark
        self.model = model
        self.year = year

    def __str__(self):
        return f'Автомобиль: {self.mark}, {self.model}, {self.year}'


class Passenger(Car):

    def __init__(self, name, model, year, car_body):
        super().__init__(name, model, year)
        self.car_body = car_body

    def __str__(self):
        a = Car(self.mark, self.model, self.year)
        # print(a)
        return f'{a}, {self.car_body}'
        # return f'{super().__str__()}'


print()
a = Car('Лада', 'Гранта', 2012)
print(a)
a1 = Passenger('BMW', 'm5', 2026, 'Седан')
print(a1)