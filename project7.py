import sqlite3
from datetime import datetime

def main():
    db = 'project7.db'
    conn = sqlite3.connect(db)
    conn.execute("PRAGMA foreign_keys = ON")

    done = False
    while not done:
        print("\nMain Menu")
        print("\nA - Admin Menu")
        print("S - Start New Order")
        print("P - Past Orders")
        print("C - View All Customers")
        print("Q - Quit")

        choice = input("Choice: ").upper()

        if choice == "A":
            admin(conn)
        elif choice == "S":
            restaurant(conn)
        elif choice == "P":
            past_orders(conn)
        elif choice == "C":
            view_customers(conn)
        elif choice == "Q":
            print("Quitting!")
            done = True
        else:
            print("Invalid, try again!")

    #close the connection
    conn.close()

# admin function
def admin(conn):
    print("\nAdmin Menu")

    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")

    done = False
    while not done:
        print("\nCREATE1 - Create menu table")
        print("CREATE2 - Create customers table")
        print("CREATE3 - Create orders table")
        print("CREATE4 - Create order_items table")
        print("INSERT1 - Insert menu items")
        print("S - View All Menu Items")
        print("P - Past Orders")
        print("C - View All Customers")
        print("Q - Quit Admin menu")

        choice = input("Choice: ").upper()

        if choice == "CREATE1":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS menu (
                menu_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL,
                price REAL NOT NULL,
                description TEXT
            )
            """)
            conn.commit()

            print("\nMenu table created!")

        elif choice == "CREATE2":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS customers (
                customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                street_address TEXT NOT NULL,
                city TEXT NOT NULL,
                state TEXT NOT NULL,
                zip_code TEXT NOT NULL,
                phone_number TEXT NOT NULL
            )
            """)
            conn.commit()

            print("\nCustomers table created!")

        elif choice == "CREATE3":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS orders (
                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
                customer_id INTEGER NOT NULL,
                order_number TEXT UNIQUE NOT NULL,
                date_time TEXT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
            )
            """)
            conn.commit()

            print("\nOrders table created!")

        elif choice == "CREATE4":
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS order_items (
                order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                order_number TEXT NOT NULL,
                menu_id INTEGER NOT NULL,
                quantity INTEGER NOT NULL,
                FOREIGN KEY (order_number) REFERENCES orders(order_number),
                FOREIGN KEY (menu_id) REFERENCES menu(menu_id)
            )
            """)
            conn.commit()

            print("\nOrder items table created!")

        elif choice == "INSERT1":
           items = [
                ("Takoyaki Octopus Balls (5pcs)", "Appetizers", 8.99, "Octopus balls topped with dry bonito flakes, aonori, mayo, and teriyaki sauce."),
                ("Pan-Fried Gyoza Dumplings (6pcs)", "Appetizers", 7.99, "Japanese Style Dumpling served with gyoza sauce."),
                ("Shrimp Tempura (4pcs)", "Appetizers", 7.99, "Fried shrimp tempura served with sauce"),
                ("Steamed Pork Bao Buns (2pcs)", "Appetizers", 8.99, "Braised pork between Bao Bun served with fresh veggies and KYURAMEN special sauce."),
                ("Yakitori Platter (5 Skewers)", "Appetizers", 15.95, "Skewers of chicken thigh w. leek, beef skirt, pork belly, baby scallop, and zucchini."),

                ("Tonkatsu Omurice with Curry Sauce", "Entrees", 24.99, "Fluffy omelet egg and pork tonkatsu on top of chicken fried rice, topped with your choice of Curry Sauce or Demi Glace."),
                ("Yinyang Bowl", "Entrees", 20.99, "Tonkotsu shoyu ramen + sapporo miso ramen served with toppings."),
                ("Kyushu Spicy Tonkotsu Ramen", "Entrees", 17.99, "Served with chashu pork, half marinated egg, corn, bamboo shoots, wakame, scallion, and nori in pork broth."),
                ("Diced Braised Pork Don", "Entrees", 14.99, "White rice topped with diced braised pork, zucchini, scallion, and half marinated egg."),
                ("Katsuobushi Pork Ramen", "Entrees", 18.99, "Served with braised pork belly, katsuobushi, half marinated egg, bamboo shoots, corn, scallion, nori, sesame, and shichimi in pork broth."),

                ("Matcha Tiramisu", "Desserts", 7.99, "Sweet tiramisu topped with matcha powder."),
                ("Matcha Pudding with Red Bean", "Desserts", 4.99, "Matcha pudding topped with sweet red beans, served with fresh milk on the side."),
                ("Japanese Cherry Blossom Jelly", "Desserts", 4.99, "Japanese sweet cherry blossom flavored jelly served with white pearl."),
                ("Matcha Mille Crepe Cake", "Desserts", 9.99, "Matcha flavored mille crepe Cake topped with matcha powder."),
                ("Mango Mille Crepe Cake", "Desserts", 9.99, "Mille crepe stuffed and topped with fresh mango."),

                ("Thai Iced Tea", "Beverages", 4.99, "Our in-house Thai Iced Tea."),
                ("Amazing Lemonade", "Beverages", 4.99, "Our in-house Lemonade."),
                ("Moshi Yuzu Sparkling Drink (Original)", "Beverages", 5.99, "Moshi Yuzu's flagship drink. Tart & fragrant!"),
                ("Moshi Yuzu Sparkling Drink (White Peach)", "Beverages", 5.99, "Moshi Yuzu's fan favorite. Aromatic & sweet!"),
                ("Japanese Ramune", "Beverages", 4.25, "Strawberry or Lychee Flavor")
                ]

           cursor.executemany("""
                INSERT INTO menu (name, category, price, description) VALUES (?, ?, ?, ?)
                """, items)

           conn.commit()

           print("\nMenu items inserted!")

        elif choice == "S":
            cursor.execute("SELECT * FROM menu")
            rows = cursor.fetchall()

            for item in rows:
                print(f"{item[0]}.) {item[1]} ({item[2]}) - ${item[3]}: {item[4]}")


        elif choice == "P":
            past_orders(conn)

        elif choice == "C":
            view_customers(conn)

        elif choice == "Q":
            print("Quitting!")
            done = True

        else:
            print("Invalid, try again!")

