"""
013 - AVL Tree Implementation
============================

This module implements AVL Tree (Adelson-Velsky and Landis Tree):
- Self-balancing binary search tree
- Height-balanced with balance factor ∈ {-1, 0, 1}
- Automatic rotations to maintain balance
- All BST operations with guaranteed O(log n) complexity

Time Complexity:
- Search: O(log n) guaranteed
- Insertion: O(log n) guaranteed
- Deletion: O(log n) guaranteed
- Height: O(log n) guaranteed

Balance Factor = height(left subtree) - height(right subtree)
"""

class AVLNode:
    """Node class for AVL Tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 1  # Height of the node
    
    def __str__(self):
        return str(self.data)


class AVLTree:
    """AVL Tree implementation with auto-balancing"""
    
    def __init__(self):
        self.root = None
    
    # ============= UTILITY METHODS =============
    
    def get_height(self, node):
        """Get height of node"""
        if node is None:
            return 0
        return node.height
    
    def get_balance(self, node):
        """Get balance factor of node"""
        if node is None:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)
    
    def update_height(self, node):
        """Update height of node"""
        if node:
            node.height = 1 + max(self.get_height(node.left), 
                                  self.get_height(node.right))
    
    # ============= ROTATION OPERATIONS =============
    
    def rotate_right(self, y):
        """Right rotation around node y"""
        #     y                x
        #    / \\              / \\
        #   x   C    -->      A   y
        #  / \\                  / \\
        # A   B                B   C
        
        x = y.left
        B = x.right
        
        # Perform rotation
        x.right = y
        y.left = B
        
        # Update heights
        self.update_height(y)
        self.update_height(x)
        
        return x  # New root of subtree
    
    def rotate_left(self, x):
        """Left rotation around node x"""
        #   x                    y
        #  / \\                 / \\
        # A   y      -->       x   C
        #    / \\              / \\
        #   B   C            A   B
        
        y = x.right
        B = y.left
        
        # Perform rotation
        y.left = x
        x.right = B
        
        # Update heights
        self.update_height(x)
        self.update_height(y)
        
        return y  # New root of subtree
    
    # ============= INSERTION =============
    
    def insert(self, data):
        """Insert data into AVL tree"""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Recursive helper for insertion with balancing"""
        # 1. Perform normal BST insertion
        if node is None:
            return AVLNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        else:
            # Duplicate values not allowed
            return node
        
        # 2. Update height of current node
        self.update_height(node)
        
        # 3. Get balance factor
        balance = self.get_balance(node)
        
        # 4. If unbalanced, perform appropriate rotations
        
        # Left Left Case
        if balance > 1 and data < node.left.data:
            return self.rotate_right(node)
        
        # Right Right Case
        if balance < -1 and data > node.right.data:
            return self.rotate_left(node)
        
        # Left Right Case
        if balance > 1 and data > node.left.data:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Right Left Case
        if balance < -1 and data < node.right.data:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        # Return unchanged node if balanced
        return node
    
    # ============= DELETION =============
    
    def delete(self, data):
        """Delete data from AVL tree"""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Recursive helper for deletion with balancing"""
        # 1. Perform normal BST deletion
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Node with two children
            # Get inorder successor (smallest in right subtree)
            temp = self._find_min(node.right)
            
            # Copy successor's data to this node
            node.data = temp.data
            
            # Delete the successor
            node.right = self._delete_recursive(node.right, temp.data)
        
        # 2. Update height of current node
        self.update_height(node)
        
        # 3. Get balance factor
        balance = self.get_balance(node)
        
        # 4. If unbalanced, perform appropriate rotations
        
        # Left Left Case
        if balance > 1 and self.get_balance(node.left) >= 0:
            return self.rotate_right(node)
        
        # Left Right Case
        if balance > 1 and self.get_balance(node.left) < 0:
            node.left = self.rotate_left(node.left)
            return self.rotate_right(node)
        
        # Right Right Case
        if balance < -1 and self.get_balance(node.right) <= 0:
            return self.rotate_left(node)
        
        # Right Left Case
        if balance < -1 and self.get_balance(node.right) > 0:
            node.right = self.rotate_right(node.right)
            return self.rotate_left(node)
        
        return node
    
    def _find_min(self, node):
        """Find minimum node in subtree"""
        while node.left:
            node = node.left
        return node
    
    # ============= SEARCH OPERATIONS =============
    
    def search(self, data):
        """Search for data in AVL tree"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Recursive search helper"""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def contains(self, data):
        """Check if tree contains data"""
        return self.search(data) is not None
    
    # ============= TRAVERSALS =============
    
    def inorder(self, node=None, result=None):
        """In-order traversal (sorted order)"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.inorder(node.left, result)
            result.append(node.data)
            self.inorder(node.right, result)
        
        return result
    
    def preorder(self, node=None, result=None):
        """Pre-order traversal"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            result.append(node.data)
            self.preorder(node.left, result)
            self.preorder(node.right, result)
        
        return result
    
    # ============= TREE PROPERTIES =============
    
    def height(self):
        """Get height of tree"""
        return self.get_height(self.root)
    
    def size(self, node=None):
        """Get number of nodes in tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.size(node.left) + self.size(node.right)
    
    def is_balanced(self, node=None):
        """Check if tree is balanced (should always be true for AVL)"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        balance = self.get_balance(node)
        
        return (abs(balance) <= 1 and 
                self.is_balanced(node.left) and 
                self.is_balanced(node.right))
    
    def min_value(self):
        """Find minimum value in tree"""
        if self.root is None:
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def max_value(self):
        """Find maximum value in tree"""
        if self.root is None:
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    # ============= VALIDATION =============
    
    def is_valid_avl(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Validate if tree is a valid AVL tree"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        # Check BST property
        if node.data <= min_val or node.data >= max_val:
            return False
        
        # Check balance factor
        if abs(self.get_balance(node)) > 1:
            return False
        
        # Check height property
        expected_height = 1 + max(self.get_height(node.left), 
                                 self.get_height(node.right))
        if node.height != expected_height:
            return False
        
        # Recursively validate subtrees
        return (self.is_valid_avl(node.left, min_val, node.data) and
                self.is_valid_avl(node.right, node.data, max_val))
    
    # ============= DISPLAY METHODS =============
    
    def display(self):
        """Display AVL tree structure with heights and balance factors"""
        if self.root is None:
            print("Tree is empty")
            return
        
        def print_tree(node, level=0, prefix="Root: "):
            if node is not None:
                balance = self.get_balance(node)
                print(" " * (level * 4) + f"{prefix}{node.data} (h:{node.height}, b:{balance})")
                
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
    
    def get_statistics(self):
        """Get tree statistics"""
        return {
            'height': self.height(),
            'size': self.size(),
            'is_balanced': self.is_balanced(),
            'is_valid_avl': self.is_valid_avl(),
            'min_value': self.min_value(),
            'max_value': self.max_value()
        }


def test_avl_tree():
    """Test AVL tree implementation"""
    print("=== Testing AVL Tree Implementation ===\n")
    
    avl = AVLTree()
    
    # Test insertions that would cause imbalance in regular BST
    print("=== Testing Insertions ===")
    insert_values = [10, 20, 30, 40, 50, 25]
    
    for val in insert_values:
        print(f"Inserting {val}:")
        avl.insert(val)
        print(f"Tree height: {avl.height()}, Balanced: {avl.is_balanced()}")
        print("Tree structure:")
        avl.display()
        print()
    
    # Test tree properties
    print("=== Tree Properties ===")
    stats = avl.get_statistics()
    for key, value in stats.items():
        print(f"{key.replace('_', ' ').title()}: {value}")
    print()
    
    # Test traversals
    print("=== Traversals ===")
    print(f"In-order (sorted): {avl.inorder()}")
    print(f"Pre-order: {avl.preorder()}")
    print()
    
    # Test search operations
    print("=== Search Operations ===")
    search_values = [25, 35, 10]
    for val in search_values:
        found = avl.contains(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    print()
    
    # Test deletions
    print("=== Testing Deletions ===")
    delete_values = [30, 10, 50]
    
    for val in delete_values:
        print(f"Deleting {val}:")
        avl.delete(val)
        print(f"Tree height: {avl.height()}, Balanced: {avl.is_balanced()}")
        print(f"In-order: {avl.inorder()}")
        print("Tree structure:")
        avl.display()
        print()
    
    # Test worst case for regular BST
    print("=== Testing Worst Case Scenario ===")
    avl_worst = AVLTree()
    
    print("Inserting sequential values 1-10 (worst case for regular BST):")
    for i in range(1, 11):
        avl_worst.insert(i)
    
    print("AVL Tree structure (should be balanced):")
    avl_worst.display()
    
    stats = avl_worst.get_statistics()
    print(f"Height: {stats['height']} (log₂(10) ≈ 3.32)")
    print(f"Expected height for regular BST: 9 (degenerate)")
    print(f"AVL maintains balance: {stats['is_balanced']}")
    print()
    
    # Performance comparison simulation
    print("=== Performance Analysis ===")
    import time
    import random
    
    # Create larger AVL tree
    large_avl = AVLTree()
    values = list(range(1000))
    random.shuffle(values)
    
    # Time insertions
    start_time = time.time()
    for val in values:
        large_avl.insert(val)
    insert_time = time.time() - start_time
    
    # Time searches
    search_vals = random.sample(values, 100)
    start_time = time.time()
    for val in search_vals:
        large_avl.contains(val)
    search_time = time.time() - start_time
    
    stats = large_avl.get_statistics()
    print(f"Tree with 1000 nodes:")
    print(f"Height: {stats['height']} (optimal: ~{int(__import__('math').log2(1000))})")
    print(f"Insertion time: {insert_time:.4f} seconds")
    print(f"Search time (100 queries): {search_time:.4f} seconds")
    print(f"Average search time: {search_time/100*1000:.4f} ms per search")
    print(f"Tree remains balanced: {stats['is_balanced']}")


def test_rotation_cases():
    """Test all rotation cases explicitly"""
    print("\n=== Testing Rotation Cases ===\n")
    
    # Test Left-Left case
    print("Left-Left Case:")
    ll_tree = AVLTree()
    for val in [30, 20, 10]:  # Will trigger right rotation
        ll_tree.insert(val)
    print("After inserting 30, 20, 10:")
    ll_tree.display()
    print()
    
    # Test Right-Right case
    print("Right-Right Case:")
    rr_tree = AVLTree()
    for val in [10, 20, 30]:  # Will trigger left rotation
        rr_tree.insert(val)
    print("After inserting 10, 20, 30:")
    rr_tree.display()
    print()
    
    # Test Left-Right case
    print("Left-Right Case:")
    lr_tree = AVLTree()
    for val in [30, 10, 20]:  # Will trigger left-right rotation
        lr_tree.insert(val)
    print("After inserting 30, 10, 20:")
    lr_tree.display()
    print()
    
    # Test Right-Left case
    print("Right-Left Case:")
    rl_tree = AVLTree()
    for val in [10, 30, 20]:  # Will trigger right-left rotation
        rl_tree.insert(val)
    print("After inserting 10, 30, 20:")
    rl_tree.display()


if __name__ == "__main__":
    test_avl_tree()
    test_rotation_cases()
