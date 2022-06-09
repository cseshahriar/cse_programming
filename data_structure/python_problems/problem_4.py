n = int(input("Please enter list input numbers "))
numbers = []

for i in range(0, n):
    input_number =  int(input("Please enter a number "))
    numbers.append(input_number)

print("The summation is ", sum(numbers))