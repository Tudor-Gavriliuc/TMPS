import os

from Abstraction import CreateshowRoom, Prototype, IVehicleBuilder, Iterator
import copy

# Prototype Pattern
class VehiclePrototype(Prototype):
    def __init__(self, vehicle):
        self.vehicle = vehicle

    def clone(self):
        return copy.deepcopy(self.vehicle)

# Vehicle Class
class Vehicle:
    def __init__(self):
        self.wheel = None
        self.grill = None
        self.bumper = None
        self.window = None
        self.roof = None
        self.door = None
        self.head_light = None

    def describe(self):
        return (f"Wheel: {self.wheel or 'Not Set'}, Grill: {self.grill or 'Not Set'}, "
                f"Bumper: {self.bumper or 'Not Set'}, Window: {self.window or 'Not Set'}, "
                f"Roof: {self.roof or 'Not Set'}, Door: {self.door or 'Not Set'}, "
                f"Head Light: {self.head_light or 'Not Set'}")

# Builder Pattern
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

# Structural Patterns

# Decorator Pattern
class VehicleDecorator:
    def __init__(self, vehicle):
        self._vehicle = vehicle

    def describe(self):
        return self._vehicle.describe()


class SportPackage(VehicleDecorator):
    def describe(self):
        return self._vehicle.describe() + ", with Sport Package"


class LuxuryPackage(VehicleDecorator):
    def describe(self):
        return self._vehicle.describe() + ", with Luxury Package"

# Facade Pattern
class VehicleFacade:
    def __init__(self):
        self.builder = VehicleBuilder()

    def configure_sport_car(self):
        return (
            self.builder
            .setWheel("Alloy")
            .setGrill("Chrome")
            .setBumper("Sport")
            .setRoof("Sunroof")
            .setDoor("Gull-wing")
            .setHeadLight("LED")
            .build()
        )

    def configure_basic_car(self):
        return (
            self.builder
            .setWheel("Steel")
            .setGrill("Plastic")
            .setBumper("Standard")
            .setRoof("Hardtop")
            .setDoor("Standard")
            .setHeadLight("Halogen")
            .build()
        )

# Composite Pattern
class Component:
    def __init__(self, name):
        self.name = name

    def display(self, depth=0):
        print("  " * depth + self.name)


class CompositeComponent(Component):
    def __init__(self, name):
        super().__init__(name)
        self.children = []

    def add(self, component):
        self.children.append(component)

    def remove(self, component):
        self.children.remove(component)

    def display(self, depth=0):
        print("  " * depth + self.name)
        for child in self.children:
            child.display(depth + 1)

# Singleton Pattern
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

# Iterator Implementation for Files
class FileIterator(Iterator):
    def __init__(self, file_list):
        self.file_list = file_list
        self.current_index = 0

    def has_next(self):
        return self.current_index < len(self.file_list)

    def next(self):
        if not self.has_next():
            raise StopIteration
        file = self.file_list[self.current_index]
        self.current_index += 1
        return file


class FileManager:
    def __init__(self, directory="configurations"):
        self.files = []
        self.directory = directory
        os.makedirs(self.directory, exist_ok=True)

    def add_file(self, file):
        self.files.append(file)

    def save_configuration(self, filename, configuration):
        path = os.path.join(self.directory, filename)
        with open(path, "w") as file:
            file.write(configuration)
        self.add_file(filename)

    def get_file_iterator(self):
        return FileIterator(self.files)
