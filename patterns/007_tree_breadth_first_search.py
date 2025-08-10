"""
Tree Breadth First Search (BFS) Pattern

This pattern is based on the Breadth First Search (BFS) technique to traverse 
a tree and uses a queue to keep track of all the nodes of a level before jumping 
onto the next level. Any problem involving the traversal of a tree in a level-by-level 
order can be efficiently solved using this approach.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(w) where w is the maximum width of the tree

Common Problems:
- Binary Tree Level Order Traversal
- Reverse Level Order Traversal
- Zigzag Traversal
- Level Averages in a Binary Tree
- Minimum Depth of a Binary Tree
- Level Order Successor
- Connect Level Order Siblings
"""

from collections import deque


class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def level_order_traversal(root):
    """
    Traverse the tree level by level.
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of lists containing nodes at each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            
            # Add child nodes to the queue for the next level
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(current_level)
    
    return result


def reverse_level_order_traversal(root):
    """
    Traverse the tree in reverse level order (bottom-up).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of lists containing nodes at each level (bottom-up)
    """
    if not root:
        return []
    
    result = deque()
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        for _ in range(level_size):
            current_node = queue.popleft()
            current_level.append(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.appendleft(current_level)  # Add to the beginning
    
    return list(result)


def zigzag_level_order(root):
    """
    Traverse the tree in zigzag pattern (alternating left-to-right and right-to-left).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of lists containing nodes at each level in zigzag order
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = deque()
        
        for _ in range(level_size):
            current_node = queue.popleft()
            
            # Add to front or back of level based on direction
            if left_to_right:
                current_level.append(current_node.val)
            else:
                current_level.appendleft(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(list(current_level))
        left_to_right = not left_to_right  # Flip direction
    
    return result


def find_level_averages(root):
    """
    Find the average value of the nodes on each level.
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of average values for each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        level_sum = 0
        
        for _ in range(level_size):
            current_node = queue.popleft()
            level_sum += current_node.val
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
        
        result.append(level_sum / level_size)
    
    return result


def find_minimum_depth(root):
    """
    Find the minimum depth of a binary tree.
    
    Args:
        root: root of the binary tree
    
    Returns:
        minimum depth of the tree
    """
    if not root:
        return 0
    
    queue = deque([root])
    minimum_tree_depth = 0
    
    while queue:
        minimum_tree_depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            current_node = queue.popleft()
            
            # Check if this is a leaf node
            if not current_node.left and not current_node.right:
                return minimum_tree_depth
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return minimum_tree_depth


def find_maximum_depth(root):
    """
    Find the maximum depth of a binary tree.
    
    Args:
        root: root of the binary tree
    
    Returns:
        maximum depth of the tree
    """
    if not root:
        return 0
    
    queue = deque([root])
    maximum_tree_depth = 0
    
    while queue:
        maximum_tree_depth += 1
        level_size = len(queue)
        
        for _ in range(level_size):
            current_node = queue.popleft()
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return maximum_tree_depth


def find_level_order_successor(root, key):
    """
    Find the level order successor of a given node.
    
    Args:
        root: root of the binary tree
        key: value of the node whose successor to find
    
    Returns:
        successor node value, None if not found
    """
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        current_node = queue.popleft()
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
        
        # If we found the key, return the next node
        if current_node.val == key:
            break
    
    return queue[0].val if queue else None


class TreeNodeWithNext:
    """Tree node with next pointer for connecting level order siblings."""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None
        self.next = None


def connect_level_order_siblings(root):
    """
    Connect each node to its next right node (level order sibling).
    
    Args:
        root: root of the binary tree with next pointers
    
    Returns:
        root of the modified tree
    """
    if not root:
        return None
    
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            current_node = queue.popleft()
            
            # Connect to next node in the same level
            if i < level_size - 1:
                current_node.next = queue[0]
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return root


def connect_all_level_order_siblings(root):
    """
    Connect each node to its next node (across all levels).
    
    Args:
        root: root of the binary tree with next pointers
    
    Returns:
        root of the modified tree
    """
    if not root:
        return None
    
    queue = deque([root])
    current_node = None
    prev_node = None
    
    while queue:
        current_node = queue.popleft()
        
        if prev_node:
            prev_node.next = current_node
        
        prev_node = current_node
        
        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
    
    return root


def tree_right_view(root):
    """
    Find the right view of a binary tree (rightmost node at each level).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of rightmost nodes at each level
    """
    if not root:
        return []
    
    result = []
    queue = deque([root])
    
    while queue:
        level_size = len(queue)
        
        for i in range(level_size):
            current_node = queue.popleft()
            
            # If this is the last node of the current level, add it to result
            if i == level_size - 1:
                result.append(current_node.val)
            
            if current_node.left:
                queue.append(current_node.left)
            if current_node.right:
                queue.append(current_node.right)
    
    return result


def tree_boundary_traversal(root):
    """
    Find the boundary traversal of a binary tree.
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of boundary nodes (anticlockwise)
    """
    if not root:
        return []
    
    result = [root.val]
    
    # Get left boundary (excluding leaves)
    def get_left_boundary(node):
        boundary = []
        while node:
            if node.left or node.right:  # Not a leaf
                boundary.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
        return boundary
    
    # Get leaf nodes
    def get_leaves(node):
        if not node:
            return []
        if not node.left and not node.right:
            return [node.val]
        return get_leaves(node.left) + get_leaves(node.right)
    
    # Get right boundary (excluding leaves)
    def get_right_boundary(node):
        boundary = []
        while node:
            if node.left or node.right:  # Not a leaf
                boundary.append(node.val)
            if node.right:
                node = node.right
            else:
                node = node.left
        return boundary[::-1]  # Reverse for anticlockwise order
    
    if root.left:
        result.extend(get_left_boundary(root.left))
    
    # Add leaves (excluding root if it's a leaf)
    if root.left or root.right:
        result.extend(get_leaves(root))
    
    if root.right:
        result.extend(get_right_boundary(root.right))
    
    return result


# Helper functions for creating test trees
def create_binary_tree():
    """Create a sample binary tree for testing."""
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    return root


def print_tree_with_next(root):
    """Print tree with next pointers."""
    result = []
    current = root
    
    while current:
        level = []
        level_start = current
        
        while current:
            level.append(current.val)
            current = current.next
        
        result.append(level)
        
        # Move to next level
        current = level_start
        while current and not current.left and not current.right:
            current = current.next
        
        if current:
            current = current.left if current.left else current.right
    
    return result


# Example usage and test cases
if __name__ == "__main__":
    # Create test tree
    root = create_binary_tree()
    
    # Test level_order_traversal
    print("=== Level Order Traversal ===")
    result = level_order_traversal(root)
    print(f"Level order: {result}")  # [[12], [7, 1], [9, 2, 10, 5]]
    
    # Test reverse_level_order_traversal
    print("\n=== Reverse Level Order Traversal ===")
    result = reverse_level_order_traversal(root)
    print(f"Reverse level order: {result}")  # [[9, 2, 10, 5], [7, 1], [12]]
    
    # Test zigzag_level_order
    print("\n=== Zigzag Level Order ===")
    result = zigzag_level_order(root)
    print(f"Zigzag order: {result}")  # [[12], [1, 7], [9, 2, 10, 5]]
    
    # Test find_level_averages
    print("\n=== Level Averages ===")
    result = find_level_averages(root)
    print(f"Level averages: {result}")  # [12.0, 4.0, 6.5]
    
    # Test find_minimum_depth
    print("\n=== Minimum Depth ===")
    result = find_minimum_depth(root)
    print(f"Minimum depth: {result}")  # 3
    
    # Test find_maximum_depth
    print("\n=== Maximum Depth ===")
    result = find_maximum_depth(root)
    print(f"Maximum depth: {result}")  # 3
    
    # Test find_level_order_successor
    print("\n=== Level Order Successor ===")
    result = find_level_order_successor(root, 9)
    print(f"Successor of 9: {result}")  # 2
    
    # Test tree_right_view
    print("\n=== Tree Right View ===")
    result = tree_right_view(root)
    print(f"Right view: {result}")  # [12, 1, 5]
