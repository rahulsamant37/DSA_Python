"""
Binary Search Pattern

Binary Search is used to search a sorted collection efficiently. The key insight 
behind Binary Search is that we can eliminate half of the search space in each 
iteration, leading to O(log n) time complexity.

Time Complexity: O(log n)
Space Complexity: O(1) for iterative, O(log n) for recursive

Common Problems:
- Binary Search
- Search in Sorted Infinite Array
- Find Peak Element
- Search in Rotated Sorted Array
- Search for Range
- Search Insert Position
"""

def binary_search(arr, target):
    """
    Search for target in sorted array.
    
    Args:
        arr: sorted array
        target: target value to search
    
    Returns:
        index of target if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_ceiling_of_number(arr, key):
    """
    Find the smallest element in array that is greater than or equal to key.
    
    Args:
        arr: sorted array
        key: target key
    
    Returns:
        index of ceiling element, -1 if not found
    """
    if key > arr[-1]:  # key is bigger than the biggest element
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] >= key:
            if mid == 0 or arr[mid - 1] < key:
                return mid
            right = mid - 1
        else:
            left = mid + 1
    
    return -1


def search_floor_of_number(arr, key):
    """
    Find the largest element in array that is smaller than or equal to key.
    
    Args:
        arr: sorted array
        key: target key
    
    Returns:
        index of floor element, -1 if not found
    """
    if key < arr[0]:  # key is smaller than the smallest element
        return -1
    
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] <= key:
            if mid == len(arr) - 1 or arr[mid + 1] > key:
                return mid
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_next_letter(letters, key):
    """
    Find the smallest letter in array that is greater than key.
    
    Args:
        letters: sorted array of lowercase letters
        key: target key
    
    Returns:
        next letter greater than key
    """
    n = len(letters)
    
    # If key is greater than or equal to the last letter, wrap around
    if key >= letters[n - 1]:
        return letters[0]
    
    left, right = 0, n - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if letters[mid] > key:
            if mid == 0 or letters[mid - 1] <= key:
                return letters[mid]
            right = mid - 1
        else:
            left = mid + 1
    
    return letters[0]


def find_range(arr, key):
    """
    Find the range (start and end indices) of target in sorted array.
    
    Args:
        arr: sorted array with duplicates
        key: target key
    
    Returns:
        [start_index, end_index] of key, [-1, -1] if not found
    """
    result = [-1, -1]
    
    # Find first occurrence
    result[0] = binary_search_first(arr, key)
    
    if result[0] != -1:  # no need to search if key is not present
        result[1] = binary_search_last(arr, key)
    
    return result


def binary_search_first(arr, key):
    """Find first occurrence of key in sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            if mid == 0 or arr[mid - 1] != key:
                return mid
            right = mid - 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def binary_search_last(arr, key):
    """Find last occurrence of key in sorted array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            if mid == len(arr) - 1 or arr[mid + 1] != key:
                return mid
            left = mid + 1
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_in_infinite_array(reader, key):
    """
    Search in a sorted infinite array (or very large array).
    
    Args:
        reader: array reader interface
        key: target key
    
    Returns:
        index of key if found, -1 otherwise
    """
    # Find bounds for binary search
    left, right = 0, 1
    
    while reader.get(right) < key:
        left = right
        right *= 2  # increase to double the bounds
    
    # Now do binary search
    while left <= right:
        mid = left + (right - left) // 2
        
        if reader.get(mid) == key:
            return mid
        elif reader.get(mid) < key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def find_peak_element(arr):
    """
    Find a peak element in array (element greater than its neighbors).
    
    Args:
        arr: array of integers
    
    Returns:
        index of a peak element
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left


def search_in_rotated_array(arr, key):
    """
    Search in a rotated sorted array.
    
    Args:
        arr: rotated sorted array
        key: target key
    
    Returns:
        index of key if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
        
        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] <= key < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half is sorted
        else:
            if arr[mid] < key <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1


def find_rotation_count(arr):
    """
    Find the number of rotations in a sorted rotated array.
    
    Args:
        arr: rotated sorted array
    
    Returns:
        number of rotations
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        # If mid element is greater than the last element,
        # then the rotation point lies in second half
        if arr[mid] > arr[right]:
            left = mid + 1
        # If mid element is less than the last element,
        # then the rotation point lies in first half (including mid)
        elif arr[mid] < arr[right]:
            right = mid
        # If mid element equals the last element, we can't determine
        # which half has the rotation point, so reduce search space
        else:
            right -= 1
    
    return left


