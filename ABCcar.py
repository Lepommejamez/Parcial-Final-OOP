from abc import ABC, abstractmethod
from datetime import datetime, time

class ABCcar(ABC):
    def __init__(self, carName: str, owner:"User") -> None:
        """
        Constructor method
        """
        self.owner = owner
        self.name = carName
        self.timeOfPark = datetime.time(datetime.now())

    def __repr__(self) -> str:
        return self.name + " car owned by " + self.owner.userName

    def getParkTime(self) -> time:
        """
        Returns time the car has been parked for.
        """
        if(self.timeOfPark == time.min):
            raise Exception("Car isn't parked")
        else:
            t1 = datetime.combine(datetime.min, self.timeOfPark)
            t2 = datetime.combine(datetime.min, datetime.time(datetime.now()))
            delta = t2 - t1
            return delta
