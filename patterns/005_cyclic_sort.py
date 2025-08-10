"""
Cyclic Sort Pattern

The Cyclic Sort pattern describes an interesting approach to deal with problems 
involving arrays containing numbers in a given range. The pattern iterates over 
the array one number at a time, and if the current number is not at the correct 
index, it swaps it with the number at its correct index.

Time Complexity: O(n)
Space Complexity: O(1)

Common Problems:
- Cyclic Sort
- Find the Missing Number
- Find all Missing Numbers
- Find the Duplicate Number
- Find all Duplicate Numbers
"""

def cyclic_sort(nums):
    """
    Sort array containing numbers from 1 to n using cyclic sort.
    
    Args:
        nums: array containing numbers from 1 to n
    
    Returns:
        sorted array
    """
    i = 0
    while i < len(nums):
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    return nums


def find_missing_number(nums):
    """
    Find the missing number in array containing n distinct numbers from 0 to n.
    
    Args:
        nums: array containing n distinct numbers from 0 to n
    
    Returns:
        missing number
    """
    i = 0
    n = len(nums)
    
    # Try to place each number at its correct index
    while i < n:
        j = nums[i]  # correct index for nums[i]
        
        if nums[i] < n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    # Find the first number missing from its index
    for i in range(n):
        if nums[i] != i:
            return i
    
    return n


def find_missing_numbers(nums):
    """
    Find all missing numbers in array containing numbers from 1 to n.
    
    Args:
        nums: array containing numbers from 1 to n with some duplicates
    
    Returns:
        list of missing numbers
    """
    i = 0
    
    # Try to place each number at its correct index
    while i < len(nums):
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    missing_numbers = []
    
    # Find all indices that do not have the correct numbers
    for i in range(len(nums)):
        if nums[i] != i + 1:
            missing_numbers.append(i + 1)
    
    return missing_numbers


def find_duplicate(nums):
    """
    Find the duplicate number in array containing n+1 numbers from 1 to n.
    
    Args:
        nums: array containing n+1 numbers from 1 to n (exactly one duplicate)
    
    Returns:
        duplicate number
    """
    i = 0
    
    while i < len(nums):
        if nums[i] != i + 1:
            j = nums[i] - 1  # correct index for nums[i]
            
            if nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]  # swap
            else:
                return nums[i]  # found duplicate
        else:
            i += 1
    
    return -1


def find_all_duplicates(nums):
    """
    Find all duplicate numbers in array containing numbers from 1 to n.
    
    Args:
        nums: array containing numbers from 1 to n (some numbers appear twice)
    
    Returns:
        list of duplicate numbers
    """
    i = 0
    
    # Try to place each number at its correct index
    while i < len(nums):
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    duplicate_numbers = []
    
    # Find all numbers that are not at their correct indices
    for i in range(len(nums)):
        if nums[i] != i + 1:
            duplicate_numbers.append(nums[i])
    
    return duplicate_numbers


def find_corrupt_pair(nums):
    """
    Find the corrupt pair (duplicate and missing) in array from 1 to n.
    
    Args:
        nums: array containing numbers from 1 to n with one duplicate and one missing
    
    Returns:
        [duplicate_number, missing_number]
    """
    i = 0
    
    # Try to place each number at its correct index
    while i < len(nums):
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    # Find the number that is not at its correct index
    for i in range(len(nums)):
        if nums[i] != i + 1:
            return [nums[i], i + 1]
    
    return [-1, -1]


def find_smallest_positive_missing(nums):
    """
    Find the smallest missing positive number in unsorted array.
    
    Args:
        nums: unsorted array of integers
    
    Returns:
        smallest missing positive number
    """
    i = 0
    n = len(nums)
    
    # Try to place each positive number <= n at its correct index
    while i < n:
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    # Find the first missing positive number
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1
    
    return n + 1


