"""
deque append operations - Adding elements to both ends

deque.append() and deque.appendleft() provide O(1) insertion at both ends.
Essential for implementing queues, stacks, and double-ended data structures.
"""

from collections import deque

def append_operations():
    """Demonstrates append and appendleft operations"""
    
    print("--- Append Operations ---")
    
    # Start with empty deque
    dq = deque()
    print(f"Initial deque: {dq}")
    
    # 1. append() - add to right end
    print("\n1. append() - adding to right end:")
    dq.append(1)
    print(f"After append(1): {dq}")
    dq.append(2)
    print(f"After append(2): {dq}")
    dq.append(3)
    print(f"After append(3): {dq}")
    
    # 2. appendleft() - add to left end
    print("\n2. appendleft() - adding to left end:")
    dq.appendleft(0)
    print(f"After appendleft(0): {dq}")
    dq.appendleft(-1)
    print(f"After appendleft(-1): {dq}")
    
    print(f"\nFinal deque: {dq}")
    print("Order: left -> right")
    print()

def bounded_deque_append():
    """Demonstrates append behavior with bounded deque"""
    
    print("--- Bounded Deque Append Behavior ---")
    
    # Create bounded deque
    bounded_dq = deque([1, 2, 3], maxlen=5)
    print(f"Initial bounded deque (maxlen=5): {bounded_dq}")
    
    # Add elements normally
    print("\nAdding elements within capacity:")
    bounded_dq.append(4)
    print(f"After append(4): {bounded_dq}")
    bounded_dq.append(5)
    print(f"After append(5): {bounded_dq}")
    
    # Exceed capacity - elements are removed from opposite end
    print("\nExceeding capacity with append:")
    bounded_dq.append(6)
    print(f"After append(6): {bounded_dq}")
    print("Note: Element 1 was removed from left")
    
    bounded_dq.append(7)
    print(f"After append(7): {bounded_dq}")
    print("Note: Element 2 was removed from left")
    
    # Exceed capacity with appendleft
    print("\nExceeding capacity with appendleft:")
    bounded_dq.appendleft(0)
    print(f"After appendleft(0): {bounded_dq}")
    print("Note: Element 7 was removed from right")
    print()

def extend_operations():
    """Demonstrates extend and extendleft operations"""
    
    print("--- Extend Operations ---")
    
    dq = deque([2, 3])
    print(f"Initial deque: {dq}")
    
    # 1. extend() - add multiple elements to right
    print("\n1. extend() - adding multiple elements to right:")
    dq.extend([4, 5, 6])
    print(f"After extend([4, 5, 6]): {dq}")
    
    # 2. extendleft() - add multiple elements to left (reversed!)
    print("\n2. extendleft() - adding multiple elements to left:")
    dq.extendleft([1, 0, -1])
    print(f"After extendleft([1, 0, -1]): {dq}")
    print("Note: Elements are added one by one from left, so order is reversed!")
    
    # Demonstrate the reversal
    print("\nDemonstrating extendleft reversal:")
    test_dq = deque(['middle'])
    print(f"Starting with: {test_dq}")
    test_dq.extendleft(['a', 'b', 'c'])
    print(f"After extendleft(['a', 'b', 'c']): {test_dq}")
    print("Expected order: ['c', 'b', 'a', 'middle']")
    print()

def dsa_use_cases():
    """DSA applications of append operations"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Implement a queue
    print("1. Queue Implementation:")
    class Queue:
        def __init__(self):
            self.items = deque()
        
        def enqueue(self, item):
            """Add item to rear of queue - O(1)"""
            self.items.append(item)
        
        def dequeue(self):
            """Remove item from front of queue - O(1)"""
            if self.items:
                return self.items.popleft()
            raise IndexError("Queue is empty")
        
        def peek(self):
            """Look at front item without removing - O(1)"""
            if self.items:
                return self.items[0]
            raise IndexError("Queue is empty")
        
        def is_empty(self):
            return len(self.items) == 0
        
        def size(self):
            return len(self.items)
        
        def __str__(self):
            return f"Queue({list(self.items)})"
    
    queue = Queue()
    print("Creating queue and adding elements:")
    for i in range(1, 4):
        queue.enqueue(i)
        print(f"Enqueue {i}: {queue}")
    
    print("\nRemoving elements:")
    while not queue.is_empty():
        item = queue.dequeue()
        print(f"Dequeue {item}: {queue}")
    print()
    
    # Use Case 2: Palindrome checker using deque
    print("2. Palindrome Checker:")
    def is_palindrome(s):
        """
        Check if string is palindrome using deque.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        # Clean string - remove non-alphanumeric and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        dq = deque(cleaned)
        
        while len(dq) > 1:
            if dq.popleft() != dq.pop():
                return False
        return True
    
    test_strings = [
        "A man a plan a canal Panama",
        "race a car",
        "hello",
        "madam",
        "Madam, I'm Adam"
    ]
    
    for s in test_strings:
        result = is_palindrome(s)
        print(f"'{s}' is palindrome: {result}")
    print()
    
    # Use Case 3: Sliding window maximum using deque
    print("3. Sliding Window Maximum:")
    def sliding_window_maximum(nums, k):
        """
        Find maximum in each sliding window of size k.
        Time Complexity: O(n), Space Complexity: O(k)
        """
        if not nums or k == 0:
            return []
        
        dq = deque()  # Store indices
        result = []
        
        for i in range(len(nums)):
            # Remove indices outside current window
            while dq and dq[0] <= i - k:
                dq.popleft()
            
            # Remove indices of smaller elements (they can't be maximum)
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            
            dq.append(i)
            
            # Add maximum of current window to result
            if i >= k - 1:
                result.append(nums[dq[0]])
        
        return result
    
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    result = sliding_window_maximum(nums, k)
    print(f"Array: {nums}")
    print(f"Window size: {k}")
    print(f"Sliding window maximums: {result}")
    
    # Show the windows
    print("Windows:")
    for i in range(len(nums) - k + 1):
        window = nums[i:i+k]
        print(f"  {window} -> max = {max(window)}")

if __name__ == "__main__":
    append_operations()
    bounded_deque_append()
    extend_operations()
    dsa_use_cases()
