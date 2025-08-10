"""
001 - Deque Node Definition
===========================

Basic node class for linked list-based deque implementation.

Time Complexity:
- Initialization: O(1)
"""

class DequeNode:
    """Node class for linked list deque"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None
    
    def __str__(self):
        return str(self.data)


def demo_deque_node():
    """Demonstrate DequeNode functionality"""
    print("=== Deque Node Demo ===")
    
    # Create nodes
    node1 = DequeNode(10)
    node2 = DequeNode(20)
    node3 = DequeNode(30)
    
    # Link nodes bidirectionally for deque
    node1.next = node2
    node2.prev = node1
    node2.next = node3
    node3.prev = node2
    
    print("Forward traversal (front to rear):")
    current = node1
    while current:
        print(f"  {current}")
        current = current.next
    
    print("Backward traversal (rear to front):")
    current = node3
    while current:
        print(f"  {current}")
        current = current.prev


if __name__ == "__main__":
    demo_deque_node()
