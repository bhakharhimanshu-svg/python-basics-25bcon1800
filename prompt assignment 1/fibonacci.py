```python
def fibonacci(n):
    a, b = 0, 1
    sequence = []

    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b

    return sequence

def main():
    print("=== FIBONACCI GENERATOR ===")

    try:
        n = int(input("Enter number of terms (0-10000): "))

        if not 0 <= n <= 10000:
            print("Enter a number between 0 and 10000.")
            return

        result = fibonacci(n)

        print("Fibonacci Sequence:")
        print(*result, sep=", ")

    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
```