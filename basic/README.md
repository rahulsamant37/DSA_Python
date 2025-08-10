# 🚀 DSA Python - Microservice Architecture Data Structures & Algorithms

Welcome to the most comprehensive and modular implementation of Data Structures and Algorithms in Python! This repository follows a **microservice-inspired architecture** where each functionality is separated into dedicated files, following the principle of "one function per file" for optimal learning and maintainability.

## 📋 Repository Overview

This repository contains **18 specialized folders** with **80+ individual implementation files** covering all fundamental data structures and algorithmic concepts. Each folder represents a complete microservice-like module with related functionality broken down into single-responsibility files.

## 🏗️ Microservice Architecture Structure

```
DSA_Python/basic/
├── 000_repository_overview/           📊 Documentation & Learning Guide
│   ├── 001_repository_structure.py    │   Repository organization
│   ├── 002_learning_path.py          │   Progressive learning roadmap
│   └── 003_complexity_analysis.py    │   Algorithm complexity guide
│
├── 001_arrays_basic_operations/       📈 Array Fundamentals
│   ├── 001_array_class.py            │   Core array implementation
│   ├── 002_insertion_operations.py    │   Insert at various positions
│   ├── 003_deletion_operations.py     │   Delete by index/value
│   ├── 004_search_operations.py       │   Find elements and indices
│   └── 005_update_operations.py       │   Modify array elements
│
├── 002_arrays_searching/              🔍 Search Algorithms
│   ├── 001_linear_search.py          │   Sequential search
│   ├── 002_binary_search.py          │   Divide and conquer search
│   ├── 003_jump_search.py            │   Block-based search
│   ├── 004_interpolation_search.py    │   Estimation-based search
│   └── 005_exponential_search.py      │   Range-finding search
│
├── 003_arrays_sorting/                📊 Sorting Algorithms
│   ├── 001_bubble_sort.py            │   Simple comparison sort
│   ├── 002_selection_sort.py         │   Minimum finding sort
│   ├── 003_insertion_sort.py         │   Incremental building sort
│   ├── 004_merge_sort.py             │   Divide and conquer sort
│   ├── 005_quick_sort.py             │   Partition-based sort
│   └── 006_heap_sort.py              │   Heap-based sort
│
├── 004_singly_linked_list/            🔗 Single-Direction Links
│   ├── 001_node_implementation.py     │   Basic node structure
│   ├── 002_linkedlist_class.py       │   List management
│   ├── 003_insertion_methods.py      │   Add nodes (head/tail/middle)
│   ├── 004_deletion_methods.py       │   Remove nodes by value/position
│   └── 005_traversal_search.py       │   Navigate and find nodes
│
├── 005_doubly_linked_list/            ↔️ Bidirectional Links
│   ├── 001_doubly_node.py            │   Node with prev/next pointers
│   ├── 002_doubly_linkedlist.py      │   Bidirectional list class
│   ├── 003_insertion_operations.py    │   Insert in both directions
│   ├── 004_deletion_operations.py     │   Remove with backlinks
│   └── 005_traversal_operations.py    │   Forward/backward navigation
│
├── 006_circular_linked_list/          🔄 Circular Connections
│   ├── 001_circular_singly.py        │   Single circular list
│   ├── 002_circular_doubly.py        │   Double circular list
│   ├── 003_josephus_problem.py       │   Classic application
│   └── 004_circular_applications.py   │   Real-world use cases
│
├── 007_stack_implementation/          📚 LIFO Data Structure
│   ├── 001_array_based_stack.py      │   Fixed-size stack
│   ├── 002_linkedlist_stack.py       │   Dynamic stack
│   ├── 003_builtin_stack.py          │   Python list as stack
│   ├── 004_stack_applications.py     │   Expression evaluation, etc.
│   └── 005_stack_problems.py         │   Classic stack problems
│
├── 008_queue_implementation/          🎯 FIFO Data Structure
│   ├── 001_array_based_queue.py      │   Circular array queue
│   ├── 002_linkedlist_queue.py       │   Dynamic queue
│   ├── 003_builtin_queue.py          │   Collections.deque
│   ├── 004_priority_queue.py         │   Heap-based queue
│   └── 005_queue_applications.py     │   BFS, scheduling, etc.
│
├── 009_deque_implementation/          ↕️ Double-Ended Queue
│   ├── 001_array_based_deque.py      │   Circular array deque
│   ├── 002_linkedlist_deque.py       │   Doubly-linked deque
│   ├── 003_builtin_deque.py          │   Collections.deque wrapper
│   └── 004_deque_applications.py     │   Sliding window, palindrome
│
├── 010_binary_tree/                  🌳 Hierarchical Structure
│   ├── 001_tree_node.py              │   Basic tree node
│   ├── 002_binary_tree_class.py      │   Tree container class
│   ├── 003_tree_construction.py      │   Build trees from arrays
│   ├── 004_basic_operations.py       │   Insert, delete, find
│   └── 005_tree_properties.py        │   Height, size, depth
│
├── 011_binary_search_tree/           🔍 Ordered Binary Tree
│   ├── 001_bst_node.py               │   BST node with ordering
│   ├── 002_bst_class.py              │   BST container
│   ├── 003_insertion_operation.py    │   Maintain order on insert
│   ├── 004_deletion_operation.py     │   Complex deletion cases
│   └── 005_search_operations.py      │   Efficient search/validation
│
├── 012_tree_traversals/              🚶 Tree Navigation
│   ├── 001_inorder_traversal.py      │   Left-Root-Right
│   ├── 002_preorder_traversal.py     │   Root-Left-Right
│   ├── 003_postorder_traversal.py    │   Left-Right-Root
│   ├── 004_levelorder_traversal.py   │   Breadth-first traversal
│   └── 005_traversal_applications.py │   Expression trees, etc.
│
├── 013_avl_tree/                     ⚖️ Self-Balancing Tree
│   ├── 001_avl_node.py               │   Node with balance factor
│   ├── 002_rotation_operations.py    │   LL, RR, LR, RL rotations
│   ├── 003_avl_tree_class.py         │   Self-balancing BST
│   └── 004_avl_insertion.py          │   Insert with rebalancing
│
├── 014_hash_table_implementation/    🗝️ Key-Value Storage
│   ├── 001_hash_functions.py         │   Various hashing methods
│   ├── 002_collision_resolution.py   │   Chaining & open addressing
│   ├── 003_hash_table_class.py       │   Complete hash table
│   ├── 004_dynamic_resizing.py       │   Load factor management
│   └── 005_hash_applications.py      │   Caching, frequency counting
│
├── 015_heap_implementation/          ⛰️ Priority-Based Structure
│   ├── 001_min_heap.py               │   Minimum heap implementation
│   ├── 002_max_heap.py               │   Maximum heap implementation
│   ├── 003_priority_queue.py         │   Heap-based priority queue
│   ├── 004_heap_sort.py              │   Sorting using heaps
│   └── 005_heap_applications.py      │   Median finding, top-K problems
│
├── 016_graph_implementation/         🕸️ Network Structures
│   ├── 001_graph_representation.py   │   Adjacency list/matrix
│   ├── 002_graph_traversal.py        │   BFS/DFS implementations
│   ├── 003_shortest_path.py          │   Dijkstra, Bellman-Ford
│   ├── 004_topological_sort.py       │   DAG ordering algorithms
│   └── 005_minimum_spanning_tree.py  │   Kruskal's, Prim's algorithms
│
└── 017_dynamic_programming/          🧠 Optimization Techniques
    ├── 001_fibonacci_dp.py           │   Classic DP introduction
    ├── 002_knapsack_problems.py      │   0/1, unbounded, bounded
    ├── 003_longest_common_subsequence.py │ String matching problems
    └── 004_edit_distance.py          │   Levenshtein distance
```

