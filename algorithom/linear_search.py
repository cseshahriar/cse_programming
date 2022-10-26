"""
linear search in python
Linear Search Complexities
Time Complexity: O(n)
Space Complexity: O(1)
"""

def linear_search(data, item):
    # going through array sequentially
    for i in range(len(data)):
        if(data[i] == item):
            return i
    return -1

# 
data = [2, 4, 0, 1, 9]
item = 1

result = linear_search(data, item)

if result >= 0:
    print(f"{item} is found at index {result}")
else :
    print("{item} was not found")