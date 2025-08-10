"""
003 - Iterative Tree Traversals
===============================

Depth-first tree traversals using iterative approach with stack.

Time Complexity: O(n) for all traversals
Space Complexity: O(h) where h is height of tree

Iterative versions avoid recursion stack overflow for deep trees.
"""

from tree_node_001 import TreeNode, create_sample_tree


def inorder_iterative(root):
    """In-order traversal using stack (iterative)"""
    result = []
    stack = []
    current = root
    
    while stack or current:
        # Go to leftmost node
        while current:
            stack.append(current)
            current = current.left
        
        # Current is None, so pop from stack
        current = stack.pop()
        result.append(current.data)
        
        # Visit right subtree
        current = current.right
    
    return result


def preorder_iterative(root):
    """Pre-order traversal using stack (iterative)"""
    if not root:
        return []
    
    result = []
    stack = [root]
    
    while stack:
        node = stack.pop()
        result.append(node.data)
        
        # Push right first, then left (stack is LIFO)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    
    return result


def postorder_iterative(root):
    """Post-order traversal using two stacks (iterative)"""
    if not root:
        return []
    
    result = []
    stack1 = [root]
    stack2 = []
    
    # Use two stacks approach
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        if node.left:
            stack1.append(node.left)
        if node.right:
            stack1.append(node.right)
    
    # Pop from second stack to get postorder
    while stack2:
        result.append(stack2.pop().data)
    
    return result


def postorder_iterative_single_stack(root):
    """Post-order traversal using single stack (more complex)"""
    if not root:
        return []
    
    result = []
    stack = []
    last_visited = None
    current = root
    
    while stack or current:
        if current:
            stack.append(current)
            current = current.left
        else:
            peek_node = stack[-1]
            
            # If right child exists and hasn't been processed yet
            if peek_node.right and last_visited != peek_node.right:
                current = peek_node.right
            else:
                result.append(peek_node.data)
                last_visited = stack.pop()
    
    return result


def demo_iterative_traversals():
    """Demonstrate iterative tree traversals"""
    print("=== Iterative Tree Traversals Demo ===")
    
    # Create sample tree
    root = create_sample_tree()
    
    print("Sample tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print()
    
    # Perform iterative traversals
    print("Iterative Traversal Results:")
    print(f"Inorder   (iterative): {inorder_iterative(root)}")
    print(f"Preorder  (iterative): {preorder_iterative(root)}")
    print(f"Postorder (two stack): {postorder_iterative(root)}")
    print(f"Postorder (one stack): {postorder_iterative_single_stack(root)}")
    
    print()
    print("Advantages of Iterative Traversals:")
    print("- Avoids recursion stack overflow for very deep trees")
    print("- More memory efficient for some cases")
    print("- Can be paused and resumed easily")
    print("- Better for very large trees")


if __name__ == "__main__":
    demo_iterative_traversals()
