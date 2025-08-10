"""
004 - Python List-Based Stack Implementation
===========================================

Stack implementation using Python's built-in list.

Time Complexity:
- Push: O(1) amortized
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

Most practical approach for Python development.
"""

class PythonListStack:
    """Stack implementation using Python's built-in list"""
    
    def __init__(self):
        self.data = []
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.data) == 0
    
    def size(self):
        """Return current size of stack"""
        return len(self.data)
    
    def push(self, item):
        """Push item onto stack"""
        self.data.append(item)
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        return self.data.pop()
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.data[-1]
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        for i in range(len(self.data) - 1, -1, -1):
            print(f"  {self.data[i]}")


def demo_python_list_stack():
    """Demonstrate PythonListStack functionality"""
    print("=== Python List Stack Demo ===")
    
    # Create stack
    stack = PythonListStack()
    
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
    demo_python_list_stack()
