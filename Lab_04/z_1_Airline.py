# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a) список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;
import datetime

import self as self


class Airline:

    def __init__(self, destination, flight_id, plane_type, depart_date, depart_time, day_of_week):

        try:
            if depart_date < datetime.datetime.today().strftime("%Y-%m-%d"):
                raise Exception("Wrong data")
            else:
                self.__destination = destination  # Пункт назначения
                self.__flight_id = flight_id  # Номер рейса
                self.__plane_type = plane_type  # Тип самолета
                self.__depart_date = depart_date  # Дата вылета
                self.__depart_time = depart_time  # Время вылета
                self.__day_of_week = day_of_week  # День недели
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

    @staticmethod
    def findBydestination(airlineList, destination):
        print(f"Список рейсов до пункта назначения: {destination}")
        for i in airlineList:
            if i.getDestination() == destination:
                print(f"Номер рейса: {i.getFlight_id()}, Тип самолета: {i.getPlane_type()}, День и время вылета: "
                      f"{i.getDay_of_week()} {i.getDepart_date()} {i.getDepart_time()}")


airlineList = []
airline1 = Airline("New-York", "AA7594", "Boeing 777", "2022-10-25", "11:00", "Tuesday")
airline2 = Airline("London", "DF8845", "Airbus A320", "2022-11-10", "12:30", "Thursday")
airline3 = Airline("Paris", "GT8392", "Boeing 737", "2022-10-26", "14:00", "Wednesday")
airline4 = Airline("New-York", "AB9503", "Boeing 787 Dreamliner", "2022-11-7", "9:00", "Monday")
airline5 = Airline("Tokio", "RI9432", "Airbus A320", "2022-12-16", "22:30", "Friday")
airline6 = Airline("Washington", "NH1123", "Airbus A350", "2022-11-19", "17:00", "Saturday")
airline7 = Airline("Paris", "EW9731", "Boeing 787", "2022-10-23", "10:00", "Sunday")
airline8 = Airline("Barcelona", "MH0742", "Embraer E175", "2022-12-23", "20:30", "Friday")
airline9 = Airline("Warsaw", "SW2109", "Airbus A320", "2022-11-8", "15:00", "Tuesday")

airlineList.append(airline1)
airlineList.append(airline2)
airlineList.append(airline3)
airlineList.append(airline4)
airlineList.append(airline5)
airlineList.append(airline6)
airlineList.append(airline7)
airlineList.append(airline8)
airlineList.append(airline9)

Airline.findBydestination(airlineList, "New-York")
