# binary search
def binary_search(element_list: list, item):
    first = 0
    last = len(element_list) - 1
    found = False
    
    while (first <= last and not found):
        mid = (first + last) // 2
        if element_list[mid] == item:
            found = True
        elif item < element_list[mid]:
            last = mid -1
        else:
            first = mid + 1
    return found

print(binary_search([1,2,3,5,8], 6)) # must sorted
print(binary_search([1,2,3,5,8], 5))