"""
011 - Binary Search Tree (BST) Implementation
=============================================

This module implements Binary Search Tree with all fundamental operations:
- BST creation and insertion
- Search operations
- Deletion with all cases
- Tree traversals
- BST validation
- BST properties and utilities

Time Complexity:
- Search: O(log n) average, O(n) worst case
- Insertion: O(log n) average, O(n) worst case
- Deletion: O(log n) average, O(n) worst case
- Traversal: O(n)

BST Property: For each node, all nodes in left subtree < node < all nodes in right subtree
"""

class BSTNode:
    """Node class for Binary Search Tree"""
    
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)


class BinarySearchTree:
    """Binary Search Tree implementation"""
    
    def __init__(self):
        self.root = None
    
    def is_empty(self):
        """Check if BST is empty"""
        return self.root is None
    
    # ============= INSERTION OPERATIONS =============
    
    def insert(self, data):
        """Insert data into BST"""
        self.root = self._insert_recursive(self.root, data)
    
    def _insert_recursive(self, node, data):
        """Helper method for recursive insertion"""
        if node is None:
            return BSTNode(data)
        
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        elif data > node.data:
            node.right = self._insert_recursive(node.right, data)
        # If data == node.data, we don't insert (no duplicates)
        
        return node
    
    def insert_iterative(self, data):
        """Insert data into BST iteratively"""
        new_node = BSTNode(data)
        
        if self.is_empty():
            self.root = new_node
            return
        
        current = self.root
        parent = None
        
        while current:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return  # Duplicate, don't insert
        
        if data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node
    
    # ============= SEARCH OPERATIONS =============
    
    def search(self, data):
        """Search for data in BST"""
        return self._search_recursive(self.root, data)
    
    def _search_recursive(self, node, data):
        """Helper method for recursive search"""
        if node is None or node.data == data:
            return node
        
        if data < node.data:
            return self._search_recursive(node.left, data)
        else:
            return self._search_recursive(node.right, data)
    
    def search_iterative(self, data):
        """Search for data in BST iteratively"""
        current = self.root
        
        while current:
            if data == current.data:
                return current
            elif data < current.data:
                current = current.left
            else:
                current = current.right
        
        return None
    
    def contains(self, data):
        """Check if BST contains data"""
        return self.search(data) is not None
    
    # ============= DELETION OPERATIONS =============
    
    def delete(self, data):
        """Delete data from BST"""
        self.root = self._delete_recursive(self.root, data)
    
    def _delete_recursive(self, node, data):
        """Helper method for recursive deletion"""
        if node is None:
            return node
        
        if data < node.data:
            node.left = self._delete_recursive(node.left, data)
        elif data > node.data:
            node.right = self._delete_recursive(node.right, data)
        else:
            # Node to be deleted found
            
            # Case 1: Node with no children (leaf)
            if node.left is None and node.right is None:
                return None
            
            # Case 2: Node with one child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            
            # Case 3: Node with two children
            else:
                # Find inorder successor (smallest node in right subtree)
                successor = self._find_min(node.right)
                
                # Replace node's data with successor's data
                node.data = successor.data
                
                # Delete the successor
                node.right = self._delete_recursive(node.right, successor.data)
        
        return node
    
    def _find_min(self, node):
        """Find minimum node in subtree"""
        while node.left:
            node = node.left
        return node
    
    def _find_max(self, node):
        """Find maximum node in subtree"""
        while node.right:
            node = node.right
        return node
    
    # ============= TRAVERSAL OPERATIONS =============
    
    def inorder(self, node=None, result=None):
        """In-order traversal (gives sorted order for BST)"""
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
    
    def postorder(self, node=None, result=None):
        """Post-order traversal"""
        if result is None:
            result = []
        if node is None:
            node = self.root
        
        if node:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.data)
        
        return result
    
    # ============= BST PROPERTIES =============
    
    def find_minimum(self):
        """Find minimum value in BST"""
        if self.is_empty():
            return None
        
        current = self.root
        while current.left:
            current = current.left
        return current.data
    
    def find_maximum(self):
        """Find maximum value in BST"""
        if self.is_empty():
            return None
        
        current = self.root
        while current.right:
            current = current.right
        return current.data
    
    def height(self, node=None):
        """Calculate height of BST"""
        if node is None:
            node = self.root
        
        if node is None:
            return -1
        
        return max(self.height(node.left), self.height(node.right)) + 1
    
    def size(self, node=None):
        """Calculate total number of nodes"""
        if node is None:
            node = self.root
        
        if node is None:
            return 0
        
        return 1 + self.size(node.left) + self.size(node.right)
    
    # ============= BST VALIDATION =============
    
    def is_valid_bst(self, node=None, min_val=float('-inf'), max_val=float('inf')):
        """Check if tree is a valid BST"""
        if node is None:
            node = self.root
        
        if node is None:
            return True
        
        if node.data <= min_val or node.data >= max_val:
            return False
        
        return (self.is_valid_bst(node.left, min_val, node.data) and
                self.is_valid_bst(node.right, node.data, max_val))
    
    def is_balanced(self, node=None):
        """Check if BST is balanced (height difference <= 1)"""
        if node is None:
            node = self.root
        
        def check_balance(node):
            if node is None:
                return 0, True
            
            left_height, left_balanced = check_balance(node.left)
            right_height, right_balanced = check_balance(node.right)
            
            height = max(left_height, right_height) + 1
            balanced = (left_balanced and right_balanced and 
                       abs(left_height - right_height) <= 1)
            
            return height, balanced
        
        _, is_balanced = check_balance(node)
        return is_balanced
    
    # ============= RANGE AND SUCCESSOR/PREDECESSOR =============
    
    def range_query(self, min_val, max_val):
        """Find all values in given range [min_val, max_val]"""
        result = []
        self._range_query_helper(self.root, min_val, max_val, result)
        return result
    
    def _range_query_helper(self, node, min_val, max_val, result):
        """Helper for range query"""
        if node is None:
            return
        
        if min_val <= node.data <= max_val:
            result.append(node.data)
        
        if node.data > min_val:
            self._range_query_helper(node.left, min_val, max_val, result)
        
        if node.data < max_val:
            self._range_query_helper(node.right, min_val, max_val, result)
    
    def find_successor(self, data):
        """Find inorder successor of given data"""
        node = self.search(data)
        if node is None:
            return None
        
        # Case 1: Node has right subtree
        if node.right:
            return self._find_min(node.right).data
        
        # Case 2: Find ancestor that is left child of its parent
        successor = None
        current = self.root
        
        while current:
            if data < current.data:
                successor = current
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                break
        
        return successor.data if successor else None
    
    def find_predecessor(self, data):
        """Find inorder predecessor of given data"""
        node = self.search(data)
        if node is None:
            return None
        
        # Case 1: Node has left subtree
        if node.left:
            return self._find_max(node.left).data
        
        # Case 2: Find ancestor that is right child of its parent
        predecessor = None
        current = self.root
        
        while current:
            if data > current.data:
                predecessor = current
                current = current.right
            elif data < current.data:
                current = current.left
            else:
                break
        
        return predecessor.data if predecessor else None
    
    # ============= UTILITY METHODS =============
    
    def kth_smallest(self, k):
        """Find kth smallest element (1-indexed)"""
        result = []
        self._inorder_with_count(self.root, k, result)
        return result[0] if result else None
    
    def _inorder_with_count(self, node, k, result):
        """Helper for finding kth smallest"""
        if node is None or len(result) >= 1:
            return
        
        self._inorder_with_count(node.left, k, result)
        
        k -= 1
        if k == 0:
            result.append(node.data)
            return
        
        self._inorder_with_count(node.right, k, result)
    
    def kth_largest(self, k):
        """Find kth largest element (1-indexed)"""
        result = []
        self._reverse_inorder_with_count(self.root, k, result)
        return result[0] if result else None
    
    def _reverse_inorder_with_count(self, node, k, result):
        """Helper for finding kth largest"""
        if node is None or len(result) >= 1:
            return
        
        self._reverse_inorder_with_count(node.right, k, result)
        
        k -= 1
        if k == 0:
            result.append(node.data)
            return
        
        self._reverse_inorder_with_count(node.left, k, result)
    
    def lowest_common_ancestor(self, p, q):
        """Find lowest common ancestor of two nodes"""
        return self._lca_helper(self.root, p, q)
    
    def _lca_helper(self, node, p, q):
        """Helper for LCA"""
        if node is None:
            return None
        
        if p < node.data and q < node.data:
            return self._lca_helper(node.left, p, q)
        elif p > node.data and q > node.data:
            return self._lca_helper(node.right, p, q)
        else:
            return node.data
    
    # ============= DISPLAY METHODS =============
    
    def display(self):
        """Display BST structure"""
        if self.is_empty():
            print("BST is empty")
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
    
    def to_sorted_array(self):
        """Convert BST to sorted array"""
        return self.inorder()