## 🎯 Learning Path

### Phase 1: Foundation (Weeks 1-2)
- **001-003**: Array operations, searching algorithms, and sorting techniques
- **Focus**: Build understanding of basic operations and algorithm analysis
- **Files**: 17 specialized implementations covering all array fundamentals

### Phase 2: Linear Structures (Weeks 3-4)  
- **004-009**: Linked lists, stacks, queues, and deques
- **Focus**: Master pointer manipulation and linear data structure operations
- **Files**: 24 microservice files covering all linear structure variants

### Phase 3: Tree Structures (Weeks 5-6)
- **010-013**: Binary trees, BST, traversals, and AVL trees
- **Focus**: Understand hierarchical data organization and tree algorithms  
- **Files**: 18 specialized files covering complete tree ecosystem

### Phase 4: Advanced Structures (Week 7)
- **014-015**: Hash tables and heaps with comprehensive applications
- **Focus**: Learn efficient data access and priority-based operations
- **Files**: 10 files covering hashing and heap-based algorithms

### Phase 5: Graph Theory (Week 8)
- **016**: Complete graph implementations and algorithms
- **Focus**: Master complex relationship modeling and graph traversals
- **Files**: 5 comprehensive graph algorithm implementations  

### Phase 6: Optimization (Weeks 9-10)
- **017**: Dynamic programming with classic problems
- **Focus**: Develop optimization thinking and problem-solving patterns
- **Files**: 4 essential DP problem categories

