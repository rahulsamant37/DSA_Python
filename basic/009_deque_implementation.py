"""
009 - Deque (Double-ended Queue) Implementation
==============================================

This module implements Deque (Double-ended Queue) using different approaches:
- Array-based Deque (Circular)
- Linked List-based Deque
- Python collections.deque wrapper
- Deque applications and problems

Time Complexity:
- Add/Remove from both ends: O(1)
- Access by index: O(1) for array-based, O(n) for linked list
- Search: O(n)

Deque allows insertion and deletion from both ends efficiently.
Applications: Sliding window problems, palindrome checking, undo/redo operations
"""

from collections import deque as python_deque

class ArrayDeque:
    """Deque implementation using circular array"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.deque_size = 0
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.deque_size == 0
    
    def is_full(self):
        """Check if deque is full"""
        return self.deque_size == self.capacity
    
    def size(self):
        """Return current size of deque"""
        return self.deque_size
    
    def add_front(self, item):
        """Add item to front of deque"""
        if self.is_full():
            raise OverflowError("Deque overflow")
        
        self.front = (self.front - 1) % self.capacity
        self.data[self.front] = item
        self.deque_size += 1
    
    def add_rear(self, item):
        """Add item to rear of deque"""
        if self.is_full():
            raise OverflowError("Deque overflow")
        
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.deque_size += 1
    
    def remove_front(self):
        """Remove and return item from front"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.deque_size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return item from rear"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        self.rear = (self.rear - 1) % self.capacity
        item = self.data[self.rear]
        self.data[self.rear] = None
        self.deque_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.data[self.front]
    
    def peek_rear(self):
        """Peek at rear item without removing"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        rear_index = (self.rear - 1) % self.capacity
        return self.data[rear_index]
    
    def display(self):
        """Display deque contents"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        elements = []
        index = self.front
        for _ in range(self.deque_size):
            elements.append(str(self.data[index]))
            index = (index + 1) % self.capacity
        
        print("Deque: [" + ", ".join(elements) + "]")


class DequeNode:
    """Node class for linked list deque"""
    
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class LinkedListDeque:
    """Deque implementation using doubly linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.deque_size = 0
    
    def is_empty(self):
        """Check if deque is empty"""
        return self.front is None
    
    def size(self):
        """Return current size of deque"""
        return self.deque_size
    
    def add_front(self, item):
        """Add item to front of deque"""
        new_node = DequeNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        
        self.deque_size += 1
    
    def add_rear(self, item):
        """Add item to rear of deque"""
        new_node = DequeNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev = self.rear
            self.rear.next = new_node
            self.rear = new_node
        
        self.deque_size += 1
    
    def remove_front(self):
        """Remove and return item from front"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.front.data
        
        if self.deque_size == 1:
            self.front = self.rear = None
        else:
            self.front = self.front.next
            self.front.prev = None
        
        self.deque_size -= 1
        return item
    
    def remove_rear(self):
        """Remove and return item from rear"""
        if self.is_empty():
            raise IndexError("Deque underflow")
        
        item = self.rear.data
        
        if self.deque_size == 1:
            self.front = self.rear = None
        else:
            self.rear = self.rear.prev
            self.rear.next = None
        
        self.deque_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.front.data
    
    def peek_rear(self):
        """Peek at rear item without removing"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.rear.data
    
    def display(self):
        """Display deque contents"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        elements = []
        current = self.front
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("Deque: [" + ", ".join(elements) + "]")


