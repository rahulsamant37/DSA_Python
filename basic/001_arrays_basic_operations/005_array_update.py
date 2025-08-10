"""
005 - Array Update Operations
=============================

Update elements in the array.

Time Complexity:
- Update element: O(1)
"""

from array_class import Array
from array_insertion import display_array


def update_element(arr, index, new_value):
    """Update element at given index"""
    if index < 0 or index >= arr.size:
        raise IndexError("Index out of bounds")
    
    old_value = arr.data[index]
    arr.data[index] = new_value
    return old_value


def demo_update_operations():
    """Demonstrate array update operations"""
    print("=== Array Update Operations Demo ===")
    
    # Create and populate array
    arr = Array(5)
    arr.data = [10, 20, 30, 40, 50]
    arr.size = 5
    
    print("Initial array:")
    display_array(arr)
    
    # Update element
    print("\nUpdating element at index 2 to 99:")
    old_value = update_element(arr, 2, 99)
    print(f"Old value: {old_value}")
    print("Updated array:")
    display_array(arr)


if __name__ == "__main__":
    demo_update_operations()
