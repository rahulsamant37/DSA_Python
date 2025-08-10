# DSA Patterns in Python

This folder contains implementations of the most important Data Structures and Algorithms patterns in Python. Each pattern file includes detailed explanations, multiple problem implementations, and comprehensive test cases.

## Pattern Overview

### 1. Two Pointers (`001_two_pointers.py`)
**Time Complexity:** O(n) or O(n log n)  
**Space Complexity:** O(1)

Essential for problems involving sorted arrays or linked lists where you need to find pairs, triplets, or subarrays that meet certain criteria.

**Key Problems:**
- Pair with Target Sum
- Remove Duplicates
- Squaring a Sorted Array
- Triplet Sum to Zero
- Compare Strings containing Backspaces

### 2. Sliding Window (`002_sliding_window.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1) for most problems

Perfect for problems involving contiguous subarrays or substrings with specific constraints.

**Key Problems:**
- Maximum Sum Subarray of Size K
- Smallest Subarray with Sum ≥ S
- Longest Substring with K Distinct Characters
- Fruits into Baskets
- No-repeat Substring

### 3. Fast and Slow Pointers (`003_fast_slow_pointers.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Also known as Floyd's Cycle Detection Algorithm. Used for cycle detection and finding middle elements.

**Key Problems:**
- LinkedList Cycle Detection
- Start of LinkedList Cycle
- Happy Number
- Middle of the LinkedList
- Palindrome LinkedList

### 4. Merge Intervals (`004_merge_intervals.py`)
**Time Complexity:** O(n log n) due to sorting  
**Space Complexity:** O(n)

Efficient technique for dealing with overlapping intervals.

**Key Problems:**
- Merge Intervals
- Insert Interval
- Intervals Intersection
- Conflicting Appointments
- Employee Free Time

### 5. Cyclic Sort (`005_cyclic_sort.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Specialized pattern for arrays containing numbers in a given range.

**Key Problems:**
- Cyclic Sort
- Find the Missing Number
- Find all Missing Numbers
- Find the Duplicate Number
- Find all Duplicate Numbers

### 6. In-place Reversal of LinkedList (`006_in_place_reversal_linkedlist.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Essential for reversing linked list nodes without using extra memory.

**Key Problems:**
- Reverse a LinkedList
- Reverse a Sub-list
- Reverse every K-element Sub-list
- Reverse alternating K-element Sub-list
- Rotate a LinkedList

### 7. Tree Breadth First Search (`007_tree_breadth_first_search.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(w) where w is maximum width

Level-by-level tree traversal using a queue.

**Key Problems:**
- Binary Tree Level Order Traversal
- Reverse Level Order Traversal
- Zigzag Traversal
- Level Averages in a Binary Tree
- Minimum Depth of a Binary Tree

### 8. Tree Depth First Search (`008_tree_depth_first_search.py`)
**Time Complexity:** O(n)  
**Space Complexity:** O(H) where H is height

Recursive tree traversal for path-related problems.

**Key Problems:**
- Binary Tree Path Sum
- All Paths for a Sum
- Sum of Path Numbers
- Path With Given Sequence
- Count Paths for a Sum

### 9. Binary Search (`009_binary_search.py`)
**Time Complexity:** O(log n)  
**Space Complexity:** O(1) iterative, O(log n) recursive

Essential for searching in sorted collections efficiently.

**Key Problems:**
- Binary Search
- Search in Rotated Sorted Array
- Find Peak Element
- Search for Range
- Search Insert Position

### 10. Backtracking (`010_backtracking.py`)
**Time Complexity:** Often O(2^n) or O(n!)  
**Space Complexity:** O(depth of recursion)

Systematic way to explore all possible solutions by building candidates incrementally.

**Key Problems:**
- Subsets
- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver
- Word Search

### 11. Dynamic Programming (`011_dynamic_programming.py`)
**Time Complexity:** Usually O(n), O(n²), or O(n*m)  
**Space Complexity:** Often O(n) or O(n*m)

Solves complex problems by breaking them into simpler subproblems with overlapping solutions.

**Key Problems:**
- Fibonacci Numbers
- Climbing Stairs
- House Robber
- Coin Change
- Longest Common Subsequence
- Knapsack Problem

### 12. Greedy Algorithms (`012_greedy_algorithms.py`)
**Time Complexity:** Usually O(n log n) due to sorting  
**Space Complexity:** Usually O(1) or O(n)

Makes locally optimal choices at each step to find a global optimum.

**Key Problems:**
- Activity Selection
- Fractional Knapsack
- Job Scheduling
- Minimum Spanning Tree
- Gas Station
- Jump Game

## How to Use

Each pattern file is self-contained and includes:

1. **Pattern Description**: Explanation of when and how to use the pattern
2. **Time/Space Complexity**: Big O analysis
3. **Multiple Problem Implementations**: Real coding interview problems
4. **Comprehensive Test Cases**: Examples with expected outputs
5. **Helper Functions**: Utility functions for testing

### Running the Files

```bash
# Run any pattern file to see examples
python patterns/001_two_pointers.py
python patterns/002_sliding_window.py
# ... and so on
```

### Study Approach

1. **Start with fundamentals**: Begin with Two Pointers and Sliding Window
2. **Practice regularly**: Implement the problems from scratch
3. **Understand the pattern**: Focus on when to apply each technique
4. **Time complexity**: Always analyze the efficiency of your solutions
5. **Variations**: Try to solve similar problems using the same pattern

## Pattern Selection Guide

| Problem Type | Recommended Pattern |
|--------------|-------------------|
| Array pairs/triplets | Two Pointers |
| Contiguous subarray | Sliding Window |
| Cycle detection | Fast & Slow Pointers |
| Overlapping intervals | Merge Intervals |
| Missing numbers | Cyclic Sort |
| Reverse linked lists | In-place Reversal |
| Level order traversal | Tree BFS |
| Path problems in trees | Tree DFS |
| Search in sorted data | Binary Search |
| Generate combinations | Backtracking |
| Optimization problems | Dynamic Programming |
| Selection problems | Greedy Algorithms |

## Contributing

Feel free to add more problems to existing patterns or suggest new patterns that are commonly used in coding interviews.

## Resources

- Time and Space Complexity: Focus on understanding Big O notation
- Practice Platforms: LeetCode, HackerRank, CodeSignal
- Books: "Cracking the Coding Interview", "Elements of Programming Interviews"

Happy coding! 🚀
