"""
Two Pointers Pattern

The Two Pointers pattern is used when dealing with sorted arrays or linked lists and 
need to find a set of elements that fulfill certain constraints. The set of elements 
could be a pair, a triplet, or even a subarray.

Time Complexity: Usually O(n) or O(n log n)
Space Complexity: O(1)

Common Problems:
- Pair with Target Sum
- Remove Duplicates
- Squaring a Sorted Array
- Triplet Sum to Zero
- Compare Strings containing Backspaces
"""

def pair_with_target_sum(arr, target_sum):
    """
    Find a pair in the array that sums up to the target sum.
    
    Args:
        arr: sorted array of integers
        target_sum: target sum to find
    
    Returns:
        indices of the two numbers that add up to target_sum
    """
    left, right = 0, len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target_sum:
            return [left, right]
        elif current_sum < target_sum:
            left += 1
        else:
            right -= 1
    
    return [-1, -1]  # pair not found


def remove_duplicates(arr):
    """
    Remove duplicates in-place from a sorted array.
    
    Args:
        arr: sorted array with duplicates
    
    Returns:
        length of array after removing duplicates
    """
    if len(arr) <= 1:
        return len(arr)
    
    next_non_duplicate = 1
    
    for i in range(1, len(arr)):
        if arr[next_non_duplicate - 1] != arr[i]:
            arr[next_non_duplicate] = arr[i]
            next_non_duplicate += 1
    
    return next_non_duplicate


def make_squares(arr):
    """
    Square each number in a sorted array and return sorted squares.
    
    Args:
        arr: sorted array (can have negative numbers)
    
    Returns:
        sorted array of squares
    """
    n = len(arr)
    squares = [0] * n
    left, right = 0, n - 1
    highest_square_idx = n - 1
    
    while left <= right:
        left_square = arr[left] ** 2
        right_square = arr[right] ** 2
        
        if left_square > right_square:
            squares[highest_square_idx] = left_square
            left += 1
        else:
            squares[highest_square_idx] = right_square
            right -= 1
        
        highest_square_idx -= 1
    
    return squares


def triplet_sum_to_zero(arr):
    """
    Find all unique triplets in the array that sum up to zero.
    
    Args:
        arr: array of integers
    
    Returns:
        list of triplets that sum to zero
    """
    arr.sort()
    triplets = []
    
    for i in range(len(arr)):
        if i > 0 and arr[i] == arr[i - 1]:  # skip duplicates
            continue
        
        search_pair(arr, -arr[i], i + 1, triplets)
    
    return triplets


def search_pair(arr, target_sum, left, triplets):
    """Helper function for triplet_sum_to_zero"""
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target_sum:  # found the triplet
            triplets.append([-target_sum, arr[left], arr[right]])
            left += 1
            right -= 1
            
            # skip duplicates
            while left < right and arr[left] == arr[left - 1]:
                left += 1
            while left < right and arr[right] == arr[right + 1]:
                right -= 1
        elif target_sum > current_sum:
            left += 1
        else:
            right -= 1


def backspace_compare(str1, str2):
    """
    Compare two strings containing backspaces '#'.
    
    Args:
        str1, str2: strings with possible backspace characters
    
    Returns:
        True if both strings are equal after processing backspaces
    """
    index1 = len(str1) - 1
    index2 = len(str2) - 1
    
    while index1 >= 0 or index2 >= 0:
        # Get next valid character from str1
        i1 = get_next_valid_char_index(str1, index1)
        
        # Get next valid character from str2
        i2 = get_next_valid_char_index(str2, index2)
        
        # If both strings are processed completely
        if i1 < 0 and i2 < 0:
            return True
        
        # If only one string is processed completely
        if i1 < 0 or i2 < 0:
            return False
        
        # If characters don't match
        if str1[i1] != str2[i2]:
            return False
        
        index1 = i1 - 1
        index2 = i2 - 1
    
    return True


def get_next_valid_char_index(s, index):
    """Helper function for backspace_compare"""
    backspace_count = 0
    
    while index >= 0:
        if s[index] == '#':  # backspace character
            backspace_count += 1
        elif backspace_count > 0:  # non-backspace character
            backspace_count -= 1
        else:
            break
        
        index -= 1
    
    return index


# Example usage and test cases
if __name__ == "__main__":
    # Test pair_with_target_sum
    print("=== Pair with Target Sum ===")
    arr = [1, 2, 3, 4, 6]
    target = 6
    result = pair_with_target_sum(arr, target)
    print(f"Array: {arr}, Target: {target}")
    print(f"Pair indices: {result}")  # [1, 3]
    
    # Test remove_duplicates
    print("\n=== Remove Duplicates ===")
    arr = [2, 3, 3, 3, 6, 9, 9]
    length = remove_duplicates(arr)
    print(f"Array after removing duplicates: {arr[:length]}")  # [2, 3, 6, 9]
    
    # Test make_squares
    print("\n=== Squared Sorted Array ===")
    arr = [-2, -1, 0, 2, 3]
    squares = make_squares(arr)
    print(f"Original: {arr}")
    print(f"Squares: {squares}")  # [0, 1, 4, 4, 9]
    
    # Test triplet_sum_to_zero
    print("\n=== Triplet Sum to Zero ===")
    arr = [-3, 0, 1, 2, -1, 1, -2]
    triplets = triplet_sum_to_zero(arr)
    print(f"Array: {arr}")
    print(f"Triplets that sum to zero: {triplets}")
    
    # Test backspace_compare
    print("\n=== Backspace String Compare ===")
    str1, str2 = "xy#z", "xzz#"
    result = backspace_compare(str1, str2)
    print(f"'{str1}' == '{str2}': {result}")  # True
    
    str1, str2 = "xy#z", "xyz#"
    result = backspace_compare(str1, str2)
    print(f"'{str1}' == '{str2}': {result}")  # False
