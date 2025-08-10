"""
003 - Array Deletion Operations
===============================

Delete elements from different positions in the array.

Time Complexity:
- Delete from end: O(1)
- Delete from beginning: O(n)
- Delete from position: O(n)
"""

from array_class import Array
from array_insertion import display_array


def delete_from_end(arr):
    """Delete element from end of array"""
    if arr.is_empty():
        raise IndexError("Array is empty")
    
    deleted_element = arr.data[arr.size - 1]
    arr.data[arr.size - 1] = None
    arr.size -= 1
    return deleted_element


def delete_from_beginning(arr):
    """Delete element from beginning of array"""
    if arr.is_empty():
        raise IndexError("Array is empty")
    
    deleted_element = arr.data[0]
    
    # Shift all elements to left
    for i in range(1, arr.size):
        arr.data[i-1] = arr.data[i]
    
    arr.data[arr.size - 1] = None
    arr.size -= 1
    return deleted_element


def delete_from_position(arr, position):
    """Delete element from given position"""
    if arr.is_empty():
        raise IndexError("Array is empty")
    
    if position < 0 or position >= arr.size:
        raise IndexError("Invalid position")
    
    deleted_element = arr.data[position]
    
    # Shift elements to left from position
    for i in range(position + 1, arr.size):
        arr.data[i-1] = arr.data[i]
    
    arr.data[arr.size - 1] = None
    arr.size -= 1
    return deleted_element


def demo_deletion_operations():
    """Demonstrate array deletion operations"""
    print("=== Array Deletion Operations Demo ===")
    
    # Create and populate array
    arr = Array(5)
    arr.data = [10, 20, 30, 40, 50]
    arr.size = 5
    
    print("Initial array:")
    display_array(arr)
    
    # Delete from end
    print("\nDeleting from end:")
    deleted = delete_from_end(arr)
    print(f"Deleted element: {deleted}")
    display_array(arr)
    
    # Delete from beginning
    print("\nDeleting from beginning:")
    deleted = delete_from_beginning(arr)
    print(f"Deleted element: {deleted}")
    display_array(arr)
    
    # Delete from position
    print("\nDeleting from position 1:")
    deleted = delete_from_position(arr, 1)
    print(f"Deleted element: {deleted}")
    display_array(arr)


if __name__ == "__main__":
    demo_deletion_operations()
