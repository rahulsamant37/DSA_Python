"""
Tree Breadth First Search Pattern - Level Order Traversal
=========================================================

Traverse tree level by level using queue (BFS).

Time Complexity: O(n)
Space Complexity: O(w) where w is maximum width of tree
"""

from collections import deque


class TreeNode:
    """Simple binary tree node"""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(root):
    """
    Traverse binary tree level by level.
    
    Args:
        root: Root of the binary tree
        
    Returns:
        List of lists, each containing values at that level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.popleft()
            current_level.append(node.val)
            
            # Add children to queue for next level
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        
        result.append(current_level)
    
    return result


def example_usage():
    """Demonstrate level order traversal"""
    # Create tree:     3
    #                 / \
    #                9   20
    #                   /  \
    #                  15   7
    
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = level_order_traversal(root)
    print("Level order traversal:", result)
    # Output: [[3], [9, 20], [15, 7]]


if __name__ == "__main__":
    example_usage()
