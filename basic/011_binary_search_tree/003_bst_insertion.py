"""
003 - BST Insertion Operations
==============================

Insert elements into Binary Search Tree maintaining BST property.

Time Complexity:
- Insert: O(log n) average, O(n) worst case
- Height of tree determines performance
"""

from bst_node_001 import BSTNode
from bst_class_002 import BinarySearchTree


def insert(bst, data):
    """Insert data into BST"""
    if bst.is_empty():
        bst.root = BSTNode(data)
        return
    
    _insert_recursive(bst.root, data)


def _insert_recursive(node, data):
    """Helper function for recursive insertion"""
    if data < node.data:
        if node.left is None:
            node.left = BSTNode(data)
        else:
            _insert_recursive(node.left, data)
    elif data > node.data:
        if node.right is None:
            node.right = BSTNode(data)
        else:
            _insert_recursive(node.right, data)
    # If data == node.data, do nothing (no duplicates)


def insert_iterative(bst, data):
    """Insert data into BST iteratively"""
    if bst.is_empty():
        bst.root = BSTNode(data)
        return
    
    current = bst.root
    while True:
        if data < current.data:
            if current.left is None:
                current.left = BSTNode(data)
                break
            else:
                current = current.left
        elif data > current.data:
            if current.right is None:
                current.right = BSTNode(data)
                break
            else:
                current = current.right
        else:
            # Duplicate value, do nothing
            break


def demo_bst_insertion():
    """Demonstrate BST insertion operations"""
    print("=== BST Insertion Operations Demo ===")
    
    # Create BST
    bst = BinarySearchTree()
    
    # Insert elements
    values = [50, 30, 70, 20, 40, 60, 80]
    print(f"Inserting values: {values}")
    
    for value in values:
        insert(bst, value)
    
    print(f"Inorder traversal (sorted): {bst.inorder_traversal()}")
    
    # Test iterative insertion
    bst2 = BinarySearchTree()
    print(f"\nTesting iterative insertion:")
    
    for value in [25, 15, 35, 10, 20, 30, 40]:
        insert_iterative(bst2, value)
    
    print(f"Inorder traversal: {bst2.inorder_traversal()}")
    
    # Test duplicate insertion
    print(f"\nInserting duplicate value 25:")
    insert(bst2, 25)
    print(f"Inorder traversal (no change): {bst2.inorder_traversal()}")


if __name__ == "__main__":
    demo_bst_insertion()
