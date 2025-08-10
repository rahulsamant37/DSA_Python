"""
003 - Linked List Insertion Operations
======================================

Insert elements at different positions in the linked list.

Time Complexity:
- Prepend (insert at beginning): O(1)
- Append (insert at end): O(n)
- Insert at position: O(n)
"""

from list_node_001 import ListNode
from singly_linked_list_class_002 import SinglyLinkedList


def prepend(sll, data):
    """Insert element at the beginning of the list"""
    new_node = ListNode(data)
    new_node.next = sll.head
    sll.head = new_node
    sll.size += 1


def append(sll, data):
    """Insert element at the end of the list"""
    new_node = ListNode(data)
    
    if sll.is_empty():
        sll.head = new_node
    else:
        current = sll.head
        while current.next:
            current = current.next
        current.next = new_node
    
    sll.size += 1


def insert_at_position(sll, data, position):
    """Insert element at given position (0-indexed)"""
    if position < 0 or position > sll.size:
        raise IndexError("Position out of bounds")
    
    if position == 0:
        prepend(sll, data)
        return
    
    if position == sll.size:
        append(sll, data)
        return
    
    new_node = ListNode(data)
    current = sll.head
    
    # Traverse to position-1
    for _ in range(position - 1):
        current = current.next
    
    new_node.next = current.next
    current.next = new_node
    sll.size += 1


def demo_insertion_operations():
    """Demonstrate linked list insertion operations"""
    print("=== Linked List Insertion Operations Demo ===")
    
    # Create list
    sll = SinglyLinkedList()
    
    # Prepend elements
    print("\nPrepending elements: 30, 20, 10")
    prepend(sll, 30)
    prepend(sll, 20)
    prepend(sll, 10)
    sll.display()
    
    # Append elements
    print("\nAppending elements: 40, 50")
    append(sll, 40)
    append(sll, 50)
    sll.display()
    
    # Insert at position
    print("\nInserting 25 at position 2:")
    insert_at_position(sll, 25, 2)
    sll.display()
    
    print(f"\nFinal size: {sll.get_size()}")


if __name__ == "__main__":
    demo_insertion_operations()
