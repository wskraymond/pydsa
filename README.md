## Set up For VSCcode
- Profile Template: https://code.visualstudio.com/docs/editor/profiles#_profile-templates
- VSCode for python: https://code.visualstudio.com/docs/python/python-quick-start
- Project structure: https://dagster.io/blog/python-project-best-practices#9-best-practices-for-structuring-python-projects
- dependency management: https://dagster.io/blog/python-packages-primer-2#managing-dependencies-the-old-way-setuppy
- Testing: https://code.visualstudio.com/docs/python/testing

## Eclipse Keymap Extensions for VSCode
- alphabotsec.vscode-eclipse-keybindings
- fabioz.vscode-eclipse-pydev-windows-keymap
- tzraeq.vscode-eclipse-win-keybindings (Ctrl + C/V for copy/paste)

***For Mac Users, disable keyboard shortcut for mission control(ctrl + left/right/up/down)***

## Developing inside a Container
The Dev Containers extension supports two primary operating models:

- You can use a container as your full-time development environment
- You can attach to a running container to inspect it.

One of the useful things about developing in a container is that you can use specific versions of dependencies that your application needs without impacting your local development environment.

- https://code.visualstudio.com/docs/devcontainers/containers
- https://code.visualstudio.com/docs/containers/overview

![alt text](doc/dev_container_chart.png?raw=true "Chart")
![alt text](doc/dev_container_edit.png?raw=true "Edit")

### 1. Working with Git
#### Git Repo in an isolated container volume (improved disk performance!)
https://code.visualstudio.com/docs/devcontainers/containers#_quick-start-open-a-git-repository-or-github-pr-in-an-isolated-container-volume

- While you can open a locally cloned repository in a container, you may want to work with an isolated copy of a repository for a PR review or to investigate another branch without impacting your work.

- Repository Containers use isolated, local Docker volumes instead of binding to the local filesystem. In addition to not polluting your file tree, local volumes have the added benefit of improved performance on Windows and macOS.

#### Git inside a Container
- https://code.visualstudio.com/remote/advancedcontainers/sharing-git-credentials
- between window and WSL: https://code.visualstudio.com/docs/remote/troubleshooting#_resolving-git-line-ending-issues-in-wsl-resulting-in-many-modified-files

### 2. Working with Docker 
#### Docker outside of Docker
https://github.com/devcontainers/templates/tree/main/src/docker-outside-of-docker
Access your host's Docker install from inside a dev container. Installs Docker extension in the container along with needed CLIs.

- While you can directly build and run the application inside the dev container you create, you may also want to test it by deploying a built container image into your local Docker Desktop instance without affecting your dev container

- using the docker-outside-of-docker feature in your devcontainer.json can help resolve the issue with Docker socket permissions.
  1. enableNonRootDocker: This setting allows Docker to be used without requiring root privileges inside the container.

  2. moby: This specifies whether to use Moby, an open-source Docker project. When set to true, it ensures that the Moby project is used.

```json
{
  "name": "Python Dev Container",
  "build": {
    "dockerfile": "Dockerfile"
  },
  "features": {
    "ghcr.io/devcontainers/features/docker-outside-of-docker:1": {
      "version": "latest",
      "enableNonRootDocker": "true",
      "moby": "true"
    }
  },
  "extensions": [
    "ms-python.python",
    "ms-python.vscode-pylance",
    "ms-azuretools.vscode-docker",
    "charliermarsh.ruff",
    "donjayamanne.python-environment-manager",
    "ms-toolsai.jupyter",
    "ms-toolsai.jupyter-keymap",
    "ms-toolsai.jupyter-renderers",
    "ms-toolsai.vscode-jupyter-cell-tags",
    "ms-toolsai.vscode-jupyter-slideshow",
    "njpwerner.autodocstring",
    "tamasfe.even-better-toml",
    "alphabotsec.vscode-eclipse-keybindings"
  ]
}
```

