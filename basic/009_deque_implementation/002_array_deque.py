"""
002 - Array-Based Deque Implementation
======================================

Deque implementation using circular array with fixed capacity.

Time Complexity:
- Add/Remove from both ends: O(1)
- Access by index: O(1)
- Search: O(n)

Space Complexity: O(n) where n is capacity
"""

class ArrayDeque:
    """Deque implementation using circular array"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.deque_size = 0
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.deque_size == 0
    
    def is_full(self):
        """Check if deque is full"""
        return self.deque_size == self.capacity
    
    def size(self):
        """Return current size of deque"""
        return self.deque_size
    
    def add_front(self, item):
        """Add item to front of deque"""
        if self.is_full():
            raise OverflowError("Deque overflow")
        
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = item
        self.deque_size += 1
    
    def add_rear(self, item):
        """Add item to rear of deque"""
        if self.is_full():
            raise OverflowError("Deque overflow")
        
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.deque_size += 1
    
    def remove_front(self):
        """Remove and return item from front of deque"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.deque_size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return item from rear of deque"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        self.rear = (self.rear - 1) % self.capacity
        item = self.data[self.rear]
        self.data[self.rear] = None
        self.deque_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.data[self.front]
    
    def peek_rear(self):
        """Peek at rear item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        rear_index = (self.rear - 1) % self.capacity
        return self.data[rear_index]
    
    def display(self):
        """Display deque contents"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        print("Deque (front to rear):", end=" ")
        i = self.front
        for _ in range(self.deque_size):
            print(self.data[i], end=" ")
            i = (i + 1) % self.capacity
        print()


def demo_array_deque():
    """Demonstrate ArrayDeque functionality"""
    print("=== Array Deque Demo ===")
    
    # Create deque
    deque = ArrayDeque(5)
    
    # Add elements to both ends
    print("Adding to rear: 10, 20")
    deque.add_rear(10)
    deque.add_rear(20)
    deque.display()
    
    print("\nAdding to front: 5, 0")
    deque.add_front(5)
    deque.add_front(0)
    deque.display()
    
    # Peek operations
    print(f"\nFront element (peek): {deque.peek_front()}")
    print(f"Rear element (peek): {deque.peek_rear()}")
    print(f"Deque size: {deque.size()}")
    
    # Remove from both ends
    print(f"\nRemoving from front: {deque.remove_front()}")
    print(f"Removing from rear: {deque.remove_rear()}")
    deque.display()


if __name__ == "__main__":
    demo_array_deque()
