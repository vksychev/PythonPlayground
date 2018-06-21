import csv
import os


class CarBase:
    def __init__(self, car_type, brand, photo_file_name, carrying):
        self.car_type = car_type
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        r = os.path.splitext(self.photo_file_name)
        return r[1]
    def print_type(self):
        print(self.car_type)

class Car(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, body_whl):
        super().__init__(car_type, brand, photo_file_name, carrying)
        whl = str(body_whl).split('x')
        self.body_width = float(whl[0])
        self.body_height = float(whl[1])
        self.body_length = float(whl[2])

    def get_body_volume(self):
        return self.body_width * self.body_height * self.body_length


class SpecMachine(CarBase):
    def __init__(self, car_type, brand, photo_file_name, carrying, extra):
        super().__init__(car_type, brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')

        next(reader)

        for car_attributes in reader:
            try:
                car_type = car_attributes[0]
            except Exception:
                pass
            print(car_attributes)
            print(car_type)
            if car_type == 'car':
                try:
                    car_list.append(Car(car_attributes[0], car_attributes[1], car_attributes[3],
                                         car_attributes[5], int(car_attributes[2])))
                    print('get')
                except Exception:
                    pass
            elif car_type == "truck":

                r= car_attributes[4]
                if r == '':
                    r = '0x0x0'
                try:
                    car_list.append(Truck(car_attributes[0], car_attributes[1], car_attributes[3],
                                          car_attributes[5], r))
                    print('get')
                except Exception:
                    pass
            elif car_type == "spec_machine":
                try:
                    car_list.append(SpecMachine(car_attributes[0], car_attributes[1], car_attributes[3],
                                                car_attributes[5], car_attributes[6]))
                    print('get')
                except Exception:
                    pass
    return car_list

#get_car_list('coursera.csv')