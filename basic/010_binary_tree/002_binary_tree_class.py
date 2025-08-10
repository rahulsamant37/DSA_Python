"""
002 - Binary Tree Class
=======================

Basic binary tree class with initialization.

Time Complexity:
- Initialization: O(1)
- is_empty: O(1)
"""

from tree_node_001 import TreeNode


class BinaryTree:
    """Binary Tree implementation"""
    
    def __init__(self, root_data=None):
        if root_data is not None:
            self.root = TreeNode(root_data)
        else:
            self.root = None
    
    def is_empty(self):
        """Check if the tree is empty"""
        return self.root is None


def demo_binary_tree():
    """Demonstrate BinaryTree basic functionality"""
    print("=== Binary Tree Class Demo ===")
    
    # Create empty tree
    bt1 = BinaryTree()
    print(f"Empty tree - Is empty: {bt1.is_empty()}")
    
    # Create tree with root
    bt2 = BinaryTree(10)
    print(f"Tree with root 10 - Is empty: {bt2.is_empty()}")
    print(f"Root data: {bt2.root.data}")


if __name__ == "__main__":
    demo_binary_tree()
