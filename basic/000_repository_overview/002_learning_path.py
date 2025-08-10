"""
002 - Learning Path Guide
=========================

Recommended learning sequence for mastering data structures and algorithms.

This module outlines the progressive learning path through the repository.
"""


def print_learning_path():
    """Print the recommended learning sequence"""
    learning_path = """
RECOMMENDED LEARNING PATH:
=========================

Phase 1: FUNDAMENTALS (001-003)
------------------------------
1. Arrays Basic Operations
   - Array class and basic operations
   - Insertion, deletion, search, update
   - Time complexity analysis

2. Arrays Searching
   - Linear search implementation
   - Binary search (iterative & recursive)
   - Advanced search algorithms

3. Arrays Sorting
   - Simple sorts: bubble, selection, insertion
   - Efficient sorts: merge, quick, heap
   - Comparison and analysis

Phase 2: LINKED STRUCTURES (004-006)
-----------------------------------
4. Singly Linked List
   - Node structure and basic operations
   - Insertion and deletion techniques
   - Traversal and search methods

5. Doubly Linked List
   - Bidirectional linking
   - Forward and backward traversal
   - Advantages over singly linked lists

6. Circular Linked List
   - Circular structure benefits
   - Applications in real-world problems

Phase 3: STACK & QUEUE (007-009)
--------------------------------
7. Stack Implementation
   - Array-based and linked implementations
   - Applications: parentheses matching, expression evaluation
   - Function call stack simulation

8. Queue Implementation
   - Simple, circular, and priority queues
   - Applications: BFS, task scheduling
   - Producer-consumer problems

9. Deque Implementation
   - Double-ended queue operations
   - Sliding window applications
   - Optimization techniques

Phase 4: TREE STRUCTURES (010-013)
----------------------------------
10. Binary Tree
    - Tree terminology and properties
    - Level-order insertion and traversals
    - Tree height and depth calculations

11. Binary Search Tree
    - BST property maintenance
    - Search, insert, delete operations
    - In-order traversal for sorted output

12. Tree Traversals
    - Recursive vs iterative approaches
    - Pre-order, in-order, post-order
    - Level-order (breadth-first)

13. AVL Tree
    - Self-balancing concepts
    - Rotation operations
    - Maintaining balance factor

Phase 5: ADVANCED STRUCTURES (014-017)
--------------------------------------
14. Hash Table
    - Hash function design
    - Collision resolution techniques
    - Performance analysis

15. Heap Implementation
    - Min-heap and max-heap properties
    - Priority queue applications
    - Heap sort algorithm

16. Graph Implementation
    - Adjacency list vs adjacency matrix
    - Graph traversals: BFS, DFS
    - Shortest path algorithms

17. Dynamic Programming
    - Memoization and tabulation
    - Classic DP problems
    - Optimization techniques
    """
    print(learning_path)


def get_prerequisites(topic):
    """Get prerequisites for a specific topic"""
    prerequisites = {
        "arrays_searching": ["arrays_basic_operations"],
        "arrays_sorting": ["arrays_basic_operations", "arrays_searching"],
        "linked_lists": ["arrays_basic_operations"],
        "stacks": ["linked_lists"],
        "queues": ["linked_lists", "stacks"],
        "trees": ["linked_lists", "stacks", "queues"],
        "graphs": ["trees", "queues"],
        "dynamic_programming": ["arrays", "trees", "graphs"]
    }
    return prerequisites.get(topic, [])


def main():
    """Main function to demonstrate learning path"""
    print("=== DSA Learning Path Guide ===")
    print_learning_path()
    
    print("\nPrerequisites for Trees:")
    prereqs = get_prerequisites("trees")
    for prereq in prereqs:
        print(f"  - {prereq}")


if __name__ == "__main__":
    main()
