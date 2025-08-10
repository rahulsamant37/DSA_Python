"""
001 - Bubble Sort Implementation
===============================

Sort array using bubble sort algorithm.

Time Complexity: O(n²) worst/average case, O(n) best case
Space Complexity: O(1)

Simple but inefficient sorting algorithm.
"""


def bubble_sort(arr):
    """
    Sort array using bubble sort algorithm
    
    Args:
        arr: List of elements to sort
        
    Returns:
        Sorted list
    """
    n = len(arr)
    arr = arr.copy()  # Don't modify original array
    
    for i in range(n):
        # Flag to optimize for already sorted arrays
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swapping occurred, array is sorted
        if not swapped:
            break
    
    return arr


def bubble_sort_inplace(arr):
    """
    Sort array in-place using bubble sort
    
    Args:
        arr: List of elements to sort (modified in-place)
    """
    n = len(arr)
    
    for i in range(n):
        swapped = False
        
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        if not swapped:
            break


def demo_bubble_sort():
    """Demonstrate bubble sort functionality"""
    print("=== Bubble Sort Demo ===")
    
    # Test array
    arr = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original array: {arr}")
    
    # Sort using copy version
    sorted_arr = bubble_sort(arr)
    print(f"Sorted array: {sorted_arr}")
    print(f"Original unchanged: {arr}")
    
    # Sort in-place
    print(f"\nIn-place sorting: {arr}")
    bubble_sort_inplace(arr)
    print(f"After in-place sort: {arr}")
    
    # Test with already sorted array
    sorted_test = [1, 2, 3, 4, 5]
    print(f"\nAlready sorted test: {sorted_test}")
    result = bubble_sort(sorted_test)
    print(f"Result: {result}")


if __name__ == "__main__":
    demo_bubble_sort()
