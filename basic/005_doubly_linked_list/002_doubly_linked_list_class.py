"""
002 - Doubly Linked List Class
==============================

Basic doubly linked list class with head and tail pointers.

Time Complexity:
- Initialization: O(1)
- is_empty: O(1)
- get_size: O(1)

Maintains both head and tail for efficient operations at both ends.
"""

from doubly_node_001 import DoublyNode


class DoublyLinkedList:
    """Doubly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the linked list"""
        return self.size
    
    def display_forward(self):
        """Display all elements from head to tail"""
        if self.is_empty():
            print("List is empty")
            return
        
        print("Forward traversal:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" <-> " if current.next else "")
            current = current.next
        print()
    
    def display_backward(self):
        """Display all elements from tail to head"""
        if self.is_empty():
            print("List is empty")
            return
        
        print("Backward traversal:", end=" ")
        current = self.tail
        while current:
            print(current.data, end=" <-> " if current.prev else "")
            current = current.prev
        print()


def demo_doubly_linked_list():
    """Demonstrate DoublyLinkedList basic functionality"""
    print("=== Doubly Linked List Class Demo ===")
    
    # Create list
    dll = DoublyLinkedList()
    print(f"Created empty doubly linked list")
    print(f"Is empty: {dll.is_empty()}")
    print(f"Size: {dll.get_size()}")
    dll.display_forward()
    
    # Manually create a small list for demonstration
    dll.head = DoublyNode(10)
    second = DoublyNode(20)
    third = DoublyNode(30)
    
    # Link them bidirectionally
    dll.head.next = second
    second.prev = dll.head
    second.next = third
    third.prev = second
    dll.tail = third
    dll.size = 3
    
    print(f"\nAfter adding nodes manually:")
    print(f"Is empty: {dll.is_empty()}")
    print(f"Size: {dll.get_size()}")
    dll.display_forward()
    dll.display_backward()


if __name__ == "__main__":
    demo_doubly_linked_list()
