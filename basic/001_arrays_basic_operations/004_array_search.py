"""
004 - Array Search Operations
=============================

Search and access elements in the array.

Time Complexity:
- Find element: O(n)
- Get element by index: O(1)
"""

from array_class import Array


def find_element(arr, element):
    """Find element in array and return its index"""
    for i in range(arr.size):
        if arr.data[i] == element:
            return i
    return -1


def get_element(arr, index):
    """Get element at given index"""
    if index < 0 or index >= arr.size:
        raise IndexError("Index out of bounds")
    return arr.data[index]


def demo_search_operations():
    """Demonstrate array search operations"""
    print("=== Array Search Operations Demo ===")
    
    # Create and populate array
    arr = Array(5)
    arr.data = [10, 20, 30, 40, 50]
    arr.size = 5
    
    print("Array:", [arr.data[i] for i in range(arr.size)])
    
    # Find element
    print("\nSearching for element 30:")
    index = find_element(arr, 30)
    if index != -1:
        print(f"Element 30 found at index: {index}")
    else:
        print("Element not found")
    
    print("\nSearching for element 60:")
    index = find_element(arr, 60)
    if index != -1:
        print(f"Element 60 found at index: {index}")
    else:
        print("Element not found")
    
    # Get element by index
    print("\nGetting element at index 2:")
    element = get_element(arr, 2)
    print(f"Element at index 2: {element}")


if __name__ == "__main__":
    demo_search_operations()
