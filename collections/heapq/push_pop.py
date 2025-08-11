"""
heappush and heappop - Adding and removing elements from heap

heappush() and heappop() maintain the heap invariant while adding/removing elements.
These are the fundamental operations for implementing priority queues and heap algorithms.
"""

import heapq

def heappush_examples():
    """Demonstrates heappush operation"""
    
    print("--- heappush Examples ---")
    
    # Start with empty heap
    heap = []
    print(f"Initial heap: {heap}")
    
    # Push elements one by one
    elements = [4, 1, 7, 3, 8, 5, 2]
    print("\nPushing elements:")
    
    for element in elements:
        heapq.heappush(heap, element)
        print(f"Push {element}: {heap}")
    
    print(f"\nFinal heap: {heap}")
    print(f"Minimum element (heap[0]): {heap[0]}")
    print()

def heappop_examples():
    """Demonstrates heappop operation"""
    
    print("--- heappop Examples ---")
    
    # Create a heap
    heap = [1, 3, 5, 7, 9, 8, 6]
    print(f"Initial heap: {heap}")
    
    print("\nPopping elements:")
    original_heap = heap.copy()
    
    while heap:
        min_element = heapq.heappop(heap)
        print(f"Popped {min_element}: remaining = {heap}")
    
    print("Note: Elements are popped in sorted order (min to max)")
    print()
    
    # Demonstrate error handling
    print("--- Error Handling ---")
    empty_heap = []
    try:
        heapq.heappop(empty_heap)
    except IndexError as e:
        print(f"heappop on empty heap: {e}")
    print()

def combined_operations():
    """Demonstrates combined push and pop operations"""
    
    print("--- Combined Push and Pop Operations ---")
    
    heap = []
    
    # Simulate a dynamic priority queue
    operations = [
        ('push', 5), ('push', 2), ('push', 8),
        ('pop', None), ('push', 1), ('push', 9),
        ('pop', None), ('pop', None), ('push', 3)
    ]
    
    print("Simulating dynamic operations:")
    for op, value in operations:
        if op == 'push':
            heapq.heappush(heap, value)
            print(f"Push {value}: {heap}")
        elif op == 'pop' and heap:
            popped = heapq.heappop(heap)
            print(f"Pop {popped}: {heap}")
        elif op == 'pop':
            print("Pop from empty heap: skipped")
    
    print(f"\nFinal heap: {heap}")
    print()

def heap_with_priorities():
    """Using heappush/heappop with priority tuples"""
    
    print("--- Priority-based Operations ---")
    
    # Task scheduling with priorities
    task_queue = []
    
    tasks = [
        (2, "Medium priority task A"),
        (1, "High priority task B"),
        (3, "Low priority task C"),
        (1, "High priority task D"),
        (2, "Medium priority task E")
    ]
    
    print("Adding tasks to priority queue:")
    for priority, task in tasks:
        heapq.heappush(task_queue, (priority, task))
        print(f"Added: priority={priority}, task='{task}'")
    
    print(f"\nTask queue: {task_queue}")
    
    print("\nProcessing tasks by priority:")
    while task_queue:
        priority, task = heapq.heappop(task_queue)
        print(f"Execute: priority={priority}, task='{task}'")
    print()

def performance_characteristics():
    """Demonstrates performance characteristics of heap operations"""
    
    print("--- Performance Characteristics ---")
    
    import time
    import random
    
    # Test with different heap sizes
    sizes = [1000, 10000, 100000]
    
    for size in sizes:
        # Generate random data
        data = [random.randint(1, 1000000) for _ in range(size)]
        
        # Test heappush performance
        heap = []
        start_time = time.time()
        for element in data:
            heapq.heappush(heap, element)
        push_time = time.time() - start_time
        
        # Test heappop performance
        start_time = time.time()
        results = []
        while heap:
            results.append(heapq.heappop(heap))
        pop_time = time.time() - start_time
        
        print(f"Size: {size:,}")
        print(f"  Push all elements: {push_time:.4f} seconds")
        print(f"  Pop all elements: {pop_time:.4f} seconds")
        print(f"  Total time: {push_time + pop_time:.4f} seconds")
        print(f"  Average per operation: {(push_time + pop_time) / (2 * size) * 1000:.4f} ms")
        print()

