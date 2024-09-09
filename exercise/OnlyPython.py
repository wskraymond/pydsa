#n  # try to access an undefined variable
#Traceback (most recent call last):
#File "<stdin>", line 1, in <module>
#NameError: name 'n' is not defined

# None is null (absence of value)
n = 4
n = None
print("n =", n)

# Multiple assignments for dynamic type
n, m = True, "abc"
n, m, z = 0.125, 0, False

# Parentheses needed for multi-line conditions.
# and = &&
# or  = ||
n, m = 1, 2
if ((n > 2 and
     n != m) or n == m):
    n += 1

n = 5
while n < 5:
    print(n)
    n += 1

# Looping from i = 0 to i = 4
for i in range(5):
    print(i)

# Looping from i = 2 to i = 5
for i in range(2, 6):
    print(i)

# Looping from i = 5 to i = 2
for i in range(5, 1, -1):
    print(i)

################Math#############################

# Division is decimal by default
print(5 / 2)

# Double slash rounds down
print(5 // 2)

# CAREFUL: most languages round towards 0 by default
# So negative numbers will round down
print(-3 // 2)

# A workaround for rounding towards zero
# is to use decimal division and then convert to int.
print(int(-3 / 2))

# Modding is similar to most languages
print(10 % 3)

# Except for negative values
print(-10 % 3)

# To be consistent with other languages modulo
import math
#from multiprocessing import heap

print(math.fmod(-10, 3))

# More math helpers
print(math.floor(3 / 2))
print(math.ceil(3 / 2))
print(math.sqrt(2))
print(math.pow(2, 3))


###Python uses 64 bit floats (Double precision IEEE754) and unlimited (well, as much as your computer can handle) integer lengths

# Max / Min Int
float("inf")
float("-inf")

# Python numbers are infinite so they never overflow
print(math.pow(2, 200))

# But still less than infinity
print(math.pow(2, 200) < float("inf"))
