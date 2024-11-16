# Structural Design Patterns

## Author
**Gavriliuc Tudor**

---

## Introduction/Theory/Motivation

Structural design patterns are design principles used to simplify and structure complex software systems by establishing relationships between objects or components. These patterns focus on the composition of classes and objects to create flexible and efficient designs.

In this laboratory work, we implemented three structural design patterns—**Composite**, **Decorator**, and **Facade**—to enhance the functionality and organization of a vehicle showroom configuration application. These patterns help in achieving:

- **Scalability**: Easily manage hierarchical structures like vehicle categories.
- **Flexibility**: Dynamically extend functionality without modifying existing code.
- **Simplicity**: Provide a unified and simplified interface for complex processes.

---

## Implementation & Explanation

### 1. **Composite Pattern**

**Main Idea**: Represents a tree structure where individual components and their groups are treated uniformly.

**Motivation**: In this project, the Composite pattern is used to categorize vehicles (e.g., Sport Vehicles, Luxury Vehicles) and manage them hierarchically.

**Location**: `Tools.py`

**Code Snippet**:
```python
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
```
**Usage**:
- Manages hierarchical structures of vehicles.
- Allows adding, removing, and displaying categories like Sport Vehicles and Luxury Vehicles.

---

### 2. **Decorator Pattern**

**Main Idea**: Extends the functionality of an object dynamically without modifying its structure.

**Motivation**: In this project, the Decorator pattern allows dynamically adding additional features (e.g., Sport Package, Luxury Package) to vehicle configurations.

**Location**: `Tools.py`

**Code Snippet**:
```python
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
```

**Usage**:
- Dynamically enhances vehicle configurations during runtime.

---

### 3. **Facade Pattern**

**Main Idea**: Provides a simplified and unified interface for a set of complex subsystems.

**Motivation**: The Facade pattern abstracts the complexity of the vehicle-building process, allowing users to create default configurations or pre-configured vehicles easily.

**Location**: `Tools.py`

**Code Snippet**:
```python
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
```

**Usage**:
- Simplifies the vehicle configuration process for sport and basic cars.
- Provides a clean interface for users to interact with complex subsystems.

---

## Results/Screenshots/Conclusions

### Results
After implementing these patterns, the system:

1. **Manages vehicles hierarchically** using the Composite pattern.
2. **Dynamically extends vehicle configurations** with packages like Sport and Luxury using the Decorator pattern.
3. **Simplifies user interaction** for default configurations through the Facade pattern.

---

### Sample Execution

1. **Configure Manually and Add to Sport Vehicles**:
   ![Alt Text](https://github.com/Tudor-Gavriliuc/TMPS/blob/main/Lab_2/img/Screenshot%20(31).png?raw=true)
2. **Use Default Configuration and Categorize**:
  ![Alt Text](https://github.com/Tudor-Gavriliuc/TMPS/blob/main/Lab_2/img/Screenshot%20(32).png) 

3. **View All Vehicles in the Hierarchy**:
   ![Alt Text](https://github.com/Tudor-Gavriliuc/TMPS/blob/main/Lab_2/img/Screenshot%20(33).png) 

---

### Conclusions

In conclusion, I can say that the **Composite pattern** effectively streamlined the management of vehicle categories and their hierarchical structure, making it easier to organize and display vehicles. The **Decorator pattern** provided flexibility by enabling dynamic feature additions to vehicles without altering the underlying base code, enhancing the customization process. Lastly, the **Facade pattern** simplified user interaction by abstracting the complexity of vehicle configuration, providing a clean and user-friendly interface.

