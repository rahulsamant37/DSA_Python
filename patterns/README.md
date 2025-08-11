# DSA Patterns in Python

This folder contains implementations of the most important Data Structures and Algorithms patterns in Python. Each pattern is organized in its own subdirectory with focused function implementations that demonstrate core concepts clearly.

## New Structure 🎯

Each pattern now contains **individual function files** that focus on one specific algorithm or technique. This approach helps you:
- **Understand** each function's purpose clearly
- **Learn** step-by-step implementations
- **Practice** individual concepts
- **Analyze** time/space complexity for specific functions

## Pattern Overview

### 1. Two Pointers (`001_two_pointers/`)
**Time Complexity:** O(n) or O(n log n)  
**Space Complexity:** O(1)

Essential for problems involving sorted arrays or linked lists where you need to find pairs, triplets, or subarrays that meet certain criteria.

**Available Functions:**
- `two_sum.py` - Find two numbers that add up to target sum

**More Key Problems to Implement:**
- Remove Duplicates
- Squaring a Sorted Array
- Triplet Sum to Zero
- Compare Strings containing Backspaces

### 2. Sliding Window (`002_sliding_window/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1) for most problems

Perfect for problems involving contiguous subarrays or substrings with specific constraints.

**Available Functions:**
- `max_sum_subarray.py` - Maximum sum subarray of size K and minimum window with sum

**More Key Problems to Implement:**
- Longest Substring with K Distinct Characters
- Fruits into Baskets
- No-repeat Substring

### 3. Fast and Slow Pointers (`003_fast_slow_pointers/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Also known as Floyd's Cycle Detection Algorithm. Used for cycle detection and finding middle elements.

**Available Functions:**
- `cycle_detection.py` - Detect cycles in linked lists, find cycle start and length

**More Key Problems to Implement:**
- Happy Number
- Middle of the LinkedList
- Palindrome LinkedList

### 4. Merge Intervals (`004_merge_intervals/`)
**Time Complexity:** O(n log n) due to sorting  
**Space Complexity:** O(n)

Efficient technique for dealing with overlapping intervals.

**Available Functions:**
- `interval_operations.py` - Merge intervals, insert interval, find intersections

**More Key Problems to Implement:**
- Conflicting Appointments
- Employee Free Time

### 5. Cyclic Sort (`005_cyclic_sort/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Specialized pattern for arrays containing numbers in a given range.

**Available Functions:**
- `missing_numbers.py` - Find missing numbers, duplicates using cyclic sort

**More Key Problems to Implement:**
- Find all Duplicate Numbers
- Find the Corrupt Pair

### 6. In-place Reversal of LinkedList (`006_in_place_reversal_linkedlist/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(1)

Essential for reversing linked list nodes without using extra memory.

**Available Functions:**
- `reverse_operations.py` - Reverse entire list, sublists, and every K elements

**More Key Problems to Implement:**
- Reverse alternating K-element Sub-list
- Rotate a LinkedList

### 7. Tree Breadth First Search (`007_tree_breadth_first_search/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(w) where w is maximum width

Level-by-level tree traversal using a queue.

**Available Functions:**
- `level_order.py` - Level order traversal using BFS

**More Key Problems to Implement:**
- Reverse Level Order Traversal
- Zigzag Traversal
- Level Averages in a Binary Tree
- Minimum Depth of a Binary Tree

### 8. Tree Depth First Search (`008_tree_depth_first_search/`)
**Time Complexity:** O(n)  
**Space Complexity:** O(H) where H is height

Recursive tree traversal for path-related problems.

**Available Functions:**
- `path_sum.py` - Find root-to-leaf paths with given sum

**More Key Problems to Implement:**
- All Paths for a Sum
- Sum of Path Numbers
- Path With Given Sequence
- Count Paths for a Sum

### 9. Binary Search (`009_binary_search/`)
**Time Complexity:** O(log n)  
**Space Complexity:** O(1) iterative, O(log n) recursive

Essential for searching in sorted collections efficiently.

**Available Functions:**
- `search_sorted.py` - Classic binary search implementation

**More Key Problems to Implement:**
- Search in Rotated Sorted Array
- Find Peak Element
- Search for Range
- Search Insert Position

