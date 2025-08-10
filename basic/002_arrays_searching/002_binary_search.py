"""
002 - Binary Search Implementation
==================================

Search for an element in a sorted array using binary search.

Time Complexity: O(log n)
Space Complexity: O(1) iterative, O(log n) recursive

Requires sorted array.
"""


def binary_search_iterative(arr, target):
    """
    Perform binary search iteratively
    
    Args:
        arr: Sorted list of elements
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_recursive(arr, target, left=0, right=None):
    """
    Perform binary search recursively
    
    Args:
        arr: Sorted list of elements
        target: Element to find
        left: Left boundary
        right: Right boundary
        
    Returns:
        Index of target if found, -1 otherwise
    """
    if right is None:
        right = len(arr) - 1
    
    if left > right:
        return -1
    
    mid = left + (right - left) // 2
    
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)


def demo_binary_search():
    """Demonstrate binary search functionality"""
    print("=== Binary Search Demo ===")
    
    # Test array (must be sorted)
    arr = [11, 12, 22, 25, 34, 64, 90]
    print(f"Sorted array: {arr}")
    
    # Test iterative version
    target = 22
    result = binary_search_iterative(arr, target)
    print(f"\nIterative search for {target}:")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")
    
    # Test recursive version
    target = 90
    result = binary_search_recursive(arr, target)
    print(f"\nRecursive search for {target}:")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")
    
    # Test with non-existing element
    target = 99
    result = binary_search_iterative(arr, target)
    print(f"\nSearch for non-existing {target}:")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")


if __name__ == "__main__":
    demo_binary_search()
