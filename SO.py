# Single Responsibility Principle (SRP)
# Open/Closed Principle (OCP)

from abc import ABC, abstractmethod

class House:
    def __init__(self, surface, rooms):
        self.surface = surface
        self.rooms = rooms

class returnPrice(ABC):
    @abstractmethod
    def getPrice(self, house: House):
        pass

class ChisinauHousePrice(returnPrice):
    def getPrice(self, house: House):
        return house.surface * 1000

class BaltiHousePrice(returnPrice):
    def getPrice(self, house: House):
        return house.surface * 500

class numberOfRooms:
    def getRoomsNum(self, house: House):
        print("You have", house.rooms, "rooms")

building = House(65, 3)

building_chisinau = ChisinauHousePrice()
building_balti = BaltiHousePrice()

building_chisinau_price = building_chisinau.getPrice(building)
building_balti_price = building_balti.getPrice(building)

rooms = numberOfRooms()
nr_of_rooms = rooms.getRoomsNum(building)


print("Chisinau", building_chisinau_price)
print("Balti", building_balti_price)