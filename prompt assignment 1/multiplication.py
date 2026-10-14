```python
def generate_table(number, start, end, reverse=False):
    numbers = range(start, end + 1)

    if reverse:
        numbers = range(end, start - 1, -1)

    print(f"\nMultiplication Table of {number}")

    for i in numbers:
        print(f"{number} x {i} = {number * i}")

def main():
    print("=== TABLE GENERATOR ===")

    try:
        number = int(input("Enter number: "))
        start = int(input("Starting multiplier: "))
        end = int(input("Ending multiplier: "))

        if start < 0 or end < 0:
            print("Multipliers cannot be negative.")
            return

        if start > end:
            print("Starting multiplier must be <= ending multiplier.")
            return

        if end - start > 999:
            print("Please choose a range of at most 1000 terms.")
            return

        order = input("Reverse order? (yes/no): ").strip().lower()

        if order not in ("yes", "no"):
            print("Enter yes or no.")
            return

        generate_table(
            number, start, end,
            reverse=(order == "yes")
        )

    except ValueError:
        print("Invalid input! Please enter integers.")

if __name__ == "__main__":
    main()
```