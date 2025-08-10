"""
003 - Time Complexity Analysis Guide
====================================

Comprehensive guide to understanding time and space complexity analysis.

This module provides examples and explanations of complexity analysis.
"""


def explain_big_o_notation():
    """Explain Big O notation with examples"""
    explanation = """
BIG O NOTATION GUIDE:
====================

O(1) - Constant Time
-------------------
- Array access by index: arr[i]
- Hash table lookup (average case)
- Stack push/pop operations

Examples:
- Accessing first element of array
- Checking if number is even/odd
- Basic arithmetic operations

O(log n) - Logarithmic Time
--------------------------
- Binary search in sorted array
- Tree operations in balanced trees
- Finding element in heap

Examples:
- Binary search algorithm
- BST search in balanced tree
- Heap insert/delete operations

O(n) - Linear Time
-----------------
- Linear search through array
- Traversing linked list
- Single loop through data

Examples:
- Finding maximum in unsorted array
- Printing all elements in list
- Checking if array contains duplicates

O(n log n) - Linearithmic Time
-----------------------------
- Efficient sorting algorithms
- Merge sort, heap sort
- Many divide-and-conquer algorithms

Examples:
- Merge sort algorithm
- Quick sort (average case)
- Building heap from array

O(n²) - Quadratic Time
---------------------
- Nested loops over data
- Simple sorting algorithms
- Comparing all pairs

Examples:
- Bubble sort, selection sort
- Matrix multiplication
- Finding all pairs in array

O(2^n) - Exponential Time
------------------------
- Recursive algorithms without memoization
- Generating all subsets
- Solving NP-complete problems

Examples:
- Naive fibonacci recursive
- Traveling salesman problem
- Subset sum (brute force)
    """
    print(explanation)


def compare_algorithms():
    """Compare time complexities of different algorithms"""
    comparisons = """
ALGORITHM COMPLEXITY COMPARISON:
===============================

Searching Algorithms:
--------------------
- Linear Search:    O(n)
- Binary Search:    O(log n)
- Hash Lookup:      O(1) average

Sorting Algorithms:
------------------
- Bubble Sort:      O(n²)
- Selection Sort:   O(n²)
- Insertion Sort:   O(n²)
- Merge Sort:       O(n log n)
- Quick Sort:       O(n log n) average, O(n²) worst
- Heap Sort:        O(n log n)

Tree Operations:
---------------
- BST Search:       O(log n) average, O(n) worst
- AVL Search:       O(log n) guaranteed
- Tree Traversal:   O(n)

Graph Algorithms:
----------------
- BFS/DFS:          O(V + E)
- Dijkstra:         O((V + E) log V)
- Floyd-Warshall:   O(V³)

Space Complexity:
----------------
- In-place algorithms:     O(1)
- Recursive algorithms:    O(depth)
- Dynamic programming:     O(problem size)
    """
    print(comparisons)


def analyze_complexity_examples():
    """Provide examples of complexity analysis"""
    examples = """
COMPLEXITY ANALYSIS EXAMPLES:
=============================

Example 1: Finding Maximum
--------------------------
def find_max(arr):
    max_val = arr[0]        # O(1)
    for i in range(1, len(arr)):  # O(n)
        if arr[i] > max_val:      # O(1)
            max_val = arr[i]      # O(1)
    return max_val              # O(1)

Time: O(n), Space: O(1)

Example 2: Nested Loops
-----------------------
def print_pairs(arr):
    for i in range(len(arr)):     # O(n)
        for j in range(len(arr)): # O(n)
            print(arr[i], arr[j])  # O(1)

Time: O(n²), Space: O(1)

Example 3: Binary Search
------------------------
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:          # O(log n)
        mid = (left + right) // 2  # O(1)
        if arr[mid] == target:     # O(1)
            return mid
        elif arr[mid] < target:    # O(1)
            left = mid + 1
        else:
            right = mid - 1
    return -1

Time: O(log n), Space: O(1)
    """
    print(examples)


def main():
    """Main function to demonstrate complexity analysis"""
    print("=== Time Complexity Analysis Guide ===")
    
    print("\n1. Big O Notation:")
    explain_big_o_notation()
    
    print("\n2. Algorithm Comparisons:")
    compare_algorithms()
    
    print("\n3. Analysis Examples:")
    analyze_complexity_examples()


if __name__ == "__main__":
    main()
