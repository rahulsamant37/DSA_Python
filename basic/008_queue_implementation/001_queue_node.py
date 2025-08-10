"""
001 - Queue Node Definition
===========================

Basic node class for linked list-based queue implementation.

Time Complexity:
- Initialization: O(1)
"""

class QueueNode:
    """Node class for linked list queue"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


def demo_queue_node():
    """Demonstrate QueueNode functionality"""
    print("=== Queue Node Demo ===")
    
    # Create nodes
    node1 = QueueNode(10)
    node2 = QueueNode(20)
    node3 = QueueNode(30)
    
    # Link nodes (first to last)
    node1.next = node2
    node2.next = node3
    
    print("Linked nodes (front to rear):")
    current = node1
    while current:
        print(f"  {current}")
        current = current.next


if __name__ == "__main__":
    demo_queue_node()
