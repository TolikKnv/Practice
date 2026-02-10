# # __repr__ vs __str__
# class Book:
#     def __init__(self, title, author):
#         self.title = title
#         self.author = author

#     def __repr__(self):
#         return f"Book(title='{self.title}', author='{self.author}')"

#     def __str__(self):
#         return f"{self.title} — {self.author}"


# book = Book("1984", "George Orwell")


# print(book)
# print()
# print(repr(book))
# print()
# print([book], {book})


# Задача
"""Клиент обращается в банк с целью получения кредита.
При рассмотрении заявки банк анализирует финансовое положение клиента, учитывая его ежемесячный доход, общую стоимость
имущества и сумму запрашиваемого кредита.

Известно, что максимально допустимый размер кредита рассчитывается как сумма 12 ежемесячных доходов клиента и 50% от стоимости его имущества.
Если запрашиваемая сумма превышает этот лимит, банк автоматически уменьшает сумму кредита до максимально возможной.

Условия кредитования зависят от одобренной суммы:
- если сумма кредита не превышает 500 000 рублей — устанавливается процентная ставка 10% годовых, срок кредита составляет 3 года;
- если сумма кредита больше 500 000, но не превышает 1 000 000 рублей — ставка составляет 12% годовых, срок — 5 лет;
- если сумма превышает 1 000 000 рублей — ставка составляет 15% годовых, срок — 10 лет.

Итоговая сумма выплаты рассчитывается по формуле простых процентов:
итоговая выплата = сумма кредита * (1 + процентная ставка * срок).

Требуется определить максимально возможную сумму кредита для клиента, рассчитать условия кредитования (процентную ставку и срок),
а также вычислить итоговую сумму возврата.


Решить задачу в парадигме ООП.
"""


class Credit:

    def __init__(self, income, property, requested_loan):
        self.income = income
        self.property = property
        self.requested_loan = requested_loan

    def calculate_max_loan(self):
        return self.income * 12 + self.property * 0.5

    def calculate_loan_terms(self):

        max_loan = self.calculate_max_loan()

        if self.requested_loan > max_loan:
            print("Кредит не одобрен: запрошенная сумма превышает допустимый лимит.")
            print()
            print(f"Максимально допустимая сумма кредита: {max_loan:.2f} рублей.")
            print()
            self.requested_loan = max_loan

        if self.requested_loan <= 500000:
            rate = 0.10
            years = 3
        elif self.requested_loan <= 1000000:
            rate = 0.12
            years = 5
        else:
            rate = 0.15
            years = 10

        total_payment = self.requested_loan * (1 + rate * years)

        return {
            "Одобренная сумма": self.requested_loan,
            "Процентная ставка": rate * 100,
            "Срок (лет)": years,
            "Итоговая выплата": round(total_payment, 2),
        }

    # def __repr__(self):
    #     return (
    #         f"LoanApplicant(income={self.monthly_income}, "
    #         f"property={self.property_value}, "
    #         f"requested={self.requested_loan})"
    #     )


income = float(input("Введите ежемесячный доход клиента: "))
print()
property = float(input("Введите общую стоимость имущества клиента: "))
print()
requested_loan = float(input("Введите запрашиваемую сумму кредита: "))
print()

crediter = Credit(income, property, requested_loan)
stats = crediter.calculate_loan_terms()
for key, value in stats.items():
    print(f"{key}: {value}")
