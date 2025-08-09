"""
010 - Binary Tree Implementation
===============================

This module implements basic binary tree with all fundamental operations:
- TreeNode class definition
- Binary tree creation and insertion
- Tree traversals (In-order, Pre-order, Post-order, Level-order)
- Tree properties (height, size, depth)
- Tree operations (search, deletion, etc.)

Time Complexity:
- Search: O(n) worst case (unbalanced), O(log n) average case
- Insertion: O(n) worst case, O(log n) average case  
- Deletion: O(n) worst case, O(log n) average case
- Traversal: O(n)

Tree Structure Example:
       1
      / \
     2   3
    / \   \
   4   5   6
"""

from collections import deque

class TreeNode:
    """Node class for binary tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


class BinaryTree:
    """Binary Tree implementation with various operations"""
    
    def __init__(self, root_data=None):
        if root_data is not None:
            self.root = TreeNode(root_data)
        else:
            self.root = None
    
    def is_empty(self):
        """Check if tree is empty"""
        return self.root is None
    
    def insert_level_order(self, data):
        """Insert node in level order (complete binary tree)"""
        new_node = TreeNode(data)
        
        if self.is_empty():
            self.root = new_node
            return
        
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            
            if current.left is None:
                current.left = new_node
                return
            elif current.right is None:
                current.right = new_node
                return
            else:
                queue.append(current.left)
                queue.append(current.right)
    
    def insert_recursive(self, data, current=None):
        """Insert node recursively (left-biased)"""
        if current is None:
            current = self.root
        
        if self.is_empty():
            self.root = TreeNode(data)
            return self.root
        
        if current.left is None:
            current.left = TreeNode(data)
            return current.left
        elif current.right is None:
            current.right = TreeNode(data)
            return current.right
        else:
            # Recursively insert in left subtree first
            return self.insert_recursive(data, current.left)
    
    # ============= TREE TRAVERSALS =============
    
    def inorder_traversal(self, node=None, result=None):
        """In-order traversal: Left -> Root -> Right"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder_traversal(node.left, result)
            result.append(node.data)
            self.inorder_traversal(node.right, result)
        
        return result
    
    def preorder_traversal(self, node=None, result=None):
        """Pre-order traversal: Root -> Left -> Right"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.data)
            self.preorder_traversal(node.left, result)
            self.preorder_traversal(node.right, result)
        
        return result
    
    def postorder_traversal(self, node=None, result=None):
        """Post-order traversal: Left -> Right -> Root"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder_traversal(node.left, result)
            self.postorder_traversal(node.right, result)
            result.append(node.data)
        
        return result
    
    def level_order_traversal(self):
        """Level-order traversal using queue"""
        if self.is_empty():
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            current = queue.popleft()
            result.append(current.data)
            
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        
        return result
    
    def level_order_with_levels(self):
        """Level-order traversal showing each level separately"""
        if self.is_empty():
            return []
        
        result = []
        queue = deque([self.root])
        
        while queue:
            level_size = len(queue)
            current_level = []
            
            for _ in range(level_size):
                current = queue.popleft()
                current_level.append(current.data)
                
                if current.left:
                    queue.append(current.left)
                if current.right:
                    queue.append(current.right)
            
            result.append(current_level)
        
        return result
    
    # ============= ITERATIVE TRAVERSALS =============
    
    def inorder_iterative(self):
        """Iterative in-order traversal using stack"""
        if self.is_empty():
            return []
        
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Current is None, pop from stack
            current = stack.pop()
            result.append(current.data)
            
            # Visit right subtree
            current = current.right
        
        return result
    
    def preorder_iterative(self):
        """Iterative pre-order traversal using stack"""
        if self.is_empty():
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            current = stack.pop()
            result.append(current.data)
            
            # Push right first, then left
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        return result
    
    def postorder_iterative(self):
        """Iterative post-order traversal using two stacks"""
        if self.is_empty():
            return []
        
        result = []
        stack1 = [self.root]
        stack2 = []
        
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        
        while stack2:
            result.append(stack2.pop().data)
        
        return result
    
    # ============= TREE PROPERTIES =============
    
    def height(self, node=None):
        """Calculate height of tree (longest path from root to leaf)"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        left_height = self.height(node.left)
        right_height = self.height(node.right)
        
        return max(left_height, right_height) + 1
    
    def depth(self, target, node=None, current_depth=0):
        """Calculate depth of a specific node"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        if node.data == target:
            return current_depth
        
        left_depth = self.depth(target, node.left, current_depth + 1)
        if left_depth != -1:
            return left_depth
        
        return self.depth(target, node.right, current_depth + 1)
    
    def size(self, node=None):
        """Calculate total number of nodes in tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.size(node.left) + self.size(node.right)
    
    def count_leaves(self, node=None):
        """Count number of leaf nodes"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        if node.left is None and node.right is None:
            return 1
        
        return self.count_leaves(node.left) + self.count_leaves(node.right)
    
    def count_internal_nodes(self):
        """Count number of internal (non-leaf) nodes"""
        return self.size() - self.count_leaves()
    
    # ============= SEARCH AND OPERATIONS =============
    
    def search(self, target, node=None):
        """Search for a value in the tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return False
        
        if node.data == target:
            return True
        
        return self.search(target, node.left) or self.search(target, node.right)
    
    def find_node(self, target, node=None):
        """Find and return the node with target value"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        if node.data == target:
            return node
        
        left_result = self.find_node(target, node.left)
        if left_result:
            return left_result
        
        return self.find_node(target, node.right)
    
    def find_parent(self, target, node=None, parent=None):
        """Find parent of target node"""
        if node is None:
            node = self.root
        
        if node is None:
            return None
        
        if node.data == target:
            return parent
        
        left_parent = self.find_parent(target, node.left, node)
        if left_parent:
            return left_parent
        
        return self.find_parent(target, node.right, node)
    
    def delete_node(self, target):
        """Delete a node from the tree"""
        if self.is_empty():
            return False
        
        # Find the node to delete and its parent
        target_node = self.find_node(target)
        if not target_node:
            return False
        
        parent = self.find_parent(target)
        
        # Case 1: Leaf node
        if target_node.left is None and target_node.right is None:
            if parent is None:  # Root node
                self.root = None
            elif parent.left == target_node:
                parent.left = None
            else:
                parent.right = None
        
        # Case 2: Node with one child
        elif target_node.left is None or target_node.right is None:
            child = target_node.left if target_node.left else target_node.right
            
            if parent is None:  # Root node
                self.root = child
            elif parent.left == target_node:
                parent.left = child
            else:
                parent.right = child
        
        # Case 3: Node with two children
        else:
            # Find inorder successor (leftmost node in right subtree)
            successor = target_node.right
            while successor.left:
                successor = successor.left
            
            # Replace target's data with successor's data
            target_node.data = successor.data
            
            # Delete the successor (which has at most one child)
            self.delete_node(successor.data)
        
        return True
    
    # ============= TREE VALIDATION =============
    
    def is_complete(self):
        """Check if tree is complete binary tree"""
        if self.is_empty():
            return True
        
        queue = deque([self.root])
        found_non_full = False
        
        while queue:
            current = queue.popleft()
            
            if current.left:
                if found_non_full:
                    return False
                queue.append(current.left)
            else:
                found_non_full = True
            
            if current.right:
                if found_non_full:
                    return False
                queue.append(current.right)
            else:
                found_non_full = True
        
        return True
    
    def is_full(self, node=None):
        """Check if tree is full binary tree (every node has 0 or 2 children)"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        # Leaf node
        if node.left is None and node.right is None:
            return True
        
        # Node with both children
        if node.left and node.right:
            return self.is_full(node.left) and self.is_full(node.right)
        
        # Node with only one child
        return False
    
    def is_perfect(self):
        """Check if tree is perfect binary tree"""
        return self.is_full() and self.is_complete()
    
    # ============= DISPLAY METHODS =============
    
    def display_tree(self):
        """Display tree structure visually"""
        if self.is_empty():
            print("Tree is empty")
            return
        
        def print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                print(" " * (level * 4) + prefix + str(node.data))
                if node.left or node.right:
                    if node.left:
                        print_tree(node.left, level + 1, "L--- ")
                    else:
                        print(" " * ((level + 1) * 4) + "L--- None")
                    
                    if node.right:
                        print_tree(node.right, level + 1, "R--- ")
                    else:
                        print(" " * ((level + 1) * 4) + "R--- None")
        
        print_tree(self.root)
    
    def print_traversals(self):
        """Print all traversal methods"""
        print("Tree Traversals:")
        print(f"In-order (Recursive):   {self.inorder_traversal()}")
        print(f"Pre-order (Recursive):  {self.preorder_traversal()}")
        print(f"Post-order (Recursive): {self.postorder_traversal()}")
        print(f"Level-order:            {self.level_order_traversal()}")
        print()
        print("Iterative Traversals:")
        print(f"In-order (Iterative):   {self.inorder_iterative()}")
        print(f"Pre-order (Iterative):  {self.preorder_iterative()}")
        print(f"Post-order (Iterative): {self.postorder_iterative()}")


def test_binary_tree():
    """Test binary tree implementation"""
    print("=== Testing Binary Tree Implementation ===\n")
    
    # Create tree and insert nodes
    tree = BinaryTree()
    
    print("Creating tree with level-order insertion:")
    values = [1, 2, 3, 4, 5, 6, 7]
    for val in values:
        tree.insert_level_order(val)
    
    print("Tree structure:")
    tree.display_tree()
    print()
    
    # Test traversals
    print("=== Tree Traversals ===")
    tree.print_traversals()
    print()
    
    # Test level-order with levels
    print("=== Level-order by Levels ===")
    levels = tree.level_order_with_levels()
    for i, level in enumerate(levels):
        print(f"Level {i}: {level}")
    print()
    
    # Test tree properties
    print("=== Tree Properties ===")
    print(f"Height: {tree.height()}")
    print(f"Size: {tree.size()}")
    print(f"Number of leaves: {tree.count_leaves()}")
    print(f"Number of internal nodes: {tree.count_internal_nodes()}")
    print(f"Is complete: {tree.is_complete()}")
    print(f"Is full: {tree.is_full()}")
    print(f"Is perfect: {tree.is_perfect()}")
    print()
    
    # Test search operations
    print("=== Search Operations ===")
    search_values = [5, 8, 1]
    for val in search_values:
        found = tree.search(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
        
        if found:
            depth = tree.depth(val)
            parent = tree.find_parent(val)
            parent_data = parent.data if parent else "None (root)"
            print(f"  Depth of {val}: {depth}")
            print(f"  Parent of {val}: {parent_data}")
    print()
    
    # Test deletion
    print("=== Deletion Operations ===")
    print("Before deletion:")
    tree.display_tree()
    
    delete_val = 2
    success = tree.delete_node(delete_val)
    print(f"\nDeleting node {delete_val}: {'Success' if success else 'Failed'}")
    
    print("After deletion:")
    tree.display_tree()
    print()
    
    # Create different tree types for testing
    print("=== Testing Different Tree Types ===")
    
    # Full binary tree
    full_tree = BinaryTree(1)
    full_tree.root.left = TreeNode(2)
    full_tree.root.right = TreeNode(3)
    full_tree.root.left.left = TreeNode(4)
    full_tree.root.left.right = TreeNode(5)
    full_tree.root.right.left = TreeNode(6)
    full_tree.root.right.right = TreeNode(7)
    
    print("Full Binary Tree:")
    full_tree.display_tree()
    print(f"Is full: {full_tree.is_full()}")
    print(f"Is complete: {full_tree.is_complete()}")
    print(f"Is perfect: {full_tree.is_perfect()}")
    print()
    
    # Incomplete tree
    incomplete_tree = BinaryTree(1)
    incomplete_tree.root.left = TreeNode(2)
    incomplete_tree.root.right = TreeNode(3)
    incomplete_tree.root.left.left = TreeNode(4)
    incomplete_tree.root.right.right = TreeNode(5)
    
    print("Incomplete Binary Tree:")
    incomplete_tree.display_tree()
    print(f"Is full: {incomplete_tree.is_full()}")
    print(f"Is complete: {incomplete_tree.is_complete()}")


if __name__ == "__main__":
    test_binary_tree()
