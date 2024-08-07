#From 1-100, If a number is divisible by 3 print Fizz, divisible by 5 print Buss, and divisible by 3 and 5 print FizzBuzz.

for i in range(1,101):
    if i%3 == 0 and i%5 ==0:
        print("FIZZBUZZ")
    
    elif i%3 == 0:

        print("FIZZ")
    
    elif i%5 == 0:

         print("BUZZ")

    else:

        print(i)
