"""
deque rotation operations - Rotating elements left and right

deque.rotate() shifts elements efficiently in O(k) time where k is the rotation count.
Useful for circular buffers, cyclic operations, and certain algorithmic patterns.
"""

from collections import deque

def basic_rotation():
    """Demonstrates basic rotation operations"""
    
    print("--- Basic Rotation Operations ---")
    
    # Create sample deque
    dq = deque([1, 2, 3, 4, 5])
    print(f"Original deque: {dq}")
    
    # 1. Rotate right (positive values)
    print("\n1. Rotating right (positive values):")
    dq_copy = dq.copy()
    
    dq_copy.rotate(1)
    print(f"rotate(1):  {dq_copy}")
    
    dq_copy = dq.copy()
    dq_copy.rotate(2)
    print(f"rotate(2):  {dq_copy}")
    
    dq_copy = dq.copy()
    dq_copy.rotate(3)
    print(f"rotate(3):  {dq_copy}")
    
    # 2. Rotate left (negative values)
    print("\n2. Rotating left (negative values):")
    dq_copy = dq.copy()
    dq_copy.rotate(-1)
    print(f"rotate(-1): {dq_copy}")
    
    dq_copy = dq.copy()
    dq_copy.rotate(-2)
    print(f"rotate(-2): {dq_copy}")
    
    dq_copy = dq.copy()
    dq_copy.rotate(-3)
    print(f"rotate(-3): {dq_copy}")
    
    # 3. Full rotation
    print("\n3. Full rotations:")
    dq_copy = dq.copy()
    length = len(dq_copy)
    
    dq_copy.rotate(length)
    print(f"rotate({length}):  {dq_copy} (full rotation right)")
    
    dq_copy.rotate(-length)
    print(f"rotate(-{length}): {dq_copy} (full rotation left)")
    
    # 4. Zero rotation
    print("\n4. Zero rotation:")
    dq_copy = dq.copy()
    dq_copy.rotate(0)
    print(f"rotate(0):  {dq_copy} (no change)")
    print()

def rotation_properties():
    """Demonstrates properties and edge cases of rotation"""
    
    print("--- Rotation Properties ---")
    
    dq = deque(['a', 'b', 'c', 'd'])
    print(f"Original: {dq}")
    
    # 1. Rotation beyond length
    print("\n1. Rotation beyond deque length:")
    dq_copy = dq.copy()
    dq_copy.rotate(6)  # 6 % 4 = 2, same as rotate(2)
    print(f"rotate(6): {dq_copy} (equivalent to rotate(2))")
    
    dq_copy = dq.copy()
    dq_copy.rotate(-6)  # -6 % 4 = -2, same as rotate(-2)
    print(f"rotate(-6): {dq_copy} (equivalent to rotate(-2))")
    
    # 2. Empty deque rotation
    print("\n2. Empty deque rotation:")
    empty_dq = deque()
    empty_dq.rotate(5)
    print(f"Empty deque after rotate(5): {empty_dq}")
    
    # 3. Single element rotation
    print("\n3. Single element rotation:")
    single_dq = deque([42])
    print(f"Before rotation: {single_dq}")
    single_dq.rotate(3)
    print(f"After rotate(3): {single_dq}")
    
    # 4. Understanding the direction
    print("\n4. Understanding rotation direction:")
    dq = deque([1, 2, 3, 4, 5])
    print(f"Original: {dq}")
    print("Think of it as: positive = move right edge to left, negative = move left edge to right")
    
    dq_right = dq.copy()
    dq_right.rotate(1)
    print(f"rotate(1): {dq_right} <- last element moved to front")
    
    dq_left = dq.copy()
    dq_left.rotate(-1)
    print(f"rotate(-1): {dq_left} <- first element moved to end")
    print()

def performance_comparison():
    """Compares deque rotation with manual list rotation"""
    
    print("--- Performance Comparison ---")
    
    import time
    
    # Create large datasets
    size = 100000
    large_deque = deque(range(size))
    large_list = list(range(size))
    
    # Test deque rotation
    start_time = time.time()
    large_deque.rotate(1000)
    deque_time = time.time() - start_time
    
    # Test manual list rotation (inefficient)
    start_time = time.time()
    k = 1000 % len(large_list)
    rotated_list = large_list[-k:] + large_list[:-k]
    list_time = time.time() - start_time
    
    print(f"Dataset size: {size:,} elements")
    print(f"Rotation count: 1000")
    print(f"Deque rotation time: {deque_time:.6f} seconds")
    print(f"List rotation time: {list_time:.6f} seconds")
    print(f"Deque is {list_time/deque_time:.1f}x faster")
    print()

