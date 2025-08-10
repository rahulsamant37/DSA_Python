"""
001 - Hash Table Node Definition
===============================

Basic node class for hash table implementations using chaining.

Time Complexity:
- Initialization: O(1)
"""

class HashNode:
    """Node for separate chaining in hash table"""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
    
    def __str__(self):
        return f"({self.key}: {self.value})"


def demo_hash_node():
    """Demonstrate HashNode functionality"""
    print("=== Hash Node Demo ===")
    
    # Create nodes
    node1 = HashNode("apple", 100)
    node2 = HashNode("banana", 200)
    node3 = HashNode("cherry", 300)
    
    # Link nodes for chaining
    node1.next = node2
    node2.next = node3
    
    print("Hash nodes in chain:")
    current = node1
    while current:
        print(f"  {current}")
        current = current.next


if __name__ == "__main__":
    demo_hash_node()
