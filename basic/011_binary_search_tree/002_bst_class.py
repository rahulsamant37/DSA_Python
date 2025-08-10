"""
002 - Binary Search Tree Class
==============================

Basic Binary Search Tree class with initialization.

Time Complexity:
- Initialization: O(1)
- is_empty: O(1)

BST property: For any node, left subtree < node < right subtree
"""

from bst_node_001 import BSTNode


class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self, root_data=None):
        if root_data is not None:
            self.root = BSTNode(root_data)
        else:
            self.root = None
    
    def is_empty(self):
        """Check if the BST is empty"""
        return self.root is None
    
    def inorder_traversal(self, node=None, result=None):
        """Inorder traversal (left-root-right) for sorted output"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node is not None:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        
        return result


def demo_binary_search_tree():
    """Demonstrate BinarySearchTree basic functionality"""
    print("=== Binary Search Tree Class Demo ===")
    
    # Create empty BST
    bst1 = BinarySearchTree()
    print(f"Empty BST - Is empty: {bst1.is_empty()}")
    
    # Create BST with root
    bst2 = BinarySearchTree(50)
    print(f"BST with root 50 - Is empty: {bst2.is_empty()}")
    print(f"Root data: {bst2.root.data}")
    
    # Manually create a small BST for demonstration
    bst2.root.left = BSTNode(30)
    bst2.root.right = BSTNode(70)
    bst2.root.left.left = BSTNode(20)
    bst2.root.left.right = BSTNode(40)
    
    print(f"Inorder traversal (sorted): {bst2.inorder_traversal()}")


if __name__ == "__main__":
    demo_binary_search_tree()
