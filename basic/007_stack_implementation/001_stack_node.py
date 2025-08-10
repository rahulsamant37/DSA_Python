"""
001 - Stack Node Definition
===========================

Basic node class for linked list-based stack implementation.

Time Complexity:
- Initialization: O(1)
"""

class StackNode:
    """Node class for linked list stack"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


def demo_stack_node():
    """Demonstrate StackNode functionality"""
    print("=== Stack Node Demo ===")
    
    # Create nodes
    node1 = StackNode(10)
    node2 = StackNode(20)
    node3 = StackNode(30)
    
    # Link nodes
    node3.next = node2
    node2.next = node1
    
    print("Linked nodes (top to bottom):")
    current = node3
    while current:
        print(f"  {current}")
        current = current.next


if __name__ == "__main__":
    demo_stack_node()
