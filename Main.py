# Menu and Prices
menu = {
    "F001": {"name": "Chicken Fried Rice", "price": 1500},
    "F002": {"name": "Egg Burger with Fried Mushroom", "price": 1000},
    "F003": {"name": "Vegetable Pizza", "price": 600},
    "B001": {"name": "Avocado Milkshake", "price": 500},
    "B002": {"name": "Hot Fresh Milk", "price": 400},
    "B003": {"name": "Coca-Cola", "price": 300}
}

# Table Booking
tables = {1: None, 2: None, 3: None, 4: None} # None = Availible

# Displaying Menu Fuction
def display_menu():
    print("Available Menu Items:")
    for code, item in menu.items():
        print(f"{code}: {item['name']} - LKR {item['price']}")

# Booking Function
def book_table():
    print("Checking available tables...")
    available_tables = [table for table, booking in tables.items() if booking is None]
    
    if not available_tables:
        print("Sorry, no tables are available.")
        return
    
    table_no = available_tables[0]  # Checking the Table is availible or not
    print(f"Table {table_no} is available for booking.")
    
    # Confirming Order
    order_list = []
    total_bill = 0
    
    display_menu()
    while True:
        item_code = input("Enter the item code to order (or 'done' to finish): ").upper()
        if item_code == 'DONE':
            break
        elif item_code in menu:
            quantity = int(input(f"How many {menu[item_code]['name']}s would you like to order? "))
            item_cost = menu[item_code]['price'] * quantity
            order_list.append((menu[item_code]['name'], quantity, item_cost))
            total_bill += item_cost
        else:
            print("Invalid item code. Please try again.")
    
    if not order_list:
        print("No items were ordered. Cancelling booking.")
        return
    
    # Storing Order
    tables[table_no] = {
        "orders": order_list,
        "total_bill": total_bill
    }
    
    print(f"Table {table_no} has been successfully booked!")
    print(f"Total bill for this table is: LKR {total_bill}")

# Payment Handling
def process_payment(table_no):
    booking = tables[table_no]
    if not booking:
        print(f"Table {table_no} has no booking.")
        return
    
    print(f"Processing payment for Table {table_no}. Total bill: LKR {booking['total_bill']}")
    
    payment_type = input("Enter payment type (cash/card): ").lower()
    if payment_type == "card":
        extra_charge = booking["total_bill"] * 0.02  # Card Transaction Fee
        total_with_fee = booking["total_bill"] + extra_charge
        print(f"Card payment detected. An additional charge of 2% is applied.")
        print(f"Total amount to pay with fee: LKR {total_with_fee}")
        booking["total_bill"] = total_with_fee
    else:
        print(f"Total amount to pay: LKR {booking['total_bill']}")
    
    print(f"Payment completed for Table {table_no}.")
    
# Calculate Total Income
def calculate_total_income():
    total_income = sum(booking["total_bill"] for booking in tables.values() if booking is not None)
    print(f"Total income from all tables: LKR {total_income}")
    return total_income

# Main Part of the Program
def main():
    while True:
        print("\n1. Book a Table")
        print("2. Process Payment")
        print("3. Show Total Income")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        if choice == '1':
            book_table()
        elif choice == '2':
            table_no = int(input("Enter table number to process payment: "))
            if table_no in tables:
                process_payment(table_no)
            else:
                print("Invalid table number.")
        elif choice == '3':
            calculate_total_income()
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


# END