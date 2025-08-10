"""
001 - BST Node Definition
=========================

Basic node class for Binary Search Tree.

Time Complexity:
- Initialization: O(1)
"""

class BSTNode:
    """Node class for Binary Search Tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


def demo_bst_node():
    """Demonstrate BSTNode functionality"""
    print("=== BST Node Demo ===")
    
    # Create nodes
    root = BSTNode(50)
    left_child = BSTNode(30)
    right_child = BSTNode(70)
    
    # Link nodes following BST property
    root.left = left_child
    root.right = right_child
    
    print(f"Root: {root}")
    print(f"Left child: {root.left}")
    print(f"Right child: {root.right}")
    print(f"BST property: {root.left.data} < {root.data} < {root.right.data}")


if __name__ == "__main__":
    demo_bst_node()
