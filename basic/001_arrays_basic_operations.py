"""
001 - Arrays Basic Operations
=============================

This module demonstrates basic array operations including:
- Creation and initialization
- Insertion at different positions
- Deletion from different positions
- Traversal and display
- Finding elements

Time Complexity:
- Access: O(1)
- Search: O(n)
- Insertion: O(n) worst case, O(1) best case
- Deletion: O(n) worst case, O(1) best case
"""

class Array:
    def __init__(self, capacity):
        """Initialize array with given capacity"""
        self.capacity = capacity
        self.data = [None] * capacity
        self.size = 0
    
    def is_full(self):
        """Check if array is full"""
        return self.size == self.capacity
    
    def is_empty(self):
        """Check if array is empty"""
        return self.size == 0
    
    def insert_at_end(self, element):
        """Insert element at the end of array"""
        if self.is_full():
            raise OverflowError("Array is full")
        
        self.data[self.size] = element
        self.size += 1
        return True
    
    def insert_at_beginning(self, element):
        """Insert element at the beginning of array"""
        if self.is_full():
            raise OverflowError("Array is full")
        
        # Shift all elements to right
        for i in range(self.size, 0, -1):
            self.data[i] = self.data[i-1]
        
        self.data[0] = element
        self.size += 1
        return True
    
    def insert_at_position(self, element, position):
        """Insert element at given position"""
        if self.is_full():
            raise OverflowError("Array is full")
        
        if position < 0 or position > self.size:
            raise IndexError("Invalid position")
        
        # Shift elements to right from position
        for i in range(self.size, position, -1):
            self.data[i] = self.data[i-1]
        
        self.data[position] = element
        self.size += 1
        return True
    
    def delete_from_end(self):
        """Delete element from end of array"""
        if self.is_empty():
            raise IndexError("Array is empty")
        
        deleted_element = self.data[self.size - 1]
        self.data[self.size - 1] = None
        self.size -= 1
        return deleted_element
    
    def delete_from_beginning(self):
        """Delete element from beginning of array"""
        if self.is_empty():
            raise IndexError("Array is empty")
        
        deleted_element = self.data[0]
        
        # Shift all elements to left
        for i in range(1, self.size):
            self.data[i-1] = self.data[i]
        
        self.data[self.size - 1] = None
        self.size -= 1
        return deleted_element
    
    def delete_from_position(self, position):
        """Delete element from given position"""
        if self.is_empty():
            raise IndexError("Array is empty")
        
        if position < 0 or position >= self.size:
            raise IndexError("Invalid position")
        
        deleted_element = self.data[position]
        
        # Shift elements to left from position
        for i in range(position + 1, self.size):
            self.data[i-1] = self.data[i]
        
        self.data[self.size - 1] = None
        self.size -= 1
        return deleted_element
    
    def find_element(self, element):
        """Find element in array and return its index"""
        for i in range(self.size):
            if self.data[i] == element:
                return i
        return -1
    
    def get_element(self, index):
        """Get element at given index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        return self.data[index]
    
    def update_element(self, index, new_value):
        """Update element at given index"""
        if index < 0 or index >= self.size:
            raise IndexError("Index out of bounds")
        
        old_value = self.data[index]
        self.data[index] = new_value
        return old_value
    
    def display(self):
        """Display all elements in array"""
        if self.is_empty():
            print("Array is empty")
            return
        
        print("Array elements:", end=" ")
        for i in range(self.size):
            print(self.data[i], end=" ")
        print()
    
    def get_size(self):
        """Return current size of array"""
        return self.size
    
    def get_capacity(self):
        """Return capacity of array"""
        return self.capacity


def test_array_operations():
    """Test all array operations"""
    print("=== Testing Array Basic Operations ===\n")
    
    # Create array with capacity 5
    arr = Array(5)
    print(f"Created array with capacity: {arr.get_capacity()}")
    print(f"Initial size: {arr.get_size()}")
    print(f"Is empty: {arr.is_empty()}")
    print()
    
    # Insert elements
    print("Inserting elements at end: 10, 20, 30")
    arr.insert_at_end(10)
    arr.insert_at_end(20)
    arr.insert_at_end(30)
    arr.display()
    print()
    
    print("Inserting 5 at beginning:")
    arr.insert_at_beginning(5)
    arr.display()
    print()
    
    print("Inserting 15 at position 2:")
    arr.insert_at_position(15, 2)
    arr.display()
    print(f"Array is full: {arr.is_full()}")
    print()
    
    # Search operations
    print("Finding element 15:")
    index = arr.find_element(15)
    print(f"Element 15 found at index: {index}")
    print()
    
    print("Getting element at index 3:")
    element = arr.get_element(3)
    print(f"Element at index 3: {element}")
    print()
    
    # Update operation
    print("Updating element at index 1 to 25:")
    old_value = arr.update_element(1, 25)
    print(f"Old value: {old_value}")
    arr.display()
    print()
    
    # Delete operations
    print("Deleting from end:")
    deleted = arr.delete_from_end()
    print(f"Deleted element: {deleted}")
    arr.display()
    print()
    
    print("Deleting from beginning:")
    deleted = arr.delete_from_beginning()
    print(f"Deleted element: {deleted}")
    arr.display()
    print()
    
    print("Deleting from position 1:")
    deleted = arr.delete_from_position(1)
    print(f"Deleted element: {deleted}")
    arr.display()
    print()
    
    print(f"Final size: {arr.get_size()}")


if __name__ == "__main__":
    test_array_operations()
