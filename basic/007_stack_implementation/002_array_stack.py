"""
002 - Array-Based Stack Implementation
=====================================

Stack implementation using array (list) with fixed capacity.

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

Stack follows LIFO (Last In, First Out) principle.
"""

class ArrayStack:
    """Stack implementation using array (list)"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.top_index = -1
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.top_index == -1
    
    def is_full(self):
        """Check if stack is full"""
        return self.top_index == self.capacity - 1
    
    def size(self):
        """Return current size of stack"""
        return self.top_index + 1
    
    def push(self, item):
        """Push item onto stack"""
        if self.is_full():
            raise OverflowError("Stack overflow")
        
        self.top_index += 1
        self.data[self.top_index] = item
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        item = self.data[self.top_index]
        self.data[self.top_index] = None
        self.top_index -= 1
        return item
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.data[self.top_index]
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        for i in range(self.top_index, -1, -1):
            print(f"  {self.data[i]}")


def demo_array_stack():
    """Demonstrate ArrayStack functionality"""
    print("=== Array Stack Demo ===")
    
    # Create stack
    stack = ArrayStack(5)
    
    # Push elements
    print("Pushing elements: 10, 20, 30")
    stack.push(10)
    stack.push(20)
    stack.push(30)
    stack.display()
    
    # Peek
    print(f"\nTop element (peek): {stack.peek()}")
    print(f"Stack size: {stack.size()}")
    
    # Pop elements
    print(f"\nPopping: {stack.pop()}")
    print(f"Popping: {stack.pop()}")
    stack.display()


if __name__ == "__main__":
    demo_array_stack()