def dsa_use_cases():
    """DSA applications of heappush and heappop"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: K Smallest Elements
    print("1. Find K Smallest Elements:")
    def k_smallest(arr, k):
        """
        Find k smallest elements using heap.
        Time Complexity: O(n log k)
        """
        if k >= len(arr):
            return sorted(arr)
        
        # Use max heap to keep track of k smallest
        # Python heapq is min heap, so use negative values for max heap
        max_heap = []
        
        for num in arr:
            if len(max_heap) < k:
                heapq.heappush(max_heap, -num)  # Negative for max heap
            elif -max_heap[0] > num:  # Current max > new number
                heapq.heappop(max_heap)
                heapq.heappush(max_heap, -num)
        
        # Convert back to positive and sort
        return sorted([-x for x in max_heap])
    
    arr = [7, 10, 4, 3, 20, 15]
    k = 3
    result = k_smallest(arr, k)
    print(f"Array: {arr}")
    print(f"K={k} smallest elements: {result}")
    print()
    
    # Use Case 2: Merge K Sorted Lists
    print("2. Merge K Sorted Lists:")
    def merge_k_sorted_lists(lists):
        """
        Merge k sorted lists using heap.
        Time Complexity: O(n log k) where n is total elements
        """
        import itertools
        
        heap = []
        result = []
        
        # Add first element from each list to heap
        for i, lst in enumerate(lists):
            if lst:
                heapq.heappush(heap, (lst[0], i, 0))  # (value, list_index, element_index)
        
        while heap:
            value, list_idx, elem_idx = heapq.heappop(heap)
            result.append(value)
            
            # Add next element from the same list
            if elem_idx + 1 < len(lists[list_idx]):
                next_value = lists[list_idx][elem_idx + 1]
                heapq.heappush(heap, (next_value, list_idx, elem_idx + 1))
        
        return result
    
    sorted_lists = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    
    merged = merge_k_sorted_lists(sorted_lists)
    print(f"Input lists: {sorted_lists}")
    print(f"Merged result: {merged}")
    print()
    
    # Use Case 3: Top K Frequent Elements
    print("3. Top K Frequent Elements:")
    def top_k_frequent(nums, k):
        """
        Find k most frequent elements.
        Time Complexity: O(n log k)
        """
        from collections import Counter
        
        # Count frequencies
        count = Counter(nums)
        
        # Use min heap to keep track of k most frequent
        heap = []
        
        for num, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, num))
            elif heap[0][0] < freq:
                heapq.heappop(heap)
                heapq.heappush(heap, (freq, num))
        
        # Extract elements (order doesn't matter for this problem)
        return [num for freq, num in heap]
    
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f"Array: {nums}")
    print(f"Top {k} frequent elements: {result}")
    print()
    
    # Use Case 4: Running Median
    print("4. Running Median:")
    class MedianFinder:
        """
        Find median of a stream of numbers using two heaps.
        """
        def __init__(self):
            self.small = []  # Max heap (use negative values)
            self.large = []  # Min heap
        
        def add_number(self, num):
            """Add number and maintain median property"""
            if len(self.small) == len(self.large):
                heapq.heappush(self.large, -heapq.heappushpop(self.small, -num))
            else:
                heapq.heappush(self.small, -heapq.heappushpop(self.large, num))
        
        def find_median(self):
            """Return current median"""
            if len(self.small) == len(self.large):
                return (-self.small[0] + self.large[0]) / 2.0
            else:
                return float(self.large[0])
    
    mf = MedianFinder()
    numbers = [5, 15, 1, 3, 8, 7, 9, 2, 10]
    
    print("Adding numbers and finding running median:")
    for num in numbers:
        mf.add_number(num)
        median = mf.find_median()
        print(f"Add {num}: median = {median}")

if __name__ == "__main__":
    heappush_examples()
    heappop_examples()
    combined_operations()
    heap_with_priorities()
    performance_characteristics()
    dsa_use_cases()
