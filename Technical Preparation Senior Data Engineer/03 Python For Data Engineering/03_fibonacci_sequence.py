# /*
# * Write a program that prints the first 50 numbers of the Fibonacci sequence
# * starting at 0.
# * - The Fibonacci series consists of a sequence of numbers in which
# * the next one is always the sum of the two previous ones.
# * 0, 1, 1, 2, 3, 5, 8, 13...
# */

# Define a function to generate the first 'n' Fibonacci numbers
def fibonacci(n):
    """Generate the first 'n' numbers in the Fibonacci sequence."""
    
    # Initialize the first two Fibonacci numbers
    a, b = 0, 1
    
    # Use a loop to generate the sequence
    for _ in range(n):
        yield a  # Yield the current number (allows the function to act as a generator)
        a, b = b, a + b  # Update values: shift 'a' to 'b', and 'b' to 'a + b'

#all: it was my fist attempt i use chat gpt to solve a part