def find_first_k_missing_positive(nums, k):
    """
    Find the first k missing positive numbers in unsorted array.
    
    Args:
        nums: unsorted array of integers
        k: number of missing positive numbers to find
    
    Returns:
        list of first k missing positive numbers
    """
    i = 0
    n = len(nums)
    
    # Try to place each positive number <= n at its correct index
    while i < n:
        j = nums[i] - 1  # correct index for nums[i]
        
        if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
            nums[i], nums[j] = nums[j], nums[i]  # swap
        else:
            i += 1
    
    missing_numbers = []
    extra_numbers = set()
    
    # Find missing and extra numbers
    for i in range(n):
        if len(missing_numbers) < k:
            if nums[i] != i + 1:
                missing_numbers.append(i + 1)
                extra_numbers.add(nums[i])
    
    # Add additional missing numbers if needed
    i = 1
    while len(missing_numbers) < k:
        candidate_number = i + n
        
        # Make sure the candidate number is not in the original array
        if candidate_number not in extra_numbers:
            missing_numbers.append(candidate_number)
        
        i += 1
    
    return missing_numbers


def find_duplicate_file_in_system(paths):
    """
    Find duplicate files in a file system based on content.
    
    Args:
        paths: list of directory paths with files and their content
    
    Returns:
        list of groups where each group contains duplicate files
    """
    content_map = {}
    
    for path in paths:
        parts = path.split(' ')
        directory = parts[0]
        
        for i in range(1, len(parts)):
            file_info = parts[i]
            file_name = file_info[:file_info.index('(')]
            content = file_info[file_info.index('(') + 1:file_info.index(')')]
            
            full_path = directory + '/' + file_name
            
            if content not in content_map:
                content_map[content] = []
            content_map[content].append(full_path)
    
    # Return groups with more than one file (duplicates)
    return [group for group in content_map.values() if len(group) > 1]


# Example usage and test cases
if __name__ == "__main__":
    # Test cyclic_sort
    print("=== Cyclic Sort ===")
    nums = [3, 1, 5, 4, 2]
    sorted_nums = cyclic_sort(nums.copy())
    print(f"Original: {nums}")
    print(f"Sorted: {sorted_nums}")  # [1, 2, 3, 4, 5]
    
    # Test find_missing_number
    print("\n=== Find Missing Number ===")
    nums = [4, 0, 3, 1]
    missing = find_missing_number(nums.copy())
    print(f"Array: {nums}")
    print(f"Missing number: {missing}")  # 2
    
    nums = [8, 3, 5, 2, 4, 6, 0, 1]
    missing = find_missing_number(nums.copy())
    print(f"Array: {nums}")
    print(f"Missing number: {missing}")  # 7
    
    # Test find_missing_numbers
    print("\n=== Find All Missing Numbers ===")
    nums = [2, 3, 1, 8, 2, 3, 5, 1]
    missing_nums = find_missing_numbers(nums.copy())
    print(f"Array: {nums}")
    print(f"Missing numbers: {missing_nums}")  # [4, 6, 7]
    
    # Test find_duplicate
    print("\n=== Find Duplicate Number ===")
    nums = [1, 4, 4, 3, 2]
    duplicate = find_duplicate(nums.copy())
    print(f"Array: {nums}")
    print(f"Duplicate number: {duplicate}")  # 4
    
    # Test find_all_duplicates
    print("\n=== Find All Duplicates ===")
    nums = [5, 4, 7, 2, 3, 5, 3]
    duplicates = find_all_duplicates(nums.copy())
    print(f"Array: {nums}")
    print(f"Duplicate numbers: {duplicates}")  # [3, 5]
    
    # Test find_corrupt_pair
    print("\n=== Find Corrupt Pair ===")
    nums = [3, 1, 2, 5, 2]
    corrupt_pair = find_corrupt_pair(nums.copy())
    print(f"Array: {nums}")
    print(f"Corrupt pair [duplicate, missing]: {corrupt_pair}")  # [2, 4]
    
    # Test find_smallest_positive_missing
    print("\n=== Find Smallest Missing Positive ===")
    nums = [-3, 1, 5, 4, 2]
    smallest_missing = find_smallest_positive_missing(nums.copy())
    print(f"Array: {nums}")
    print(f"Smallest missing positive: {smallest_missing}")  # 3
    
    nums = [3, -2, 0, 1, 2]
    smallest_missing = find_smallest_positive_missing(nums.copy())
    print(f"Array: {nums}")
    print(f"Smallest missing positive: {smallest_missing}")  # 4
    
    # Test find_first_k_missing_positive
    print("\n=== Find First K Missing Positive ===")
    nums = [3, -1, 4, 5, 5]
    k = 3
    missing_k = find_first_k_missing_positive(nums.copy(), k)
    print(f"Array: {nums}, K: {k}")
    print(f"First {k} missing positive numbers: {missing_k}")  # [1, 2, 6]
