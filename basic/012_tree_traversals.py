"""
012 - Tree Traversals Implementation
===================================

This module implements all tree traversal algorithms:
- Depth-First Traversals (Recursive and Iterative)
- Breadth-First Traversals
- Morris Traversal (Space-optimized)
- Vertical and Diagonal Traversals
- Boundary Traversal
- Zigzag Traversal

Time Complexity: O(n) for all traversals
Space Complexity: 
- Recursive: O(h) where h is height
- Iterative: O(w) where w is maximum width
- Morris: O(1)
"""

from collections import deque, defaultdict

class TreeNode:
    """Node class for tree traversals"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


class TreeTraversals:
    """Complete implementation of tree traversal algorithms"""
    
    def __init__(self, root=None):
        self.root = root
    
    # ============= DEPTH-FIRST TRAVERSALS (RECURSIVE) =============
    
    def inorder_recursive(self, node=None, result=None):
        """In-order: Left -> Root -> Right"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder_recursive(node.left, result)
            result.append(node.data)
            self.inorder_recursive(node.right, result)
        
        return result
    
    def preorder_recursive(self, node=None, result=None):
        """Pre-order: Root -> Left -> Right"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.data)
            self.preorder_recursive(node.left, result)
            self.preorder_recursive(node.right, result)
        
        return result
    
    def postorder_recursive(self, node=None, result=None):
        """Post-order: Left -> Right -> Root"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder_recursive(node.left, result)
            self.postorder_recursive(node.right, result)
            result.append(node.data)
        
        return result
    
    # ============= DEPTH-FIRST TRAVERSALS (ITERATIVE) =============
    
    def inorder_iterative(self):
        """Iterative in-order traversal using stack"""
        if not self.root:
            return []
        
        result = []
        stack = []
        current = self.root
        
        while stack or current:
            # Go to leftmost node
            while current:
                stack.append(current)
                current = current.left
            
            # Process current node
            current = stack.pop()
            result.append(current.data)
            
            # Move to right subtree
            current = current.right
        
        return result
    
    def preorder_iterative(self):
        """Iterative pre-order traversal using stack"""
        if not self.root:
            return []
        
        result = []
        stack = [self.root]
        
        while stack:
            current = stack.pop()
            result.append(current.data)
            
            # Push right first, then left (stack is LIFO)
            if current.right:
                stack.append(current.right)
            if current.left:
                stack.append(current.left)
        
        return result
    
    def postorder_iterative(self):
        """Iterative post-order traversal using two stacks"""
        if not self.root:
            return []
        
        result = []
        stack1 = [self.root]
        stack2 = []
        
        # First stack for traversal, second for result
        while stack1:
            current = stack1.pop()
            stack2.append(current)
            
            if current.left:
                stack1.append(current.left)
            if current.right:
                stack1.append(current.right)
        
        # Pop from second stack to get post-order
        while stack2:
            result.append(stack2.pop().data)
        
        return result
    
    def postorder_single_stack(self):
        """Post-order using single stack (more complex)"""
        if not self.root:
            return []
        
        result = []
        stack = []
        last_visited = None
        current = self.root
        
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
    
    # ============= BREADTH-FIRST TRAVERSALS =============
    
    def level_order(self):
        """Level-order (BFS) traversal"""
        if not self.root:
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
        """Level-order traversal with level separation"""
        if not self.root:
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
    
    def reverse_level_order(self):
        """Bottom-up level order traversal"""
        if not self.root:
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
            
            result.insert(0, current_level)  # Insert at beginning
        
        return result
    
    def zigzag_traversal(self):
        """Zigzag (spiral) level order traversal"""
        if not self.root:
            return []
        
        result = []
        queue = deque([self.root])
        left_to_right = True
        
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
            
            if not left_to_right:
                current_level.reverse()
            
            result.extend(current_level)
            left_to_right = not left_to_right
        
        return result
    
    # ============= MORRIS TRAVERSALS (O(1) SPACE) =============
    
    def morris_inorder(self):
        """Morris in-order traversal with O(1) space"""
        if not self.root:
            return []
        
        result = []
        current = self.root
        
        while current:
            if current.left is None:
                result.append(current.data)
                current = current.right
            else:
                # Find inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Make current as right child of predecessor
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the changes
                    predecessor.right = None
                    result.append(current.data)
                    current = current.right
        
        return result
    
    def morris_preorder(self):
        """Morris pre-order traversal with O(1) space"""
        if not self.root:
            return []
        
        result = []
        current = self.root
        
        while current:
            if current.left is None:
                result.append(current.data)
                current = current.right
            else:
                # Find inorder predecessor
                predecessor = current.left
                while predecessor.right and predecessor.right != current:
                    predecessor = predecessor.right
                
                if predecessor.right is None:
                    # Make current as right child of predecessor
                    result.append(current.data)  # Process before going left
                    predecessor.right = current
                    current = current.left
                else:
                    # Revert the changes
                    predecessor.right = None
                    current = current.right
        
        return result
    
    # ============= SPECIAL TRAVERSALS =============
    
    def boundary_traversal(self):
        """Boundary traversal: left boundary + leaves + right boundary"""
        if not self.root:
            return []
        
        result = []
        
        # Add root if it's not a leaf
        if not self._is_leaf(self.root):
            result.append(self.root.data)
        
        # Add left boundary (excluding root and leaves)
        self._add_left_boundary(self.root.left, result)
        
        # Add all leaves
        self._add_leaves(self.root, result)
        
        # Add right boundary (excluding root and leaves, in reverse)
        self._add_right_boundary(self.root.right, result)
        
        return result
    
    def _is_leaf(self, node):
        """Check if node is a leaf"""
        return node and not node.left and not node.right
    
    def _add_left_boundary(self, node, result):
        """Add left boundary nodes"""
        if node:
            if not self._is_leaf(node):
                result.append(node.data)
            
            if node.left:
                self._add_left_boundary(node.left, result)
            elif node.right:
                self._add_left_boundary(node.right, result)
    
    def _add_right_boundary(self, node, result):
        """Add right boundary nodes in reverse"""
        if node:
            if node.right:
                self._add_right_boundary(node.right, result)
            elif node.left:
                self._add_right_boundary(node.left, result)
            
            if not self._is_leaf(node):
                result.append(node.data)
    
    def _add_leaves(self, node, result):
        """Add all leaf nodes"""
        if node:
            if self._is_leaf(node):
                result.append(node.data)
            else:
                self._add_leaves(node.left, result)
                self._add_leaves(node.right, result)
    
    def vertical_traversal(self):
        """Vertical order traversal"""
        if not self.root:
            return []
        
        # Dictionary to store nodes at each horizontal distance
        node_map = defaultdict(list)
        
        # Queue stores (node, horizontal_distance, level)
        queue = deque([(self.root, 0, 0)])
        
        while queue:
            node, hd, level = queue.popleft()
            node_map[hd].append((node.data, level))
            
            if node.left:
                queue.append((node.left, hd - 1, level + 1))
            if node.right:
                queue.append((node.right, hd + 1, level + 1))
        
        # Sort by horizontal distance and then by level
        result = []
        for hd in sorted(node_map.keys()):
            # Sort nodes at same horizontal distance by level
            node_map[hd].sort(key=lambda x: x[1])
            result.extend([data for data, level in node_map[hd]])
        
        return result
    
    def diagonal_traversal(self):
        """Diagonal traversal (top-left to bottom-right)"""
        if not self.root:
            return []
        
        # Dictionary to store nodes at each diagonal
        diagonal_map = defaultdict(list)
        
        # Queue stores (node, diagonal_index)
        queue = deque([(self.root, 0)])
        
        while queue:
            node, diagonal = queue.popleft()
            diagonal_map[diagonal].append(node.data)
            
            if node.left:
                queue.append((node.left, diagonal + 1))
            if node.right:
                queue.append((node.right, diagonal))
        
        result = []
        for diagonal in sorted(diagonal_map.keys()):
            result.extend(diagonal_map[diagonal])
        
        return result
    
    # ============= UTILITY METHODS =============
    
    def print_all_traversals(self):
        """Print all traversal results"""
        print("=== Recursive Traversals ===")
        print(f"In-order:    {self.inorder_recursive()}")
        print(f"Pre-order:   {self.preorder_recursive()}")
        print(f"Post-order:  {self.postorder_recursive()}")
        print()
        
        print("=== Iterative Traversals ===")
        print(f"In-order:    {self.inorder_iterative()}")
        print(f"Pre-order:   {self.preorder_iterative()}")
        print(f"Post-order:  {self.postorder_iterative()}")
        print()
        
        print("=== Breadth-First Traversals ===")
        print(f"Level-order: {self.level_order()}")
        print(f"Zigzag:      {self.zigzag_traversal()}")
        print()
        
        print("=== Morris Traversals (O(1) space) ===")
        print(f"In-order:    {self.morris_inorder()}")
        print(f"Pre-order:   {self.morris_preorder()}")
        print()
        
        print("=== Special Traversals ===")
        print(f"Boundary:    {self.boundary_traversal()}")
        print(f"Vertical:    {self.vertical_traversal()}")
        print(f"Diagonal:    {self.diagonal_traversal()}")


