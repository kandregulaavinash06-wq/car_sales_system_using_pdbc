from database import DatabaseConnection

class CarSalesSystem:
 
    def __init__(self):
        self.db = DatabaseConnection()

    def add_car(self, car):
        try:
            con = self.db.connect()
            cur = con.cursor()

            sql = """
            INSERT INTO Cars (brand, model, price, available_quantity)
            VALUES (%s, %s, %s, %s)
            """

            cur.execute(sql, (
                car.brand,
                car.model,
                car.price,
                car.available_quantity
            ))

            con.commit()
            print("Car added successfully")

        except Exception as e:
            print("Error adding car:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def view_cars(self):
        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute("SELECT * FROM Cars")
            cars = cur.fetchall()

            if not cars:
                print("No cars found")
                return

            print("\nID | Brand | Model | Price | Quantity")
            print("-" * 55)

            for car in cars:
                print(car)

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def search_car(self):
        brand = input("Enter brand to search: ")

        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute(
                "SELECT * FROM Cars WHERE brand LIKE %s",
                ("%" + brand + "%",)
            )

            cars = cur.fetchall()

            if not cars:
                print("Car not found")
            else:
                for car in cars:
                    print(car)

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def update_car(self):
        car_id = int(input("Enter car ID: "))
        price = float(input("Enter new price: "))
        quantity = int(input("Enter new quantity: "))

        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute("""
                UPDATE Cars
                SET price=%s, available_quantity=%s
                WHERE car_id=%s
            """, (price, quantity, car_id))

            con.commit()

            if cur.rowcount == 0:
                print("Car not found")
            else:
                print("Car updated successfully")

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def delete_car(self):
        car_id = int(input("Enter car ID: "))

        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute(
                "DELETE FROM Cars WHERE car_id=%s",
                (car_id,)
            )

            con.commit()

            if cur.rowcount == 0:
                print("Car not found")
            else:
                print("Car deleted successfully")

        except Exception as e:
            print("Error deleting car:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def add_customer(self, customer):
        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute("""
                INSERT INTO Customers (name, phone, email)
                VALUES (%s, %s, %s)
            """, (
                customer.name,
                customer.phone,
                customer.email
            ))

            con.commit()
            print("Customer added successfully")

        except Exception as e:
            print("Error adding customer:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def view_customers(self):
        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute("SELECT * FROM Customers")
            customers = cur.fetchall()

            if not customers:
                print("No customers found")
                return

            print("\nID | Name | Phone | Email")
            print("-" * 60)

            for customer in customers:
                print(customer)

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def sell_car(self):
        customer_id = int(input("Enter customer ID: "))
        car_id = int(input("Enter car ID: "))
        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than 0")
            return

        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute(
                "SELECT price, available_quantity FROM Cars WHERE car_id=%s",
                (car_id,)
            )

            car = cur.fetchone()

            if car is None:
                print("Car not found")
                return

            price, available_quantity = car

            if available_quantity < quantity:
                print("Not enough cars available")
                return

            cur.execute(
                "SELECT customer_id FROM Customers WHERE customer_id=%s",
                (customer_id,)
            )

            customer = cur.fetchone()

            if customer is None:
                print("Customer not found")
                return

            total_price = price * quantity

            for i in range(quantity):
                cur.execute("""
                    INSERT INTO Sales
                    (car_id, customer_id, sale_date, sale_price)
                    VALUES (%s, %s, CURDATE(), %s)
                """, (
                    car_id,
                    customer_id,
                    price
                ))

            cur.execute("""
                UPDATE Cars
                SET available_quantity = available_quantity - %s
                WHERE car_id=%s
            """, (quantity, car_id))

            con.commit()

            print("Car sold successfully")
            print("Total price:", total_price)

        except Exception as e:
            print("Error selling car:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass

    def view_sales(self):
        try:
            con = self.db.connect()
            cur = con.cursor()

            cur.execute("""
                SELECT
                    s.sale_id,
                    c.name,
                    ca.brand,
                    ca.model,
                    s.sale_price,
                    s.sale_date
                FROM Sales s
                JOIN Customers c
                    ON s.customer_id = c.customer_id
                JOIN Cars ca
                    ON s.car_id = ca.car_id
            """)

            sales = cur.fetchall()

            if not sales:
                print("No sales found")
                return

            print("\nSale ID | Customer | Brand | Model | Price | Date")
            print("-" * 70)

            for sale in sales:
                print(sale)

        except Exception as e:
            print("Error:", e)

        finally:
            try:
                cur.close()
                con.close()
            except:
                pass