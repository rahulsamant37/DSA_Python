"""
001 - List Node Definition
==========================

Basic node class for singly linked list.

Time Complexity:
- Initialization: O(1)
"""

class ListNode:
    """Node class for singly linked list"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)


def demo_list_node():
    """Demonstrate ListNode functionality"""
    print("=== List Node Demo ===")
    
    # Create nodes
    node1 = ListNode(10)
    node2 = ListNode(20)
    node3 = ListNode(30)
    
    # Link nodes
    node1.next = node2
    node2.next = node3
    
    print("Linked nodes:")
    current = node1
    while current:
        print(f"  {current}")
        current = current.next


if __name__ == "__main__":
    demo_list_node()
