"""
003 - Circular List Insertion Operations
========================================

Insert elements into circular linked list maintaining circular property.

Time Complexity:
- Insert at head: O(1) if we maintain tail pointer, O(n) otherwise
- Insert at tail: O(1) if we maintain tail pointer, O(n) otherwise
- Insert at position: O(n)
"""

from circular_node_001 import CircularSinglyListNode
from circular_singly_list_002 import CircularSinglyLinkedList


def insert_at_head(csl, data):
    """Insert element at the head of circular list"""
    new_node = CircularSinglyListNode(data)
    
    if csl.is_empty():
        new_node.next = new_node  # Points to itself
        csl.head = new_node
    else:
        # Find the last node
        current = csl.head
        while current.next != csl.head:
            current = current.next
        
        # Insert new node at head
        new_node.next = csl.head
        current.next = new_node
        csl.head = new_node
    
    csl.size += 1


def insert_at_tail(csl, data):
    """Insert element at the tail of circular list"""
    new_node = CircularSinglyListNode(data)
    
    if csl.is_empty():
        new_node.next = new_node  # Points to itself
        csl.head = new_node
    else:
        # Find the last node
        current = csl.head
        while current.next != csl.head:
            current = current.next
        
        # Insert new node at tail
        new_node.next = csl.head
        current.next = new_node
    
    csl.size += 1


def insert_at_position(csl, data, position):
    """Insert element at given position (0-indexed)"""
    if position < 0 or position > csl.size:
        raise IndexError("Position out of bounds")
    
    if position == 0:
        insert_at_head(csl, data)
        return
    
    if position == csl.size:
        insert_at_tail(csl, data)
        return
    
    new_node = CircularSinglyListNode(data)
    current = csl.head
    
    # Traverse to position-1
    for _ in range(position - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    csl.size += 1


def demo_circular_insertion_operations():
    """Demonstrate circular list insertion operations"""
    print("=== Circular List Insertion Operations Demo ===")
    
    # Create circular list
    csl = CircularSinglyLinkedList()
    
    # Insert at head
    print("\nInserting at head: 30, 20, 10")
    insert_at_head(csl, 30)
    csl.display()
    insert_at_head(csl, 20)
    csl.display()
    insert_at_head(csl, 10)
    csl.display()
    
    # Insert at tail
    print("\nInserting at tail: 40, 50")
    insert_at_tail(csl, 40)
    csl.display()
    insert_at_tail(csl, 50)
    csl.display()
    
    # Insert at position
    print("\nInserting 25 at position 2:")
    insert_at_position(csl, 25, 2)
    csl.display()
    
    print(f"\nFinal size: {csl.get_size()}")
    print("Showing circular nature:")
    csl.display_full_cycle(1)


if __name__ == "__main__":
    demo_circular_insertion_operations()
