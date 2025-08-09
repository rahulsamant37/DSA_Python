"""
002 - Arrays Searching Algorithms
=================================

This module implements various searching algorithms:
- Linear Search
- Binary Search
- Jump Search
- Interpolation Search

Time Complexity:
- Linear Search: O(n)
- Binary Search: O(log n) - requires sorted array
- Jump Search: O(√n) - requires sorted array
- Interpolation Search: O(log log n) average case - requires sorted array
"""

import math

class SearchAlgorithms:
    
    @staticmethod
    def linear_search(arr, target):
        """
        Linear Search - Search element by checking each element
        Time Complexity: O(n), Space Complexity: O(1)
        """
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    
    @staticmethod
    def binary_search(arr, target):
        """
        Binary Search - Search in sorted array by dividing search space
        Time Complexity: O(log n), Space Complexity: O(1)
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
    
    @staticmethod
    def binary_search_recursive(arr, target, left=0, right=None):
        """
        Binary Search - Recursive implementation
        Time Complexity: O(log n), Space Complexity: O(log n)
        """
        if right is None:
            right = len(arr) - 1
        
        if left > right:
            return -1
        
        mid = left + (right - left) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            return SearchAlgorithms.binary_search_recursive(arr, target, mid + 1, right)
        else:
            return SearchAlgorithms.binary_search_recursive(arr, target, left, mid - 1)
    
    @staticmethod
    def jump_search(arr, target):
        """
        Jump Search - Search by jumping ahead by fixed steps
        Time Complexity: O(√n), Space Complexity: O(1)
        """
        n = len(arr)
        step = int(math.sqrt(n))
        prev = 0
        
        # Find the block where element is present
        while arr[min(step, n) - 1] < target:
            prev = step
            step += int(math.sqrt(n))
            if prev >= n:
                return -1
        
        # Linear search in the identified block
        while arr[prev] < target:
            prev += 1
            if prev == min(step, n):
                return -1
        
        if arr[prev] == target:
            return prev
        
        return -1
    
    @staticmethod
    def interpolation_search(arr, target):
        """
        Interpolation Search - Search by estimating position
        Time Complexity: O(log log n) average, O(n) worst case
        Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        
        while left <= right and target >= arr[left] and target <= arr[right]:
            # If array has only one element
            if left == right:
                if arr[left] == target:
                    return left
                return -1
            
            # Calculate position using interpolation formula
            pos = left + ((target - arr[left]) * (right - left)) // (arr[right] - arr[left])
            
            if arr[pos] == target:
                return pos
            elif arr[pos] < target:
                left = pos + 1
            else:
                right = pos - 1
        
        return -1
    
    @staticmethod
    def exponential_search(arr, target):
        """
        Exponential Search - Find range and then apply binary search
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        n = len(arr)
        
        # If element is at first position
        if arr[0] == target:
            return 0
        
        # Find range for binary search
        i = 1
        while i < n and arr[i] <= target:
            i *= 2
        
        # Apply binary search in the found range
        return SearchAlgorithms.binary_search(arr[i//2:min(i, n)], target)


class SearchInSpecialArrays:
    """Search algorithms for special types of arrays"""
    
    @staticmethod
    def search_in_rotated_sorted_array(arr, target):
        """
        Search in rotated sorted array
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            
            if arr[mid] == target:
                return mid
            
            # Left half is sorted
            if arr[left] <= arr[mid]:
                if arr[left] <= target < arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            # Right half is sorted
            else:
                if arr[mid] < target <= arr[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        
        return -1
    
    @staticmethod
    def find_peak_element(arr):
        """
        Find peak element in array (element greater than its neighbors)
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        left, right = 0, len(arr) - 1
        
        while left < right:
            mid = left + (right - left) // 2
            
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1
        
        return left
    
    @staticmethod
    def search_in_infinite_array(arr, target):
        """
        Search in infinite sorted array (simulated with large array)
        Time Complexity: O(log n), Space Complexity: O(1)
        """
        # Find bounds for binary search
        left, right = 0, 1
        
        try:
            while arr[right] < target:
                left = right
                right *= 2
        except IndexError:
            # Handle case where we exceed array bounds
            right = len(arr) - 1
        
        # Apply binary search in found bounds
        while left <= right:
            mid = left + (right - left) // 2
            
            try:
                if arr[mid] == target:
                    return mid
                elif arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            except IndexError:
                right = mid - 1
        
        return -1


def test_searching_algorithms():
    """Test all searching algorithms"""
    print("=== Testing Search Algorithms ===\n")
    
    # Test data
    unsorted_arr = [64, 34, 25, 12, 22, 11, 90, 5]
    sorted_arr = [2, 5, 8, 12, 16, 23, 38, 45, 56, 67, 78]
    rotated_arr = [4, 5, 6, 7, 0, 1, 2]
    target = 23
    
    search_algo = SearchAlgorithms()
    special_search = SearchInSpecialArrays()
    
    print(f"Unsorted array: {unsorted_arr}")
    print(f"Sorted array: {sorted_arr}")
    print(f"Target element: {target}")
    print()
    
    # Linear Search
    print("=== Linear Search ===")
    result = search_algo.linear_search(sorted_arr, target)
    print(f"Linear search result: {result}")
    print(f"Element found: {'Yes' if result != -1 else 'No'}")
    print()
    
    # Binary Search
    print("=== Binary Search ===")
    result = search_algo.binary_search(sorted_arr, target)
    print(f"Binary search result: {result}")
    print(f"Element found: {'Yes' if result != -1 else 'No'}")
    
    result_recursive = search_algo.binary_search_recursive(sorted_arr, target)
    print(f"Binary search (recursive) result: {result_recursive}")
    print()
    
    # Jump Search
    print("=== Jump Search ===")
    result = search_algo.jump_search(sorted_arr, target)
    print(f"Jump search result: {result}")
    print(f"Element found: {'Yes' if result != -1 else 'No'}")
    print()
    
    # Interpolation Search
    print("=== Interpolation Search ===")
    result = search_algo.interpolation_search(sorted_arr, target)
    print(f"Interpolation search result: {result}")
    print(f"Element found: {'Yes' if result != -1 else 'No'}")
    print()
    
    # Search in rotated sorted array
    print("=== Search in Rotated Sorted Array ===")
    print(f"Rotated array: {rotated_arr}")
    target_rotated = 0
    result = special_search.search_in_rotated_sorted_array(rotated_arr, target_rotated)
    print(f"Search for {target_rotated} in rotated array: {result}")
    print()
    
    # Find peak element
    print("=== Find Peak Element ===")
    peak_arr = [1, 3, 20, 4, 1, 0]
    print(f"Array: {peak_arr}")
    peak_index = special_search.find_peak_element(peak_arr)
    print(f"Peak element index: {peak_index}, element: {peak_arr[peak_index]}")
    print()
    
    # Performance comparison
    print("=== Performance Comparison ===")
    import time
    
    large_arr = list(range(0, 100000, 2))  # Even numbers from 0 to 99998
    search_target = 50000
    
    # Linear search timing
    start_time = time.time()
    result = search_algo.linear_search(large_arr, search_target)
    linear_time = time.time() - start_time
    
    # Binary search timing
    start_time = time.time()
    result = search_algo.binary_search(large_arr, search_target)
    binary_time = time.time() - start_time
    
    print(f"Array size: {len(large_arr)}")
    print(f"Target: {search_target}")
    print(f"Linear search time: {linear_time:.6f} seconds")
    print(f"Binary search time: {binary_time:.6f} seconds")
    print(f"Binary search is {linear_time/binary_time:.2f}x faster")


if __name__ == "__main__":
    test_searching_algorithms()
