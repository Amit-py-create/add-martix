def factorial_iterative(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

# Example usage
if __name__ == "__main__":
    number = int(input("Enter a non-negative integer: "))
    print("Factorial (iterative):", factorial_iterative(number))
