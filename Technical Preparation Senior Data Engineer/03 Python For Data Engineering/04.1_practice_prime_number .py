# /*
# * Write a program that checks whether a number is prime or not.
# * Once done, print the prime numbers between 1 and 100.
# */




def is_prime(n):

    if n < 2 :
        return False
    
    for i in range (2, int (n** 0.5) + 1):

        if n % i == 0:

            return False
    
    return True


# print 1 to 100
print("Numbers between 1 and 100")

for num in range (1,101):
    if is_prime(num):
        print(num,end=" ")