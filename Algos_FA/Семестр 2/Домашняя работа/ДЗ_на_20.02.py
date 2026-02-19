class Watch():
    def __init__(self, minutes):
        self.__minutes = minutes

    def to_hours(self):
        return self.__minutes / 60

    def to_seconds(self):
        return self.__minutes * 60

watch_1 = Watch(90)
print(watch_1.to_hours())
print(watch_1.to_seconds())