# start new order function
def restaurant(conn):
    cursor = conn.cursor()
    cursor.execute("PRAGMA foreign_keys = ON")


    print("\nRestaurant Menu")
    print("\nStart new order: ")

    choice = input("Are you a new (N) or existing (E) customer? ").upper()

    if choice == "N":
        print("Please, enter the info below: ")
        name = input("Name: ")
        address = input("Address: ")
        state = input("State: ")
        city = input("City: ")
        zipCode = input("Zip code:")
        phoneNum = input("Phone number: ")

        cursor.execute("""
                INSERT INTO customers (name, street_address, city, state, zip_code, phone_number) VALUES (?,?,?,?,?,?)
                """, (name,address, city, state, zipCode, phoneNum))

        conn.commit()

        customer_id = cursor.lastrowid

        print(f"New Customer created with ID: {customer_id}")

    else:
        print("Welcome back!")
        option = input("Search by name (n) or ID (i): ").upper()

        if option == "N":
            name = input("Enter name: ")
            cursor.execute("""SELECT * FROM customers WHERE name LIKE ?""", (f"%{name}%",))
            results = cursor.fetchall()

            if not results:
                print("No match found.")
                return

            print("\nMatching customer names: ")
            for row in results:
                print(row)

            customer_id = int(input("Enter your customer ID from the list: "))

        elif option == "I":
            view_customers(conn)
            customer_id = int(input("Enter your customer ID from the list: "))

        else:
            print("Invalid")
            return

    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    order_number = f"ABC-{customer_id}{timestamp}"

    date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    cursor.execute("""
        INSERT INTO orders (customer_id, order_number, date_time) VALUES (?, ?, ?)
        """, (customer_id, order_number, date_time))

    conn.commit()

    print(f"Order number created: {order_number}")

    done = False
    while not done:
        print("\nO - Order")
        print("M - Modify Order")
        print("P - Place Order")
        print("Q - Cancel")

        choice = input("Choice: ").upper()

        if choice == "O":
            ordering(conn, order_number)
        elif choice == "M":
            modify_order(conn, order_number)
        elif choice == "P":
            place_order(conn, order_number)
            done = True
        elif choice == "Q":
            done = True
        else:
            print("Invalid, try again")

def ordering(conn, order_number):
    cursor = conn.cursor()

    ordering = False
    while not ordering:
        print("\nCategories:")
        print("\nA - Appetizers")
        print("E - Entrees")
        print("D - Desserts")
        print("B - Beverages")
        print("Q - Quit Ordering")

        choice = input("Choice: ").upper()

        if choice == "A":
            category = "Appetizers"
        elif choice == "E":
            category = "Entrees"
        elif choice == "D":
            category = "Desserts"
        elif choice == "B":
            category = "Beverages"
        elif choice == "Q":
            print("Quitting!")
            ordering = True
            break
        else:
            print("Invalid, try again!")
            continue

        print(f"\n{category} Menu:")
        cursor.execute("""
            SELECT menu_id, name, price, description FROM menu WHERE category = ?
            """, (category,))

        menu = cursor.fetchall()

        if not menu:
            print("No items in this category")

        for row in menu:
            print(f"{row[0]}.) {row[1]} - ${row[2]}: {row[3]}")

        menuID = int(input("\nEnter menu ID: "))
        qty = int(input("Quantity: "))

        exist = cursor.execute("""
                    SELECT quantity FROM order_items WHERE order_number = ? AND menu_id = ?
                    """, (order_number, menuID)).fetchone()

        if exist:
            cursor.execute("""
                UPDATE order_items SET quantity = quantity + ? WHERE order_number = ? AND menu_id = ?
                """, (qty, order_number, menuID))
        else:
            cursor.execute("""
                INSERT INTO order_items (order_number, menu_id, quantity) VALUES (?, ?, ?)
                """, (order_number, menuID, qty))

        conn.commit()

        cont = input(f"\nDo you want to continue ordering? (Y/N):").upper()

        if cont != "Y":
            ordering = True

