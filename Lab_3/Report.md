# Behavioral Design Patterns: Iterator Pattern

## Author
**Gavriliuc Tudor**

---

## Introduction/Theory/Motivation

The **Iterator Pattern** is a behavioral design pattern that provides a structured way to traverse elements in a collection sequentially, without exposing its internal structure. By abstracting the traversal logic, this pattern ensures that the underlying collection implementation remains encapsulated.

In this laboratory work, the Iterator Pattern was implemented to enhance the functionality of a vehicle showroom application. It is used to manage and display saved vehicle configuration files in a systematic and user-friendly manner. This design pattern contributes to:

- **Encapsulation**: Hides the internal details of the collection and its traversal.
- **Reusability**: Separates traversal logic from the collection, allowing the same iterator to be reused for different collections.
- **Flexibility**: Enables the traversal of collections with varying implementations without altering the core logic.

---

## Implementation & Explanation

The Iterator Pattern was applied to streamline the process of managing saved vehicle configuration files. A dedicated manager was created to save, track, and provide access to these files using an iterator. The implementation focused on separating the collection's management and traversal responsibilities, ensuring a clean and modular structure.
**Code Snippet**:
```python
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
```
The **FileManager** class handles the storage of configuration files, and the **FileIterator** provides a standardized way to access these files sequentially. This separation of concerns makes the system more adaptable to changes and easier to maintain.
**Code Snippet**:
```python
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
```
---

## Results/Screenshots/Conclusions

### Results

1. The system now efficiently manages and traverses saved vehicle configuration files.
2. Users can interact with the collection through a simple and intuitive interface.
3. The encapsulated traversal logic ensures the internal structure of the collection remains hidden.

---

### Sample Execution

 ![Alt Text](https://github.com/Tudor-Gavriliuc/TMPS/blob/main/Lab_3/configurations/Screenshot%20(34).png?raw=true)

---

### Conclusions

The **Iterator Pattern** effectively enhances the modularity and scalability of the vehicle showroom application. By encapsulating the traversal logic, it simplifies the process of accessing collections while maintaining flexibility for future extensions. This approach aligns with the principles of behavioral design patterns, making the system robust and easy to maintain.
