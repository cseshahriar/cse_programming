# inputs
n = int(input("Please enter a number "))
data = list(map(int, input("Enter numbers ").strip().split()))[:n] 

def get_odd_numbers(numbers):
    for element in numbers:
        if element % 2 != 0:
            print(element, end=" ")

get_odd_numbers(data)