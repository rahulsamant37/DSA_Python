"""
003 - Doubly Linked List Insertion Operations
=============================================

Insert elements at different positions in the doubly linked list.

Time Complexity:
- Prepend (insert at beginning): O(1)
- Append (insert at end): O(1)
- Insert at position: O(n)

Advantages: Efficient insertion at both ends due to tail pointer.
"""

from doubly_node_001 import DoublyNode
from doubly_linked_list_class_002 import DoublyLinkedList


def prepend(dll, data):
    """Insert element at the beginning of the list"""
    new_node = DoublyNode(data)
    
    if dll.is_empty():
        dll.head = dll.tail = new_node
    else:
        new_node.next = dll.head
        dll.head.prev = new_node
        dll.head = new_node
    
    dll.size += 1


def append(dll, data):
    """Insert element at the end of the list"""
    new_node = DoublyNode(data)
    
    if dll.is_empty():
        dll.head = dll.tail = new_node
    else:
        new_node.prev = dll.tail
        dll.tail.next = new_node
        dll.tail = new_node
    
    dll.size += 1


def insert_at_position(dll, data, position):
    """Insert element at specific position (0-indexed)"""
    if position < 0 or position > dll.size:
        raise IndexError("Position out of bounds")
    
    if position == 0:
        prepend(dll, data)
        return
    
    if position == dll.size:
        append(dll, data)
        return
    
    new_node = DoublyNode(data)
    
    # Decide whether to traverse from head or tail (optimization)
    if position <= dll.size // 2:
        # Traverse from head
        current = dll.head
        for _ in range(position):
            current = current.next
    else:
        # Traverse from tail
        current = dll.tail
        for _ in range(dll.size - position - 1):
            current = current.prev
    
    # Insert before current
    new_node.next = current
    new_node.prev = current.prev
    current.prev.next = new_node
    current.prev = new_node
    
    dll.size += 1


def demo_doubly_insertion_operations():
    """Demonstrate doubly linked list insertion operations"""
    print("=== Doubly Linked List Insertion Operations Demo ===")
    
    # Create list
    dll = DoublyLinkedList()
    
    # Prepend elements
    print("\nPrepending elements: 30, 20, 10")
    prepend(dll, 30)
    dll.display_forward()
    prepend(dll, 20)
    dll.display_forward()
    prepend(dll, 10)
    dll.display_forward()
    
    # Append elements
    print("\nAppending elements: 40, 50")
    append(dll, 40)
    dll.display_forward()
    append(dll, 50)
    dll.display_forward()
    
    # Insert at position
    print("\nInserting 25 at position 2:")
    insert_at_position(dll, 25, 2)
    dll.display_forward()
    dll.display_backward()
    
    print(f"\nFinal size: {dll.get_size()}")
    
    # Demonstrate bidirectional capability
    print("\nBidirectional traversal capability:")
    dll.display_forward()
    dll.display_backward()


if __name__ == "__main__":
    demo_doubly_insertion_operations()
