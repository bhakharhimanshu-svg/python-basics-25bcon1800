```python
"""
Advanced Fibonacci Sequence Analyzer
Author: bhakharhimanshu-svg
Project: python-basics-25bcon1800
"""

from functools import lru_cache


def fibonacci_sequence(count: int) -> list[int]:
    """Generate Fibonacci numbers iteratively."""
    if count < 0:
        raise ValueError("Count cannot be negative.")

    sequence = []
    first, second = 0, 1

    for _ in range(count):
        sequence.append(first)
        first, second = second, first + second

    return sequence


@lru_cache(maxsize=None)
def fibonacci_recursive(n: int) -> int:
    """Calculate one Fibonacci number using memoization."""
    if n < 0:
        raise ValueError("Index cannot be negative.")

    if n < 2:
        return n

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def analyze_sequence(sequence: list[int]) -> dict:
    """Calculate useful statistics for a sequence."""
    return {
        "count": len(sequence),
        "sum": sum(sequence),
        "even_count": sum(number % 2 == 0 for number in sequence),
        "odd_count": sum(number % 2 != 0 for number in sequence),
        "maximum": max(sequence) if sequence else None,
        "minimum": min(sequence) if sequence else None,
    }


def display_sequence(sequence: list[int]) -> None:
    """Display sequence and analysis."""
    print("\n" + "=" * 50)
    print("       FIBONACCI SEQUENCE ANALYZER")
    print("=" * 50)

    print("Sequence:", sequence)

    if not sequence:
        print("No terms were generated.")
        return

    stats = analyze_sequence(sequence)

    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title():15}: {value}")

    print("\nVerification using memoized recursion:")

    for index, value in enumerate(sequence[:10]):
        verified = fibonacci_recursive(index) == value
        print(f"F({index}) = {value} | Verified: {verified}")

    print("=" * 50)


def main() -> None:
    try:
        count = int(input("Enter number of terms (0-1000): "))

        if not 0 <= count <= 1000:
            print("Please enter a number between 0 and 1000.")
            return

        sequence = fibonacci_sequence(count)
        display_sequence(sequence)

    except ValueError:
        print("Error: Enter a valid integer.")

    except KeyboardInterrupt:
        print("\nProgram stopped by user.")


if __name__ == "__main__":
    main()
```