### 10. Backtracking (`010_backtracking/`)
**Time Complexity:** Often O(2^n) or O(n!)  
**Space Complexity:** O(depth of recursion)

Systematic way to explore all possible solutions by building candidates incrementally.

**Available Functions:**
- `generate_subsets.py` - Generate all possible subsets using backtracking

**More Key Problems to Implement:**
- Permutations
- Combination Sum
- N-Queens
- Sudoku Solver
- Word Search

### 11. Dynamic Programming (`011_dynamic_programming/`)
**Time Complexity:** Usually O(n), O(n²), or O(n*m)  
**Space Complexity:** Often O(n) or O(n*m)

Solves complex problems by breaking them into simpler subproblems with overlapping solutions.

**Available Functions:**
- `fibonacci.py` - Fibonacci with memoization and iterative approaches

**More Key Problems to Implement:**
- Climbing Stairs
- House Robber
- Coin Change
- Longest Common Subsequence
- Knapsack Problem

### 12. Greedy Algorithms (`012_greedy_algorithms/`)
**Time Complexity:** Usually O(n log n) due to sorting  
**Space Complexity:** Usually O(1) or O(n)

Makes locally optimal choices at each step to find a global optimum.

**Available Functions:**
- `activity_selection.py` - Select maximum non-overlapping activities

**More Key Problems to Implement:**
- Fractional Knapsack
- Job Scheduling
- Minimum Spanning Tree
- Gas Station
- Jump Game

## How to Use

Each pattern directory contains focused function files that include:

1. **Single Function Focus**: Each file demonstrates one core concept clearly
2. **Comprehensive Documentation**: Detailed explanations with complexity analysis  
3. **Practical Examples**: Real-world usage demonstrations
4. **Step-by-step Implementation**: Easy to understand code structure
5. **Educational Comments**: Learn the "why" behind each step

### Running Individual Functions

```bash
# Run any function file to see examples
python patterns/001_two_pointers/two_sum.py
python patterns/002_sliding_window/max_sum_subarray.py
python patterns/003_fast_slow_pointers/cycle_detection.py
python patterns/009_binary_search/search_sorted.py
# ... and so on
```

### Study Approach

1. **Start with basics**: Begin with Two Pointers and Sliding Window patterns
2. **One function at a time**: Focus on understanding individual implementations
3. **Run the examples**: Execute each file to see how the algorithms work
4. **Understand the pattern**: Learn when to apply each technique
5. **Expand gradually**: Add more functions to existing pattern directories
6. **Practice variations**: Implement similar problems using the same pattern

## Current Implementation Status

✅ **Completed**: Each pattern (001-012) has at least one focused function implementation  
🔄 **Expandable**: You can add more function files to any pattern directory  
📚 **Educational**: Each file is designed for learning and understanding  

### Quick Start Guide

1. **Choose a pattern** you want to learn
2. **Navigate to its directory** (e.g., `001_two_pointers/`)
3. **Run the function file** to see it in action
4. **Study the implementation** and comments
5. **Try variations** or add new functions to the same directory

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

Feel free to add more function files to existing pattern directories or suggest new patterns that are commonly used in coding interviews.

### Adding New Functions

To add a new function to any pattern:

1. **Create a new .py file** in the appropriate pattern directory
2. **Focus on one function** per file for clarity
3. **Include comprehensive documentation** with complexity analysis
4. **Add practical examples** showing how the function works
5. **Follow the established naming convention** (descriptive_name.py)

Example structure for new functions:
```python
"""
Pattern Name - Function Purpose
===============================

Brief description of what the function does.

Time Complexity: O(?)
Space Complexity: O(?)
"""

def your_function(parameters):
    """
    Detailed function documentation.
    
    Args:
        param1: Description
        param2: Description
        
    Returns:
        Description of return value
    """
    # Implementation here
    pass

def example_usage():
    """Demonstrate the function"""
    # Example code here
    pass

if __name__ == "__main__":
    example_usage()
```

## Resources

- Time and Space Complexity: Focus on understanding Big O notation
- Practice Platforms: LeetCode, HackerRank, CodeSignal
- Books: "Cracking the Coding Interview", "Elements of Programming Interviews"

Happy coding! 🚀
