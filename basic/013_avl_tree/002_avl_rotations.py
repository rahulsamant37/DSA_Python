"""
002 - AVL Tree Rotation Operations
==================================

Four types of rotations to maintain AVL tree balance.

Time Complexity: O(1) for each rotation
Space Complexity: O(1)

Rotation Types:
- Right Rotation (for Left-Left case)
- Left Rotation (for Right-Right case)
- Left-Right Rotation (for Left-Right case)
- Right-Left Rotation (for Right-Left case)
"""

from avl_node_001 import AVLNode, get_height, update_height


def right_rotate(y):
    """
    Right rotation (used for Left-Left case)
    
    Before:     After:
        y          x
       / \\        / \\
      x   T3      T1  y
     / \\            / \\
    T1  T2          T2  T3
    """
    x = y.left
    T2 = x.right
    
    # Perform rotation
    x.right = y
    y.left = T2
    
    # Update heights
    update_height(y)
    update_height(x)
    
    # Return new root
    return x


def left_rotate(x):
    """
    Left rotation (used for Right-Right case)
    
    Before:     After:
       x           y
      / \\        / \\
     T1  y       x   T3
        / \\    / \\
       T2  T3  T1  T2
    """
    y = x.right
    T2 = y.left
    
    # Perform rotation
    y.left = x
    x.right = T2
    
    # Update heights
    update_height(x)
    update_height(y)
    
    # Return new root
    return y


def left_right_rotate(node):
    """
    Left-Right rotation (used for Left-Right case)
    
    First left rotate on left child, then right rotate on node
    """
    node.left = left_rotate(node.left)
    return right_rotate(node)


def right_left_rotate(node):
    """
    Right-Left rotation (used for Right-Left case)
    
    First right rotate on right child, then left rotate on node
    """
    node.right = right_rotate(node.right)
    return left_rotate(node)


def demo_rotations():
    """Demonstrate AVL tree rotations"""
    print("=== AVL Tree Rotations Demo ===")
    
    # Create an unbalanced tree for demonstration
    # Right-Right case: 1 -> 2 -> 3 (left rotation needed)
    print("Right-Right Case (needs left rotation):")
    print("Before: 1 -> 2 -> 3 (linear)")
    
    root = AVLNode(1)
    root.right = AVLNode(2)
    root.right.right = AVLNode(3)
    
    # Update heights
    update_height(root.right.right)
    update_height(root.right)
    update_height(root)
    
    print(f"Root: {root.data}, Right: {root.right.data}, Right-Right: {root.right.right.data}")
    
    # Perform left rotation
    new_root = left_rotate(root)
    print(f"After left rotation:")
    print(f"New root: {new_root.data}")
    print(f"Left child: {new_root.left.data}")
    print(f"Right child: {new_root.right.data}")
    
    print("\n" + "="*50)
    
    # Left-Left case: 3 -> 2 -> 1 (right rotation needed)
    print("Left-Left Case (needs right rotation):")
    print("Before: 3 -> 2 -> 1 (linear)")
    
    root2 = AVLNode(3)
    root2.left = AVLNode(2)
    root2.left.left = AVLNode(1)
    
    # Update heights
    update_height(root2.left.left)
    update_height(root2.left)
    update_height(root2)
    
    print(f"Root: {root2.data}, Left: {root2.left.data}, Left-Left: {root2.left.left.data}")
    
    # Perform right rotation
    new_root2 = right_rotate(root2)
    print(f"After right rotation:")
    print(f"New root: {new_root2.data}")
    print(f"Left child: {new_root2.left.data}")
    print(f"Right child: {new_root2.right.data}")
    
    print("\nRotation Rules:")
    print("- Left-Left case: Right rotation")
    print("- Right-Right case: Left rotation")
    print("- Left-Right case: Left rotation on left child, then right rotation")
    print("- Right-Left case: Right rotation on right child, then left rotation")


if __name__ == "__main__":
    demo_rotations()
