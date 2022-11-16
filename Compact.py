from ABCcar import ABCcar
from datetime import datetime, time

class Compact(ABCcar):
    def __init__(self, carName: str, owner:"User") -> None:
        """
        Constructor method
        """
        self.owner = owner
        self.name = carName
        self.timeOfPark = time(0,0,0,0)
        