def create_sample_tree():
    """Create a sample tree for testing"""
    #       1
    #      / \
    #     2   3
    #    / \   \
    #   4   5   6
    #  /       / \
    # 7       8   9
    
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.left.left.left = TreeNode(7)
    root.right.right.left = TreeNode(8)
    root.right.right.right = TreeNode(9)
    
    return root


def test_tree_traversals():
    """Test all tree traversal implementations"""
    print("=== Testing Tree Traversals ===\n")
    
    # Create sample tree
    root = create_sample_tree()
    traversals = TreeTraversals(root)
    
    print("Sample Tree Structure:")
    print("       1")
    print("      / \\")
    print("     2   3")
    print("    / \\   \\")
    print("   4   5   6")
    print("  /       / \\")
    print(" 7       8   9")
    print()
    
    # Test all traversals
    traversals.print_all_traversals()
    
    # Test level-order with levels
    print("=== Level-order with Levels ===")
    levels = traversals.level_order_with_levels()
    for i, level in enumerate(levels):
        print(f"Level {i}: {level}")
    print()
    
    # Test reverse level order
    print("=== Reverse Level Order ===")
    reverse_levels = traversals.reverse_level_order()
    for i, level in enumerate(reverse_levels):
        print(f"Level {len(reverse_levels)-1-i}: {level}")
    print()
    
    # Performance comparison
    print("=== Performance Comparison ===")
    import time
    
    # Test with larger tree
    def create_large_tree(n):
        """Create a larger tree for performance testing"""
        if n <= 0:
            return None
        
        root = TreeNode(n)
        root.left = create_large_tree(n - 1)
        root.right = create_large_tree(n - 2)
        return root
    
    large_root = create_large_tree(15)
    large_traversals = TreeTraversals(large_root)
    
    # Time different traversal methods
    methods = [
        ("Recursive In-order", large_traversals.inorder_recursive),
        ("Iterative In-order", large_traversals.inorder_iterative),
        ("Morris In-order", large_traversals.morris_inorder)
    ]
    
    for name, method in methods:
        start_time = time.time()
        result = method()
        end_time = time.time()
        print(f"{name}: {end_time - start_time:.6f} seconds, {len(result)} nodes")
    
    print("\nNote: Morris traversal uses O(1) extra space!")


