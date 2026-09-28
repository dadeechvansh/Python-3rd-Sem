# Library Management System (Simple Version)

library = {
    "Python": "Available",
    "C Programming": "Available",
    "Data Science": "Available"
}

def show_books():
    print("\n--- Library Books ---")
    for book, status in library.items():
        print(f"{book} - {status}")

def lend_book():
    book = input("Enter book name to borrow: ")
    if book in library and library[book] == "Available":
        library[book] = "Issued"
        print(f"You borrowed '{book}'. Please return on time.")
    else:
        print("Book not available!")

def return_book():
    book = input("Enter book name to return: ")
    if book in library and library[book] == "Issued":
        late_days = int(input("Enter how many days late (0 if on time): "))
        fine = late_days * 5
        library[book] = "Available"
        print(f"Book returned. Fine = ₹{fine}")
    else:
        print("Invalid book or not issued.")

def add_book():
    book = input("Enter new book name: ")
    library[book] = "Available"
    print(f"'{book}' added to library.")

# --- Menu ---
while True:
    print("\n1. Show Books\n2. Lend Book\n3. Return Book\n4. Add Book\n5. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        show_books()
    elif choice == "2":
        lend_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Exiting Library System...")
        break
    else:
        print("Invalid choice! Try again.")




# Hotel Booking and Billing System (Simple Version)
'''
import os

rooms = {
    101: {"type": "Single", "price": 1000, "status": "Available"},
    102: {"type": "Double", "price": 1500, "status": "Available"},
    103: {"type": "Suite",  "price": 2500, "status": "Available"}
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_rooms():
    clear_screen()
    print(" HOTEL BOOKING SYSTEM ".center(60, "="))
    print("{:<10}{:<15}{:<10}{:<20}".format("Room No", "Type", "Price", "Status"))
    print("-" * 60)
    for num, info in rooms.items():
        print("{:<10}{:<15}{:<10}{:<20}".format(num, info["type"], info["price"], info["status"]))
    print("-" * 60)

def book_room():
    show_rooms()
    try:
        room_no = int(input("Enter room number to book: ").strip())
        if room_no not in rooms:
            print("Invalid room number.")
            return

        if rooms[room_no]["status"] != "Available":
            print("Room already booked.")
            return

        name = input("Enter customer name: ").strip()
        days = int(input("Enter number of days: ").strip())
        total = rooms[room_no]["price"] * days
        rooms[room_no]["status"] = f"Booked by {name}"

        print("\n" + " INVOICE ".center(50, "="))
        print(f"Customer Name : {name}")
        print(f"Room Number   : {room_no}")
        print(f"Room Type     : {rooms[room_no]['type']}")
        print(f"Days of Stay  : {days}")
        print(f"Total Amount  : ₹{total}")
        print("=" * 50)

        with open("hotel_bookings.txt", "a") as file:
            file.write(f"{name}, Room {room_no}, {rooms[room_no]['type']}, {days} days, ₹{total}\n")

        print("\nBooking details saved successfully.")

    except ValueError:
        print("Invalid input. Please enter valid numbers only.")

def checkout():
    try:
        room_no = int(input("Enter room number to checkout: ").strip())
        if room_no in rooms:
            if rooms[room_no]["status"] == "Available":
                print("Room is already free.")
            else:
                rooms[room_no]["status"] = "Available"
                print(f"Room {room_no} is now available.")
        else:
            print("Invalid room number.")
    except ValueError:
        print("Please enter a valid number.")

while True:
    print("\n" + "=" * 40)
    print("1. Show Rooms")
    print("2. Book Room")
    print("3. Checkout")
    print("4. Exit")
    print("=" * 40)

    choice = input("Enter your choice: ").strip()

    if choice == "1":
        show_rooms()
    elif choice == "2":
        book_room()
    elif choice == "3":
        checkout()
    elif choice == "4":
        print("Exiting Hotel System...")
        break
    else:
        print("Invalid choice. Try again.")
'''
