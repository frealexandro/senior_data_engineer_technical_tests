# /*
# * Write a program that checks whether a number is prime or not.
# * Once done, print the prime numbers between 1 and 100.
# */


#def the function of is prime 
def is_prime(n):

    #discard the numbers less thant 2 
    if n < 0 :

        
        return False 
    
    #we iterate over the formula where the root is square  the formula range(2,int(n**0.05)+1): 
    for i in range(2,int(n**0.05)+1):

        #discard the number if the module root is equal to 0 
        if n % i == 0 :

            return False
        
    
    return True





#iterate the numbers prime 

for i in range (1,100):

    if is_prime(i):

        print(i, end=" ")