def dsa_use_cases():
    """DSA applications of deque rotation"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Circular buffer implementation
    print("1. Circular Buffer:")
    class CircularBuffer:
        def __init__(self, size):
            self.buffer = deque(maxlen=size)
            self.size = size
        
        def add(self, item):
            """Add item to buffer"""
            self.buffer.append(item)
        
        def get_all(self):
            """Get all items in order"""
            return list(self.buffer)
        
        def rotate_view(self, steps):
            """Rotate the view of buffer without changing data"""
            view = deque(self.buffer)
            view.rotate(steps)
            return list(view)
        
        def __str__(self):
            return f"CircularBuffer({list(self.buffer)})"
    
    buffer = CircularBuffer(5)
    print("Adding elements to circular buffer:")
    for i in range(8):
        buffer.add(i)
        print(f"Add {i}: {buffer}")
    
    print("\nDifferent views of the buffer:")
    print(f"Normal view: {buffer.get_all()}")
    print(f"Rotated +1: {buffer.rotate_view(1)}")
    print(f"Rotated -2: {buffer.rotate_view(-2)}")
    print()
    
    # Use Case 2: Caesar cipher implementation
    print("2. Caesar Cipher:")
    def caesar_cipher(text, shift):
        """
        Implement Caesar cipher using deque rotation.
        Time Complexity: O(n), Space Complexity: O(1) for alphabet
        """
        alphabet = deque('abcdefghijklmnopqrstuvwxyz')
        shifted_alphabet = deque(alphabet)
        shifted_alphabet.rotate(-shift)  # Negative for forward shift
        
        # Create translation table
        translation = str.maketrans(''.join(alphabet), ''.join(shifted_alphabet))
        
        return text.lower().translate(translation)
    
    def caesar_decrypt(text, shift):
        """Decrypt Caesar cipher"""
        return caesar_cipher(text, -shift)
    
    message = "hello world"
    shift = 3
    
    encrypted = caesar_cipher(message, shift)
    decrypted = caesar_decrypt(encrypted, shift)
    
    print(f"Original: '{message}'")
    print(f"Encrypted (shift {shift}): '{encrypted}'")
    print(f"Decrypted: '{decrypted}'")
    print()
    
    # Use Case 3: Array rotation problems
    print("3. Array Rotation Problem:")
    def rotate_array(nums, k):
        """
        Rotate array to the right by k steps.
        Time Complexity: O(k), Space Complexity: O(n)
        """
        dq = deque(nums)
        dq.rotate(k)
        return list(dq)
    
    def rotate_array_in_place(nums, k):
        """
        Rotate array in place (modifies original list).
        Uses deque for efficient rotation then copies back.
        """
        if not nums or k == 0:
            return
        
        dq = deque(nums)
        dq.rotate(k % len(nums))
        nums[:] = dq
    
    original = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    
    rotated = rotate_array(original, k)
    print(f"Original array: {original}")
    print(f"Rotated by {k}: {rotated}")
    
    # In-place rotation
    test_array = original.copy()
    rotate_array_in_place(test_array, k)
    print(f"In-place rotation: {test_array}")
    print()
    
    # Use Case 4: Sliding window with rotation
    print("4. Sliding Window with Rotation:")
    def sliding_window_with_rotation(arr, window_size):
        """
        Generate all possible sliding windows using rotation.
        Demonstrates how rotation can be used for window operations.
        """
        if len(arr) < window_size:
            return []
        
        dq = deque(arr)
        windows = []
        
        for i in range(len(arr) - window_size + 1):
            # Current window is the first 'window_size' elements
            window = list(dq)[:window_size]
            windows.append(window)
            
            # Rotate to get next window position
            if i < len(arr) - window_size:
                dq.rotate(-1)  # Move first element to end
        
        return windows
    
    arr = [1, 2, 3, 4, 5]
    window_size = 3
    windows = sliding_window_with_rotation(arr, window_size)
    
    print(f"Array: {arr}")
    print(f"Window size: {window_size}")
    print("All sliding windows:")
    for i, window in enumerate(windows):
        print(f"  Window {i+1}: {window}")

if __name__ == "__main__":
    basic_rotation()
    rotation_properties()
    performance_comparison()
    dsa_use_cases()
