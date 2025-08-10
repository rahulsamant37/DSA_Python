"""
001 - Array Class Definition
===========================

Basic Array class with capacity and size management.

Time Complexity:
- Initialization: O(1)
- is_full/is_empty: O(1)
- get_size/get_capacity: O(1)
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
    
    def get_size(self):
        """Return current size of array"""
        return self.size
    
    def get_capacity(self):
        """Return capacity of array"""
        return self.capacity


def demo_array_class():
    """Demonstrate Array class basic functionality"""
    print("=== Array Class Demo ===")
    
    # Create array
    arr = Array(5)
    print(f"Created array with capacity: {arr.get_capacity()}")
    print(f"Initial size: {arr.get_size()}")
    print(f"Is empty: {arr.is_empty()}")
    print(f"Is full: {arr.is_full()}")


if __name__ == "__main__":
    demo_array_class()
