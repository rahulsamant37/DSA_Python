"""
001 - Linear Search Implementation
=================================

Search for an element in an array using linear search.

Time Complexity: O(n)
Space Complexity: O(1)

Best for unsorted arrays and small datasets.
"""


def linear_search(arr, target):
    """
    Perform linear search on array
    
    Args:
        arr: List of elements to search
        target: Element to find
        
    Returns:
        Index of target if found, -1 otherwise
    """
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


def linear_search_all_occurrences(arr, target):
    """
    Find all occurrences of target in array
    
    Args:
        arr: List of elements to search
        target: Element to find
        
    Returns:
        List of indices where target is found
    """
    indices = []
    for i in range(len(arr)):
        if arr[i] == target:
            indices.append(i)
    return indices


def demo_linear_search():
    """Demonstrate linear search functionality"""
    print("=== Linear Search Demo ===")
    
    # Test array
    arr = [64, 34, 25, 12, 22, 11, 90, 12]
    print(f"Array: {arr}")
    
    # Search for existing element
    target = 22
    result = linear_search(arr, target)
    print(f"\nSearching for {target}:")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")
    
    # Search for non-existing element
    target = 99
    result = linear_search(arr, target)
    print(f"\nSearching for {target}:")
    if result != -1:
        print(f"Found at index: {result}")
    else:
        print("Not found")
    
    # Find all occurrences
    target = 12
    indices = linear_search_all_occurrences(arr, target)
    print(f"\nAll occurrences of {target}: {indices}")


if __name__ == "__main__":
    demo_linear_search()
