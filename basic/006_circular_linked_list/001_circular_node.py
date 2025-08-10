"""
001 - Circular List Node Definition
===================================

Basic node class for circular linked list implementations.

Time Complexity:
- Initialization: O(1)
"""

class CircularSinglyListNode:
    """Node class for circular singly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


class CircularDoublyListNode:
    """Node class for circular doubly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)


def demo_circular_nodes():
    """Demonstrate circular node functionality"""
    print("=== Circular Node Demo ===")
    
    # Create singly circular nodes
    node1 = CircularSinglyListNode(10)
    node2 = CircularSinglyListNode(20)
    node3 = CircularSinglyListNode(30)
    
    # Create circular connection
    node1.next = node2
    node2.next = node3
    node3.next = node1  # Back to first node
    
    print("Circular Singly Linked Nodes:")
    current = node1
    count = 0
    while count < 6:  # Show circular nature
        print(f"  {current}")
        current = current.next
        count += 1
    
    print("\nCircular Doubly Linked Node created:")
    dbl_node = CircularDoublyListNode(100)
    print(f"  Node data: {dbl_node}")


if __name__ == "__main__":
    demo_circular_nodes()
