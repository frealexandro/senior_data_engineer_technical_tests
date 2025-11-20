# /*
# * Write a program that prints the first 50 numbers of the Fibonacci sequence
# * starting at 0.
# * - The Fibonacci series consists of a sequence of numbers in which
# * the next one is always the sum of the two previous ones.
# * 0, 1, 1, 2, 3, 5, 8, 13...
# */

def fibonacci(n):
    a, b = 0, 1

    for _ in range(n):
    
        yield a
    
        a, b = b, a + b

print(list(fibonacci(50)))



#all: it was my second attempt i use chat gpt to solve a part