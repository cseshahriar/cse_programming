n = int(input("please enter n "))
numbers = []

for i in range(n):
    imput_data = int(input("Please enter number "))
    numbers.append(imput_data)
    
def reverse(data):
    """return given list""" 
    length = len(data)
    s = length

    new_list = [None]*length

    for item in data:
        s = s - 1
        new_list[s] = item
    return new_list

print(reverse(numbers))