def modify_order(conn, order_number):
    print("\nCurrent order:")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT menu.menu_id, menu.name, order_items.quantity FROM order_items
        INNER JOIN menu ON menu.menu_id = order_items.menu_id
        WHERE order_items.order_number = ?
        """, (order_number,))

    items = cursor.fetchall()

    if not items:
        print("No items!")

    for item in items:
        print(f"{item[0]}.) {item[1]} X {item[2]}")

    modify = input("\nDo you want to modify order? (Y/N): ").upper()

    if modify == "Y":

        menuID = int(input("Enter the menu ID you want to modify: "))
        action = input("Do you want to update (U) or delete (D)? ").upper()

        if action == "U":
            qty = int(input("New quantity: "))

            cursor.execute("""
                UPDATE order_items SET quantity = ? WHERE order_number = ? AND menu_id = ?
                """, (qty, order_number, menuID))

        elif action == "D":
            cursor.execute("""

            DELETE FROM order_items WHERE order_number = ? AND menu_id = ?
            """, (order_number, menuID))

        conn.commit()

def place_order(conn, order_number):
    print("\nPlace order:")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT customers.name, orders.order_number, menu.name, order_items.quantity, menu.price FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        INNER JOIN order_items ON orders.order_number = order_items.order_number
        INNER JOIN menu ON menu.menu_id = order_items.menu_id
        WHERE orders.order_number = ?
        """, (order_number,))

    items = cursor.fetchall()

    subtotal = 0

    for customer, order_num,name, qty, price in items:
        total = qty * price
        subtotal += total
        print(f"{name} {qty} X ${price} - ${total}")

    print(f"\nSubtotal: ${subtotal}")

    coupon = input("Do you have a coupon? (Y/N): ").upper()

    if coupon == "Y":
        cType = input("Is the coupon percentage (P) or dollar (D)? ").upper()

        if cType == "P":
            percent = int(input("Enter percentage (wihtout %): "))
            discount = subtotal * (percent/100)
            discountedSubtotal = subtotal - discount
        elif cType == "D":
            amount = float(input("Enter dollar amount: "))
            discountedSubtotal = subtotal - amount
    else:
        discountedSubtotal = subtotal

    print("Tip options: 15%, 18%, 20%, 25%")

    tipChoice = int(input("Enter the tip (without %): "))
    tipAmount = discountedSubtotal * (tipChoice/100)

    tax = discountedSubtotal * 0.06625

    method = input("Do you want pickup or delivery? ").upper()

    if method == "DELIVERY":
        fee = 5.00
    else:
        fee = 0.00

    total = discountedSubtotal + tipAmount + tax + fee

    cursor.execute("SELECT date_time FROM orders WHERE order_number = ?", (order_number,))
    date_time = cursor.fetchone()[0]

    customer = items[0][0]
    order_num = items[0][1]

    print("\nReceipt:")
    print("-------------------------")
    print("Customer: " + customer)
    print("Order number: " + order_num)
    print("Date/Time: " + date_time)
    print("-------------------------")
    print("Subtotal after coupon: $" + str(discountedSubtotal))
    print("Tip: $" + str(tipAmount))
    print("Tax: $" + str(tax))
    print("Delivery fee: $" + str(fee))
    print("Total: $" + str(total))
    print("Thank you for dining at Kyuramen!")

# past orders function
def past_orders(conn):
    print("\nPast Orders:")

    cursor = conn.cursor()

    cursor.execute("""
        SELECT customers.customer_id, customers.name, orders.order_number, orders.date_time FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        """)

    orders = cursor.fetchall()

    if not orders:
        print("No past orders found.")
        return

    print("\nCustomer Orders:")
    for row in orders:
        print(f"Customer ID: {row[0]} | Name: {row[1]} | Order number: {row[2]} | Date/Time: {row[3]}")

    order_number = input("\nEnter order number to view details: ")

    cursor.execute("""
        SELECT order_items.quantity, orders.order_number, menu.menu_id, menu.name, menu.price FROM orders
        INNER JOIN order_items ON order_items.order_number = orders.order_number
        INNER JOIN menu ON menu.menu_id = order_items.menu_id
        WHERE orders.order_number = ?
        """, (order_number,))

    items = cursor.fetchall()

    if not items:
        print("No items found for this order.")
        return

    print("\nOrder Details:")
    subtotal = 0

    for qty, order_num, menu_id, name, price in items:
        total = qty * price
        print(f"{name} - {qty} X ${price} - ${total}")

# view customers function
def view_customers(conn):
    print("\nView Customers:")

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM customers")

    customers = cursor.fetchall()

    for row in customers:
        print(row)

main()
