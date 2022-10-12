# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a) список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;
import datetime


class Airline:
    def __init__(self, destination, flight_id, plane_type, depart_date, depart_time, day_of_week):
        try:
            if depart_date < datetime.datetime.today().strftime("%d.%m.%Y"):
                raise Exception("Missing data")
            else:
                self.destination = destination
                self.flight_id = flight_id
                self.plane_type = plane_type
                self.depart_date = depart_date
                self.depart_time = depart_time
                self.day_of_week = day_of_week
        except:
            print("Your departure date is incorrect")


# import datetime
# a = datetime.datetime.today().strftime("%d.%m.%Y")
# print(a)
# print(type(a))