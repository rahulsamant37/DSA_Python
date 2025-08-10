"""
001 - Doubly Linked List Node
=============================

Basic node class for doubly linked list.

Time Complexity:
- Initialization: O(1)
"""

class DoublyNode:
    """Node class for doubly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)


def demo_doubly_node():
    """Demonstrate DoublyNode functionality"""
    print("=== Doubly Node Demo ===")
    
    # Create nodes
    node1 = DoublyNode(10)
    node2 = DoublyNode(20)
    node3 = DoublyNode(30)
    
    # Link nodes bidirectionally
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    
    print("Forward traversal:")
    current = node1
    while current:
        print(f"  {current}")
        current = current.next
    
    print("Backward traversal:")
    current = node3
    while current:
        print(f"  {current}")
        current = current.prev


if __name__ == "__main__":
    demo_doubly_node()
