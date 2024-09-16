'''Implement a program that calculates the Fibonacci sequence up to a specified number using both iterative and recursive approaches.'''

def fibonacci_iterative(n):
    sequence = []
    a, b = 0, 1
    while a <= n:
        sequence.append(a)
        a, b = b, a + b
    return sequence

def fibonacci_recursive(n, a=0, b=1, sequence=None):
    if sequence is None:
        sequence = []
    if a > n:
        return sequence
    sequence.append(a)
    return fibonacci_recursive(n, b, a + b, sequence)

max_value = int(input("Enter the maximum value for the Fibonacci sequence: "))

iterative_sequence = fibonacci_iterative(max_value)
recursive_sequence = fibonacci_recursive(max_value)

print(f"Fibonacci sequence up to {max_value} (Iterative): {iterative_sequence}")
print(f"Fibonacci sequence up to {max_value} (Recursive): {recursive_sequence}")
