# Classes are blueprints for creating objects. Think of it as just one architectural drawing for different buildings.
#
# The variable/properties in classes are the details of the object, while the methods are the things the object can do.

class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def moves(self):
        print("Moves along...")

    def get_make_model(self):
        print(f"I'm a {self.make} {self.model}")


my_car = Vehicle('Tesla', 'Model 3')
print()

# print(my_car.make)
# print(my_car.model)
my_car.get_make_model()
my_car.moves()

your_car = Vehicle('Cadillac', 'Escalade')
your_car.get_make_model()
your_car.moves()
print()

# Inheritance - Other classes (child classes/sub classes) inheriting what the parent class/super class has.


class Airplane(Vehicle):

    def __init__(self, make, model, faa_id):
        super().__init__(make, model)
        self.faa_id = faa_id

    def moves(self):
        print("Flies along...")


class Truck(Vehicle):

    def moves(self):
        print("Rombles along...")


class GolfCart(Vehicle):
    pass


cessna = Airplane('Cessna', 'SkyHawk', 'N-12345')
mack = Truck('Mack', 'Pinnacle')
golf_wagon = GolfCart('Yamaha', 'GC100')

cessna.get_make_model()
cessna.moves()
print()
mack.get_make_model()
mack.moves()
print()
golf_wagon.get_make_model()
golf_wagon.moves()
print('\n')

# Polymorphism - The ability to behave differently in response to the same input messages.

for v in (my_car, your_car, cessna, mack, golf_wagon):
    v.get_make_model()
    v.moves()
print()
