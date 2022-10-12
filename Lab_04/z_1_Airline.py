# Kласс Airline: Пункт назначения, Номер рейса, Тип самолета, Время вылета, Дни недели.
# Функции-члены реализуют запись и считывание полей (проверка корректности).
# Создать список объектов. Вывести:
# a) список рейсов для заданного пункта назначения;
# б) список рейсов для заданного дня недели;

class Airline:
    def __init__(self, destination, flight_id, plane_type, depart_time, day_of_week):
        self.destination = destination
        self.flight_id = flight_id
        self.plane_type = plane_type
        self.depart_time = depart_time
        self.day_of_week = day_of_week
