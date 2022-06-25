# Java static array
# int scores[] = new int[5];
# scores[0] = 32;
# scores[1] = 25;
# scores[2] = 12;
# scores[3] = 98;
# scores[4] = 56;

# C++ static array
# int scores[5] = {32, 25, 12, 98, 56};

# C static array
# static int scores[] = {32, 25, 12, 98, 56};

"""
Time Complexities of Python Dynamic Array Operations

    Lookup — O(1)

    Append — A(1)

    Prepend — O(N)

    Insert — O(N)

    Delete/remove — O(N)

    Popright — O(1)

    List.pop(0) — O(N)
"""

my_list = [1, 2, 3, "EduCBA", "makes learning fun!"]
print(my_list)


"""
1. Append
The append() method is used to add elements at the end of the list. 
This method can only add a single element at a time. To add multiple elements, the append() method can be used inside a loop.
"""

my_list.append(4)  # insert in end of list
my_list.append(5)


for i in range(4, 10):
    my_list.append(i)


print(my_list)

"""
2. extend()
The extend() method is used to add more than one element at the end of the list.
Although it can add more than one element, unlike append(),
it adds them at the end of the list like append().
"""
my_list.extend([4, 5, 6])  # append multiple vales
print(my_list)


"""
3. insert()
The insert() method can add an element at a given position in the list. Thus,
unlike append(), it can add elements at any position, but like append(), 
it can add only one element at a time. This method takes two arguments. 
The first argument specifies the position, and the second argument specifies
the element to be inserted.
"""

my_list.insert(3, 4) # position, value
my_list.insert(4, 5)
my_list.insert(5, 6)
print(my_list)

"""
4. remove()
The remove() method is used to remove an element from the list. In the case of
 multiple occurrences of the same element, only the first occurrence is removed.
"""
my_list.remove('makes learning fun!')  # value removed, can multiple
my_list.insert(4, 'makes')
my_list.insert(5, 'learning')
my_list.insert(6, 'so much fun!')
print(my_list)

"""
5. pop()
The method pop() can remove an element from any position in the list.
 The parameter supplied to this method is the index of the element to be removed.
"""
my_list.pop(4)  # index
print(my_list)

my_list.pop()  # last
print(my_list)

"""
6. slice
The slice operation is used to print a section of the list. The slice operation
 returns a specific range of elements. It does not modify the original list.
"""

print(my_list[:4])  # prints from beginning to end index
print(my_list[2:])  # prints from start index to end of list
print(my_list[2:4])  # prints from start index to end index
print(my_list[:])   # prints from beginning to end of list


"""
7. reverse()
The reverse() operation is used to reverse the elements of the list. 
This method modifies the original list. To reverse a list without modifying 
the original one, we use the slice operation with negative indices. Specifying 
negative indices iterates the list from the rear end to the front end of the list.
"""

print(my_list[::-1])  # does not modify the original list
print(my_list)

rev_my_list = my_list.reverse()     # modifies the original list
print(rev_my_list)


# 8. len()
print(len(my_list))


# 9. min() & max()
print(max(my_list))
print(min(my_list))

# 10. count()
print(my_list.count(3))  # 3 occurrences times

# 11. concatenate
your_list = [4, 5, 'Python', 'is fun!']
print(my_list + your_list)

# 12. multiply 
print(my_list * 2)

# 13. index() The index() method returns the position of the first occurrence of the given element
print(my_list.index('EduCBA'))            # searches in the whole list
print(my_list.index('EduCBA', 0, 2))     # searches from 0th to 2nd position


# 14. sort() 
yourList = [4, 2, 6, 5, 0, 1]

yourList.sort()  # ascending
print(yourList)

yourList.sort(reverse=True) # descending
print(yourList)
