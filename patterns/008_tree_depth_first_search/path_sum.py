"""
Tree Depth First Search Pattern - Path Sum
===========================================

Find if there exists a root-to-leaf path with given sum.

Time Complexity: O(n)
Space Complexity: O(h) where h is height of tree
"""


class TreeNode:
    """Simple binary tree node"""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def has_path_sum(root, target_sum):
    """
    Check if there exists a root-to-leaf path with given sum.
    
    Args:
        root: Root of the binary tree
        target_sum: Target sum to find
        
    Returns:
        True if path exists, False otherwise
    """
    if not root:
        return False
    
    # If leaf node, check if remaining sum equals node value
    if not root.left and not root.right:
        return target_sum == root.val
    
    # Recursively check left and right subtrees
    remaining_sum = target_sum - root.val
    return (has_path_sum(root.left, remaining_sum) or 
            has_path_sum(root.right, remaining_sum))


def example_usage():
    """Demonstrate path sum checking"""
    # Create tree:     5
    #                 / \
    #                4   8
    #               /   / \
    #              11  13  4
    #             / \      \
    #            7   2      1
    
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    root.right.left = TreeNode(13)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    
    target = 22  # Path: 5 -> 4 -> 11 -> 2 = 22
    result = has_path_sum(root, target)
    print(f"Has path with sum {target}: {result}")
    
    target = 100
    result = has_path_sum(root, target)
    print(f"Has path with sum {target}: {result}")


if __name__ == "__main__":
    example_usage()
