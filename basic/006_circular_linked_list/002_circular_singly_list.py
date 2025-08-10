"""
002 - Circular Singly Linked List Class
=======================================

Basic circular singly linked list class with circular properties.

Time Complexity:
- Initialization: O(1)
- is_empty: O(1)
- get_size: O(1)

Key Property: Last node points back to the first node.
"""

from circular_node_001 import CircularSinglyListNode


class CircularSinglyLinkedList:
    """Circular Singly Linked List implementation"""
    
    def __init__(self):
        self.head = None
        self.size = 0
    
    def is_empty(self):
        """Check if the list is empty"""
        return self.head is None
    
    def get_size(self):
        """Return the size of the list"""
        return self.size
    
    def display(self):
        """Display all elements in the circular list"""
        if self.is_empty():
            print("Circular list is empty")
            return
        
        print("Circular list elements:", end=" ")
        current = self.head
        count = 0
        while count < self.size:
            print(current.data, end=" -> " if count < self.size - 1 else " -> (back to head)")
            current = current.next
            count += 1
        print()
    
    def display_full_cycle(self, cycles=2):
        """Display multiple cycles to show circular nature"""
        if self.is_empty():
            print("Circular list is empty")
            return
        
        print(f"Showing {cycles} complete cycles:")
        current = self.head
        total_nodes = cycles * self.size
        
        for i in range(total_nodes):
            print(current.data, end=" -> ")
            current = current.next
            if (i + 1) % self.size == 0:
                print("(cycle complete)", end=" -> ")
        print("...")


def demo_circular_singly_linked_list():
    """Demonstrate CircularSinglyLinkedList basic functionality"""
    print("=== Circular Singly Linked List Class Demo ===")
    
    # Create circular list
    csl = CircularSinglyLinkedList()
    print(f"Created empty circular list")
    print(f"Is empty: {csl.is_empty()}")
    print(f"Size: {csl.get_size()}")
    csl.display()
    
    # Manually create a small circular list for demonstration
    csl.head = CircularSinglyListNode(10)
    second = CircularSinglyListNode(20)
    third = CircularSinglyListNode(30)
    
    # Link them circularly
    csl.head.next = second
    second.next = third
    third.next = csl.head  # Circular connection
    csl.size = 3
    
    print(f"\nAfter adding nodes manually:")
    print(f"Is empty: {csl.is_empty()}")
    print(f"Size: {csl.get_size()}")
    csl.display()
    
    print(f"\nShowing circular nature:")
    csl.display_full_cycle(2)


if __name__ == "__main__":
    demo_circular_singly_linked_list()