## 🔥 Key Features

### 🎓 **Microservice Educational Design**
- **Single Responsibility**: Each file contains exactly one function/class/concept
- **Progressive Complexity**: Files numbered 001_, 002_, etc. within each folder
- **Modular Learning**: Study specific concepts without distractions
- **Comprehensive Coverage**: Every aspect of each data structure separated

### 🏗️ **Architecture Benefits**  
- **Maintainability**: Easy to update individual components
- **Testability**: Each functionality independently testable
- **Reusability**: Import and use specific implementations
- **Scalability**: Add new algorithms without affecting existing code

### 🧪 **Production-Quality Implementation**
- **Type Hints**: Modern Python typing throughout all files
- **Documentation**: Comprehensive docstrings explaining every component
- **Error Handling**: Robust exception management in each module
- **Performance Analysis**: Time/space complexity for every algorithm

## 📊 Algorithm Complexity Guide

### Searching Algorithms
| Algorithm | Time Complexity | Space Complexity |
|-----------|----------------|------------------|
| Linear Search | O(n) | O(1) |
| Binary Search | O(log n) | O(1) |
| Jump Search | O(√n) | O(1) |
| Interpolation Search | O(log log n)* | O(1) |

### Sorting Algorithms
| Algorithm | Best Case | Average Case | Worst Case | Space |
|-----------|-----------|--------------|------------|-------|
| Bubble Sort | O(n) | O(n²) | O(n²) | O(1) |
| Quick Sort | O(n log n) | O(n log n) | O(n²) | O(log n) |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) |

### Data Structure Operations
| Structure | Access | Search | Insertion | Deletion |
|-----------|--------|--------|-----------|----------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| Hash Table | O(1)* | O(1)* | O(1)* | O(1)* |
| Binary Tree | O(n) | O(n) | O(n) | O(n) |
| BST | O(log n)* | O(log n)* | O(log n)* | O(log n)* |
| AVL Tree | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) | O(n) | O(log n) | O(log n) |

*Average case

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- No external dependencies required (uses only Python standard library)

### Exploring the Microservice Structure

1. **Clone or download** this repository
2. **Navigate** to the DSA_Python/basic directory  
3. **Start with the overview folder**:
   ```bash
   cd 000_repository_overview
   python 001_repository_structure.py
   python 002_learning_path.py
   python 003_complexity_analysis.py
   ```
