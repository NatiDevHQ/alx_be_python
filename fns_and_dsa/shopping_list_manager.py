def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  # ✔ implementation of an array `shopping_list`

    while True:
        display_menu()  # ✔ calling display_menu function

        try:
            choice = int(input("Enter your choice: "))  # ✔ choice input as a number
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            item = input("Enter the item to add: ")
            shopping_list.append(item)
            print(f"{item} added to shopping list.")
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"{item} removed from shopping list.")
            else:
                print(f"{item} not found in shopping list.")
        elif choice == 3:
            if shopping_list:
                print("Current Shopping List:")
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("Shopping list is empty.")
        elif choice == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
