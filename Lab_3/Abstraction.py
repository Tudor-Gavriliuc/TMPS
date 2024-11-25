from abc import ABC, abstractmethod

class CreateshowRoom(ABC):
    @abstractmethod
    def __init__(self):
        pass

class Prototype(ABC):
    @abstractmethod
    def clone(self):
        pass

class IVehicleBuilder(ABC):
    @abstractmethod
    def setWheel(self, wheel_type: str):
        pass

    @abstractmethod
    def setGrill(self, grill_type: str):
        pass

    @abstractmethod
    def setBumper(self, bumper_type: str):
        pass

    @abstractmethod
    def setRoof(self, roof_type: str):
        pass

    @abstractmethod
    def setDoor(self, door_type: str):
        pass

    @abstractmethod
    def setHeadLight(self, head_light_type: str):
        pass

    @abstractmethod
    def build(self):
        pass

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass
