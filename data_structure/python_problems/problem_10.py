n = int(input("Please enter the n "))
data = []

largest_num = 0

for i in range(n):
    input_num = int(input("Enter the number "))
    data.append(input_num)

for i in data:
    if i > largest_num:
        largest_num = i

print(largest_num)