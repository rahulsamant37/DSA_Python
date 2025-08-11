"""
Two Pointers Pattern - Two Sum
==============================

Find two numbers in a sorted array that add up to a target sum.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def two_sum_sorted_array(arr, target):
    """
    Find two numbers in a sorted array that add up to target.
    
    Args:
        arr: Sorted array of integers
        target: Target sum
        
    Returns:
        Tuple of (index1, index2) if found, None otherwise
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            return (left, right)
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None


def example_usage():
    """Demonstrate the two sum function"""
    arr = [1, 2, 3, 4, 6, 8, 9]
    target = 10
    
    result = two_sum_sorted_array(arr, target)
    if result:
        print(f"Numbers at indices {result[0]} and {result[1]} sum to {target}")
        print(f"Values: {arr[result[0]]} + {arr[result[1]]} = {target}")
    else:
        print(f"No two numbers sum to {target}")


if __name__ == "__main__":
    example_usage()
