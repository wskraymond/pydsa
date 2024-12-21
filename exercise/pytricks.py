# 3 version of loops with same output of j
N = 10
for i in range(N-1,-1,-1):	#N-1……….0  => total loop N times
    for j in range(0,i+1):    #0…N-1, 0…..N-2, 0…..N-3,....., 0
        print(j)

for i in range(N, 0, -1):     #N………1         => total loop N times
    for j in range(0, i):       #0….N-1, 0…..N-2,0…...N-3,....., 0
        print(j)

for i in reversed(range(N)):    #range(N) -> 0…….N-1 ->reversed -> N-1……0 
    for j in range(i + 1):       #0…N-1, 0…..N-2, 0…..N-3,....., 0
        print(j)

#for - else
for num in range(5):
    if num == 3:
        break
else:
    print("Loop completed without break")

#itertools.accumulate
#useful for computing prefix sums, products
import itertools

data = [1, 2, 3, 4]
result = list(itertools.accumulate(data))
print(result)  # Output: [1, 3, 6, 10]

#tuple + @lru_cache
#The @lru_cache decorator from functools is used for memoization. Since lists are mutable and cannot be hashed, you can convert them to tuples.
from functools import lru_cache

# Define the memoized function
@lru_cache(maxsize=None)
def sum_of_list(numbers):
    # Convert the list to a tuple to make it hashable
    numbers = tuple(numbers)
    return sum(numbers)

# Test the function
list1 = [1, 2, 3, 4, 5]
list2 = [5, 4, 3, 2, 1]

# First call with list1
print(sum_of_list(list1))  # Output: 15

# Second call with list1 (should be memoized)
print(sum_of_list(list1))  # Output: 15 (retrieved from cache)

# First call with list2
print(sum_of_list(list2))  # Output: 15

# Modify list1 and call again
list1.append(6)
print(sum_of_list(list1))  # Output: 21 (not memoized, new calculation)



# defaultdict
# create a defaultdict named char_count with int as the default factory. This means that any missing key will have a default value of 0
from collections import defaultdict

def count_characters(s):
    # Create a defaultdict with int as the default factory
    char_count = defaultdict(int)
    
    # Iterate over each character in the string
    for char in s:
        char_count[char] += 1  # if_none(count,0) + 1
    
    return char_count

# Once a key is accessed in the default dict, key-default value will be initialized to it.
m = defaultdict(int)
print('a' in m) # output False
m['a']
print('a' in m) # output True

# Test the function
input_string = "hello world"
result = count_characters(input_string)

# Print the result
for char, count in result.items():
    print(f"'{char}': {count}")


# Neighbors and Bound Checking in a Matrix
# check the four possible neighbors (up, down, left, right) using a loop.
def process_neighbors(matrix):
    rows = len(matrix)
    cols = len(matrix[0])
    
    for i in range(rows):
        for j in range(cols):
            # Process the current cell (i, j)
            print(f"Processing cell ({i}, {j}) with value {matrix[i][j]}")
            
            # Check and process neighbors
            for I, J in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                if 0 <= I < rows and 0 <= J < cols:
                    print(f"  Neighbor ({I}, {J}) with value {matrix[I][J]}")

# Define the grid (matrix)
rooms = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Call the function
process_neighbors(rooms)


# max Function with key
#  take a key argument to determine the maximum based on a custom criterion.
print(max([10, 25, 11, 19], key=lambda x: x % 10))  # Output: 19

# Multiple Comparison Operators
a = 15
if 10 < a < 20:
    print("a is between 10 and 20")

# ~ Operator
# a generator expression inside the all function to compare characters from the start and end of the string
'''
    1. all, checks if every element is your list is True
    2. any, if at least one element in a list is True.
'''
# The ~i expression is equivalent to -(i + 1), which accesses the character from the end of the string
'''
Python uses two’s complement representation for integers.
For i = 2:
    Binary representation: 0010
    Bitwise NOT: 1101 (which is -3 in two’s complement)
    ~2 = -3

For the string "racecar" => 0, 1,2,middle,-3,-2,-1 
Range for Loop: range(len(s) // 2) = range(3) (i.e., 0, 1, 2)
(i = 2):
    Compare s[2] with s[~2] (i.e., s[2] with s[-3])
    s[2] = 'c', s[-3] = 'c' (they are equal)

For i = 0, ~i = -1 (last character)
For i = 1, ~i = -2 (second last character)
For i = 2, ~i = -3 (third last character)
'''
def is_palindrome(s):
    # Check if the string is a palindrome
    return all(s[i] == s[~i] for i in range(len(s) // 2))

# Test the function
test_strings = ["racecar", "hello", "level", "world", "madam"]

for s in test_strings:
    print(f"'{s}' is a palindrome: {is_palindrome(s)}")


# functools.reduce function 
# more flexible and can handle more complex accumulations. It applies a binary function cumulatively to the items of an iterable, from left to right, so as to reduce the iterable to a single value
from functools import reduce

data = [1, 2, 3, 4, 5]

# Function to find the maximum product of two consecutive elements
def max_product(acc, x):
    return max(acc, x[0] * x[1])

# Create pairs of consecutive elements
pairs = zip(data, data[1:])

# Use reduce to find the maximum product
result = reduce(max_product, pairs, float('-inf'))
print(result)  # Output: 20 (4 * 5)

