## Set up For VSCcode
- Profile Template: https://code.visualstudio.com/docs/editor/profiles#_profile-templates
- VSCode for python: https://code.visualstudio.com/docs/python/python-quick-start
- Project structure: https://dagster.io/blog/python-project-best-practices#9-best-practices-for-structuring-python-projects
- dependency management: https://dagster.io/blog/python-packages-primer-2#managing-dependencies-the-old-way-setuppy
- Testing: https://code.visualstudio.com/docs/python/testing

## Developing inside a Container
- https://code.visualstudio.com/docs/devcontainers/containers
- https://code.visualstudio.com/docs/containers/overview

![alt text](doc/dev_container_chart.png?raw=true "Chart")
![alt text](doc/dev_container_edit.png?raw=true "Edit")


***For Java developers who're gonna learn python***

## Python’s standard library 
### Built-in exceptions
It has a range of built-in exceptions, similar in spirit to Java's. Some common ones include:

- AttributeError: When an attribute reference or assignment fails.

- TypeError: When an operation or function is applied to an object of inappropriate type.

- ValueError: When a function gets an argument of the right type but an inappropriate value.

- KeyError: Raised when a dictionary key is not found.

- IndexError: When a sequence subscript is out of range.

- NameError: When a local or global name is not found.

- ImportError: When an import statement fails.

- IOError / OSError: Base classes for exceptions raised by I/O operations.

- FileNotFoundError: When a file or directory is requested but doesn’t exist.

- ZeroDivisionError: When division or modulo by zero takes place.

- RuntimeError: When an error occurs that doesn’t fall under other categories

### Dats structure 
#### Java's thing
Several built-in data structures and related design patterns that parallel Java's interfaces and generics

1. Comparable-like:
   - __lt__, __le__, __eq__, __ne__, __gt__, __ge__: Special methods for comparison, similar to Java's Comparable.

2. Iterable/Iterator:

   - __iter__, __next__: Special methods that make objects iterable, similar to Java's Iterable and Iterator.

3. Collections:

   - List (list): Dynamic arrays.

   - Tuple (tuple): Immutable sequences.

   - Set (set, frozenset): Unordered collections of unique elements.

```python
# An immutable set
fs = frozenset([1, 2, 3, 2])
```

   - Dictionary (dict): Key-value mappings.

3. Generic-like with Type Hints:

   - Type Hints (typing module): Provides generics-like behavior, e.g., List[int], Dict[str, int].

4. Queue/Deque:

   - collections.deque: Double-ended queue, supports adding and removing elements from either end efficiently.

5. Heap:

   - heapq: Implements a heap queue, useful for priority queues.

6. OrderedDict:

   - collections.OrderedDict: Dictionary that maintains the order of items.

7. enum
   - A module for creating enumerations, a set of symbolic names bound to unique, constant values
```python
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```

#### Pythonic Stuff
a few of the unique Python data structures that do not have direct analogs in Java

1. DefaultDict:

   - collections.defaultdict: Similar to Java's HashMap with a default value for missing keys.

2. Counter:

   - collections.Counter: For counting hashable objects.

```python
from collections import Counter
c = Counter(['a', 'b', 'b', 'c', 'a', 'b'])
sorted(c.elements()) # ['a', 'a', 'b', 'b', 'b', 'c']
c.total() #6

count1 = Counter({'apple': 3, 'banana': 2})
count2 = Counter({'apple': 1, 'banana': 1, 'orange': 1})
combined = count1 + count2
print(combined)  # Output: Counter({'apple': 4, 'banana': 3, 'orange': 1})

```

   - Counters support rich comparison operators for equality, subset, and superset relationships: ==, !=, <, <=, >, >=. All of those tests treat missing elements as having zero counts so that Counter(a=1) == Counter(a=1, b=0) returns true.

```python
c = Counter(a=3, b=1)
d = Counter(a=1, b=2)
c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
c == d                      # equality:  c[x] == d[x]
False
c <= d                      # inclusion:  c[x] <= d[x]
False
```

```python
from collections import Counter

# Example Counters
s = Counter({'a': 2, 'b': 1})
p = Counter({'a': 3, 'b': 1, 'c': 2})

# Use the comparison operator to check inclusion
result = s <= p
print(result)  # Output: True
```

3. NamedTuple:

   - collections.namedtuple: Lightweight object types with named fields.

```python
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
```

4. itertool

   - A module that provides a set of fast, memory-efficient tools for working with iterators.
```python
import itertools
permutations = itertools.permutations([1, 2, 3])
```

## A Curated List of 80+ Questions

>***Array/List***
#### Circular Array
- 1752\. Check if Array Is Sorted and Rotated

#### Cyclic Sort
- Cyclic Swap: 442\. Find All Duplicates in an Array

#### Fast-slow Pointers
- 142\. Linked List Cycle II

#### in-place operation
1) Remove Duplicate
   - 26\. Remove Duplicates from Sorted Array
2) Reverse Linked List
   - 234\. Palindrome Linked List
3) Reverse Array
   - 189\. Rotate Array
4) Merge array
   - 88\. Merge Sorted Array

>***Binary***
#### Binary Search
- 69\. Sqrt(x)

#### Heaps
1) Min&Max Heaps
   - 295\. Find Median from Data Stream
2) Top K Elements
   - 1086\. High Five
   - 973\. K Closest Points to Origin
