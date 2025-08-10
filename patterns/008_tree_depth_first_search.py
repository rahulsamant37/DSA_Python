"""
Tree Depth First Search (DFS) Pattern

Tree DFS is based on the Depth First Search (DFS) technique to traverse a tree.
We can use recursion (or a stack for the iterative approach) to keep track of all 
the previous (parent) nodes while traversing. This also means that the space 
complexity of the algorithm will be O(H), where 'H' is the maximum height of the tree.

Time Complexity: O(n) where n is the number of nodes
Space Complexity: O(H) where H is the height of the tree

Common Problems:
- Binary Tree Path Sum
- All Paths for a Sum
- Sum of Path Numbers
- Path With Given Sequence
- Count Paths for a Sum
"""

class TreeNode:
    """Definition for a binary tree node."""
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None


def has_path_sum(root, target_sum):
    """
    Check if tree has a path from root to leaf with given sum.
    
    Args:
        root: root of the binary tree
        target_sum: target sum to find
    
    Returns:
        True if path exists, False otherwise
    """
    if not root:
        return False
    
    # If current node is a leaf and its value equals the target sum
    if not root.left and not root.right:
        return root.val == target_sum
    
    # Recursively check left and right subtrees with remaining sum
    return (has_path_sum(root.left, target_sum - root.val) or 
            has_path_sum(root.right, target_sum - root.val))


def find_all_paths(root, target_sum):
    """
    Find all root-to-leaf paths where each path's sum equals the target sum.
    
    Args:
        root: root of the binary tree
        target_sum: target sum to find
    
    Returns:
        list of all paths that sum to target
    """
    all_paths = []
    find_paths_recursive(root, target_sum, [], all_paths)
    return all_paths


def find_paths_recursive(current_node, target_sum, current_path, all_paths):
    """Helper function for find_all_paths."""
    if not current_node:
        return
    
    # Add current node to the path
    current_path.append(current_node.val)
    
    # If current node is a leaf and path sum equals target
    if (not current_node.left and not current_node.right and 
        target_sum == current_node.val):
        all_paths.append(list(current_path))  # Copy the current path
    else:
        # Recursively check left and right subtrees
        find_paths_recursive(current_node.left, target_sum - current_node.val, 
                           current_path, all_paths)
        find_paths_recursive(current_node.right, target_sum - current_node.val, 
                           current_path, all_paths)
    
    # Backtrack: remove current node from path before returning
    del current_path[-1]


def sum_of_path_numbers(root):
    """
    Find the total sum of all root-to-leaf numbers.
    
    Args:
        root: root of the binary tree
    
    Returns:
        sum of all root-to-leaf numbers
    """
    return find_root_to_leaf_path_numbers(root, 0)


def find_root_to_leaf_path_numbers(current_node, path_sum):
    """Helper function for sum_of_path_numbers."""
    if not current_node:
        return 0
    
    # Calculate the path number
    path_sum = path_sum * 10 + current_node.val
    
    # If current node is a leaf, return the path number
    if not current_node.left and not current_node.right:
        return path_sum
    
    # Traverse left and right sub-trees
    return (find_root_to_leaf_path_numbers(current_node.left, path_sum) +
            find_root_to_leaf_path_numbers(current_node.right, path_sum))


def find_path_with_sequence(root, sequence):
    """
    Check if tree contains a path with given sequence.
    
    Args:
        root: root of the binary tree
        sequence: list representing the path sequence
    
    Returns:
        True if path with sequence exists, False otherwise
    """
    if not root:
        return len(sequence) == 0
    
    return find_path_recursive(root, sequence, 0)


