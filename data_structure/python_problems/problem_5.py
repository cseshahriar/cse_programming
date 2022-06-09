n = int(input("Please enter list input numbers "))
numbers = []

for i in range(0, n):
    input_number =  int(input("Please enter a number "))
    numbers.append(input_number)

sum_ = 0
for el in numbers:
    if el % 3 == 0 or el % 5 == 0:
        print(el, end=" ")
        sum_ += el

print(" = ", sum_)