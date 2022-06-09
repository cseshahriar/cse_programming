# inputs
n = int(input("Please enter a number "))
data = list(map(int, input("Enter numbers ").strip().split()))[:n] 

def get_sum(data: list):
    """ return sum of list """
    sum_ = 0
    for el in data:
        sum_ += el
    return sum_

print(get_sum(data))