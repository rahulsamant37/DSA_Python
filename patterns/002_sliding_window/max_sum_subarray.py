"""
Sliding Window Pattern - Maximum Sum Subarray
==============================================

Find the maximum sum of a subarray of size k.

Time Complexity: O(n)
Space Complexity: O(1)
"""


def max_sum_subarray_size_k(arr, k):
    """
    Find maximum sum of subarray of size k using sliding window.
    
    Args:
        arr: List of integers
        k: Size of subarray
        
    Returns:
        Maximum sum of subarray of size k
    """
    if len(arr) < k:
        return None
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window and update sum
    for i in range(k, len(arr)):
        # Remove leftmost element and add rightmost element
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def min_window_with_sum(arr, target_sum):
    """
    Find minimum window size with sum >= target_sum.
    
    Args:
        arr: List of positive integers
        target_sum: Target sum
        
    Returns:
        Minimum window size, or float('inf') if not possible
    """
    window_start = 0
    window_sum = 0
    min_length = float('inf')
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]
        
        # Shrink window until sum is smaller than target
        while window_sum >= target_sum and window_start <= window_end:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    return min_length if min_length != float('inf') else 0


def example_usage():
    """Demonstrate sliding window functions"""
    arr = [2, 1, 2, 1, 6, 2, 3, 1]
    k = 3
    
    max_sum = max_sum_subarray_size_k(arr, k)
    print(f"Maximum sum of subarray of size {k}: {max_sum}")
    
    target = 7
    min_window = min_window_with_sum(arr, target)
    print(f"Minimum window size with sum >= {target}: {min_window}")


if __name__ == "__main__":
    example_usage()
