"""
001 - Tree Node Definition
==========================

Basic node class for binary tree.

Time Complexity:
- Initialization: O(1)
"""

class TreeNode:
    """Node class for binary tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


def demo_tree_node():
    """Demonstrate TreeNode functionality"""
    print("=== Tree Node Demo ===")
    
    # Create nodes
    root = TreeNode(10)
    left_child = TreeNode(5)
    right_child = TreeNode(15)
    
    # Link nodes
    root.left = left_child
    root.right = right_child
    
    print(f"Root: {root}")
    print(f"Left child: {root.left}")
    print(f"Right child: {root.right}")


if __name__ == "__main__":
    demo_tree_node()
