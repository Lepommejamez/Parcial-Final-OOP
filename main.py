from User import User
from parkingLot import Parkinglot

parkinglot1 = Parkinglot(6, 18, 1, 1, 1)
user1 = User("Lepommejamez", "Password", parkinglot1)
user1.createCar("JimboMovil1",1)
user1.createCar("JimboMovil3",2)

user1.parkCar("JimboMovil1")

print(parkinglot1.parkingLot())