#### Docker in Docker
https://github.com/devcontainers/templates/tree/main/src/docker-in-docker
Creates pure "child" containers by hosting its own instance of the docker daemon inside this container. This is compared to the forementioned "docker-outside-of-docker" method that bind mounts the host's docker socket, creating "sibling" containers to the current container.

## Poetry
1. Poetry vs Maven in Java

| **Functionality**         | **Poetry Command**                         | **Maven Command**                       |
|---------------------------|--------------------------------------------|-----------------------------------------|
| **Initialize Project**    | `poetry init`                              | `mvn archetype:generate`                |
| **Add Dependency**        | `poetry add <package>`                     | `mvn dependency:resolve -Dartifact=<dependency>` |
| **Install Dependencies**  | `poetry install`                           | `mvn install`                           |
| **Update Dependencies**   | `poetry update`                            | `mvn versions:use-latest-releases`      |
| **Run Tests**             | `poetry run pytest` or `poetry run test` (`poetry run python -m unittest discover`)   | `mvn test`                              |
| **Build Project**         | `poetry build`                             | `mvn package`                           |
| **Publish Package**       | `poetry publish`                           | `mvn deploy`                            |
| **Show Dependencies**     | `poetry show`                              | `mvn dependency:list`                   |
| **Lock Dependencies**     | Automatically updates `poetry.lock` during `install` or `update` | Managed through the `pom.xml` and `versions-maven-plugin` |
| **Run Scripts**           | `poetry run <command>`                     | `mvn exec:java -Dexec.mainClass=<mainClass>` |
| **Configure Environment** | `poetry config <option> <value>`           | Managed via the `pom.xml` configuration  |

```bash
# Get virtual environment path
poetry run which python

# Run application
poetry run python app.py

# List configuration
poetry config --list
```

2. Migrate from venv to Poetry's venv

a) switch venv
```bash
# Navigate to your project directory
cd /path/to/your/project

# Initialize Poetry
poetry init

# Add existing dependencies from requirements.txt
poetry add $(cat requirements.txt)

# Install dependencies with Poetry
poetry install

# Activate Poetry environment
poetry shell
```

b) setup script for test cmd

- Edit pyproject.toml:
```script
[tool.poetry.scripts]
test = 'scripts:test'
```

- Create a scripts.py file on the root directory
```python
import subprocess

def test():
    """
    Run all unittests. Equivalent to:
    `poetry run python -u -m unittest discover`
    """
    subprocess.run(
        ['python', '-u', '-m', 'unittest', 'discover']
    )
```

- Run script:

`poetry run test`


4. poetry.lock (Dependency Locking)

The poetry.lock file locks the specific versions of dependencies and sub-dependencies that your project needs. This ensures that every time the project is installed, the exact same versions of all dependencies are used, providing consistency across different environments.

- Reproducible Builds: By locking the dependencies, poetry.lock helps in achieving reproducible builds.

- Security: It helps in preventing unintentional upgrades to newer versions of dependencies.

How It Works

a) Initial Creation or Update the current (`poetry install`)

When you run poetry install after modifying pyproject.toml:

- Check for Changes: Poetry will compare the pyproject.toml with the poetry.lock file.

- Resolve New Dependencies

- Update poetry.lock

- Install Dependencies

b) Updates (`poetry update`)

Poetry will update the dependencies to their latest compatible versions according to the specifications in pyproject.toml and then update the poetry.lock file accordingly.

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
1) i=0, j=n-1; condition: i < j
   - 125\. Valid Palindrome
   - Sorted: 259\. 3 Sum Smaller
2) i=0, j=0; condition: i<n , j<m
   - 925\. Long Pressed Name

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
   - 253\. Meeting Rooms II
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


## Understanding Comparisons
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


### Shallow copy

Syntax: a[start:stop:step] with start, stop, and step all set to their default values.

- Both a[:] and a[::] create a shallow copy of the list a.
- a[:] is a more common and concise way to copy an entire list.
- a[::] explicitly includes the step parameter, which defaults to 1, but is rarely necessary unless you want to be explicit about including all elements with a default step.

