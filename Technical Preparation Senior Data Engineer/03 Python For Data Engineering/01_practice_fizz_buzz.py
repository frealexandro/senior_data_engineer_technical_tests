
#! Write a program that prints to the console (using print)
#! the numbers from 1 to 100 (both included and with a line break between each print),
#! replacing the following:
#! Multiples of 3 with the word "fizz".
#! Multiples of 5 with the word "buzz".
#! Multiples of both 3 and 5 with the word "fizzbuzz".


def fizzbuzz_function():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz_function()


# all: it was my second attempt, I had an error in the code so I used chat gpt