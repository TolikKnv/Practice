import math


class Triangle:
    def __init__(self, side_1, side_2, side_3):
        if (
            side_1 + side_2 < side_3
            or side_1 + side_3 < side_2
            or side_3 + side_2 < side_1
        ):
            raise ValueError("Таких сторон не может быть")
        self.side_1 = side_1
        self.side_2 = side_2
        self.side_3 = side_3

    def S(self):
        p = sum([self.side_1, self.side_2, self.side_3])
        return math.sqrt(p * (p - self.side_1) * (p - self.side_2) * (p - self.side_3))

    def P(self):
        return sum([self.side_1, self.side_2, self.side_3])


# Tri = Triangle(2,3,4)
# print(Tri.S())
# print(Tri.P())


class Salary:
    def __init__(
        self,
        second_name,
        first_name,
        last_name,
        year,
        amount_in_rub,
        buff_percent,
        worked_days,
        days,
        count_sum=None,
        not_count_sum=None,
    ):
        self.second_name = second_name
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.amount_in_rub = amount_in_rub
        self.buff_percent = buff_percent
        self.worked_days = worked_days
        self.days = days
        # self.count_sum=None

    def total_amount(self):
        return (self.amount_in_rub / self.days * self.worked_days) * (1 + self.buff_percent / 100)


    def uder_amount(self):
        self.not_count_sum = self.total_amount() * 0.13
        return self.total_amount() * 0.13

    def con_amount(self):
        self.count_sum = self.total_amount() - self.uder_amount()
        return self.total_amount() - self.uder_amount()

    def _count_years(self, con_year):
        return con_year - self.year

    def __str__(self):
        return f'{self.not_count_sum}, {self.count_sum}'


# person = Salary("a", "b", "c", 2009, 49000, 5, 20, 20)
# print(person.total_amount())
# print(person.uder_amount())
# print(person.con_amount())
# print(person._count_years(2026))
# print(person)


class Uravnenie():
    def __init__(self, urav):
        self.urav = urav

    