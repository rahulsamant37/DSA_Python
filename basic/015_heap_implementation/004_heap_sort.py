"""
004 - Heap Sort Implementation
==============================

Heap sort algorithm implementation using both min-heap and max-heap.
In-place sorting algorithm with guaranteed O(n log n) time complexity.

Time Complexity: O(n log n) - best, average, and worst case
Space Complexity: O(1) - in-place sorting (excluding input array)

Advantages:
- Consistent O(n log n) performance
- In-place sorting
- Not affected by input distribution

Disadvantages:
- Not stable (doesn't preserve relative order of equal elements)
- Poor cache locality compared to quicksort
"""

from typing import List


def heapify_down(arr: List[int], n: int, root: int, ascending: bool = True):
    """
    Maintain heap property by moving element down the tree
    
    Args:
        arr: Array to heapify
        n: Size of heap
        root: Root index to start heapifying from
        ascending: If True, use max-heap (for ascending sort)
    """
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    
    # For ascending sort, we need max-heap
    # For descending sort, we need min-heap
    compare = (lambda x, y: x > y) if ascending else (lambda x, y: x < y)
    
    # Check if left child exists and is larger/smaller than root
    if left < n and compare(arr[left], arr[largest]):
        largest = left
    
    # Check if right child exists and is larger/smaller than current largest
    if right < n and compare(arr[right], arr[largest]):
        largest = right
    
    # If largest is not root, swap and continue heapifying
    if largest != root:
        arr[root], arr[largest] = arr[largest], arr[root]
        heapify_down(arr, n, largest, ascending)


