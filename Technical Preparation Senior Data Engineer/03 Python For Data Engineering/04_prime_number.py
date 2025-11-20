# /*
# * Write a program that checks whether a number is prime or not.
# * Once done, print the prime numbers between 1 and 100.
# */


def is_prime(n):
    """verify if the number is prime"""
    if n < 2:
        return False  # the numbers lees than 2 are no prime
    for i in range(2, int(n ** 0.5) + 1):  # We only check up to the square root of n
        
        if n % i == 0:
            
            return False  # if the number can divide for any number is no prime
    
    return True  #if we dont find the divisor is prime



# print the number 1 to 100
print("Númbers between 1 and 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")  # print the numbers in one line