a = int(input("Please enter a number "))
b = int(input("Please enter a number "))

if b != 0:
    if a % b == 0:
        print(a, " is divisible by ", b)
    else:
        print(a, " is not divisible ", b, " and remainder is ", a % b)