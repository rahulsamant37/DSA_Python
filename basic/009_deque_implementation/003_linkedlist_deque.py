"""
003 - Linked List-Based Deque Implementation
============================================

Deque implementation using doubly linked list (dynamic size).

Time Complexity:
- Add/Remove from both ends: O(1)
- Access by index: O(n)
- Search: O(n)

Space Complexity: O(n) where n is number of elements
"""

from deque_node_001 import DequeNode


class LinkedListDeque:
    """Deque implementation using doubly linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.deque_size = 0
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.front is None
    
    def size(self):
        """Return current size of deque"""
        return self.deque_size
    
    def add_front(self, item):
        """Add item to front of deque"""
        new_node = DequeNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        
        self.deque_size += 1
    
    def add_rear(self, item):
        """Add item to rear of deque"""
        new_node = DequeNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.deque_size += 1
    
    def remove_front(self):
        """Remove and return item from front of deque"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.front.data
        
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.deque_size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return item from rear of deque"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.rear.data
        
        if self.front == self.rear:  # Only one element
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.deque_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.front.data
    
    def peek_rear(self):
        """Peek at rear item without removing it"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        return self.rear.data
    
    def display(self):
        """Display deque contents"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        print("Deque (front to rear):", end=" ")
        current = self.front
        while current:
            print(current.data, end=" ")
            current = current.next
        print()
    
    def display_reverse(self):
        """Display deque contents in reverse"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        print("Deque (rear to front):", end=" ")
        current = self.rear
        while current:
            print(current.data, end=" ")
            current = current.prev
        print()


def demo_linkedlist_deque():
    """Demonstrate LinkedListDeque functionality"""
    print("=== Linked List Deque Demo ===")
    
    # Create deque
    deque = LinkedListDeque()
    
    # Add elements to both ends
    print("Adding to rear: 10, 20")
    deque.add_rear(10)
    deque.add_rear(20)
    deque.display()
    
    print("\nAdding to front: 5, 0")
    deque.add_front(5)
    deque.add_front(0)
    deque.display()
    deque.display_reverse()
    
    # Peek operations
    print(f"\nFront element (peek): {deque.peek_front()}")
    print(f"Rear element (peek): {deque.peek_rear()}")
    print(f"Deque size: {deque.size()}")
    
    # Remove from both ends
    print(f"\nRemoving from front: {deque.remove_front()}")
    print(f"Removing from rear: {deque.remove_rear()}")
    deque.display()


if __name__ == "__main__":
    demo_linkedlist_deque()
