"""
Binary Search Pattern - Search in Sorted Array
===============================================

Find target element in sorted array using binary search.

Time Complexity: O(log n)
Space Complexity: O(1)
"""


def binary_search(arr, target):
    """
    Search for target in sorted array using binary search.
    
    Args:
        arr: Sorted array of integers
        target: Element to search for
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1  # Search right half
        else:
            right = mid - 1  # Search left half
    
    return -1  # Target not found


def example_usage():
    """Demonstrate binary search"""
    arr = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
    
    # Search for existing element
    target = 7
    index = binary_search(arr, target)
    print(f"Array: {arr}")
    print(f"Target {target} found at index: {index}")
    
    # Search for non-existing element
    target = 6
    index = binary_search(arr, target)
    print(f"Target {target} found at index: {index}")
    
    # Search at boundaries
    target = 1
    index = binary_search(arr, target)
    print(f"Target {target} (first element) found at index: {index}")
    
    target = 19
    index = binary_search(arr, target)
    print(f"Target {target} (last element) found at index: {index}")


if __name__ == "__main__":
    example_usage()