3) K Way Merge
   - 23\. Merge k Sorted Lists

>***Graph Search & Traversal Ordering***
#### Trie(Prefix Tree)
- 208\. Implement Trie (Prefix Tree)

#### Binary Tree
1) DFS
   - Pe-order
   - In-order
   - Post-order: 124\. Binary Tree Maximum Path Sum
2) Binary Search Tree
   - In-order: 230\. Kth Smallest Element in a BST
3) BFS
   - 104\. Maximum Depth of Binary Tree
4) Serialize and Deserialize BT
   - 297\. Serialize and Deserialize Binary Tree

#### Topological Sort
- 269\. Alien Dictionary

#### Graph
1) Directed
   1) DAG
      1) DFS
         - DAG version: 797\. All Paths From Source to Target
      2) BFS
   2) Non-DAG
      1) Bellman Ford(BF)
         - 787\. Cheapest Flights Within K Stops
      2) BFS
      3) DFS
         - Non-DAG version: All Paths From Source to Target (https://www.geeksforgeeks.org/find-paths-given-source-destination/)
         - 1059\. All Paths from Source Lead to Destination
      4) Dijkstra
         - 743\. Network Delay Time
2) Undirected
   1) BFS
      - 200\. Number of Islands
      - 127\. Word Ladder
      - 126\. Word Ladder II
   2) DFS
      - 417\. Pacific Atlantic Water Flow
   3) Union Find
      - 323\. number of connected components in an undirected graph
3) Clone
- 133\. Clone Graph

>***Bruteforce***
#### Backtracking
1) Combination
   - Bound: 77\. Combinations
   - Unbound: 39\. Combination Sum 
2) Directions: 
   - 79\. Word Search
3) Permutation: 
   - 46\. Permutations
4) Subsets:
   - unique number: 78\. Subsets
   - duplicate number: 90\. Subsets II
5) Matrix: 
   - 37\. Sudoku Solver

#### DP
1) Direction
    - 64\. Minimum Path Sum
2) Fibonacci
    - 213\. House Robber II
    - 1911\. Maximum Alternating Subsequence Sum
3) Knapsack
   1) Unbound
       - 518\. Coin Change II
       - 983\. Minimum Cost For Tickets
   2) Bound
       - 416\. Partition Equal Subset Sum
       - 494\. Target Sum
4) Longest Common
      - 1143\. Longest Common Subsequence
      - 300\. Longest Increasing Subsequence
5) Palindrome
   - 516\. Longest Palindromic Subsequence

6) Word Break
   - 91\. Decode Ways
   - 139\. Word Break
   
>***Non-Bruteforce***
#### Prefix sum
- 523\. Continuous Subarray Sum
- 560\. Subarray Sum Equals K

#### Two pointers
1) Valid Palindrome
   - 125\. Valid Palindrome
2) Sum 
   - 259\. 3 Sum Smaller

#### Max Subarray (Kadane)
1) Sum
   - 134\. Gas Station
   - 121\. Best Time to Buy and Sell Stock
2) Product
   - 152\. Maximum Product Subarray
   
#### Sliding Window
1) Longest Substring
   - 340\. longest substring with at most k distinct characters
2) Target Substring
   - 567\. Permutation in String
3) Minimum Window
   - 76\. Minimum Window Substring

#### Stack 
1) Parenthesis
   - 1249\. Minimum Remove to Make Valid Parentheses
   - 32\. Longest Valid Parentheses

2) Monotonic Stack
   1) Next Greater
      - 739\. Daily Temperatures
      - 496\. Next Greater Element I
   2) Sub-array
      - 907\. Sum of Subarray Minimums
      - 1856\. Maximum Subarray Min-Product
   3) Sliding Window
      - 239\. Sliding Window Maximum

#### Greedy
- Sort: 881\. Boats to Save People
- Heap: 846\. Hand of Straights
- Set: 1899\. Merge Triplets to Form Target Triplet
- BFS: 45\. Jump Game II

#### Interval
1) Scheduling
   - 435\. Non-overlapping Intervals
2) Merge
   - 57\. Insert Interval
   
>***Others***
#### Math
- 166\. Fraction to Recurring Decimal

#### Design
- 146\. LRU Cache

>***Question Series***
- Stone Game
- Best Time to Buy and Sell Stock
- Jump Game


## Understanding Infinity Comparisons
### Distinct Value:

float('inf') represents a special value that is distinct from all finite numbers. In Python, this value is conceptually treated as an unbounded positive value. So, comparisons with float('inf') are straightforward and don't require tolerances because infinity is inherently larger than any finite number.

### Type Coercion:

When comparing an integer to float('inf'), Python automatically handles the type coercion seamlessly. Python's dynamic typing allows it to compare integers and floats directly without extra steps.

```python 
positive_infinity = float('inf')
large_integer = 10**308

print(positive_infinity > large_integer)  # Output: True
```

### No Rounding Errors
- When you compare floating-point numbers like 1.0 / 3.0 and 0.3333333333333333, you deal with rounding errors and precision issues inherent to floating-point arithmetic. This is why tolerances are necessary for meaningful comparisons.

- In contrast, comparing an integer to float('inf') does not involve rounding or precision errors. The nature of infinity ensures that it is always clearly greater than any finite value, eliminating the need for tolerance-based comparisons.