def find_path_recursive(current_node, sequence, sequence_index):
    """Helper function for find_path_with_sequence."""
    if not current_node:
        return False
    
    sequence_length = len(sequence)
    
    # Check if sequence index is valid and current node matches sequence
    if (sequence_index >= sequence_length or 
        current_node.val != sequence[sequence_index]):
        return False
    
    # If current node is a leaf, check if we've reached end of sequence
    if not current_node.left and not current_node.right:
        return sequence_index == sequence_length - 1
    
    # Recursively check left and right subtrees
    return (find_path_recursive(current_node.left, sequence, sequence_index + 1) or
            find_path_recursive(current_node.right, sequence, sequence_index + 1))


def count_paths_for_sum(root, target_sum):
    """
    Count all paths in tree that sum to target (not necessarily root-to-leaf).
    
    Args:
        root: root of the binary tree
        target_sum: target sum to find
    
    Returns:
        count of paths that sum to target
    """
    return count_paths_recursive(root, target_sum, [])


def count_paths_recursive(current_node, target_sum, current_path):
    """Helper function for count_paths_for_sum."""
    if not current_node:
        return 0
    
    # Add current node to the path
    current_path.append(current_node.val)
    path_count = 0
    path_sum = 0
    
    # Find sums of all sub-paths ending at current node
    for i in range(len(current_path) - 1, -1, -1):
        path_sum += current_path[i]
        
        # If path sum equals target, increment count
        if path_sum == target_sum:
            path_count += 1
    
    # Traverse left and right sub-trees
    path_count += count_paths_recursive(current_node.left, target_sum, current_path)
    path_count += count_paths_recursive(current_node.right, target_sum, current_path)
    
    # Backtrack: remove current node from path
    del current_path[-1]
    
    return path_count


def tree_diameter(root):
    """
    Find the diameter of a binary tree (longest path between any two nodes).
    
    Args:
        root: root of the binary tree
    
    Returns:
        diameter of the tree
    """
    tree_diameter.diameter = 0
    
    def calculate_height(node):
        if not node:
            return 0
        
        left_height = calculate_height(node.left)
        right_height = calculate_height(node.right)
        
        # Diameter at current node
        diameter = left_height + right_height + 1
        tree_diameter.diameter = max(tree_diameter.diameter, diameter)
        
        # Return height of current node
        return max(left_height, right_height) + 1
    
    calculate_height(root)
    return tree_diameter.diameter


def path_with_maximum_sum(root):
    """
    Find the path with maximum sum in a binary tree.
    
    Args:
        root: root of the binary tree
    
    Returns:
        maximum sum of any path in the tree
    """
    global_maximum_sum = float('-inf')
    
    def find_maximum_path_sum_recursive(current_node):
        nonlocal global_maximum_sum
        
        if not current_node:
            return 0
        
        max_path_sum_from_left = find_maximum_path_sum_recursive(current_node.left)
        max_path_sum_from_right = find_maximum_path_sum_recursive(current_node.right)
        
        # Ignore paths with negative sums
        max_path_sum_from_left = max(max_path_sum_from_left, 0)
        max_path_sum_from_right = max(max_path_sum_from_right, 0)
        
        # Maximum path sum at current node
        local_maximum_sum = (max_path_sum_from_left + max_path_sum_from_right + 
                           current_node.val)
        
        # Update global maximum
        global_maximum_sum = max(global_maximum_sum, local_maximum_sum)
        
        # Return maximum gain from current node
        return max(max_path_sum_from_left, max_path_sum_from_right) + current_node.val
    
    find_maximum_path_sum_recursive(root)
    return global_maximum_sum


def inorder_traversal(root):
    """
    Perform inorder traversal of binary tree (DFS).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of nodes in inorder sequence
    """
    result = []
    
    def inorder_recursive(node):
        if node:
            inorder_recursive(node.left)
            result.append(node.val)
            inorder_recursive(node.right)
    
    inorder_recursive(root)
    return result


def preorder_traversal(root):
    """
    Perform preorder traversal of binary tree (DFS).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of nodes in preorder sequence
    """
    result = []
    
    def preorder_recursive(node):
        if node:
            result.append(node.val)
            preorder_recursive(node.left)
            preorder_recursive(node.right)
    
    preorder_recursive(root)
    return result


