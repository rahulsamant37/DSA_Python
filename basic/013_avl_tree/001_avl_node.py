"""
001 - AVL Tree Node Definition
=============================

AVL tree node with height and balance factor tracking.

Time Complexity:
- Initialization: O(1)
- Height calculation: O(1)
- Balance factor calculation: O(1)

AVL Property: Balance factor ∈ {-1, 0, 1}
"""

class AVLNode:
    """Node class for AVL Tree with height tracking"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height of the node (leaf = 1)
    
    def __str__(self):
        return str(self.data)


def get_height(node):
    """Get height of node (0 for None)"""
    if node is None:
        return 0
    return node.height


def get_balance_factor(node):
    """Get balance factor of node"""
    if node is None:
        return 0
    return get_height(node.left) - get_height(node.right)


def update_height(node):
    """Update height of node based on children"""
    if node is not None:
        node.height = 1 + max(get_height(node.left), get_height(node.right))


def demo_avl_node():
    """Demonstrate AVL node functionality"""
    print("=== AVL Node Demo ===")
    
    # Create nodes
    root = AVLNode(10)
    left_child = AVLNode(5)
    right_child = AVLNode(15)
    
    # Build small tree
    root.left = left_child
    root.right = right_child
    
    # Update heights
    update_height(left_child)
    update_height(right_child)
    update_height(root)
    
    print(f"Root: {root} (height: {root.height})")
    print(f"Left child: {root.left} (height: {root.left.height})")
    print(f"Right child: {root.right} (height: {root.right.height})")
    
    # Check balance factors
    print(f"\nBalance factors:")
    print(f"Root balance factor: {get_balance_factor(root)}")
    print(f"Left child balance factor: {get_balance_factor(root.left)}")
    print(f"Right child balance factor: {get_balance_factor(root.right)}")
    
    print(f"\nAVL Property check:")
    print(f"All balance factors in [-1, 0, 1]? {all(abs(get_balance_factor(node)) <= 1 for node in [root, left_child, right_child])}")


if __name__ == "__main__":
    demo_avl_node()
