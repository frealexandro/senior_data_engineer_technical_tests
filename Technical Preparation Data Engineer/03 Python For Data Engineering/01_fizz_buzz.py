#! Write a program that prints to the console (using print)  

#! the numbers from 1 to 100 (both included and with a line break  
#! between each print), replacing the following:  
#! Multiples of 3 with the word "fizz".  
#! Multiples of 5 with the word "buzz".  
#! Multiples of both 3 and 5 with the word "fizzbuzz".  



def run():
    
    for i in range(1,101):
        if i % 3 == 0 and i % 5 == 0 :
            print("fizzbuzz") 
        if i % 3 == 0:
            print("fizz")
        if i % 5 == 0:
            print("buzz")


if __name__ == "__main__":
    run()

#all: it was my fist attempt i use chat gpt to solve a part