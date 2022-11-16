from parkingLot import Parkinglot
from ABCcar import ABCcar
from Compact import Compact
from van import Van
from Suv import Suv
from datetime import datetime, time
import typing

class User:
    def __init__(self, userName: str, Password:str, parkinglot:Parkinglot) -> None:
        """
        Constructor method
        """
        self.userName = userName
        self.Password = Password
        self.parkingLot = parkinglot
        self.__cars__ = {}
    
    @property
    def cars(self) -> dict:
        """
        returns the dictionary of cars this user has
        """
        return self.__cars__

    def createCar(self, carName:str, type:int) -> ABCcar:
        """
        Creates a new car. 
        Id 1 for a Compact car,
        Id 2 for a Van
        Id 3 for a Suv
        
        """
        if(id == 1):
            temp = Compact(carName, self)
        elif(id == 2):
            temp = Van(carName, self)
        elif(id == 3):
            temp = Suv(carName, self)
        
        self.cars[carName] = temp
        return temp
    
    def __getCar__(self, carName:str) -> ABCcar:
        """
        Finds a car in this user's list of cars
        """
        if(self.cars.get(carName, None)):
            return self.cars[carName]
        else:
            return None
    
    def parkCar(self, carName:str) -> None:
        """
        Parks a car in this user's assigned parking lot.
        """
        temp = self.__getCar__(carName)
        if(temp  != None):
            print("Car parked.")
            self.parkingLot.Park(temp)
        else:
            raise Exception("Car does not exist")

    def reserveSpot(self, carName:str):
        """
        reserves a spot for a car in this user's assigned parking lot.
        """
        temp = self.__getCar__(carName)
        if(temp  != None):
            print("Spot reserved.")
            self.parkingLot.Park(temp)
        else:
            raise Exception("Car does not exist")