**In summary, there's no functional difference between the two in the context of copying a list; it's mainly a matter of style and readability. If you want to be explicit about the step value, you can use a[::].**


### equality
```python
original_list = [1, 2, 3, 4, 5]
copied_list = original_list[:]
print(copied_list)  # Output: [1, 2, 3, 4, 5]
print(copied_list is original_list)  # Output: False
```
- == operator: Checks for value equality (whether the contents of the objects are the same).

- is operator: Checks for identity equality (whether the variables point to the same object in memory).


## Python Binary Search vs Java's `Arrays.binarySearch`

### Overview
This guide compares how binary search is handled in Python and Java for two scenarios: exact equality checking and finding the insertion position while maintaining sorted order. We'll explore the use of `bisect_left` and `bisect_right` in Python, and `Arrays.binarySearch` in Java.

### Comparison Table

| Scenario                                      | Python (`bisect_left` and `bisect_right`)                     | Java (`Arrays.binarySearch`)                                 |
|-----------------------------------------------|--------------------------------------------------------------|--------------------------------------------------------------|
| Exact Equality Check                          | `bisect_left(arr, target)` finds the index where `target` should be inserted. Use additional checks to verify equality. | `Arrays.binarySearch(arr, target)` returns the index if found, otherwise `-(insertion point) - 1` |
| Insertion Position (maintain sorted order) using `bisect_left`    | `bisect_left(arr, target)` finds the position to insert `target` to maintain order. No additional checks required. | Negative value from `Arrays.binarySearch(arr, target)` indicates the insertion point `-(index) - 1` |
| Insertion Position (maintain sorted order) using `bisect_right`   | `bisect_right(arr, target)` finds the position to insert `target` to the right of any existing entries.  | N/A                                                          |

**Java**

Java's Arrays.binarySearch method performs an exact equality check. It searches the specified array for the specified value using the binary search algorithm. If the value is found, it returns the index of the element. If the value is not found, it returns a negative value that indicates the insertion point where the value would maintain the sorted order of the array.

Here's a quick summary:
   - Exact Equality Check: Arrays.binarySearch looks for an exact match of the specified value in the array.
   - Insertion Position: If the value is not found, the method returns a negative number, which is calculated as -(insertion point) - 1. This negative value can be used to determine the position where the value should be inserted to keep the array sorted.

```java
import java.util.Arrays;

public class BinarySearchExample {
    public static void main(String[] args) {
        int[] arr = {1, 2, 4, 6, 7, 8};
        int target = 5;
        int index = Arrays.binarySearch(arr, target);
        System.out.println("Index: " + index);  // Output: Index: -4
        int insertionPoint = -index - 1;
        System.out.println("Insertion Point: " + insertionPoint);  // Output: Insertion Point: 3
    }
}
```

**Python**

```python
bisect.bisect_left(a, x, lo=0, hi=len(a), *, key=None)
```

The returned insertion point ip partitions the array a into two slices such that all(elem < x for elem in a[lo : ip]) is true for the left slice and all(elem >= x for elem in a[ip : hi]) is true for the right slice.

Here's a quick summary:
- Use bisect_left to find the insertion point before existing identical entries.
- Use bisect_right to find the insertion point after existing identical entries.

```python
import bisect

arr = [1, 2, 4, 4, 6, 7, 8]
target = 4
index = bisect.bisect_left(arr, target)
print(index)  # Output: 2
```

```python
import bisect

arr = [1, 2, 4, 4, 6, 7, 8]
target = 4
index = bisect.bisect_right(arr, target)
print(index)  # Output: 4
```

```python
import bisect

arr = [1, 2, 4, 6, 7, 8]
target = 5
index = bisect.bisect_left(arr, target)
print(f"Index where arr[i] < {target} < arr[i+1]: {index}")  # Output: Index where arr[i] < 5 < arr[i+1]: 3
```









