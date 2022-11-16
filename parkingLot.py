from ABCcar import ABCcar
from Compact import Compact
from van import Van
from Suv import Suv
from datetime import datetime, time


class Parkinglot:
    def __init__(self, morningCurfew: int, eveningCurfew:int, maxVanSpots:int, maxCompactSpots:int, maxSuvSpots:int) -> None:
        """
        Constructor method
        """
        self.morningTime = time(morningCurfew,0,0,0)
        self.eveningTime = time(eveningCurfew,0,0,0)
        self.maxVanSpots = maxVanSpots
        self.maxCompactSpots = maxCompactSpots
        self.maxSuvSpots = maxSuvSpots
        self.__suvParkingSpots__ = {}
        self.__compactParkingSpots__ = {}
        self.__vanParkingSpots__ = {}

    @property
    def curfews(self) -> dict:
        """
        Returns this parking lot's opening and closing times.
        """
        return {"The parking lot opens at: ": self.morningTime.isoformat() , "The parking lot closes at:": self.eveningTime.isoformat}

    @property
    def parkingLot(self, id:int) -> dict:
        """
        Returns this parking lots used up spots.
        id specifies which type of car parking lot
        Id 1 for a Compact car,
        Id 2 for a Van
        Id 3 for a Suv
        """
        if(id == 1):
            return self.__compactParkingSpots__
        elif(id == 2):
            return self.__vanParkingSpots__
        elif(id == 1):
            self.__vanParkingSpots__
        else:
            raise Exception("Invalid Parking Lot ID")

    def Park(self, car:ABCcar) -> None:
        """
        Parks/reserves a car. This method calls a private __parkCar__ method, which determines in which parking lot will it go.
        """
        currentTime = datetime.time(datetime.now())
        if(currentTime > self.morningTime and currentTime < self.eveningTime):
            self.__parkCar__(car)
        else:
            raise Exception("Parking Lot Currently Closed.")

    def leave(self, ownerName:str) -> None:
        """
        removes a car from a parking lot.
        """
        car = self.__suvParkingSpots__.get(ownerName, None)
        if(car != None):
            del car
        else:      
            car = self.__compactParkingSpots__.get(ownerName, None)
            if(car != None):
                del car
            else:
                car = self.__vanParkingSpots__.get(ownerName, None)
                if(car != None):
                    del car
                else:
                    raise Exception("Car does not exist")
        self.calculateCost(car)

    def __parkCar__(self, car:ABCcar) -> None:
        """
        Determines which parking lot the object car will be stored in.
        """
        if(self.__suvParkingSpots__.__contains__(car.owner) or self.__compactParkingSpots__.__contains__(car.owner) or self.__vanParkingSpots__.__contains__(car.owner)):
            raise Exception("That car is parked already")
        else:
            if(isinstance(car, Suv)):
                if(len(self.__suvParkingSpots__) < self.maxSuvSpots):
                    self.__suvParkingSpots__[car.owner] = car
                else:
                    raise Exception("Not Enough Parking Spots")
            elif(isinstance(car, Compact)):
                if(len(self.__compactParkingSpots__) < self.maxCompactSpots):
                    self.__compactParkingSpots__[car.owner] = car
                else:
                    raise Exception("Not Enough Parking Spots")
                
            elif(isinstance(car, Van)):
                if(len(self.__vanParkingSpots__) < self.maxVanSpots):
                    self.__vanParkingSpots__[car.owner] = car
                else:
                    raise Exception("Not Enough Parking Spots")
            car.timeOfPark = datetime.time(datetime.now())
    
    def calculateCost(self, car:ABCcar) -> float:
        """
        Calculates cost of a car, based on the time it has spent there.
        """
        currentTime = datetime.time(datetime.now())
        t1 = datetime.combine(datetime.min, currentTime)
        t2 = datetime.combine(datetime.min, car.timeOfPark)
        delta = t2 - t1
        print(delta)