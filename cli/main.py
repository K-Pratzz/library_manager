from inventory import Inventory

inv = Inventory()

def menu():
    print("\nLibrary Menu")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

while True:
    menu()
    choice = input("Enter choice: ")

    if choice == "1":
        title = input("Book Title: ")
        author = input("Author: ")
        inv.add_book(title, author)
        print("Book added.")

    elif choice == "2":
        books = inv.view_books()
        for b in books:
            print(f"{b.title} by {b.author} - Available: {b.available}")

    elif choice == "3":
        print("Goodbye.")
        break

    else:
        print("Invalid choice.")