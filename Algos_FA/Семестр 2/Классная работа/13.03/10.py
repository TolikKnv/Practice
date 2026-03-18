from datetime import datetime


class Worker:
    ls_worker = []

    def __init__(self, name_company, qualification, name):
        self.name = name
        self.name_company = name_company
        self.qualification = qualification
        self.ls_worker.append(self)

    def __str__(self):
        return f"{}"


class House:
    ls_house = []
    def __init__(self, floors, entrances, district, workers, start_date, end_date):
        self.floors = floors
        self.entrances = entrances
        self.district = district
        self.workers = workers
        self.start_date = datetime.strptime(start_date, "%d.%m.%Y")
        self.end_date = datetime.strptime(end_date, "%d.%m.%Y")
        self.ls_house.append(self)


def how_much(year):
    for worker in Worker.ls_worker:
        count = 0
        for house in House.ls_house:
            if (worker.name in house.workers) and (house.start_date.year==year or house.send_date.year==year):
                count+=1
        print()