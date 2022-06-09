n = int(input("Enter a number for n"))
data = []

for i in range(n):
    input_data = int(input("Enter a number "))
    data.append(input_data)


if data[1] != 0:
    if data[0] % data[1] == 0:
        print(data[0], " is divisible by ", data[1])
    else:
        print(data[0], " is not divisible ", data[1], " and remainder is ", data[0] % data[1])