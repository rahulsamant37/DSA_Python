"""
002 - Quick Sort Implementation
==============================

Sort array using quick sort algorithm.

Time Complexity: O(n log n) average, O(n²) worst case
Space Complexity: O(log n) average

Efficient divide-and-conquer sorting algorithm.
"""


def partition(arr, low, high):
    """
    Partition function for quick sort
    
    Args:
        arr: Array to partition
        low: Starting index
        high: Ending index
        
    Returns:
        Partition index
    """
    # Choose rightmost element as pivot
    pivot = arr[high]
    
    # Index of smaller element
    i = low - 1
    
    for j in range(low, high):
        # If current element is smaller than or equal to pivot
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    # Place pivot in correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_helper(arr, low, high):
    """
    Helper function for quick sort recursion
    
    Args:
        arr: Array to sort
        low: Starting index
        high: Ending index
    """
    if low < high:
        # Partition index
        pi = partition(arr, low, high)
        
        # Recursively sort elements before and after partition
        quick_sort_helper(arr, low, pi - 1)
        quick_sort_helper(arr, pi + 1, high)


def quick_sort(arr):
    """
    Sort array using quick sort algorithm
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    arr_copy = arr.copy()
    quick_sort_helper(arr_copy, 0, len(arr_copy) - 1)
    return arr_copy


def quick_sort_inplace(arr):
    """
    Sort array in-place using quick sort
    
    Args:
        arr: List of elements to sort (modified in-place)
    """
    quick_sort_helper(arr, 0, len(arr) - 1)


def demo_quick_sort():
    """Demonstrate quick sort functionality"""
    print("=== Quick Sort Demo ===")
    
    # Test array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    
    # Sort using copy version
    sorted_arr = quick_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    print(f"Original unchanged: {arr}")
    
    # Sort in-place
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"\nIn-place sorting: {test_arr}")
    quick_sort_inplace(test_arr)
    print(f"After in-place sort: {test_arr}")
    
    # Test with edge cases
    print(f"\nEdge cases:")
    print(f"Empty array: {quick_sort([])}")
    print(f"Single element: {quick_sort([42])}")
    print(f"Already sorted: {quick_sort([1, 2, 3, 4, 5])}")
    print(f"Reverse sorted: {quick_sort([5, 4, 3, 2, 1])}")


if __name__ == "__main__":
    demo_quick_sort()
