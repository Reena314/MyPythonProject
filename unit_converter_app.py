def show_menu():
    print("\n===== UNIT CONVERTER =====")
    print("1. Kilometer to Miles")
    print("2. Miles to Kilometer")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Kilograms to Pounds")
    print("6. Pounds to Kilograms")
    print("7. Exit")


def unit_converter():
    while True:
        show_menu()
        choice = input("Choose an option (1-7): ")

        if choice == "1":
            km = float(input("Enter kilometers: "))
            miles = km * 0.621371
            print(f"{km} km = {miles} miles")

        elif choice == "2":
            miles = float(input("Enter miles: "))
            km = miles / 0.621371
            print(f"{miles} miles = {km} km")

        elif choice == "3":
            c = float(input("Enter Celsius: "))
            f = (c * 9/5) + 32
            print(f"{c}°C = {f}°F")

        elif choice == "4":
            f = float(input("Enter Fahrenheit: "))
            c = (f - 32) * 5/9
            print(f"{f}°F = {c}°C")

        elif choice == "5":
            kg = float(input("Enter kilograms: "))
            lbs = kg * 2.20462
            print(f"{kg} kg = {lbs} lbs")

        elif choice == "6":
            lbs = float(input("Enter pounds: "))
            kg = lbs / 2.20462
            print(f"{lbs} lbs = {kg} kg")

        elif choice == "7":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again!")

# Run the converter
unit_converter()