def build_heap(arr: List[int], ascending: bool = True):
    """
    Build heap from array in-place
    
    Args:
        arr: Array to convert to heap
        ascending: If True, build max-heap (for ascending sort)
    """
    n = len(arr)
    
    # Start from last non-leaf node and heapify each node
    # Last non-leaf node is at index (n//2 - 1)
    for i in range(n // 2 - 1, -1, -1):
        heapify_down(arr, n, i, ascending)


def heap_sort(arr: List[int], ascending: bool = True) -> List[int]:
    """
    Sort array using heap sort algorithm
    
    Args:
        arr: Array to sort
        ascending: If True, sort in ascending order
    
    Returns:
        Sorted array
    """
    if len(arr) <= 1:
        return arr[:]
    
    # Create a copy to avoid modifying original
    result = arr[:]
    n = len(result)
    
    # Step 1: Build heap
    build_heap(result, ascending)
    
    # Step 2: Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root to end (largest/smallest element)
        result[0], result[i] = result[i], result[0]
        
        # Call heapify on reduced heap
        heapify_down(result, i, 0, ascending)
    
    return result


def heap_sort_iterative(arr: List[int], ascending: bool = True) -> List[int]:
    """
    Iterative version of heapify for better understanding
    """
    if len(arr) <= 1:
        return arr[:]
    
    result = arr[:]
    n = len(result)
    
    # Build heap
    for i in range(n // 2 - 1, -1, -1):
        # Iterative heapify
        root = i
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            
            compare = (lambda x, y: x > y) if ascending else (lambda x, y: x < y)
            
            if left < n and compare(result[left], result[largest]):
                largest = left
            
            if right < n and compare(result[right], result[largest]):
                largest = right
            
            if largest == root:
                break
            
            result[root], result[largest] = result[largest], result[root]
            root = largest
    
    # Extract elements
    for i in range(n - 1, 0, -1):
        result[0], result[i] = result[i], result[0]
        
        # Iterative heapify for reduced heap
        root = 0
        heap_size = i
        while True:
            largest = root
            left = 2 * root + 1
            right = 2 * root + 2
            
            if left < heap_size and compare(result[left], result[largest]):
                largest = left
            
            if right < heap_size and compare(result[right], result[largest]):
                largest = right
            
            if largest == root:
                break
            
            result[root], result[largest] = result[largest], result[root]
            root = largest
    
    return result


def heap_sort_with_steps(arr: List[int], ascending: bool = True) -> List[int]:
    """
    Heap sort with step-by-step visualization
    """
    print(f"=== Heap Sort ({'Ascending' if ascending else 'Descending'}) ===")
    print(f"Original array: {arr}")
    
    if len(arr) <= 1:
        return arr[:]
    
    result = arr[:]
    n = len(result)
    
    # Step 1: Build heap
    print(f"\nStep 1: Building {'max' if ascending else 'min'}-heap")
    for i in range(n // 2 - 1, -1, -1):
        print(f"  Heapifying from index {i}: {result}")
        heapify_down(result, n, i, ascending)
        print(f"  After heapify: {result}")
    
    print(f"Heap built: {result}")
    
    # Step 2: Extract elements
    print(f"\nStep 2: Extracting elements")
    for i in range(n - 1, 0, -1):
        print(f"  Heap: {result[:i+1]} | Sorted: {result[i+1:]}")
        
        # Move root to end
        result[0], result[i] = result[i], result[0]
        print(f"  Moved {result[i]} to position {i}: {result}")
        
        # Heapify reduced heap
        heapify_down(result, i, 0, ascending)
        print(f"  Heapified: {result}")
    
    print(f"\nFinal sorted array: {result}")
    return result


def compare_heap_sort():
    """Compare heap sort with other sorting algorithms"""
    print("=== Heap Sort Comparison ===")
    
    print("Heap Sort characteristics:")
    print("✓ Time Complexity: O(n log n) - all cases")
    print("✓ Space Complexity: O(1) - in-place")
    print("✓ Stable performance regardless of input")
    print("✗ Not stable (doesn't preserve equal element order)")
    print("✗ Poor cache locality")
    
    print("\nComparison with other O(n log n) sorts:")
    
    print("\nQuick Sort:")
    print("✓ Generally faster due to better cache locality")
    print("✓ Good average performance")
    print("✗ O(n²) worst case")
    print("✗ Not stable")
    
    print("\nMerge Sort:")
    print("✓ Stable sort")
    print("✓ Guaranteed O(n log n)")
    print("✓ Good for linked lists")
    print("✗ O(n) extra space")
    
    print("\nWhen to use Heap Sort:")
    print("• Need guaranteed O(n log n) performance")
    print("• Memory constraints (in-place sorting)")
    print("• Don't need stable sorting")
    print("• Want consistent performance")


def demo_heap_sort():
    """Demonstrate heap sort functionality"""
    print("=== Heap Sort Demo ===")
    
    # Test arrays
    test_cases = [
        [64, 34, 25, 12, 22, 11, 90],
        [5, 2, 8, 1, 9],
        [1],
        [],
        [3, 3, 3, 3],
        [9, 8, 7, 6, 5, 4, 3, 2, 1]  # Reverse sorted
    ]
    
    for i, arr in enumerate(test_cases, 1):
        print(f"\nTest case {i}: {arr}")
        
        # Ascending sort
        sorted_asc = heap_sort(arr, ascending=True)
        print(f"Ascending:  {sorted_asc}")
        
        # Descending sort
        sorted_desc = heap_sort(arr, ascending=False)
        print(f"Descending: {sorted_desc}")
    
    # Detailed step-by-step for one case
    print("\n" + "="*50)
    test_array = [64, 34, 25, 12, 22, 11, 90]
    heap_sort_with_steps(test_array, ascending=True)


def benchmark_heap_sort():
    """Simple performance comparison"""
    import random
    import time
    
    print("\n=== Heap Sort Performance ===")
    
    sizes = [100, 1000, 10000]
    
    for size in sizes:
        # Generate random array
        arr = [random.randint(1, 1000) for _ in range(size)]
        
        # Time heap sort
        start_time = time.time()
        sorted_arr = heap_sort(arr)
        heap_time = time.time() - start_time
        
        # Time Python's built-in sort for comparison
        arr_copy = arr[:]
        start_time = time.time()
        arr_copy.sort()
        builtin_time = time.time() - start_time
        
        print(f"Size {size:,}:")
        print(f"  Heap sort:    {heap_time:.4f} seconds")
        print(f"  Built-in sort: {builtin_time:.4f} seconds")
        print(f"  Ratio:        {heap_time/builtin_time:.2f}x")
        
        # Verify correctness
        assert sorted_arr == arr_copy, "Heap sort produced incorrect result!"
    
    print("\nNote: Python's built-in sort (Timsort) is highly optimized")
    print("and typically outperforms basic implementations.")


if __name__ == "__main__":
    demo_heap_sort()
    compare_heap_sort()
    benchmark_heap_sort()