def postorder_traversal(root):
    """
    Perform postorder traversal of binary tree (DFS).
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of nodes in postorder sequence
    """
    result = []
    
    def postorder_recursive(node):
        if node:
            postorder_recursive(node.left)
            postorder_recursive(node.right)
            result.append(node.val)
    
    postorder_recursive(root)
    return result


def binary_tree_paths(root):
    """
    Find all root-to-leaf paths in a binary tree.
    
    Args:
        root: root of the binary tree
    
    Returns:
        list of all root-to-leaf paths as strings
    """
    paths = []
    
    def find_paths(node, path):
        if not node:
            return
        
        # Add current node to path
        path.append(str(node.val))
        
        # If leaf node, add path to result
        if not node.left and not node.right:
            paths.append("->".join(path))
        else:
            # Continue search in subtrees
            find_paths(node.left, path)
            find_paths(node.right, path)
        
        # Backtrack
        path.pop()
    
    find_paths(root, [])
    return paths


# Helper functions for creating test trees
def create_binary_tree():
    """Create a sample binary tree for testing."""
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    return root


def create_path_sum_tree():
    """Create a tree for path sum testing."""
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)
    return root


# Example usage and test cases
if __name__ == "__main__":
    # Create test trees
    root = create_binary_tree()
    path_sum_root = create_path_sum_tree()
    
    # Test has_path_sum
    print("=== Has Path Sum ===")
    target = 23
    result = has_path_sum(root, target)
    print(f"Tree has path with sum {target}: {result}")  # True
    
    # Test find_all_paths
    print("\n=== Find All Paths ===")
    target = 23
    paths = find_all_paths(root, target)
    print(f"All paths with sum {target}: {paths}")  # [[12, 7, 4], [12, 1, 10]]
    
    # Test sum_of_path_numbers
    print("\n=== Sum of Path Numbers ===")
    path_sum_root = TreeNode(1)
    path_sum_root.left = TreeNode(0)
    path_sum_root.right = TreeNode(1)
    path_sum_root.left.left = TreeNode(1)
    path_sum_root.right.left = TreeNode(6)
    path_sum_root.right.right = TreeNode(5)
    
    result = sum_of_path_numbers(path_sum_root)
    print(f"Sum of all path numbers: {result}")  # 332 (101 + 116 + 115)
    
    # Test find_path_with_sequence
    print("\n=== Find Path with Sequence ===")
    sequence = [1, 0, 7]
    result = find_path_with_sequence(path_sum_root, sequence)
    print(f"Tree has path with sequence {sequence}: {result}")  # False
    
    sequence = [1, 1, 6]
    result = find_path_with_sequence(path_sum_root, sequence)
    print(f"Tree has path with sequence {sequence}: {result}")  # True
    
    # Test count_paths_for_sum
    print("\n=== Count Paths for Sum ===")
    target = 7
    count = count_paths_for_sum(root, target)
    print(f"Number of paths with sum {target}: {count}")  # 2
    
    # Test tree_diameter
    print("\n=== Tree Diameter ===")
    diameter = tree_diameter(root)
    print(f"Tree diameter: {diameter}")  # 5
    
    # Test path_with_maximum_sum
    print("\n=== Path with Maximum Sum ===")
    max_sum = path_with_maximum_sum(root)
    print(f"Maximum path sum: {max_sum}")  # 42
    
    # Test traversals
    print("\n=== Tree Traversals ===")
    print(f"Inorder: {inorder_traversal(root)}")
    print(f"Preorder: {preorder_traversal(root)}")
    print(f"Postorder: {postorder_traversal(root)}")
    
    # Test binary_tree_paths
    print("\n=== All Root-to-Leaf Paths ===")
    paths = binary_tree_paths(root)
    print(f"All paths: {paths}")
