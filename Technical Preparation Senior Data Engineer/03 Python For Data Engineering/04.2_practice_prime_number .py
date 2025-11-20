# /*
# * Write a program that checks whether a number is prime or not.
# * Once done, print the prime numbers between 1 and 100.
# */

#def function prime number 
def is_prime(n):

    # discard the nuimber less two
    if n < 2:
        return False
    
    # iterate i in the range of formula 2 int (n**0.5)+1
    for i in range (2,int(n**0.5)+1):

        #discard any number that the root is 0 divided by any number  
        if n % i == 0:

            return False
        
    # retur tru if the number pass the filters    
    return True


print("Numbers 1 to 100")

#make for in range over function is prime
for num in range (1,100):
    
    if is_prime(num):
    #print the number with space
        print(num, end=" ")

