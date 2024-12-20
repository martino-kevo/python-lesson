from car_num_plate import MySecurity, CarNotFoundException, NumberPlateNotFoundException, AdminException

my_security = MySecurity()

my_security.add_details('John Paul', 'Male', 32,
                        'Peter Parker', 'Tesla G40', 'KRD 8145f')

my_security.add_details('Mariam Winter', 'Female', 26,
                        'Mariam Winter', 'Porche Y50', '4310 LOND')

my_security.add_details('Sam Alfred', 'Male', 45,
                        'Jonny Poff', 'Porche Y50', '5610 ICE')

try:
    my_security.get_details('Porche Y50', '4310 LOND')
except CarNotFoundException as error_message:
    print(error_message)
except NumberPlateNotFoundException as error_message:
    print(error_message)

try:
    my_security.delete_details(
        True, 'Porche Y50', '4310 LOND')
except AdminException as error_message:
    print(error_message)
except NumberPlateNotFoundException as error_message:
    print(error_message)
except CarNotFoundException as error_message:
    print(error_message)


try:
    my_security.get_details('Porche Y50', '4310 LOND')
except CarNotFoundException as error_message:
    print(error_message)
except NumberPlateNotFoundException as error_message:
    print(error_message)

try:
    my_security.get_details('Porche Y50', '5610 ICE')
except CarNotFoundException as error_message:
    print(error_message)
except NumberPlateNotFoundException as error_message:
    print(error_message)