class DequeApplications:
    """Various deque applications and algorithms"""
    
    @staticmethod
    def is_palindrome(s):
        """Check if string is palindrome using deque"""
        deque = LinkedListDeque()
        
        # Remove spaces and convert to lowercase
        cleaned = ''.join(char.lower() for char in s if char.isalnum())
        
        # Add all characters to deque
        for char in cleaned:
            deque.add_rear(char)
        
        # Compare characters from both ends
        while deque.size() > 1:
            if deque.remove_front() != deque.remove_rear():
                return False
        
        return True
    
    @staticmethod
    def sliding_window_maximum(arr, k):
        """Find maximum in each sliding window using deque"""
        if not arr or k <= 0:
            return []
        
        deque = ArrayDeque(len(arr))
        result = []
        
        for i in range(len(arr)):
            # Remove indices outside current window
            while not deque.is_empty() and deque.peek_front() <= i - k:
                deque.remove_front()
            
            # Remove indices with smaller values
            while not deque.is_empty() and arr[deque.peek_rear()] <= arr[i]:
                deque.remove_rear()
            
            deque.add_rear(i)
            
            # Add maximum to result if window is complete
            if i >= k - 1:
                result.append(arr[deque.peek_front()])
        
        return result
    
    @staticmethod
    def sliding_window_minimum(arr, k):
        """Find minimum in each sliding window using deque"""
        if not arr or k <= 0:
            return []
        
        deque = ArrayDeque(len(arr))
        result = []
        
        for i in range(len(arr)):
            # Remove indices outside current window
            while not deque.is_empty() and deque.peek_front() <= i - k:
                deque.remove_front()
            
            # Remove indices with larger values
            while not deque.is_empty() and arr[deque.peek_rear()] >= arr[i]:
                deque.remove_rear()
            
            deque.add_rear(i)
            
            # Add minimum to result if window is complete
            if i >= k - 1:
                result.append(arr[deque.peek_front()])
        
        return result
    
    @staticmethod
    def reverse_first_k_elements(queue_list, k):
        """Reverse first k elements of queue using deque"""
        if k <= 0 or k > len(queue_list):
            return queue_list
        
        deque = LinkedListDeque()
        result = queue_list.copy()
        
        # Add first k elements to deque
        for i in range(k):
            deque.add_front(result.pop(0))
        
        # Remove from front of deque and add to result
        while not deque.is_empty():
            result.append(deque.remove_front())
        
        return result
    
    @staticmethod
    def first_negative_in_window(arr, k):
        """Find first negative number in each window of size k"""
        if not arr or k <= 0:
            return []
        
        deque = ArrayDeque(len(arr))
        result = []
        
        for i in range(len(arr)):
            # Remove indices outside current window
            while not deque.is_empty() and deque.peek_front() <= i - k:
                deque.remove_front()
            
            # Add current index if element is negative
            if arr[i] < 0:
                deque.add_rear(i)
            
            # Add result if window is complete
            if i >= k - 1:
                if deque.is_empty():
                    result.append(0)  # No negative number
                else:
                    result.append(arr[deque.peek_front()])
        
        return result
    
    @staticmethod
    def maximum_sum_subarray_size_k(arr, k):
        """Find maximum sum of subarray of size k using deque for optimization"""
        if not arr or k <= 0 or k > len(arr):
            return 0
        
        # Calculate sum of first window
        window_sum = sum(arr[:k])
        max_sum = window_sum
        
        # Slide the window
        for i in range(k, len(arr)):
            window_sum = window_sum - arr[i - k] + arr[i]
            max_sum = max(max_sum, window_sum)
        
        return max_sum
    
    @staticmethod
    def interleave_queue(queue_list):
        """Interleave first and second half of queue using deque"""
        if len(queue_list) % 2 != 0:
            raise ValueError("Queue length must be even")
        
        n = len(queue_list) // 2
        deque = LinkedListDeque()
        result = []
        
        # Add first half to deque
        for i in range(n):
            deque.add_rear(queue_list[i])
        
        # Interleave
        for i in range(n, len(queue_list)):
            result.append(deque.remove_front())
            result.append(queue_list[i])
        
        return result


class PythonDequeWrapper:
    """Wrapper for Python's collections.deque with additional methods"""
    
    def __init__(self, maxlen=None):
        self.deque = python_deque(maxlen=maxlen)
    
    def add_front(self, item):
        """Add item to front"""
        self.deque.appendleft(item)
    
    def add_rear(self, item):
        """Add item to rear"""
        self.deque.append(item)
    
    def remove_front(self):
        """Remove item from front"""
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque.popleft()
    
    def remove_rear(self):
        """Remove item from rear"""
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque.pop()
    
    def peek_front(self):
        """Peek at front item"""
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque[0]
    
    def peek_rear(self):
        """Peek at rear item"""
        if not self.deque:
            raise IndexError("Deque is empty")
        return self.deque[-1]
    
    def is_empty(self):
        """Check if deque is empty"""
        return len(self.deque) == 0
    
    def size(self):
        """Return size of deque"""
        return len(self.deque)
    
    def display(self):
        """Display deque contents"""
        print(f"Deque: {list(self.deque)}")


