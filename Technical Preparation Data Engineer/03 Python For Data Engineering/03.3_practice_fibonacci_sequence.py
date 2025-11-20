# /*
# * Write a program that prints the first 50 numbers of the Fibonacci sequence
# * starting at 0.
# * - The Fibonacci series consists of a sequence of numbers in which
# * the next one is always the sum of the two previous ones.
# * 0, 1, 1, 2, 3, 5, 8, 13...
# */


#declarate the function
def fibonacci(n):

    #define fist number 0 ,1 
    a,b = 0,1


    #make the for to iterate the range in this case 50 
    for _ in range (n):

        #use generator to implement the sequence 
        yield a

        #assing the formula fibonacci to variables b, a + b
        a,b = b,a + b

#transform a function before put the number
print(list(fibonacci(50)))