4. **Follow the numbered folder sequence**:
   ```bash
   cd ../001_arrays_basic_operations
   python 001_array_class.py
   python 002_insertion_operations.py
   # ... continue with remaining files in order
   ```

### Microservice Navigation
Each folder contains a complete ecosystem:
- **001_** files: Core implementations and basic concepts
- **002_** files: Essential operations and methods
- **003_** files: Advanced operations and optimizations
- **004_** files: Applications and problem-solving
- **005_** files: Extensions and variations

### Interactive Learning  
Each file is self-contained and includes:
- ✅ Single-responsibility implementation
- ✅ Comprehensive test cases with sample data
- ✅ Performance analysis and complexity documentation
- ✅ Real-world application examples
- ✅ Clear visual output demonstrations

## 💡 What You'll Learn

### 🧱 **Microservice Data Structures Mastery**
- **Arrays**: 17 specialized files covering all operations and algorithms
- **Linked Lists**: 13 files across singly, doubly, and circular variants
- **Stacks & Queues**: 9 files with multiple implementation approaches  
- **Trees**: 18 files covering binary trees, BST, traversals, and AVL
- **Hash Tables**: 5 files with comprehensive collision handling
- **Heaps**: 5 files covering min/max heaps and priority applications
- **Graphs**: 5 files with representations, traversals, and key algorithms

### 🔍 **Algorithm Expertise Across Modules**
- **Searching**: Linear, binary, jump, interpolation, exponential
- **Sorting**: Bubble, selection, insertion, merge, quick, heap
- **Tree Operations**: All traversal methods and balancing techniques  
- **Graph Algorithms**: DFS, BFS, shortest paths, MST, topological sort
- **Dynamic Programming**: Fibonacci, knapsack, LCS, edit distance
- **Optimization**: Space-time trade-offs and algorithmic improvements

### 📈 **Microservice Architecture Skills**
- **Single Responsibility Principle**: One function per file approach
- **Modular Design**: Independent, reusable components
- **Progressive Complexity**: Structured learning within each module
- **Separation of Concerns**: Clean interfaces between functionalities

## 🎯 Use Cases

### 👨‍🎓 **For Students**
- **Focused Learning**: Study specific algorithms without distraction
- **Progressive Mastery**: Build concepts incrementally within each folder
- **Comprehensive Coverage**: 80+ files covering every important concept
- **Exam Preparation**: Isolated implementations perfect for review

### 💼 **For Interview Preparation**  
- **Targeted Practice**: Focus on specific problem types
- **Multiple Solutions**: Different approaches within each folder
- **Production Code**: Real-world quality implementations
- **Performance Analysis**: Complexity analysis for every algorithm

### 👨‍💻 **For Developers**
- **Modular Components**: Import specific implementations into projects
- **Reference Library**: High-quality code for development reference
- **Architecture Example**: Microservice design principles in action
- **Best Practices**: Industry-standard coding patterns and documentation

### 🏫 **For Educators**
- **Granular Teaching**: Each concept in its own file for focused lessons
- **Flexible Curriculum**: Pick and choose specific implementations
- **Clear Progression**: Numbered files show logical learning sequence
- **Practical Examples**: Real applications for each data structure

### 🔬 **For Researchers**
- **Algorithmic Variants**: Multiple implementations for comparison
- **Performance Benchmarking**: Individual components for testing
- **Educational Analysis**: Study microservice architecture benefits
- **Extension Base**: Modular foundation for algorithm improvements

## 🔬 Advanced Features

### **Microservice Architecture Benefits**
- **Independent Modules**: Each file can be developed, tested, and maintained separately
- **Single Responsibility**: Every file has exactly one clear purpose
- **Easy Integration**: Import specific functionality without overhead
- **Scalable Learning**: Add new concepts without disrupting existing structure