def test_deque_implementations():
    """Test all deque implementations"""
    print("=== Testing Deque Implementations ===\n")
    
    # Test Array Deque
    print("=== Array-based Deque ===")
    array_deque = ArrayDeque(6)
    
    print("Adding elements to both ends:")
    array_deque.add_rear(1)
    array_deque.add_rear(2)
    array_deque.add_front(0)
    array_deque.add_front(-1)
    array_deque.display()
    print(f"Size: {array_deque.size()}")
    print(f"Front: {array_deque.peek_front()}, Rear: {array_deque.peek_rear()}")
    print()
    
    print("Removing from both ends:")
    print(f"Removed from front: {array_deque.remove_front()}")
    print(f"Removed from rear: {array_deque.remove_rear()}")
    array_deque.display()
    print()
    
    # Test Linked List Deque
    print("=== Linked List-based Deque ===")
    ll_deque = LinkedListDeque()
    
    print("Adding elements: A, B, C, D")
    ll_deque.add_rear('A')
    ll_deque.add_rear('B')
    ll_deque.add_front('C')
    ll_deque.add_front('D')
    ll_deque.display()
    print(f"Size: {ll_deque.size()}")
    print()
    
    # Test Python Deque Wrapper
    print("=== Python collections.deque Wrapper ===")
    py_deque = PythonDequeWrapper()
    
    print("Adding elements: 10, 20, 30, 40")
    py_deque.add_rear(10)
    py_deque.add_rear(20)
    py_deque.add_front(30)
    py_deque.add_front(40)
    py_deque.display()
    print()


def test_deque_applications():
    """Test deque applications"""
    print("=== Testing Deque Applications ===\n")
    
    apps = DequeApplications()
    
    # Test palindrome check
    print("=== Palindrome Check ===")
    test_strings = [
        "racecar",
        "A man a plan a canal Panama",
        "race a car",
        "hello",
        "Madam"
    ]
    
    for s in test_strings:
        is_pal = apps.is_palindrome(s)
        print(f"'{s}' is {'a palindrome' if is_pal else 'not a palindrome'}")
    print()
    
    # Test sliding window maximum
    print("=== Sliding Window Maximum ===")
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    max_values = apps.sliding_window_maximum(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Maximum in each window: {max_values}")
    print()
    
    # Test sliding window minimum
    print("=== Sliding Window Minimum ===")
    min_values = apps.sliding_window_minimum(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Minimum in each window: {min_values}")
    print()
    
    # Test first negative in window
    print("=== First Negative in Window ===")
    arr_with_negatives = [12, -1, -7, 8, -15, 30, 16, 28]
    k = 3
    first_negatives = apps.first_negative_in_window(arr_with_negatives, k)
    print(f"Array: {arr_with_negatives}")
    print(f"Window size: {k}")
    print(f"First negative in each window: {first_negatives}")
    print()
    
    # Test reverse first k elements
    print("=== Reverse First K Elements ===")
    queue = [1, 2, 3, 4, 5, 6, 7, 8]
    k = 4
    reversed_queue = apps.reverse_first_k_elements(queue, k)
    print(f"Original queue: {queue}")
    print(f"After reversing first {k} elements: {reversed_queue}")
    print()
    
    # Test interleave queue
    print("=== Interleave Queue ===")
    queue = [1, 2, 3, 4, 5, 6, 7, 8]
    interleaved = apps.interleave_queue(queue)
    print(f"Original queue: {queue}")
    print(f"Interleaved queue: {interleaved}")
    print()
    
    # Test maximum sum subarray
    print("=== Maximum Sum Subarray of Size K ===")
    arr = [1, 4, 2, 9, 7, 8, 3, 6]
    k = 3
    max_sum = apps.maximum_sum_subarray_size_k(arr, k)
    print(f"Array: {arr}")
    print(f"Subarray size: {k}")
    print(f"Maximum sum: {max_sum}")


def performance_comparison():
    """Compare performance of different deque implementations"""
    print("=== Performance Comparison ===\n")
    
    import time
    
    n = 10000
    
    # Array Deque
    start_time = time.time()
    array_deque = ArrayDeque(n)
    for i in range(n // 2):
        array_deque.add_front(i)
        array_deque.add_rear(i)
    array_time = time.time() - start_time
    
    # Linked List Deque
    start_time = time.time()
    ll_deque = LinkedListDeque()
    for i in range(n // 2):
        ll_deque.add_front(i)
        ll_deque.add_rear(i)
    ll_time = time.time() - start_time
    
    # Python Deque
    start_time = time.time()
    py_deque = python_deque()
    for i in range(n // 2):
        py_deque.appendleft(i)
        py_deque.append(i)
    py_time = time.time() - start_time
    
    print(f"Operations: {n} insertions ({n//2} from each end)")
    print(f"Array Deque: {array_time:.6f} seconds")
    print(f"Linked List Deque: {ll_time:.6f} seconds")
    print(f"Python Deque: {py_time:.6f} seconds")
    print(f"Python deque is {array_time/py_time:.2f}x faster than array deque")
    print(f"Python deque is {ll_time/py_time:.2f}x faster than linked list deque")


if __name__ == "__main__":
    test_deque_implementations()
    print("\n" + "="*50 + "\n")
    test_deque_applications()
    print("\n" + "="*50 + "\n")
    performance_comparison()
