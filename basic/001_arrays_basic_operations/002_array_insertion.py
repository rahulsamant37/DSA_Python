"""
002 - Array Insertion Operations
================================

Insert elements at different positions in the array.

Time Complexity:
- Insert at end: O(1)
- Insert at beginning: O(n)
- Insert at position: O(n)
"""

from array_class_001 import Array


def insert_at_end(arr, element):
    """Insert element at the end of array"""
    if arr.is_full():
        raise OverflowError("Array is full")
    
    arr.data[arr.size] = element
    arr.size += 1
    return True


def insert_at_beginning(arr, element):
    """Insert element at the beginning of array"""
    if arr.is_full():
        raise OverflowError("Array is full")
    
    # Shift all elements to right
    for i in range(arr.size, 0, -1):
        arr.data[i] = arr.data[i-1]
    
    arr.data[0] = element
    arr.size += 1
    return True


def insert_at_position(arr, element, position):
    """Insert element at given position"""
    if arr.is_full():
        raise OverflowError("Array is full")
    
    if position < 0 or position > arr.size:
        raise IndexError("Invalid position")
    
    # Shift elements to right from position
    for i in range(arr.size, position, -1):
        arr.data[i] = arr.data[i-1]
    
    arr.data[position] = element
    arr.size += 1
    return True


def display_array(arr):
    """Display all elements in array"""
    if arr.is_empty():
        print("Array is empty")
        return
    
    print("Array elements:", end=" ")
    for i in range(arr.size):
        print(arr.data[i], end=" ")
    print()


def demo_insertion_operations():
    """Demonstrate array insertion operations"""
    print("=== Array Insertion Operations Demo ===")
    
    # Create array
    arr = Array(5)
    
    # Insert at end
    print("\nInserting 10, 20, 30 at end:")
    insert_at_end(arr, 10)
    insert_at_end(arr, 20)
    insert_at_end(arr, 30)
    display_array(arr)
    
    # Insert at beginning
    print("\nInserting 5 at beginning:")
    insert_at_beginning(arr, 5)
    display_array(arr)
    
    # Insert at position
    print("\nInserting 15 at position 2:")
    insert_at_position(arr, 15, 2)
    display_array(arr)


if __name__ == "__main__":
    demo_insertion_operations()
