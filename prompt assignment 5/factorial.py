```python
"""
Advanced Factorial Calculator
Author: bhakharhimanshu-svg
Project: python-basics-25bcon1800
"""

import time
from math import factorial as built_in_factorial


def factorial_iterative(n: int) -> int:
    """Calculate factorial using an iterative approach."""
    if n < 0:
        raise ValueError("Number must be non-negative.")

    result = 1

    for number in range(2, n + 1):
        result *= number

    return result


def factorial_recursive(n: int) -> int:
    """Calculate factorial using recursion."""
    if n < 0:
        raise ValueError("Number must be non-negative.")

    if n <= 1:
        return 1

    return n * factorial_recursive(n - 1)


def display_result(n: int) -> None:
    """Display factorial results and execution times."""
    print("\n" + "=" * 45)
    print("       ADVANCED FACTORIAL CALCULATOR")
    print("=" * 45)

    start = time.perf_counter()
    iterative_result = factorial_iterative(n)
    iterative_time = time.perf_counter() - start

    print(f"Number             : {n}")
    print(f"Factorial          : {iterative_result}")
    print(f"Number of digits   : {len(str(iterative_result))}")
    print(f"Iterative time     : {iterative_time:.8f} seconds")

    # Recursive method is limited to smaller inputs.
    if n <= 900:
        start = time.perf_counter()
        recursive_result = factorial_recursive(n)
        recursive_time = time.perf_counter() - start

        print(f"Recursive verified : {recursive_result == iterative_result}")
        print(f"Recursive time     : {recursive_time:.8f} seconds")
    else:
        print("Recursive check    : Skipped for large input")

    print(f"Built-in verified  : {built_in_factorial(n) == iterative_result}")
    print("=" * 45)


def main() -> None:
    try:
        raw_input = input("Enter a non-negative integer: ").strip()
        number = int(raw_input)

        if number < 0:
            print("Error: Please enter a non-negative integer.")
            return

        display_result(number)

    except ValueError:
        print("Error: Enter a valid whole number.")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    main()
```