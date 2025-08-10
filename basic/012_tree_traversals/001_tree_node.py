"""
001 - Tree Node for Traversals
==============================

Basic tree node class used for tree traversal demonstrations.

Time Complexity:
- Initialization: O(1)
"""

class TreeNode:
    """Node class for tree traversals"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


def create_sample_tree():
    """Create a sample binary tree for traversal demonstrations"""
    #       1
    #      / \\
    #     2   3
    #    / \\   \\
    #   4   5   6
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    
    return root


def print_tree_structure(root, level=0, prefix="Root: "):
    """Print tree structure visually"""
    if root is not None:
        print(" " * (level * 4) + prefix + str(root.data))
        if root.left is not None or root.right is not None:
            if root.left:
                print_tree_structure(root.left, level + 1, "L--- ")
            else:
                print(" " * ((level + 1) * 4) + "L--- None")
            if root.right:
                print_tree_structure(root.right, level + 1, "R--- ")
            else:
                print(" " * ((level + 1) * 4) + "R--- None")


def demo_tree_node():
    """Demonstrate tree node and sample tree creation"""
    print("=== Tree Node Demo ===")
    
    # Create sample tree
    root = create_sample_tree()
    
    print("Sample tree structure:")
    print_tree_structure(root)
    
    print(f"\nRoot node: {root}")
    print(f"Left child: {root.left}")
    print(f"Right child: {root.right}")


if __name__ == "__main__":
    demo_tree_node()
