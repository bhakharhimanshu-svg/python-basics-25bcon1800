```python
import math

def calculate_factorial(number):
    if number < 0:
        raise ValueError("Negative numbers are not allowed.")

    return math.factorial(number)

def main():
    print("=== FACTORIAL CALCULATOR ===")

    try:
        number = int(input("Enter a non-negative integer: "))

        if number < 0:
            print("Error: Enter a number >= 0.")
        elif number > 10000:
            print("Please enter a number up to 10000.")
        else:
            result = calculate_factorial(number)
            print(f"Factorial of {number} = {result}")
            print(f"Number of digits: {len(str(result))}")

    except ValueError:
        print("Invalid input! Enter a whole number.")

if __name__ == "__main__":
    main()
```