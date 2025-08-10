"""
002 - Recursive Tree Traversals
===============================

Depth-first tree traversals using recursive approach.

Time Complexity: O(n) for all traversals
Space Complexity: O(h) where h is height of tree

Three types: Inorder, Preorder, Postorder
"""

from tree_node_001 import TreeNode, create_sample_tree


def inorder_recursive(node, result=None):
    """In-order traversal: Left -> Root -> Right"""
    if result is None:
        result = []
    
    if node:
        inorder_recursive(node.left, result)
        result.append(node.data)
        inorder_recursive(node.right, result)
    
    return result


def preorder_recursive(node, result=None):
    """Pre-order traversal: Root -> Left -> Right"""
    if result is None:
        result = []
    
    if node:
        result.append(node.data)
        preorder_recursive(node.left, result)
        preorder_recursive(node.right, result)
    
    return result


def postorder_recursive(node, result=None):
    """Post-order traversal: Left -> Right -> Root"""
    if result is None:
        result = []
    
    if node:
        postorder_recursive(node.left, result)
        postorder_recursive(node.right, result)
        result.append(node.data)
    
    return result


def demonstrate_traversal_meanings():
    """Explain what each traversal type represents"""
    explanations = """
TRAVERSAL MEANINGS:
==================

1. INORDER (Left -> Root -> Right):
   - For BST: gives sorted order
   - Use cases: Expression evaluation, BST sorting
   - Example: For expression tree (a+b)*c -> a+b*c (infix)

2. PREORDER (Root -> Left -> Right):
   - Used to create copy of tree
   - Use cases: Prefix expression, tree serialization
   - Example: For expression tree (a+b)*c -> *+abc (prefix)

3. POSTORDER (Left -> Right -> Root):
   - Used to delete tree safely
   - Use cases: Postfix expression, calculating tree size
   - Example: For expression tree (a+b)*c -> ab+c* (postfix)
    """
    print(explanations)


def demo_recursive_traversals():
    """Demonstrate recursive tree traversals"""
    print("=== Recursive Tree Traversals Demo ===")
    
    # Create sample tree
    root = create_sample_tree()
    
    print("Sample tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print()
    
    # Perform traversals
    print("Traversal Results:")
    print(f"Inorder   (L-Root-R): {inorder_recursive(root)}")
    print(f"Preorder  (Root-L-R): {preorder_recursive(root)}")
    print(f"Postorder (L-R-Root): {postorder_recursive(root)}")
    
    print()
    demonstrate_traversal_meanings()


if __name__ == "__main__":
    demo_recursive_traversals()
