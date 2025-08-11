"""
heapq basics - Creating and understanding heaps

heapq implements a binary min-heap using a regular Python list.
Essential for priority queues, finding k smallest/largest elements, and heap-based algorithms.
"""

import heapq

def heap_basics():
    """Demonstrates basic heap concepts and creation"""
    
    print("--- Heap Basics ---")
    
    # Create a heap from an existing list
    numbers = [4, 1, 7, 3, 8, 5]
    print(f"Original list: {numbers}")
    
    # Convert to heap in-place
    heapq.heapify(numbers)
    print(f"After heapify: {numbers}")
    print("Note: This is a min-heap (smallest element at index 0)")
    print()
    
    # Understand heap property
    print("--- Heap Property ---")
    print("In a min-heap, for any index i:")
    print("- Parent: heap[i] <= heap[2*i + 1] and heap[i] <= heap[2*i + 2]")
    print("- The smallest element is always at index 0")
    print()
    
    # Visualize the heap structure
    heap = [1, 3, 5, 4, 8, 7]
    print(f"Heap: {heap}")
    print("Tree structure:")
    print("       1")
    print("      / \\")
    print("     3   5")
    print("    / \\ /")
    print("   4  8 7")
    print()
    
    # Verify heap property
    def is_valid_heap(heap):
        """Check if list satisfies heap property"""
        n = len(heap)
        for i in range(n):
            left = 2 * i + 1
            right = 2 * i + 2
            
            if left < n and heap[i] > heap[left]:
                return False
            if right < n and heap[i] > heap[right]:
                return False
        return True
    
    print(f"Is valid heap: {is_valid_heap(heap)}")
    print()

def heap_creation_methods():
    """Different ways to create heaps"""
    
    print("--- Heap Creation Methods ---")
    
    # Method 1: heapify existing list
    print("1. Using heapify on existing list:")
    data = [9, 5, 6, 2, 3, 7, 1, 4, 8]
    print(f"Original: {data}")
    heapq.heapify(data)
    print(f"Heapified: {data}")
    print()
    
    # Method 2: Build heap by pushing elements
    print("2. Building heap with heappush:")
    heap = []
    elements = [9, 5, 6, 2, 3, 7, 1, 4, 8]
    
    for element in elements:
        heapq.heappush(heap, element)
        print(f"Push {element}: {heap}")
    print()
    
    # Method 3: Create heap from generator/iterator
    print("3. Creating heap from range:")
    heap_from_range = list(range(10, 0, -1))  # [10, 9, 8, ..., 1]
    print(f"Before heapify: {heap_from_range}")
    heapq.heapify(heap_from_range)
    print(f"After heapify: {heap_from_range}")
    print()

def heap_with_custom_objects():
    """Using heaps with custom objects and comparison"""
    
    print("--- Heaps with Custom Objects ---")
    
    # Using tuples (compared lexicographically)
    print("1. Heap with tuples (priority, value):")
    priority_heap = []
    
    tasks = [
        (3, "Low priority task"),
        (1, "High priority task"),
        (2, "Medium priority task"),
        (1, "Another high priority task")
    ]
    
    for priority, task in tasks:
        heapq.heappush(priority_heap, (priority, task))
    
    print("Priority heap (lower number = higher priority):")
    for item in priority_heap:
        print(f"  {item}")
    print()
    
    # Custom class with comparison
    print("2. Custom class with __lt__ method:")
    
    class Task:
        def __init__(self, priority, name):
            self.priority = priority
            self.name = name
        
        def __lt__(self, other):
            return self.priority < other.priority
        
        def __repr__(self):
            return f"Task(priority={self.priority}, name='{self.name}')"
    
    task_heap = []
    heapq.heappush(task_heap, Task(3, "Low priority"))
    heapq.heappush(task_heap, Task(1, "High priority"))
    heapq.heappush(task_heap, Task(2, "Medium priority"))
    
    print("Custom task heap:")
    for task in task_heap:
        print(f"  {task}")
    print()

def heap_properties():
    """Demonstrates heap properties and limitations"""
    
    print("--- Heap Properties ---")
    
    heap = [1, 3, 6, 5, 9, 8]
    print(f"Sample heap: {heap}")
    
    # Access minimum element (root)
    print(f"Minimum element: {heap[0]} (always at index 0)")
    
    # Heap is NOT sorted
    print("Important: Heap is NOT a sorted array!")
    print("- Only the root is guaranteed to be the minimum")
    print("- Children might not be in any particular order")
    print()
    
    # Time complexities
    print("--- Time Complexities ---")
    print("- heappush(): O(log n)")
    print("- heappop(): O(log n)")
    print("- heapify(): O(n)")
    print("- heap[0] (peek): O(1)")
    print("- Search for element: O(n) - no efficient search!")
    print()
    
    # Heap vs other data structures
    print("--- When to Use Heaps ---")
    print("✓ Priority queues")
    print("✓ Finding k smallest/largest elements")
    print("✓ Heap sort")
    print("✓ Median maintenance")
    print("✗ Random access to elements")
    print("✗ Searching for specific elements")
    print("✗ Maintaining sorted order")
    print()

def dsa_use_case():
    """Basic DSA application: Priority Queue for Dijkstra's algorithm"""
    
    print("--- DSA Use Case: Priority Queue ---")
    
    class PriorityQueue:
        """Simple priority queue implementation using heapq"""
        
        def __init__(self):
            self.heap = []
            self.entry_count = 0
        
        def push(self, priority, item):
            """Add item with given priority"""
            # Use entry_count to break ties (FIFO for same priority)
            entry = (priority, self.entry_count, item)
            heapq.heappush(self.heap, entry)
            self.entry_count += 1
        
        def pop(self):
            """Remove and return item with lowest priority"""
            if self.heap:
                priority, _, item = heapq.heappop(self.heap)
                return priority, item
            raise IndexError("Priority queue is empty")
        
        def peek(self):
            """Look at item with lowest priority without removing"""
            if self.heap:
                priority, _, item = self.heap[0]
                return priority, item
            raise IndexError("Priority queue is empty")
        
        def is_empty(self):
            return len(self.heap) == 0
        
        def size(self):
            return len(self.heap)
    
    # Demonstrate priority queue
    pq = PriorityQueue()
    
    print("Adding tasks to priority queue:")
    tasks = [
        (3, "Write documentation"),
        (1, "Fix critical bug"),
        (2, "Code review"),
        (1, "Deploy hotfix"),
        (2, "Update tests")
    ]
    
    for priority, task in tasks:
        pq.push(priority, task)
        print(f"Added: priority={priority}, task='{task}'")
    
    print(f"\nPriority queue size: {pq.size()}")
    print(f"Next task (peek): {pq.peek()}")
    
    print("\nProcessing tasks in priority order:")
    while not pq.is_empty():
        priority, task = pq.pop()
        print(f"Processing: priority={priority}, task='{task}'")

if __name__ == "__main__":
    heap_basics()
    heap_creation_methods()
    heap_with_custom_objects()
    heap_properties()
    dsa_use_case()
