class Car:
    def __init__(self, marka, model, god, probeg):
        self.marka = marka
        self.model = model
        self.god = god
        self.probeg = probeg
        self.__tip_topliva = "дизель"

    def to(self):
        if self.probeg > 10000:
            return True
        else:
            return False

    def __str__(self):
        try:
            self.__dict__.get('_Car__tip_topliva')
            return f"марка{self.marka} модель {self.model} год {self.god} пробег {self.probeg} тип топлива {self.__tip_topliva}"
        except AttributeError:
            print('qwrtygfdseghgfdfghdf')
            return f"марка{self.marka} модель {self.model} год {self.god} пробег {self.probeg} тип топлива: NO"

    @property
    def tip_topliva(self):
        return self.__tip_topliva

    @tip_topliva.setter
    def tip_topliva(self, new):
        self.__tip_topliva = new

    @tip_topliva.deleter
    def tip_topliva(self):
        del self.__tip_topliva

    # tip_topliva = property(__func1, __func2, __func3)


c1 = Car("лада", "гранта", 2020, 4000000)
print(c1)
print(c1.tip_topliva)
print(c1.__dict__)
c1.tip_topliva = 95
print(c1.__dict__)
print(c1.tip_topliva)
print(c1.__dict__)
del c1.tip_topliva
# print(c1.tip_topliva)
print(c1.__dict__)
print(c1)
