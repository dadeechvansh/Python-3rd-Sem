import os

library = {
    "Python": "Available",
    "C Programming": "Available",
    "Data Science": "Available"
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_books():
    clear_screen()
    print("Library Management System".center(60, "="))
    print("{:<30}{:<15}".format("Book Name", "Status"))
    print("-" * 45)
    for book, status in library.items():
        print("{:<30}{:<15}".format(book, status))
    print("-" * 45)

def lend_book():
    show_books()
    book = input("Enter book name to borrow: ").strip()
    if book in library and library[book] == "Available":
        borrower = input("Enter your name: ").strip()
        library[book] = f"Issued to {borrower}"

        
        print("\n" + "LENDING RECEIPT".center(50, "="))
        print(f"Borrower Name : {borrower}")
        print(f"Book Title    : {book}")
        print(f"Status        : Issued Successfully")
        print("=" * 50)
    elif book in library and "Issued" in library[book]:
        print(f"\nSorry! The book '{book}' is already issued.")
    else:
        print("\nBook not found in library.")
    input("\nPress Enter to return to main menu...")

def return_book():
    show_books()
    book = input("Enter book name to return: ").strip()
    if book in library and "Issued" in library[book]:
        try:
            late_days = int(input("Enter how many days late (0 if on time): "))
            fine = late_days * 5
            borrower = library[book].replace("Issued to ", "")
            library[book] = "Available"

            print("\n" + "RETURN RECEIPT".center(50, "="))
            print(f"Borrower Name : {borrower}")
            print(f"Book Title    : {book}")
            print(f"Late Days     : {late_days}")
            print(f"Fine Amount   : ₹{fine}")
            print(f"Status        : Returned Successfully")
            print("=" * 50)
        except ValueError:
            print("\nInvalid input! Please enter a number.")
    else:
        print("\nInvalid book name or the book was not issued.")
    input("\nPress Enter to return to main menu...")

def add_book():
    show_books()
    book = input("Enter new book name: ").strip()
    if book in library:
        print(f"\n'{book}' already exists in the library.")
    else:
        library[book] = "Available"
        print(f"\n'{book}' added successfully to the library.")
    input("\nPress Enter to return to main menu...")


while True:
    clear_screen()
    print("Library Management System".center(60, "="))
    print("\n1. Show Books\n2. Lend Book\n3. Return Book\n4. Add Book\n5. Exit")
    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_books()
        input("\nPress Enter to return to main menu...")
    elif choice == "2":
        lend_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("\nExiting Library System... Have a great day!")
        break
    else:
        print("\nInvalid choice! Please enter a valid option.")
        input("\nPress Enter to continue...")