### **Multiple Implementation Approaches**
- **Variant Comparisons**: Different algorithms for same problem across files
- **Progressive Optimization**: Basic → intermediate → advanced in numbered sequence  
- **Implementation Styles**: Recursive vs iterative, array vs pointer-based
- **Performance Trade-offs**: Space vs time optimizations clearly separated

### **Educational Microservices**
- **Concept Isolation**: Learn one thing at a time without cognitive overload
- **Dependency Clarity**: Clear relationships between concepts across files
- **Iterative Refinement**: Build understanding progressively within folders
- **Knowledge Verification**: Test specific concepts independently

## 🛠️ Customization & Extension

Each microservice implementation is designed for easy modification:

### **Individual File Customization**
- **Extend Specific Functions**: Add methods to individual implementations
- **Modify Algorithms**: Change specific files without affecting others  
- **Performance Tuning**: Optimize individual components independently
- **Feature Addition**: Add new files to folders following numbering convention

### **Folder-Level Modifications**
- **Add New Variants**: Create 006_, 007_ files for additional approaches
- **Integrate Modules**: Combine implementations across folders for complex structures
- **Create Specializations**: Build domain-specific versions of data structures
- **Performance Suites**: Add benchmarking files to each folder

### **Architecture Benefits**
- **Isolated Changes**: Modifications don't cascade through monolithic files
- **A/B Testing**: Easy to compare different implementations side-by-side
- **Gradual Migration**: Replace individual components without system-wide changes
- **Educational Customization**: Adapt specific files for different learning levels

## 📚 Additional Resources

### Recommended Next Steps
1. **Practice Problems**: Use these implementations to solve coding challenges
2. **Advanced Topics**: Explore segment trees, fenwick trees, advanced graph algorithms
3. **System Design**: Apply these concepts to scalable system architectures
4. **Competitive Programming**: Optimize implementations for contest environments

### Further Reading
- Introduction to Algorithms (CLRS)
- Algorithm Design Manual (Skiena)
- Competitive Programming resources
- System design interview guides

## 🤝 Contributing

This repository is designed for educational purposes. If you find any issues or have suggestions for improvements:
1. Review the implementation thoroughly
2. Test your suggested changes
3. Ensure educational value is maintained
4. Submit detailed explanations for any modifications

## 📄 License

This project is open source and available for educational use. Feel free to use, modify, and distribute for learning purposes.

## 🌟 Acknowledgments

This repository represents a comprehensive effort to create the most complete and educational DSA resource in Python. It's designed to bridge the gap between theoretical knowledge and practical implementation.

---

## 🚀 Start Your Microservice Learning Journey

### **Recommended Approach**
1. **Begin with**: `000_repository_overview/001_repository_structure.py` 
2. **Understand**: The microservice architecture and folder organization
3. **Progress**: Through folders in numerical order (001 → 017)
4. **Within Each Folder**: Follow file numbering (001_ → 005_)
5. **Practice**: Modify individual files to test your understanding

### **Learning Strategy**
- **One Concept Per Session**: Focus on individual files for deep understanding
- **Build Incrementally**: Each file adds one piece to the complete picture  
- **Test Frequently**: Run individual implementations to verify learning
- **Combine Concepts**: Use multiple files together for complex problems

**Remember**: The microservice architecture allows you to master each component independently while understanding how they work together as a complete system.

Happy Learning! 🎓✨

---

## 📊 Repository Statistics

- **Total Folders**: 18 specialized data structure modules
- **Total Files**: 80+ individual implementation files  
- **Code Quality**: Type hints, comprehensive documentation, error handling
- **Learning Path**: Structured progression from basics to advanced concepts
- **Architecture**: Microservice-inspired modular design
- **Coverage**: Complete DSA curriculum in digestible components

*Last Updated: August 2025 | Architecture: Microservice Design | Files: 80+ | Algorithms: 50+*