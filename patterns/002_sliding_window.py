"""
Sliding Window Pattern

The Sliding Window pattern is used to perform a required operation on a specific 
window size of a given array or linked list, such as finding the longest subarray 
containing all 1s. Sliding Windows start from the 1st element and keep shifting 
right by one element and adjust the length of the window according to the problem.

Time Complexity: Usually O(n)
Space Complexity: O(1) for most problems

Common Problems:
- Maximum Sum Subarray of Size K
- Smallest Subarray with Sum >= S
- Longest Substring with K Distinct Characters
- Fruits into Baskets
- No-repeat Substring
"""

def max_sum_subarray_size_k(arr, k):
    """
    Find maximum sum of any contiguous subarray of size k.
    
    Args:
        arr: array of integers
        k: size of subarray
    
    Returns:
        maximum sum of subarray of size k
    """
    if len(arr) < k:
        return -1
    
    # Calculate sum of first window
    window_sum = sum(arr[:k])
    max_sum = window_sum
    
    # Slide the window
    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)
    
    return max_sum


def smallest_subarray_with_sum(s, arr):
    """
    Find the length of smallest contiguous subarray whose sum >= s.
    
    Args:
        s: target sum
        arr: array of positive integers
    
    Returns:
        length of smallest subarray with sum >= s
    """
    window_sum = 0
    min_length = float('inf')
    window_start = 0
    
    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add next element
        
        # shrink the window until sum is smaller than s
        while window_sum >= s:
            min_length = min(min_length, window_end - window_start + 1)
            window_sum -= arr[window_start]
            window_start += 1
    
    return 0 if min_length == float('inf') else min_length


def longest_substring_k_distinct(s, k):
    """
    Find the length of longest substring with at most k distinct characters.
    
    Args:
        s: input string
        k: maximum number of distinct characters
    
    Returns:
        length of longest substring with k distinct characters
    """
    if len(s) == 0 or k == 0:
        return 0
    
    window_start = 0
    max_length = 0
    char_frequency = {}
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        
        # Add character to frequency map
        if right_char not in char_frequency:
            char_frequency[right_char] = 0
        char_frequency[right_char] += 1
        
        # Shrink window until we have k distinct characters
        while len(char_frequency) > k:
            left_char = s[window_start]
            char_frequency[left_char] -= 1
            
            if char_frequency[left_char] == 0:
                del char_frequency[left_char]
            
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


def fruits_into_baskets(fruits):
    """
    Find maximum number of fruits you can collect in two baskets.
    Each basket can contain only one type of fruit.
    
    Args:
        fruits: array representing fruit types
    
    Returns:
        maximum number of fruits that can be collected
    """
    window_start = 0
    max_length = 0
    fruit_frequency = {}
    
    for window_end in range(len(fruits)):
        right_fruit = fruits[window_end]
        
        if right_fruit not in fruit_frequency:
            fruit_frequency[right_fruit] = 0
        fruit_frequency[right_fruit] += 1
        
        # Shrink window until we have at most 2 fruit types
        while len(fruit_frequency) > 2:
            left_fruit = fruits[window_start]
            fruit_frequency[left_fruit] -= 1
            
            if fruit_frequency[left_fruit] == 0:
                del fruit_frequency[left_fruit]
            
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


def non_repeat_substring(s):
    """
    Find the length of longest substring with no repeating characters.
    
    Args:
        s: input string
    
    Returns:
        length of longest substring without repeating characters
    """
    window_start = 0
    max_length = 0
    char_index_map = {}
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        
        # If character is seen before, shrink window from beginning
        if right_char in char_index_map:
            # In the current window, we will not have any 'right_char' after its previous index
            # And if 'window_start' is already ahead of the last index of 'right_char', 
            # we'll keep 'window_start'
            window_start = max(window_start, char_index_map[right_char] + 1)
        
        char_index_map[right_char] = window_end  # insert right_char index
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


def longest_substring_with_replacement(s, k):
    """
    Find length of longest substring with same letters after replacing k characters.
    
    Args:
        s: input string
        k: number of characters that can be replaced
    
    Returns:
        length of longest substring after replacement
    """
    window_start = 0
    max_length = 0
    max_repeat_letter_count = 0
    frequency_map = {}
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        
        if right_char not in frequency_map:
            frequency_map[right_char] = 0
        frequency_map[right_char] += 1
        
        max_repeat_letter_count = max(max_repeat_letter_count, frequency_map[right_char])
        
        # Current window size is from window_start to window_end, overall we have 
        # a letter which is repeating 'max_repeat_letter_count' times, this means 
        # we can have a window which has one letter repeating 'max_repeat_letter_count' 
        # times and the remaining letters we should replace.
        # If the remaining letters are more than 'k', it is the time to shrink the window
        if (window_end - window_start + 1 - max_repeat_letter_count) > k:
            left_char = s[window_start]
            frequency_map[left_char] -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


