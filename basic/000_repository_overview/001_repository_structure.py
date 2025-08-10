"""
001 - Repository Structure Overview
===================================

Overview of the DSA Python repository structure and organization.

This module provides information about the repository layout and learning path.
"""


def print_repository_structure():
    """Print the complete repository structure"""
    structure = """
📁 DSA_Python/
├── basic/
│   ├── 000_repository_overview/        - Repository documentation
│   ├── 001_arrays_basic_operations/    - Array fundamentals
│   ├── 002_arrays_searching/           - Search algorithms
│   ├── 003_arrays_sorting/             - Sorting algorithms
│   ├── 004_singly_linked_list/         - Singly linked lists
│   ├── 005_doubly_linked_list/         - Doubly linked lists
│   ├── 006_circular_linked_list/       - Circular linked lists
│   ├── 007_stack_implementation/       - Stack implementations
│   ├── 008_queue_implementation/       - Queue implementations
│   ├── 009_deque_implementation/       - Deque implementations
│   ├── 010_binary_tree/                - Binary tree basics
│   ├── 011_binary_search_tree/         - BST operations
│   ├── 012_tree_traversals/            - Tree traversals
│   ├── 013_avl_tree/                   - AVL tree implementation
│   ├── 014_hash_table_implementation/  - Hash tables
│   ├── 015_heap_implementation/        - Heap data structure
│   ├── 016_graph_implementation/       - Graph algorithms
│   └── 017_dynamic_programming/        - DP techniques
└── patterns/
    ├── 001_two_pointers.py
    ├── 002_sliding_window.py
    └── ... (algorithm patterns)
    """
    print(structure)


def main():
    """Main function to demonstrate repository structure"""
    print("=== DSA Python Repository Structure ===")
    print_repository_structure()


if __name__ == "__main__":
    main()
