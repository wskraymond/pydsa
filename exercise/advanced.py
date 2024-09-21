# Nested List Comprehension
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
    ]

# tranpose matrix
[[row[i] for row in matrix] for i in range(4)]

# Unpacking Argument Lists
'''
be unpacked for a function call requiring separate positional arguments. 
For instance, the built-in range() function expects separate start and stop arguments.
If they are not available separately, write the function call with the *-operator to unpack the arguments out of a list or tuple:
'''
list(range(3, 6))            # normal call with separate arguments
args=[3,6]
list(range(*args))            # call with arguments unpacked from a list

list(zip(*matrix))             # it is equivalent to transpose of matrix above

# list_slice = original_list[start:stop:step]
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
my_list[::2]   # selects every second element from the list.
my_list[::-1]  # reverses the list.
my_list[1:8:2] # selects every second element from index 1 to 7.


# Using my_list[:] in Python creates a shallow copy of the entire list.
# This means that a new list object is created, but the elements themselves are not copied; 
# they are still references to the same objects as in the original list.
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print(copied_list)  # Output: [1, 2, 3, 4, 5]
print(copied_list is original_list)  # Output: False

'''
 while my_list[:] on the right side creates a shallow copy, 
 my_list[:] on the left side is used to modify the contents of the existing list in place. 
 They serve different purposes but are consistent in their behavior within their respective contexts
'''
my_list = [5, 6, 7, 8]
my_list[:] = [1, 2, 3, 4]
print(my_list)  # Output: [1, 2, 3, 4]


