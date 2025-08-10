"""
002 - Singly Linked List Class
==============================

Basic singly linked list class with initialization.

Time Complexity:
- Initialization: O(1)
- is_empty: O(1)
- get_size: O(1)
"""

from list_node_001 import ListNode


class SinglyLinkedList:
    """Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the linked list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the linked list"""
        return self.size
    
    def display(self):
        """Display all elements in the list"""
        if self.is_empty():
            print("List is empty")
            return
        
        print("List elements:", end=" ")
        current = self.head
        while current:
            print(current.data, end=" -> " if current.next else "")
            current = current.next
        print()


def demo_singly_linked_list():
    """Demonstrate SinglyLinkedList basic functionality"""
    print("=== Singly Linked List Class Demo ===")
    
    # Create list
    sll = SinglyLinkedList()
    print(f"Created empty list")
    print(f"Is empty: {sll.is_empty()}")
    print(f"Size: {sll.get_size()}")
    sll.display()


if __name__ == "__main__":
    demo_singly_linked_list()
