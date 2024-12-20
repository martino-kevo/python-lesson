class CarNotFoundException(Exception):
    pass


class NumberPlateNotFoundException(Exception):
    pass


class AdminException(Exception):
    pass


class NameNotFoundException(Exception):
    pass


class MySecurity:

    # constructor
    def __init__(self):
        self.security_database1 = {}
        self.security_database2 = {}

    # method
    def add_details(self, driver, driver_sex, driver_age, owner_of_car, car, number_plate):

        if self.security_database1 == {}:
            self.security_database1 = {car: number_plate}

            self.security_database2 = {self.security_database1[car]: {
                "driver's name": driver,
                "driver's sex": driver_sex,
                "driver's age": driver_age,
                "owner of car": owner_of_car
            }}
        else:
            self.security_database1[car] = number_plate

            self.security_database2[self.security_database1[car]] = {
                "driver's name": driver,
                "driver's sex": driver_sex,
                "driver's age": driver_age,
                "owner of car": owner_of_car
            }

    # method
    def get_details(self, car, number_plate):

        if car in self.security_database1.keys():

            if number_plate in self.security_database2.keys():
                print(
                    f"\n--------- Details For {car} ({number_plate}) -----------")

                print(f"\nDriver's name ---- {self.security_database2[number_plate]["driver's name"]}\nDriver's sex ---- {self.security_database2[number_plate]["driver's sex"]}\nDriver's age ---- {
                      self.security_database2[number_plate]["driver's age"]}\nOwner of car ---- {self.security_database2[number_plate]["owner of car"]}")
            else:
                raise NumberPlateNotFoundException(
                    f"\nThe number plate '{number_plate}' doesn't match any car")
        else:
            raise CarNotFoundException(f"\nThe car '{car}' doesn't exist")

    # method
    def delete_details(self, admin, car, number_plate):

        if admin == True:
            if car in self.security_database1.keys():
                if number_plate in self.security_database2.keys():
                    for c in self.security_database1.keys():
                        if self.security_database1[c] == number_plate:

                            del self.security_database1[c]

                    del self.security_database2[number_plate]

                    success_message = f"\n{
                        car} with all details has been successfully deleted 🤗"

                    print(success_message)
                else:
                    raise NumberPlateNotFoundException(
                        f"\nNumber plate '{number_plate}' doesn't exist")
            else:
                raise CarNotFoundException(f"\n{car} was not found")
        else:
            raise AdminException(
                "\nYou have to be the Admin to delete details")
