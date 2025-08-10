"""
003 - Linked List-Based Stack Implementation
============================================

Stack implementation using linked list (dynamic size).

Time Complexity:
- Push: O(1)
- Pop: O(1)
- Peek: O(1)
- Search: O(n)

No size limitation compared to array-based stack.
"""

from stack_node_001 import StackNode


class LinkedListStack:
    """Stack implementation using linked list"""
    
    def __init__(self):
        self.head = None
        self.stack_size = 0
    
    def is_empty(self):
        """Check if stack is empty"""
        return self.head is None
    
    def size(self):
        """Return current size of stack"""
        return self.stack_size
    
    def push(self, item):
        """Push item onto stack"""
        new_node = StackNode(item)
        new_node.next = self.head
        self.head = new_node
        self.stack_size += 1
    
    def pop(self):
        """Pop item from stack"""
        if self.is_empty():
            raise IndexError("Stack underflow")
        
        item = self.head.data
        self.head = self.head.next
        self.stack_size -= 1
        return item
    
    def peek(self):
        """Peek at top item without removing it"""
        if self.is_empty():
            raise IndexError("Stack is empty")
        
        return self.head.data
    
    def display(self):
        """Display stack contents"""
        if self.is_empty():
            print("Stack is empty")
            return
        
        print("Stack (top to bottom):")
        current = self.head
        while current:
            print(f"  {current.data}")
            current = current.next


def demo_linkedlist_stack():
    """Demonstrate LinkedListStack functionality"""
    print("=== Linked List Stack Demo ===")
    
    # Create stack
    stack = LinkedListStack()
    
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
    demo_linkedlist_stack()
