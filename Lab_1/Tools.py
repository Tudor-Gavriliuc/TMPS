from Abstraction import CreateshowRoom, Prototype, IVehicleBuilder
import copy

class VehiclePrototype(Prototype):
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def clone(self):
        return copy.deepcopy(self.vehicle)

class Vehicle:
    def __init__(self):
        self.wheel = None
        self.grill = None
        self.bumper = None
        self.window = None
        self.roof = None
        self.door = None
        self.head_light = None

class VehicleBuilder(IVehicleBuilder):
    def __init__(self):
        self.vehicle = Vehicle()

    def setWheel(self, wheel_type: str):
        self.vehicle.wheel = wheel_type
        return self

    def setGrill(self, grill_type: str):
        self.vehicle.grill = grill_type
        return self

    def setBumper(self, bumper_type: str):
        self.vehicle.bumper = bumper_type
        return self

    def setWindow(self, window_type: str):
        self.vehicle.window = window_type
        return self

    def setRoof(self, roof_type: str):
        self.vehicle.roof = roof_type
        return self

    def setDoor(self, door_type: str):
        self.vehicle.door = door_type
        return self

    def setHeadLight(self, head_light_type: str):
        self.vehicle.head_light = head_light_type
        return self

    def build(self):
        return self.vehicle

class UseDefaultComplectation:
    def __init__(self, carBuilder: IVehicleBuilder):
        self.car = carBuilder

    def fullComplectation(self):
        return (
            self.car
            .setWheel("Alloy")
            .setGrill("Chrome")
            .setBumper("Sport")
            .setRoof("Sunroof")
            .setDoor("Gull-wing")
            .setHeadLight("LED")
            .build()
        )

class showRoom(CreateshowRoom):
    instance = None

    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, address):
        if not hasattr(self, 'initialized'):
            self.address = address
            self.initialized = True