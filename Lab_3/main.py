from Lab_3.Tools import showRoom, VehicleBuilder, VehicleFacade, FileManager, CompositeComponent, Component, \
    VehiclePrototype, SportPackage, LuxuryPackage

if __name__ == "__main__":
    showroom = showRoom("Studentilor")
    facade = VehicleFacade()
    builder = VehicleBuilder()
    file_manager = FileManager()

    # Create a composite structure for vehicle categories
    all_vehicles = CompositeComponent("All Vehicles")
    sport_vehicles = CompositeComponent("Sport Vehicles")
    luxury_vehicles = CompositeComponent("Luxury Vehicles")

    vehicle = None  # Placeholder for the current vehicle configuration

    while True:
        print("Welcome to Vehicle Configuration!")
        print("---------------------------------------------------------------------------------------------")
        print("Please choose an option:")
        print("1. Configure manually")
        print("2. Use default configuration")
        print("3. Create a copy of existing configuration")
        print("4. Configure a Sport Car")
        print("5. Configure a Basic Car")
        print("6. View All Vehicles")
        print("7. Save Current Configuration as a File")
        print("8. Display All Saved Files")
        print("9. Exit")
        choice = int(input())

        if choice == 1:
            print("Your car was initialized, let's proceed with manual configuration.")
            while True:
                print("\nSelect an element to configure:")
                print("1. Wheel")
                print("2. Grill")
                print("3. Bumper")
                print("4. Window")
                print("5. Roof")
                print("6. Door")
                print("7. Head Light")
                print("8. Finish Configuration")
                sub_choice = int(input())

                if sub_choice == 1:
                    builder.setWheel(input("Enter wheel type: ").strip())
                elif sub_choice == 2:
                    builder.setGrill(input("Enter grill type: ").strip())
                elif sub_choice == 3:
                    builder.setBumper(input("Enter bumper type: ").strip())
                elif sub_choice == 4:
                    builder.setWindow(input("Enter window type: ").strip())
                elif sub_choice == 5:
                    builder.setRoof(input("Enter roof type: ").strip())
                elif sub_choice == 6:
                    builder.setDoor(input("Enter door type: ").strip())
                elif sub_choice == 7:
                    builder.setHeadLight(input("Enter head light type: ").strip())
                elif sub_choice == 8:
                    vehicle = builder.build()
                    print("\nConfiguration complete!")
                    print("Do you want to add this vehicle to a category?")
                    print("1. Sport Vehicles")
                    print("2. Luxury Vehicles")
                    category_choice = int(input())
                    if category_choice == 1:
                        sport_vehicles.add(Component(vehicle.describe()))
                        print("Vehicle added to Sport Vehicles.")
                    elif category_choice == 2:
                        luxury_vehicles.add(Component(vehicle.describe()))
                        print("Vehicle added to Luxury Vehicles.")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1 and 8.")

        elif choice == 2:
            print("Using default configuration...")
            vehicle = facade.configure_basic_car()
            print(f"Default configuration completed: {vehicle.describe()}")
            print("Do you want to add this vehicle to a category?")
            print("1. Sport Vehicles")
            print("2. Luxury Vehicles")
            category_choice = int(input())
            if category_choice == 1:
                sport_vehicles.add(Component(vehicle.describe()))
                print("Vehicle added to Sport Vehicles.")
            elif category_choice == 2:
                luxury_vehicles.add(Component(vehicle.describe()))
                print("Vehicle added to Luxury Vehicles.")

        elif choice == 3:
            if vehicle is None:
                print("No existing configuration to copy!")
            else:
                vehicle_copy = VehiclePrototype(vehicle).clone()
                print(f"Copy of Vehicle Configuration: {vehicle_copy.describe()}")
                print("Do you want to add this copied vehicle to a category?")
                print("1. Sport Vehicles")
                print("2. Luxury Vehicles")
                category_choice = int(input())
                if category_choice == 1:
                    sport_vehicles.add(Component(vehicle_copy.describe()))
                    print("Vehicle added to Sport Vehicles.")
                elif category_choice == 2:
                    luxury_vehicles.add(Component(vehicle_copy.describe()))
                    print("Vehicle added to Luxury Vehicles.")

        elif choice == 4:
            print("Configuring a sport car...")
            sport_car = facade.configure_sport_car()
            sport_car = SportPackage(sport_car)
            sport_vehicles.add(Component(sport_car.describe()))
            print("Sport car configured!")

        elif choice == 5:
            print("Configuring a basic car...")
            basic_car = facade.configure_basic_car()
            basic_car = LuxuryPackage(basic_car)
            luxury_vehicles.add(Component(basic_car.describe()))
            print("Basic car configured!")

        elif choice == 6:
            print("Vehicle Hierarchy:")
            all_vehicles.children.clear()  # Clear previous entries to avoid duplicates
            all_vehicles.add(sport_vehicles)
            all_vehicles.add(luxury_vehicles)
            all_vehicles.display()

        elif choice == 7:
            if vehicle is None:
                print("No current configuration to save!")
            else:
                file_name = input("Enter file name to save the configuration: ").strip()
                file_manager.save_configuration(file_name, vehicle.describe())
                print(f"Configuration saved to file: {file_name}")


        elif choice == 8:
            print("Saved Files:")
            file_iterator = file_manager.get_file_iterator()
            if not file_iterator.has_next():
                print("No files saved yet.")
            else:
                while file_iterator.has_next():
                    print(file_iterator.next())

        elif choice == 9:
            print("Exiting configuration. Goodbye!")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 8.")
