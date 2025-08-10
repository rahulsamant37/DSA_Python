"""
004 - Level Order Traversal
===========================

Breadth-first tree traversal using queue.

Time Complexity: O(n)
Space Complexity: O(w) where w is maximum width of tree

Also known as breadth-first search (BFS) for trees.
"""

from collections import deque
from tree_node_001 import TreeNode, create_sample_tree


def level_order_traversal(root):
    """Level-order traversal using queue"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        node = queue.popleft()
        result.append(node.data)
        
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    
    return result


def level_order_with_levels(root):
    """Level-order traversal showing each level separately"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def zigzag_level_order(root):
    """Zigzag level-order traversal (alternate left-to-right and right-to-left)"""
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            node = queue.popleft()
            
            if left_to_right:
                current_level.append(node.data)
            else:
                current_level.insert(0, node.data)
            
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
        left_to_right = not left_to_right
    
    return result


def vertical_order_traversal(root):
    """Vertical order traversal using horizontal distance"""
    if not root:
        return []
    
    # Dictionary to store nodes at each horizontal distance
    node_map = {}
    queue = deque([(root, 0)])  # (node, horizontal_distance)
    
    while queue:
        node, hd = queue.popleft()
        
        if hd not in node_map:
            node_map[hd] = []
        node_map[hd].append(node.data)
        
        if node.left:
            queue.append((node.left, hd - 1))
        if node.right:
            queue.append((node.right, hd + 1))
    
    # Sort by horizontal distance and return values
    result = []
    for hd in sorted(node_map.keys()):
        result.extend(node_map[hd])
    
    return result


def demo_level_order_traversals():
    """Demonstrate level-order and related traversals"""
    print("=== Level Order Traversals Demo ===")
    
    # Create sample tree
    root = create_sample_tree()
    
    print("Sample tree:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print()
    
    # Perform level-order traversals
    print("Level-order traversal:", level_order_traversal(root))
    print()
    
    print("Level-order with levels:")
    levels = level_order_with_levels(root)
    for i, level in enumerate(levels):
        print(f"  Level {i}: {level}")
    print()
    
    print("Zigzag level-order:")
    zigzag = zigzag_level_order(root)
    for i, level in enumerate(zigzag):
        direction = "L->R" if i % 2 == 0 else "R->L"
        print(f"  Level {i} ({direction}): {level}")
    print()
    
    print("Vertical order traversal:", vertical_order_traversal(root))
    
    print()
    print("Use Cases:")
    print("- Level-order: Tree serialization, finding tree width")
    print("- Zigzag: Binary tree zigzag printing")
    print("- Vertical: Vertical view of binary tree")


if __name__ == "__main__":
    demo_level_order_traversals()
