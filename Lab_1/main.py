from Tools import showRoom, VehicleBuilder, UseDefaultComplectation, VehiclePrototype

if __name__ == "__main__":
    showRoom = showRoom("Studentilor")
    builder = VehicleBuilder()

    if showRoom.instance is not None:
        while True:
            print("Welcome to Vehicle Configuration!")
            print("---------------------------------------------------------------------------------------------")
            print("Please choose an option:")
            print("1. Configure manually")
            print("2. Use default configuration")
            print("3. Create a copy of existing configuration.")
            print("4. Finish Configuration")
            choice = int(input())

            if choice == 1:
                print("Your car was initialized, let's proceed with configuration.")
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
                    choice = int(input())

                    if choice == 1:
                        builder.setWheel(input("Enter wheel type: ").strip())
                    elif choice == 2:
                        builder.setGrill(input("Enter grill type: ").strip())
                    elif choice == 3:
                        builder.setBumper(input("Enter bumper type: ").strip())
                    elif choice == 4:
                        builder.setWindow(input("Enter window type: ").strip())
                    elif choice == 5:
                        builder.setRoof(input("Enter roof type: ").strip())
                    elif choice == 6:
                        builder.setDoor(input("Enter door type: ").strip())
                    elif choice == 7:
                        builder.setHeadLight(input("Enter head light type: ").strip())
                    elif choice == 8:
                        vehicle = builder.build()
                        print("\nConfiguration complete!")
                        break
                    else:
                        print("Invalid choice. Please enter a number between 1 and 8.")
            elif choice == 2:
                configure_car = UseDefaultComplectation(builder)
                vehicle = configure_car.fullComplectation()
            elif choice == 3:
                try:
                    vehicle
                except NameError:
                    print("well, no existing car configuration!")
                else:
                    configuration_copy_obj = VehiclePrototype(vehicle)
                    configuration_copy = configuration_copy_obj.clone()
                    print(f"\nCopy Vehicle Configuration:\n"
                          f"  1. Wheel: {configuration_copy.wheel or 'Not Set'}\n"
                          f"  2. Grill: {configuration_copy.grill or 'Not Set'}\n"
                          f"  3. Bumper: {configuration_copy.bumper or 'Not Set'}\n"
                          f"  4. Window: {configuration_copy.window or 'Not Set'}\n"
                          f"  5. Roof: {configuration_copy.roof or 'Not Set'}\n"
                          f"  6. Door: {configuration_copy.door or 'Not Set'}\n"
                          f"  7. Head Light: {configuration_copy.head_light or 'Not Set'}\n")
            elif choice == 4:
                vehicle = builder.build()
                print(f"\nCurrent Vehicle Configuration:\n"
                      f"  1. Wheel: {vehicle.wheel or 'Not Set'}\n"
                      f"  2. Grill: {vehicle.grill or 'Not Set'}\n"
                      f"  3. Bumper: {vehicle.bumper or 'Not Set'}\n"
                      f"  4. Window: {vehicle.window or 'Not Set'}\n"
                      f"  5. Roof: {vehicle.roof or 'Not Set'}\n"
                      f"  6. Door: {vehicle.door or 'Not Set'}\n"
                      f"  7. Head Light: {vehicle.head_light or 'Not Set'}\n")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 3.")