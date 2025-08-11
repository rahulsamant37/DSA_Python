"""
Cyclic Sort Pattern - Find Missing Numbers
==========================================

Sort arrays containing numbers in a given range and find missing/duplicate numbers.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def cyclic_sort(nums):
    """
    Sort array containing numbers from 1 to n using cyclic sort.
    
    Args:
        nums: List of integers from 1 to n
        
    Returns:
        Sorted array
    """
    i = 0
    while i < len(nums):
        # Number should be at index (nums[i] - 1)
        correct_index = nums[i] - 1
        
        if nums[i] != nums[correct_index]:
            # Swap to correct position
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    return nums


def find_missing_number(nums):
    """
    Find missing number in array containing n numbers from 0 to n.
    
    Args:
        nums: List of integers from 0 to n with one missing
        
    Returns:
        Missing number
    """
    i = 0
    n = len(nums)
    
    # Cyclic sort (numbers 0 to n-1 should be at their indices)
    while i < n:
        if nums[i] < n and nums[i] != nums[nums[i]]:
            nums[nums[i]], nums[i] = nums[i], nums[nums[i]]
        else:
            i += 1
    
    # Find missing number
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n  # Missing number is n


def find_all_missing_numbers(nums):
    """
    Find all missing numbers in array from 1 to n.
    
    Args:
        nums: List that should contain numbers 1 to n
        
    Returns:
        List of missing numbers
    """
    i = 0
    while i < len(nums):
        correct_index = nums[i] - 1
        if nums[i] != nums[correct_index]:
            nums[i], nums[correct_index] = nums[correct_index], nums[i]
        else:
            i += 1
    
    missing = []
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing.append(i + 1)
    
    return missing


def find_duplicate_number(nums):
    """
    Find duplicate number in array containing n+1 numbers from 1 to n.
    
    Args:
        nums: List containing numbers 1 to n with one duplicate
        
    Returns:
        Duplicate number
    """
    i = 0
    while i < len(nums):
        if nums[i] != i + 1:
            correct_index = nums[i] - 1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                return nums[i]  # Found duplicate
        else:
            i += 1
    
    return -1


def example_usage():
    """Demonstrate cyclic sort operations"""
    # Cyclic sort
    nums = [3, 1, 5, 4, 2]
    print("Original:", nums)
    cyclic_sort(nums.copy())
    print("Sorted:", nums)
    
    # Find missing number
    missing_nums = [4, 0, 3, 1]
    missing = find_missing_number(missing_nums.copy())
    print(f"Missing number: {missing}")
    
    # Find all missing numbers
    nums_with_missing = [2, 3, 1, 8, 2, 3, 5, 1]
    all_missing = find_all_missing_numbers(nums_with_missing.copy())
    print(f"All missing numbers: {all_missing}")
    
    # Find duplicate
    nums_with_dup = [1, 4, 4, 3, 2]
    duplicate = find_duplicate_number(nums_with_dup.copy())
    print(f"Duplicate number: {duplicate}")


if __name__ == "__main__":
    example_usage()
