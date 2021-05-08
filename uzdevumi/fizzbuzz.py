x = 1
while x <= 100:
    if x % 5 == 0 and x % 7 == 0:
        print("FizzBuzz", end=", ")
    elif x % 5 == 0:
        print("Fizz", end=", ")
    elif x % 7 == 0:
        print("Buzz", end=", ")
    else:
        print(x, end=", ")
    x += 1




x = 1
while x <= 100:
    if x % 5 == 0 and x % 7 == 0:
        print("FizzBuzz", end=", ")
    elif x % 5 == 0:
        if x != 100:
            print("Fizz", end=", ")
        else:
            print("Fizz", end="")
    elif x % 7 == 0:
        print("Buzz", end=", ")
    else:
        print(x, end=", ")
    x += 1

