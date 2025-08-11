"""
deque pop operations - Removing elements from both ends

deque.pop() and deque.popleft() provide O(1) removal from both ends.
Essential for implementing stacks, queues, and algorithms requiring efficient end operations.
"""

from collections import deque

def pop_operations():
    """Demonstrates pop and popleft operations"""
    
    print("--- Pop Operations ---")
    
    # Create deque with sample data
    dq = deque([1, 2, 3, 4, 5])
    print(f"Initial deque: {dq}")
    
    # 1. pop() - remove from right end
    print("\n1. pop() - removing from right end:")
    while len(dq) > 2:
        removed = dq.pop()
        print(f"Removed {removed}: {dq}")
    
    # 2. popleft() - remove from left end
    print("\n2. popleft() - removing from left end:")
    while dq:
        removed = dq.popleft()
        print(f"Removed {removed}: {dq}")
    
    # 3. Handling empty deque
    print("\n3. Attempting to pop from empty deque:")
    try:
        dq.pop()
    except IndexError as e:
        print(f"pop() on empty deque: {e}")
    
    try:
        dq.popleft()
    except IndexError as e:
        print(f"popleft() on empty deque: {e}")
    print()

def safe_pop_operations():
    """Demonstrates safe pop operations with error handling"""
    
    print("--- Safe Pop Operations ---")
    
    def safe_pop(dq, from_left=False):
        """Safely pop from deque, return None if empty"""
        try:
            if from_left:
                return dq.popleft()
            else:
                return dq.pop()
        except IndexError:
            return None
    
    dq = deque([1, 2, 3])
    print(f"Initial deque: {dq}")
    
    # Pop all elements safely
    print("\nSafe popping from right:")
    while True:
        item = safe_pop(dq)
        if item is None:
            print("Deque is empty")
            break
        print(f"Popped {item}: {dq}")
    
    # Refill and pop from left
    dq.extend([10, 20, 30])
    print(f"\nRefilled deque: {dq}")
    print("Safe popping from left:")
    while True:
        item = safe_pop(dq, from_left=True)
        if item is None:
            print("Deque is empty")
            break
        print(f"Popped {item}: {dq}")
    print()

def bounded_deque_pop():
    """Demonstrates pop behavior with bounded deque"""
    
    print("--- Bounded Deque Pop Behavior ---")
    
    # Create bounded deque at capacity
    bounded_dq = deque([1, 2, 3, 4, 5], maxlen=5)
    print(f"Initial bounded deque (maxlen=5): {bounded_dq}")
    
    # Pop operations work normally
    print("\nPopping from bounded deque:")
    item = bounded_dq.pop()
    print(f"After pop(): {bounded_dq} (removed {item})")
    
    item = bounded_dq.popleft()
    print(f"After popleft(): {bounded_dq} (removed {item})")
    
    # Now we can add more elements
    print("\nAdding elements after popping:")
    bounded_dq.append(6)
    bounded_dq.appendleft(0)
    print(f"After append(6) and appendleft(0): {bounded_dq}")
    print()

def dsa_use_cases():
    """DSA applications of pop operations"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Stack implementation
    print("1. Stack Implementation:")
    class Stack:
        def __init__(self):
            self.items = deque()
        
        def push(self, item):
            """Push item onto stack - O(1)"""
            self.items.append(item)
        
        def pop(self):
            """Pop item from stack - O(1)"""
            if self.items:
                return self.items.pop()
            raise IndexError("Stack is empty")
        
        def peek(self):
            """Look at top item without removing - O(1)"""
            if self.items:
                return self.items[-1]
            raise IndexError("Stack is empty")
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
        
        def __str__(self):
            return f"Stack({list(self.items)})"
    
    stack = Stack()
    print("Creating stack and pushing elements:")
    for i in range(1, 5):
        stack.push(i)
        print(f"Push {i}: {stack}")
    
    print("\nPopping elements (LIFO):")
    while not stack.is_empty():
        item = stack.pop()
        print(f"Pop {item}: {stack}")
    print()
    
    # Use Case 2: Valid parentheses checker
    print("2. Valid Parentheses Checker:")
    def is_valid_parentheses(s):
        """
        Check if parentheses are properly balanced.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        stack = deque()
        mapping = {')': '(', '}': '{', ']': '['}
        
        for char in s:
            if char in mapping:  # Closing bracket
                if not stack or stack.pop() != mapping[char]:
                    return False
            else:  # Opening bracket
                stack.append(char)
        
        return len(stack) == 0
    
    test_cases = [
        "()",
        "()[]{}",
        "(]",
        "([)]",
        "{[]}",
        "((()))",
        "())",
        "((("
    ]
    
    for test in test_cases:
        result = is_valid_parentheses(test)
        print(f"'{test}' is valid: {result}")
    print()
    
    # Use Case 3: Reverse a string/list using deque
    print("3. Reverse Using Deque:")
    def reverse_string(s):
        """
        Reverse a string using deque.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        dq = deque(s)
        reversed_chars = []
        
        while dq:
            reversed_chars.append(dq.pop())  # Pop from right
        
        return ''.join(reversed_chars)
    
    test_string = "algorithm"
    reversed_string = reverse_string(test_string)
    print(f"Original: '{test_string}'")
    print(f"Reversed: '{reversed_string}'")
    print()
    
    # Use Case 4: Monotonic deque for sliding window problems
    print("4. Monotonic Deque - Sliding Window Minimum:")
    def sliding_window_minimum(nums, k):
        """
        Find minimum in each sliding window of size k using monotonic deque.
        Time Complexity: O(n), Space Complexity: O(k)
        """
        if not nums or k == 0:
            return []
        
        dq = deque()  # Store indices, maintain increasing order of values
        result = []
        
        for i in range(len(nums)):
            # Remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Maintain monotonic property (remove larger elements)
            while dq and nums[dq[-1]] >= nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add minimum of current window to result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_minimum(nums, k)
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print(f"Sliding window minimums: {result}")
    
    # Show the windows
    print("Windows:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        print(f"  {window} -> min = {min(window)}")

if __name__ == "__main__":
    pop_operations()
    safe_pop_operations()
    bounded_deque_pop()
    dsa_use_cases()
