"""
003 - Binary Tree Insertion Operations
======================================

Insert elements into binary tree using level-order insertion.

Time Complexity:
- Level-order insertion: O(n)
"""

from collections import deque
from tree_node_001 import TreeNode
from binary_tree_class_002 import BinaryTree


def insert_level_order(bt, data):
    """Insert element using level-order (breadth-first) approach"""
    new_node = TreeNode(data)
    
    if bt.is_empty():
        bt.root = new_node
        return
    
    # Use queue for level-order traversal
    queue = deque([bt.root])
    
    while queue:
        current = queue.popleft()
        
        # Check left child
        if current.left is None:
            current.left = new_node
            return
        else:
            queue.append(current.left)
        
        # Check right child
        if current.right is None:
            current.right = new_node
            return
        else:
            queue.append(current.right)


def display_level_order(bt):
    """Display tree in level-order"""
    if bt.is_empty():
        print("Tree is empty")
        return
    
    queue = deque([bt.root])
    print("Level-order traversal:", end=" ")
    
    while queue:
        current = queue.popleft()
        print(current.data, end=" ")
        
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
    print()


def demo_insertion_operations():
    """Demonstrate binary tree insertion operations"""
    print("=== Binary Tree Insertion Operations Demo ===")
    
    # Create tree
    bt = BinaryTree()
    
    # Insert elements
    print("\nInserting elements: 1, 2, 3, 4, 5, 6, 7")
    for i in range(1, 8):
        insert_level_order(bt, i)
    
    display_level_order(bt)


if __name__ == "__main__":
    demo_insertion_operations()
