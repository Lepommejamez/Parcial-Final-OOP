from ABCcar import ABCcar
from datetime import datetime, time

class Suv(ABCcar):
    """
    Constructor method
    """
    def __init__(self, carName: str, owner:"User") -> None:
        self.owner = owner
        self.name = carName
        self.timeOfPark = time(0,0,0,0)