def longest_subarray_with_ones_replacement(arr, k):
    """
    Find length of longest subarray with all 1s after replacing k 0s.
    
    Args:
        arr: binary array (0s and 1s)
        k: number of 0s that can be replaced
    
    Returns:
        length of longest subarray with all 1s after replacement
    """
    window_start = 0
    max_length = 0
    max_ones_count = 0
    
    for window_end in range(len(arr)):
        if arr[window_end] == 1:
            max_ones_count += 1
        
        # Current window size is from window_start to window_end, overall we have 
        # a maximum of 1s repeating 'max_ones_count' times, this means we can have 
        # a window with 'max_ones_count' 1s and the remaining are 0s which should 
        # replace with 1s.
        # Now, if the remaining 0s are more than 'k', it is the time to shrink the window
        if (window_end - window_start + 1 - max_ones_count) > k:
            if arr[window_start] == 1:
                max_ones_count -= 1
            window_start += 1
        
        max_length = max(max_length, window_end - window_start + 1)
    
    return max_length


def find_permutation(s, pattern):
    """
    Check if string contains any permutation of pattern.
    
    Args:
        s: input string
        pattern: pattern string
    
    Returns:
        True if s contains any permutation of pattern
    """
    window_start = 0
    matched = 0
    char_frequency = {}
    
    # Create frequency map for pattern
    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1
    
    for window_end in range(len(s)):
        right_char = s[window_end]
        
        if right_char in char_frequency:
            char_frequency[right_char] -= 1
            if char_frequency[right_char] == 0:
                matched += 1
        
        if matched == len(char_frequency):
            return True
        
        if window_end >= len(pattern) - 1:
            left_char = s[window_start]
            window_start += 1
            
            if left_char in char_frequency:
                if char_frequency[left_char] == 0:
                    matched -= 1
                char_frequency[left_char] += 1
    
    return False


# Example usage and test cases
if __name__ == "__main__":
    # Test max_sum_subarray_size_k
    print("=== Maximum Sum Subarray of Size K ===")
    arr = [2, 1, 5, 1, 3, 2]
    k = 3
    result = max_sum_subarray_size_k(arr, k)
    print(f"Array: {arr}, K: {k}")
    print(f"Maximum sum: {result}")  # 9
    
    # Test smallest_subarray_with_sum
    print("\n=== Smallest Subarray with Sum ===")
    arr = [2, 1, 2, 3, 3, 1, 1, 1]
    s = 8
    result = smallest_subarray_with_sum(s, arr)
    print(f"Array: {arr}, Target sum: {s}")
    print(f"Smallest subarray length: {result}")  # 3
    
    # Test longest_substring_k_distinct
    print("\n=== Longest Substring with K Distinct Characters ===")
    s = "araaci"
    k = 2
    result = longest_substring_k_distinct(s, k)
    print(f"String: '{s}', K: {k}")
    print(f"Longest substring length: {result}")  # 4
    
    # Test fruits_into_baskets
    print("\n=== Fruits into Baskets ===")
    fruits = ['A', 'B', 'C', 'A', 'C']
    result = fruits_into_baskets(fruits)
    print(f"Fruits: {fruits}")
    print(f"Maximum fruits: {result}")  # 3
    
    # Test non_repeat_substring
    print("\n=== No-repeat Substring ===")
    s = "aabccbb"
    result = non_repeat_substring(s)
    print(f"String: '{s}'")
    print(f"Longest substring length: {result}")  # 3
    
    # Test longest_substring_with_replacement
    print("\n=== Longest Substring with Same Letters after Replacement ===")
    s = "aabccbb"
    k = 2
    result = longest_substring_with_replacement(s, k)
    print(f"String: '{s}', K: {k}")
    print(f"Longest substring length: {result}")  # 5
    
    # Test find_permutation
    print("\n=== String Contains Permutation ===")
    s = "oidbcaf"
    pattern = "abc"
    result = find_permutation(s, pattern)
    print(f"String: '{s}', Pattern: '{pattern}'")
    print(f"Contains permutation: {result}")  # True
