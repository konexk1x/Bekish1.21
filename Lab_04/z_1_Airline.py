# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a) список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;
import datetime


class Airline:
    def __init__(self, destination, flight_id, plane_type, depart_date, depart_time, day_of_week):

        try:
            if depart_date < datetime.datetime.today().strftime("%Y-%m-%d"):
                raise Exception("Wrong data")
            else:
                self.__destination = destination
                self.__flight_id = flight_id
                self.__plane_type = plane_type
                self.__depart_date = depart_date
                self.__depart_time = depart_time
                self.__day_of_week = day_of_week
        except:
            print("Your departure date is incorrect")

    def getDestination(self):
        return self.__destination

    def getFlight_id(self):
        return self.__flight_id

    def getPlane_type(self):
        return self.__plane_type

    def getDepart_date(self):
        try:
            if self.__depart_date < datetime.datetime.today().strftime("%Y-%m-%d"):
                raise Exception("Wrong data")
            else:
                return self.__depart_date
        except:
            print("Your departure date is incorrect")
            return

    def getDepart_time(self):
        return self.__depart_time

    def getDay_of_week(self):
        return self.__day_of_week

    def setDestination(self, destination):
        self.__destination = destination

    def setFlight_id(self, flight_id):
        self.__flight_id = flight_id

    def setPlane_type(self, plane_type):
        self.__plane_type = plane_type

    def setDepart_date(self, depart_date):
        if self.__depart_date < datetime.datetime.today().strftime("%Y-%m-%d"):
            raise Exception("Wrong data")
            return
        self.__depart_date = depart_date
        return

    def __str__(self):
        return f"{self.__destination}, {self.__flight_id}, {self.__plane_type}, {self.__depart_date}, {self.__depart_time}, {self.__day_of_week}"


airlineList = []
airline1 = Airline("New-York", "BD-9934", "Boeing 787", "2022-10-14", "17:00", "Wednesday")
airline2 = Airline("New-York", "BD-9934", "Boeing 787", "2022-10-16", "17:00", "Wednesday")

airlineList.append(airline1)
airlineList.append(airline2)

print(f"реализация __str__: {airline1}")
