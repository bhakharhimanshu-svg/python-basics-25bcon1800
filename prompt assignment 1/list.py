```python
# Save this file as list_program.py
# Avoid naming it list.py to prevent module conflicts.

def display_list(items):
    if items:
        print("Current List:", items)
    else:
        print("The list is empty.")

def main():
    items = []

    while True:
        print("\n=== LIST MANAGER ===")
        print("1. Add Item")
        print("2. Remove Item")
        print("3. Search Item")
        print("4. Sort List")
        print("5. Display List")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            value = input("Enter item: ").strip()

            if value:
                items.append(value)
                print("Item added!")
            else:
                print("Item cannot be empty.")

        elif choice == "2":
            value = input("Enter item to remove: ")

            if value in items:
                items.remove(value)
                print("Item removed!")
            else:
                print("Item not found.")

        elif choice == "3":
            value = input("Enter item to search: ")

            if value in items:
                print("Item found at index:", items.index(value))
            else:
                print("Item not found.")

        elif choice == "4":
            items.sort(key=str.casefold)
            print("List sorted!")

        elif choice == "5":
            display_list(items)

        elif choice == "6":
            print("Goodbye!")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
```