### SOLID Principles Report  
**Author:** Gavriliuc Tudor, FAF - 221  

---

### **Objectives:**

- Get familiar with the SOLID principles.
- Choose a specific domain.
- Implement at least 2 SOLID principles for the chosen domain.

---

### **Domain: Real Estate Pricing System**

The domain selected for this report is a **Real Estate Pricing System**. The system calculates prices for houses based on their characteristics (such as surface area and number of rooms) and location (e.g., Chisinau and Balti). The implementation follows SOLID principles to ensure flexibility, maintainability, and scalability, allowing for easy extension of pricing strategies for additional locations in the future.

---

### **Used SOLID Principles:**

1. **Single Responsibility Principle (SRP)**  
   Each class is responsible for a single task, avoiding mixed responsibilities.

2. **Open/Closed Principle (OCP)**  
   The system can be extended with new pricing strategies without modifying existing code, allowing for better flexibility and scalability.

---

### **Implementation**

#### **Single Responsibility Principle (SRP)**  
The `House` class is responsible for storing the information about a house. The `returnPrice` interface defines how to calculate the price for different types of houses, while the specific implementations (`ChisinauHousePrice`, `BaltiHousePrice`) handle the logic for calculating prices for their respective regions. This division ensures that the responsibility of calculating prices is separated from the data structure.

#### **Open/Closed Principle (OCP)**  
The use of the `returnPrice` interface allows for the addition of new price calculation methods (e.g., for different cities) without modifying the existing classes. New implementations can be added as needed, maintaining the core logic intact.

---

### **Snippets from the Code:**

```python
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
rooms.getRoomsNum(building)

print("Chisinau Price:", building_chisinau_price)
print("Balti Price:", building_balti_price)
```

### **Conclusions**

- The **Single Responsibility Principle (SRP)** was effectively implemented by separating the responsibilities of the `House` class, which stores house information, and the `returnPrice` interface, which defines how to calculate prices for different locations. This separation of concerns allows for easier modifications and enhancements to the pricing logic without affecting the core data structure.

- The **Open/Closed Principle (OCP)** was demonstrated through the use of the `returnPrice` interface, which enables the addition of new pricing strategies (such as for additional cities) without modifying existing classes. This approach ensures that the system can evolve over time to accommodate new requirements without introducing bugs in the existing functionality.

By adhering to SOLID principles, the Real Estate Pricing System is designed to be maintainable, flexible, and easily extendable, allowing for straightforward adaptations as business needs change while minimizing the risk of breaking existing code.
