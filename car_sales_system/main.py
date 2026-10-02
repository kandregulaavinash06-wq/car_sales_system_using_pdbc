from car_sales_system import CarSalesSystem
from car import Car
from customer import Customer


system = CarSalesSystem()


while True:

    print("\n===== CAR SALES MANAGEMENT SYSTEM =====")
    print("1. Add Car.  2. View Cars   3. Search Car   4. Add Customer   5. View Customers")
    print("6. Sell Car   7. View Sales   8. Update Car  9. Delete Car   10. Exit")

    choice = input("Enter your choice: ")

    try:

        if choice == "1":
            brand = input("Enter brand: ")
            model = input("Enter model: ")
            price = float(input("Enter price: "))
            quantity = int(input("Enter quantity: "))

            car = Car(None, brand, model, price, quantity)
            system.add_car(car)

        elif choice == "2":
            system.view_cars()

        elif choice == "3":
            system.search_car()

        elif choice == "4":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")

            customer = Customer(None, name, phone, email)
            system.add_customer(customer)

        elif choice == "5":
            system.view_customers()

        elif choice == "6":
            system.sell_car()

        elif choice == "7":
            system.view_sales()

        elif choice == "8":
            system.update_car()

        elif choice == "9":
            system.delete_car()

        elif choice == "10":
            print("Thank you!")
            break

        else:
            print("Invalid choice")

    except ValueError:
        print("Please enter valid input")