def test_binary_search_tree():
    """Test BST implementation"""
    print("=== Testing Binary Search Tree ===\n")
    
    # Create BST and insert elements
    bst = BinarySearchTree()
    
    print("Inserting elements: 50, 30, 70, 20, 40, 60, 80")
    elements = [50, 30, 70, 20, 40, 60, 80]
    for elem in elements:
        bst.insert(elem)
    
    print("BST structure:")
    bst.display()
    print()
    
    # Test traversals
    print("=== Traversals ===")
    print(f"In-order (sorted):   {bst.inorder()}")
    print(f"Pre-order:           {bst.preorder()}")
    print(f"Post-order:          {bst.postorder()}")
    print()
    
    # Test search operations
    print("=== Search Operations ===")
    search_values = [40, 25, 70]
    for val in search_values:
        found = bst.contains(val)
        print(f"Search for {val}: {'Found' if found else 'Not found'}")
    print()
    
    # Test BST properties
    print("=== BST Properties ===")
    print(f"Minimum value: {bst.find_minimum()}")
    print(f"Maximum value: {bst.find_maximum()}")
    print(f"Height: {bst.height()}")
    print(f"Size: {bst.size()}")
    print(f"Is valid BST: {bst.is_valid_bst()}")
    print(f"Is balanced: {bst.is_balanced()}")
    print()
    
    # Test range query
    print("=== Range Query ===")
    range_result = bst.range_query(25, 65)
    print(f"Values in range [25, 65]: {range_result}")
    print()
    
    # Test successor and predecessor
    print("=== Successor and Predecessor ===")
    test_vals = [30, 50, 70]
    for val in test_vals:
        succ = bst.find_successor(val)
        pred = bst.find_predecessor(val)
        print(f"Value: {val}, Successor: {succ}, Predecessor: {pred}")
    print()
    
    # Test kth smallest/largest
    print("=== Kth Smallest/Largest ===")
    for k in range(1, 4):
        smallest = bst.kth_smallest(k)
        largest = bst.kth_largest(k)
        print(f"{k}th smallest: {smallest}, {k}th largest: {largest}")
    print()
    
    # Test LCA
    print("=== Lowest Common Ancestor ===")
    lca_pairs = [(20, 40), (60, 80), (20, 80)]
    for p, q in lca_pairs:
        lca = bst.lowest_common_ancestor(p, q)
        print(f"LCA of {p} and {q}: {lca}")
    print()
    
    # Test deletion
    print("=== Deletion Operations ===")
    print("Before deletion:")
    bst.display()
    print(f"In-order: {bst.inorder()}")
    
    delete_vals = [20, 30, 50]
    for val in delete_vals:
        print(f"\nDeleting {val}:")
        bst.delete(val)
        print(f"In-order after deletion: {bst.inorder()}")
    
    print("\nFinal BST structure:")
    bst.display()
    print()
    
    # Test with different insertion order
    print("=== Testing Different Insertion Order ===")
    bst2 = BinarySearchTree()
    elements2 = [1, 2, 3, 4, 5, 6, 7]  # Ascending order (worst case)
    
    print(f"Inserting in ascending order: {elements2}")
    for elem in elements2:
        bst2.insert(elem)
    
    print("Resulting BST (degenerate tree):")
    bst2.display()
    print(f"Height: {bst2.height()} (should be {len(elements2)-1} for degenerate)")
    print(f"Is balanced: {bst2.is_balanced()}")
    print()
    
    # Balanced BST
    bst3 = BinarySearchTree()
    balanced_elements = [4, 2, 6, 1, 3, 5, 7]  # More balanced insertion
    
    print(f"Inserting for balance: {balanced_elements}")
    for elem in balanced_elements:
        bst3.insert(elem)
    
    print("Resulting BST (more balanced):")
    bst3.display()
    print(f"Height: {bst3.height()}")
    print(f"Is balanced: {bst3.is_balanced()}")


if __name__ == "__main__":
    test_binary_search_tree()
