"""
Creating a deque - Double-ended queue initialization

deque (double-ended queue) provides O(1) append and pop operations from both ends.
Essential for algorithms requiring efficient operations at both ends like BFS, sliding window.
"""

from collections import deque

def create_deque_examples():
    """Demonstrates different ways to create a deque object"""
    
    # 1. Create empty deque
    print("1. Creating empty deque:")
    empty_deque = deque()
    print(f"Empty deque: {empty_deque}")
    print(f"Type: {type(empty_deque)}")
    print()
    
    # 2. Create from iterable
    print("2. Creating deque from iterables:")
    
    # From list
    list_deque = deque([1, 2, 3, 4, 5])
    print(f"From list [1,2,3,4,5]: {list_deque}")
    
    # From string
    string_deque = deque("hello")
    print(f"From string 'hello': {string_deque}")
    
    # From range
    range_deque = deque(range(5))
    print(f"From range(5): {range_deque}")
    print()
    
    # 3. Create with maxlen (bounded deque)
    print("3. Creating bounded deque with maxlen:")
    bounded_deque = deque([1, 2, 3], maxlen=5)
    print(f"Bounded deque (maxlen=5): {bounded_deque}")
    print(f"Max length: {bounded_deque.maxlen}")
    
    # Adding elements to bounded deque
    bounded_deque.append(4)
    bounded_deque.append(5)
    print(f"After adding 4, 5: {bounded_deque}")
    
    bounded_deque.append(6)  # This will remove element from left
    print(f"After adding 6: {bounded_deque}")
    print("Note: Oldest element (1) was automatically removed")
    print()
    
    # 4. Create deque from another deque
    print("4. Creating deque from another deque:")
    original = deque([1, 2, 3])
    copied = deque(original)
    print(f"Original: {original}")
    print(f"Copy: {copied}")
    print(f"Are they the same object? {original is copied}")
    print()

def basic_properties():
    """Demonstrates basic properties and methods for inspection"""
    
    print("--- Basic Properties ---")
    
    dq = deque([1, 2, 3, 4, 5], maxlen=10)
    
    # Length
    print(f"Deque: {dq}")
    print(f"Length: {len(dq)}")
    print(f"Max length: {dq.maxlen}")
    print(f"Is empty: {len(dq) == 0}")
    print()
    
    # Accessing elements (note: no random access like lists)
    print("Element access:")
    print(f"First element (dq[0]): {dq[0]}")
    print(f"Last element (dq[-1]): {dq[-1]}")
    print(f"Second element (dq[1]): {dq[1]}")
    print()
    
    # Iteration
    print("Iteration:")
    print("Forward:", end=" ")
    for item in dq:
        print(item, end=" ")
    print()
    
    print("Reverse:", end=" ")
    for item in reversed(dq):
        print(item, end=" ")
    print()
    print()

def dsa_use_case():
    """Common DSA use case: BFS implementation"""
    
    print("--- DSA Use Case: BFS on Binary Tree ---")
    
    class TreeNode:
        def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
        
        def __repr__(self):
            return f"TreeNode({self.val})"
    
    def level_order_traversal(root):
        """
        Perform level-order (BFS) traversal of binary tree.
        Time Complexity: O(n), Space Complexity: O(w) where w is max width
        """
        if not root:
            return []
        
        result = []
        queue = deque([root])  # deque is perfect for BFS queue
        
        while queue:
            level_size = len(queue)
            level_nodes = []
            
            for _ in range(level_size):
                node = queue.popleft()  # O(1) operation
                level_nodes.append(node.val)
                
                if node.left:
                    queue.append(node.left)   # O(1) operation
                if node.right:
                    queue.append(node.right)  # O(1) operation
            
            result.append(level_nodes)
        
        return result
    
    # Create a sample binary tree:
    #       3
    #      / \
    #     9   20
    #        /  \
    #       15   7
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(7)
    
    result = level_order_traversal(root)
    print("Binary tree level-order traversal:")
    for i, level in enumerate(result):
        print(f"Level {i}: {level}")
    
    print("\nWhy deque is better than list for BFS:")
    print("- queue.popleft() is O(1) vs list.pop(0) which is O(n)")
    print("- queue.append() is O(1) same as list.append()")
    print("- Better memory efficiency for queue operations")

if __name__ == "__main__":
    create_deque_examples()
    basic_properties()
    dsa_use_case()