def search_bitonic_array(arr, key):
    """
    Search in a bitonic array (first increasing then decreasing).
    
    Args:
        arr: bitonic array
        key: target key
    
    Returns:
        index of key if found, -1 otherwise
    """
    max_index = find_max_in_bitonic_array(arr)
    key_index = binary_search(arr[:max_index + 1], key)
    
    if key_index != -1:
        return key_index
    
    return binary_search_descending(arr[max_index:], key) + max_index


def find_max_in_bitonic_array(arr):
    """Find the maximum element in a bitonic array."""
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    
    return left


def binary_search_descending(arr, key):
    """Binary search in descending order array."""
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1


def search_insert_position(arr, target):
    """
    Find the index to insert target in sorted array to maintain order.
    
    Args:
        arr: sorted array
        target: target value
    
    Returns:
        index where target should be inserted
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return left


def find_minimum_in_rotated_array(arr):
    """
    Find minimum element in rotated sorted array.
    
    Args:
        arr: rotated sorted array
    
    Returns:
        minimum element
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = left + (right - left) // 2
        
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid
    
    return arr[left]


class ArrayReader:
    """Mock class for infinite array reader."""
    def __init__(self, arr):
        self.arr = arr
    
    def get(self, index):
        if index >= len(self.arr):
            return float('inf')
        return self.arr[index]


# Example usage and test cases
if __name__ == "__main__":
    # Test binary_search
    print("=== Binary Search ===")
    arr = [4, 6, 10]
    target = 6
    result = binary_search(arr, target)
    print(f"Array: {arr}, Target: {target}")
    print(f"Index: {result}")  # 1
    
    # Test search_ceiling_of_number
    print("\n=== Ceiling of Number ===")
    arr = [4, 6, 10]
    key = 6
    result = search_ceiling_of_number(arr, key)
    print(f"Array: {arr}, Key: {key}")
    print(f"Ceiling index: {result}")  # 1
    
    # Test find_next_letter
    print("\n=== Next Letter ===")
    letters = ['a', 'c', 'f', 'h']
    key = 'f'
    result = find_next_letter(letters, key)
    print(f"Letters: {letters}, Key: '{key}'")
    print(f"Next letter: '{result}'")  # 'h'
    
    # Test find_range
    print("\n=== Find Range ===")
    arr = [4, 6, 6, 6, 9]
    key = 6
    result = find_range(arr, key)
    print(f"Array: {arr}, Key: {key}")
    print(f"Range: {result}")  # [1, 3]
    
    # Test search_in_rotated_array
    print("\n=== Search in Rotated Array ===")
    arr = [10, 15, 1, 3, 8]
    key = 15
    result = search_in_rotated_array(arr, key)
    print(f"Array: {arr}, Key: {key}")
    print(f"Index: {result}")  # 1
    
    # Test find_rotation_count
    print("\n=== Rotation Count ===")
    arr = [10, 15, 1, 3, 8]
    result = find_rotation_count(arr)
    print(f"Array: {arr}")
    print(f"Rotation count: {result}")  # 2
    
    # Test search_bitonic_array
    print("\n=== Search in Bitonic Array ===")
    arr = [1, 3, 8, 4, 2]
    key = 4
    result = search_bitonic_array(arr, key)
    print(f"Array: {arr}, Key: {key}")
    print(f"Index: {result}")  # 3
    
    # Test search_insert_position
    print("\n=== Search Insert Position ===")
    arr = [1, 3, 8, 10, 15]
    target = 12
    result = search_insert_position(arr, target)
    print(f"Array: {arr}, Target: {target}")
    print(f"Insert position: {result}")  # 4
    
    # Test find_minimum_in_rotated_array
    print("\n=== Minimum in Rotated Array ===")
    arr = [10, 15, 1, 3, 8]
    result = find_minimum_in_rotated_array(arr)
    print(f"Array: {arr}")
    print(f"Minimum element: {result}")  # 1
