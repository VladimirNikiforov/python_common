import os


class CarBase:
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)


class Car(CarBase):
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        self.car_type = "car"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.passenger_seats_count = passenger_seats_count


class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl):
        self.car_type = "truck"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        if body_whl == "":
            self.body_length, self.body_width, self.body_height = 0, 0, 0
        else:
            bwhl = body_whl.split('x')
            self.body_length, self.body_width, self.body_height = float(bwhl[0]), float(bwhl[1]), float(bwhl[2])

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra):
        self.car_type = "spec_machine"
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = carrying
        self.extra = extra


def get_car_list(csv_filename):
    car_list = []

    import csv

    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            print(row)
            try:
                if row[0] == "car":
                    car_list.append(Car(row[1], row[3], float(row[5]), int(row[2])))
                elif row[0] == "truck":
                    car_list.append(Truck(row[1], row[3], float(row[5]), row[4]))
                elif row[0] == "spec_machine":
                    car_list.append(SpecMachine(row[1], row[3], float(row[5]), row[6]))
            except:
                pass
    return car_list

# print(get_car_list("coursera_week3_cars.csv"))
