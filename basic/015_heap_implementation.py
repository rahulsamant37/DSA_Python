"""
015 - Heap Implementation (Binary Heap)
======================================

This module implements binary heaps (both min-heap and max-heap) with:
- Array-based representation
- Heap operations: insert, extract, peek, heapify
- Heap sort algorithm
- Priority queue implementation
- Heap applications (K largest/smallest elements, merge K sorted arrays)

Time Complexity:
- Insert: O(log n)
- Extract min/max: O(log n) 
- Peek: O(1)
- Build heap: O(n)
- Heap sort: O(n log n)
- Space complexity: O(1) auxiliary (in-place operations)

Mathematical Properties:
- For node at index i:
  - Parent: (i-1)//2
  - Left child: 2*i + 1
  - Right child: 2*i + 2
"""

import heapq
from typing import List, Any, Callable


class MinHeap:
    """Min-heap implementation using array"""
    
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def has_parent(self, index):
        """Check if node has parent"""
        return self.parent(index) >= 0
    
    def has_left_child(self, index):
        """Check if node has left child"""
        return self.left_child(index) < self.size
    
    def has_right_child(self, index):
        """Check if node has right child"""
        return self.right_child(index) < self.size
    
    def swap(self, index1, index2):
        """Swap elements at two indices"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def peek(self):
        """Get minimum element without removing it"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def insert(self, value):
        """Insert element into heap"""
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def extract_min(self):
        """Remove and return minimum element"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        
        min_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        
        if self.size > 0:
            self._heapify_down(0)
        
        return min_value
    
    def _heapify_up(self, index):
        """Restore heap property by moving element up"""
        while (self.has_parent(index) and 
               self.heap[self.parent(index)] > self.heap[index]):
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def _heapify_down(self, index):
        """Restore heap property by moving element down"""
        while self.has_left_child(index):
            smaller_child_index = self.left_child(index)
            
            # Find smaller child
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] < self.heap[smaller_child_index]):
                smaller_child_index = self.right_child(index)
            
            # If heap property is satisfied, stop
            if self.heap[index] <= self.heap[smaller_child_index]:
                break
            
            self.swap(index, smaller_child_index)
            index = smaller_child_index
    
    def build_heap(self, array):
        """Build heap from array in O(n) time"""
        self.heap = array[:]
        self.size = len(array)
        
        # Start from last non-leaf node and heapify down
        for i in range(self.parent(self.size - 1), -1, -1):
            self._heapify_down(i)
    
    def is_empty(self):
        """Check if heap is empty"""
        return self.size == 0
    
    def get_size(self):
        """Get heap size"""
        return self.size
    
    def display(self):
        """Display heap as array and tree structure"""
        if self.size == 0:
            print("Heap is empty")
            return
        
        print(f"Heap array: {self.heap[:self.size]}")
        print("Tree structure:")
        self._display_tree(0, 0)
    
    def _display_tree(self, index, level):
        """Helper method to display tree structure"""
        if index >= self.size:
            return
        
        # Display right subtree
        if self.has_right_child(index):
            self._display_tree(self.right_child(index), level + 1)
        
        # Display current node
        print("  " * level + str(self.heap[index]))
        
        # Display left subtree
        if self.has_left_child(index):
            self._display_tree(self.left_child(index), level + 1)


class MaxHeap:
    """Max-heap implementation using array"""
    
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, index):
        return (index - 1) // 2
    
    def left_child(self, index):
        return 2 * index + 1
    
    def right_child(self, index):
        return 2 * index + 2
    
    def has_parent(self, index):
        return self.parent(index) >= 0
    
    def has_left_child(self, index):
        return self.left_child(index) < self.size
    
    def has_right_child(self, index):
        return self.right_child(index) < self.size
    
    def swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def peek(self):
        """Get maximum element without removing it"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def insert(self, value):
        """Insert element into heap"""
        self.heap.append(value)
        self.size += 1
        self._heapify_up(self.size - 1)
    
    def extract_max(self):
        """Remove and return maximum element"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        
        max_value = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.heap.pop()
        
        if self.size > 0:
            self._heapify_down(0)
        
        return max_value
    
    def _heapify_up(self, index):
        """Restore heap property by moving element up"""
        while (self.has_parent(index) and 
               self.heap[self.parent(index)] < self.heap[index]):
            self.swap(index, self.parent(index))
            index = self.parent(index)
    
    def _heapify_down(self, index):
        """Restore heap property by moving element down"""
        while self.has_left_child(index):
            larger_child_index = self.left_child(index)
            
            # Find larger child
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] > self.heap[larger_child_index]):
                larger_child_index = self.right_child(index)
            
            # If heap property is satisfied, stop
            if self.heap[index] >= self.heap[larger_child_index]:
                break
            
            self.swap(index, larger_child_index)
            index = larger_child_index
    
    def build_heap(self, array):
        """Build heap from array in O(n) time"""
        self.heap = array[:]
        self.size = len(array)
        
        for i in range(self.parent(self.size - 1), -1, -1):
            self._heapify_down(i)
    
    def is_empty(self):
        return self.size == 0
    
    def get_size(self):
        return self.size
    
    def display(self):
        """Display heap as array and tree structure"""
        if self.size == 0:
            print("Heap is empty")
            return
        
        print(f"Heap array: {self.heap[:self.size]}")
        print("Tree structure:")
        self._display_tree(0, 0)
    
    def _display_tree(self, index, level):
        if index >= self.size:
            return
        
        if self.has_right_child(index):
            self._display_tree(self.right_child(index), level + 1)
        
        print("  " * level + str(self.heap[index]))
        
        if self.has_left_child(index):
            self._display_tree(self.left_child(index), level + 1)


class PriorityQueue:
    """Priority queue implementation using min-heap"""
    
    def __init__(self):
        self.heap = []
    
    def enqueue(self, item, priority):
        """Add item with priority"""
        heapq.heappush(self.heap, (priority, item))
    
    def dequeue(self):
        """Remove and return highest priority item"""
        if not self.heap:
            raise IndexError("Priority queue is empty")
        priority, item = heapq.heappop(self.heap)
        return item
    
    def peek(self):
        """Get highest priority item without removing it"""
        if not self.heap:
            raise IndexError("Priority queue is empty")
        return self.heap[0][1]
    
    def is_empty(self):
        return len(self.heap) == 0
    
    def size(self):
        return len(self.heap)
    
    def display(self):
        print("Priority Queue contents:")
        for priority, item in sorted(self.heap):
            print(f"  Priority {priority}: {item}")


class HeapSort:
    """Heap sort implementation using max-heap"""
    
    @staticmethod
    def sort(array):
        """Sort array using heap sort algorithm"""
        if not array:
            return array
        
        n = len(array)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            HeapSort._heapify(array, n, i)
        
        # Extract elements one by one
        for i in range(n - 1, 0, -1):
            # Move current root to end
            array[0], array[i] = array[i], array[0]
            
            # Call heapify on reduced heap
            HeapSort._heapify(array, i, 0)
        
        return array
    
    @staticmethod
    def _heapify(array, heap_size, root_index):
        """Heapify subtree rooted at given index"""
        largest = root_index
        left = 2 * root_index + 1
        right = 2 * root_index + 2
        
        # Check if left child is larger than root
        if left < heap_size and array[left] > array[largest]:
            largest = left
        
        # Check if right child is larger than largest so far
        if right < heap_size and array[right] > array[largest]:
            largest = right
        
        # If largest is not root, swap and continue heapifying
        if largest != root_index:
            array[root_index], array[largest] = array[largest], array[root_index]
            HeapSort._heapify(array, heap_size, largest)


class HeapApplications:
    """Common heap applications and algorithms"""
    
    @staticmethod
    def find_k_largest(array, k):
        """Find K largest elements using min-heap"""
        if k <= 0 or k > len(array):
            return []
        
        min_heap = []
        
        for num in array:
            if len(min_heap) < k:
                heapq.heappush(min_heap, num)
            elif num > min_heap[0]:
                heapq.heapreplace(min_heap, num)
        
        return sorted(min_heap, reverse=True)
    
    @staticmethod
    def find_k_smallest(array, k):
        """Find K smallest elements using max-heap"""
        if k <= 0 or k > len(array):
            return []
        
        max_heap = []
        
        for num in array:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -num)  # Negate for max-heap
            elif num < -max_heap[0]:
                heapq.heapreplace(max_heap, -num)
        
        return sorted([-x for x in max_heap])
    
    @staticmethod
    def merge_k_sorted_arrays(arrays):
        """Merge K sorted arrays using min-heap"""
        if not arrays:
            return []
        
        min_heap = []
        result = []
        
        # Initialize heap with first element from each array
        for i, array in enumerate(arrays):
            if array:
                heapq.heappush(min_heap, (array[0], i, 0))
        
        while min_heap:
            value, array_index, element_index = heapq.heappop(min_heap)
            result.append(value)
            
            # Add next element from same array if available
            if element_index + 1 < len(arrays[array_index]):
                next_value = arrays[array_index][element_index + 1]
                heapq.heappush(min_heap, (next_value, array_index, element_index + 1))
        
        return result
    
    @staticmethod
    def find_median_stream():
        """Find median in a stream of integers using two heaps"""
        max_heap = []  # For smaller half (negated values)
        min_heap = []  # For larger half
        
        def add_number(num):
            # Add to appropriate heap
            if not max_heap or num <= -max_heap[0]:
                heapq.heappush(max_heap, -num)
            else:
                heapq.heappush(min_heap, num)
            
            # Balance heaps
            if len(max_heap) > len(min_heap) + 1:
                value = -heapq.heappop(max_heap)
                heapq.heappush(min_heap, value)
            elif len(min_heap) > len(max_heap) + 1:
                value = heapq.heappop(min_heap)
                heapq.heappush(max_heap, -value)
        
        def get_median():
            if len(max_heap) == len(min_heap):
                if not max_heap:
                    return None
                return (-max_heap[0] + min_heap[0]) / 2.0
            elif len(max_heap) > len(min_heap):
                return -max_heap[0]
            else:
                return min_heap[0]
        
        return add_number, get_median


def test_heaps():
    """Test heap implementations"""
    print("=== Testing Heap Implementations ===\n")
    
    # Test Min Heap
    print("=== Min Heap ===")
    min_heap = MinHeap()
    
    # Insert elements
    elements = [10, 20, 15, 30, 40, 50, 100, 25, 45]
    print(f"Inserting elements: {elements}")
    
    for element in elements:
        min_heap.insert(element)
        print(f"Inserted {element}, min: {min_heap.peek()}")
    
    print()
    min_heap.display()
    print()
    
    # Extract elements
    print("Extracting elements:")
    while not min_heap.is_empty():
        min_val = min_heap.extract_min()
        print(f"Extracted: {min_val}")
    print()
    
    # Test Max Heap
    print("=== Max Heap ===")
    max_heap = MaxHeap()
    
    # Build heap from array
    array = [4, 10, 3, 5, 1, 6, 7, 8, 9, 2]
    print(f"Building heap from array: {array}")
    max_heap.build_heap(array)
    max_heap.display()
    print()
    
    # Test Priority Queue
    print("=== Priority Queue ===")
    pq = PriorityQueue()
    
    tasks = [
        ("High priority task", 1),
        ("Medium priority task", 5),
        ("Low priority task", 10),
        ("Critical task", 0),
        ("Normal task", 7)
    ]
    
    print("Adding tasks to priority queue:")
    for task, priority in tasks:
        pq.enqueue(task, priority)
        print(f"Added: '{task}' with priority {priority}")
    
    print()
    pq.display()
    print()
    
    print("Processing tasks by priority:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"Processing: {task}")
    print()
    
    # Test Heap Sort
    print("=== Heap Sort ===")
    unsorted = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {unsorted}")
    
    sorted_array = HeapSort.sort(unsorted[:])  # Copy to preserve original
    print(f"Sorted array: {sorted_array}")
    print()


def test_heap_applications():
    """Test heap applications"""
    print("=== Testing Heap Applications ===\n")
    
    # Test K largest/smallest
    print("=== Finding K Largest/Smallest ===")
    array = [3, 2, 1, 5, 6, 4, 7, 8, 9, 10]
    k = 3
    
    print(f"Array: {array}")
    print(f"K = {k}")
    
    k_largest = HeapApplications.find_k_largest(array, k)
    k_smallest = HeapApplications.find_k_smallest(array, k)
    
    print(f"{k} largest elements: {k_largest}")
    print(f"{k} smallest elements: {k_smallest}")
    print()
    
    # Test merging K sorted arrays
    print("=== Merging K Sorted Arrays ===")
    arrays = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9],
        [0, 10, 11]
    ]
    
    print("Arrays to merge:")
    for i, arr in enumerate(arrays):
        print(f"  Array {i + 1}: {arr}")
    
    merged = HeapApplications.merge_k_sorted_arrays(arrays)
    print(f"Merged array: {merged}")
    print()
    
    # Test median in stream
    print("=== Median in Stream ===")
    add_number, get_median = HeapApplications.find_median_stream()
    
    stream = [5, 15, 1, 3, 8, 2, 9, 12, 4]
    print(f"Stream: {stream}")
    print("Adding numbers and finding median:")
    
    for num in stream:
        add_number(num)
        median = get_median()
        print(f"Added {num}, median: {median}")


def performance_analysis():
    """Analyze heap performance"""
    print("\n=== Performance Analysis ===\n")
    
    import time
    import random
    
    # Test different heap sizes
    sizes = [1000, 5000, 10000]
    
    for size in sizes:
        print(f"Testing with {size} elements:")
        
        # Generate random data
        data = [random.randint(1, size * 10) for _ in range(size)]
        
        # Test Min Heap operations
        min_heap = MinHeap()
        
        # Insert performance
        start_time = time.time()
        for value in data:
            min_heap.insert(value)
        insert_time = time.time() - start_time
        
        # Extract performance
        start_time = time.time()
        extracted = []
        while not min_heap.is_empty():
            extracted.append(min_heap.extract_min())
        extract_time = time.time() - start_time
        
        # Verify sorted order
        is_sorted = all(extracted[i] <= extracted[i + 1] for i in range(len(extracted) - 1))
        
        print(f"  Insert {size} elements: {insert_time:.4f}s")
        print(f"  Extract {size} elements: {extract_time:.4f}s")
        print(f"  Result is sorted: {is_sorted}")
        
        # Test build heap performance
        start_time = time.time()
        build_heap = MinHeap()
        build_heap.build_heap(data)
        build_time = time.time() - start_time
        
        print(f"  Build heap from array: {build_time:.4f}s")
        print()


if __name__ == "__main__":
    test_heaps()
    test_heap_applications()
    performance_analysis()