def test_special_cases():
    """Test traversals on special tree cases"""
    print("\n=== Testing Special Cases ===\n")
    
    # Single node tree
    print("Single Node Tree:")
    single_node = TreeNode(42)
    single_traversals = TreeTraversals(single_node)
    print(f"In-order: {single_traversals.inorder_recursive()}")
    print(f"Level-order: {single_traversals.level_order()}")
    print()
    
    # Linear tree (like linked list)
    print("Linear Tree (Right Skewed):")
    linear_root = TreeNode(1)
    current = linear_root
    for i in range(2, 6):
        current.right = TreeNode(i)
        current = current.right
    
    linear_traversals = TreeTraversals(linear_root)
    print(f"In-order: {linear_traversals.inorder_recursive()}")
    print(f"Pre-order: {linear_traversals.preorder_recursive()}")
    print(f"Morris In-order: {linear_traversals.morris_inorder()}")
    print()
    
    # Perfect binary tree
    print("Perfect Binary Tree:")
    perfect_root = TreeNode(1)
    perfect_root.left = TreeNode(2)
    perfect_root.right = TreeNode(3)
    perfect_root.left.left = TreeNode(4)
    perfect_root.left.right = TreeNode(5)
    perfect_root.right.left = TreeNode(6)
    perfect_root.right.right = TreeNode(7)
    
    perfect_traversals = TreeTraversals(perfect_root)
    print(f"Boundary: {perfect_traversals.boundary_traversal()}")
    print(f"Vertical: {perfect_traversals.vertical_traversal()}")
    print(f"Diagonal: {perfect_traversals.diagonal_traversal()}")


if __name__ == "__main__":
    test_tree_traversals()
    test_special_cases()
