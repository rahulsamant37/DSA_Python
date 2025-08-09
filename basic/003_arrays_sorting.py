"""
003 - Arrays Sorting Algorithms
===============================

This module implements various sorting algorithms:
- Bubble Sort
- Selection Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Heap Sort
- Counting Sort
- Radix Sort

Time Complexity Analysis:
- Bubble Sort: O(n²) average and worst case, O(n) best case
- Selection Sort: O(n²) all cases
- Insertion Sort: O(n²) average and worst case, O(n) best case
- Merge Sort: O(n log n) all cases
- Quick Sort: O(n log n) average case, O(n²) worst case
- Heap Sort: O(n log n) all cases
- Counting Sort: O(n + k) where k is the range of input
- Radix Sort: O(d × (n + k)) where d is the number of digits
"""

import random
import time

class SortingAlgorithms:
    
    @staticmethod
    def bubble_sort(arr):
        """
        Bubble Sort - Compare adjacent elements and swap if needed
        Time Complexity: O(n²), Space Complexity: O(1)
        """
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            swapped = False
            for j in range(0, n - i - 1):
                if arr_copy[j] > arr_copy[j + 1]:
                    arr_copy[j], arr_copy[j + 1] = arr_copy[j + 1], arr_copy[j]
                    swapped = True
            
            # If no swapping occurred, array is sorted
            if not swapped:
                break
        
        return arr_copy
    
    @staticmethod
    def selection_sort(arr):
        """
        Selection Sort - Find minimum element and place it at beginning
        Time Complexity: O(n²), Space Complexity: O(1)
        """
        n = len(arr)
        arr_copy = arr.copy()
        
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if arr_copy[j] < arr_copy[min_idx]:
                    min_idx = j
            
            arr_copy[i], arr_copy[min_idx] = arr_copy[min_idx], arr_copy[i]
        
        return arr_copy
    
    @staticmethod
    def insertion_sort(arr):
        """
        Insertion Sort - Insert each element in its correct position
        Time Complexity: O(n²), Space Complexity: O(1)
        """
        arr_copy = arr.copy()
        
        for i in range(1, len(arr_copy)):
            key = arr_copy[i]
            j = i - 1
            
            # Move elements greater than key one position ahead
            while j >= 0 and arr_copy[j] > key:
                arr_copy[j + 1] = arr_copy[j]
                j -= 1
            
            arr_copy[j + 1] = key
        
        return arr_copy
    
    @staticmethod
    def merge_sort(arr):
        """
        Merge Sort - Divide and conquer approach
        Time Complexity: O(n log n), Space Complexity: O(n)
        """
        if len(arr) <= 1:
            return arr
        
        mid = len(arr) // 2
        left = SortingAlgorithms.merge_sort(arr[:mid])
        right = SortingAlgorithms.merge_sort(arr[mid:])
        
        return SortingAlgorithms._merge(left, right)
    
    @staticmethod
    def _merge(left, right):
        """Helper function for merge sort"""
        result = []
        i = j = 0
        
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        
        result.extend(left[i:])
        result.extend(right[j:])
        return result
    
    @staticmethod
    def quick_sort(arr):
        """
        Quick Sort - Divide and conquer with pivot
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n)
        """
        if len(arr) <= 1:
            return arr
        
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        
        return (SortingAlgorithms.quick_sort(left) + 
                middle + 
                SortingAlgorithms.quick_sort(right))
    
    @staticmethod
    def quick_sort_inplace(arr, low=0, high=None):
        """
        Quick Sort - In-place implementation
        Time Complexity: O(n log n) average, O(n²) worst case
        Space Complexity: O(log n)
        """
        if high is None:
            high = len(arr) - 1
            arr_copy = arr.copy()
        else:
            arr_copy = arr
        
        if low < high:
            pi = SortingAlgorithms._partition(arr_copy, low, high)
            SortingAlgorithms.quick_sort_inplace(arr_copy, low, pi - 1)
            SortingAlgorithms.quick_sort_inplace(arr_copy, pi + 1, high)
        
        return arr_copy if high == len(arr) - 1 else arr
    
    @staticmethod
    def _partition(arr, low, high):
        """Helper function for in-place quick sort"""
        pivot = arr[high]
        i = low - 1
        
        for j in range(low, high):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        
        arr[i + 1], arr[high] = arr[high], arr[i + 1]
        return i + 1
    
    @staticmethod
    def heap_sort(arr):
        """
        Heap Sort - Build max heap and extract maximum elements
        Time Complexity: O(n log n), Space Complexity: O(1)
        """
        arr_copy = arr.copy()
        n = len(arr_copy)
        
        # Build max heap
        for i in range(n // 2 - 1, -1, -1):
            SortingAlgorithms._heapify(arr_copy, n, i)
        
        # Extract elements from heap one by one
        for i in range(n - 1, 0, -1):
            arr_copy[0], arr_copy[i] = arr_copy[i], arr_copy[0]
            SortingAlgorithms._heapify(arr_copy, i, 0)
        
        return arr_copy
    
    @staticmethod
    def _heapify(arr, n, i):
        """Helper function for heap sort"""
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2
        
        if left < n and arr[left] > arr[largest]:
            largest = left
        
        if right < n and arr[right] > arr[largest]:
            largest = right
        
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            SortingAlgorithms._heapify(arr, n, largest)
    
    @staticmethod
    def counting_sort(arr):
        """
        Counting Sort - Sort by counting occurrences (for non-negative integers)
        Time Complexity: O(n + k), Space Complexity: O(k)
        where k is the range of input
        """
        if not arr:
            return arr
        
        max_val = max(arr)
        min_val = min(arr)
        range_val = max_val - min_val + 1
        
        # Count occurrences
        count = [0] * range_val
        output = [0] * len(arr)
        
        for num in arr:
            count[num - min_val] += 1
        
        # Calculate cumulative count
        for i in range(1, range_val):
            count[i] += count[i - 1]
        
        # Build output array
        for i in range(len(arr) - 1, -1, -1):
            output[count[arr[i] - min_val] - 1] = arr[i]
            count[arr[i] - min_val] -= 1
        
        return output
    
    @staticmethod
    def radix_sort(arr):
        """
        Radix Sort - Sort by processing digits from least to most significant
        Time Complexity: O(d × (n + k)), Space Complexity: O(n + k)
        """
        if not arr:
            return arr
        
        max_val = max(arr)
        exp = 1
        arr_copy = arr.copy()
        
        while max_val // exp > 0:
            SortingAlgorithms._counting_sort_for_radix(arr_copy, exp)
            exp *= 10
        
        return arr_copy
    
    @staticmethod
    def _counting_sort_for_radix(arr, exp):
        """Helper function for radix sort"""
        n = len(arr)
        output = [0] * n
        count = [0] * 10
        
        # Count occurrences of digits
        for i in range(n):
            index = arr[i] // exp
            count[index % 10] += 1
        
        # Calculate cumulative count
        for i in range(1, 10):
            count[i] += count[i - 1]
        
        # Build output array
        i = n - 1
        while i >= 0:
            index = arr[i] // exp
            output[count[index % 10] - 1] = arr[i]
            count[index % 10] -= 1
            i -= 1
        
        # Copy output array to arr
        for i in range(n):
            arr[i] = output[i]


class SortingAnalyzer:
    """Class to analyze and compare sorting algorithms"""
    
    @staticmethod
    def time_algorithm(sort_func, arr):
        """Time a sorting algorithm"""
        start_time = time.time()
        sorted_arr = sort_func(arr)
        end_time = time.time()
        return end_time - start_time, sorted_arr
    
    @staticmethod
    def is_sorted(arr):
        """Check if array is sorted"""
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    @staticmethod
    def generate_test_arrays():
        """Generate different types of test arrays"""
        random.seed(42)  # For reproducible results
        
        return {
            'random': [random.randint(1, 1000) for _ in range(1000)],
            'sorted': list(range(1000)),
            'reverse_sorted': list(range(1000, 0, -1)),
            'nearly_sorted': list(range(1000)) + [random.randint(1, 1000) for _ in range(10)],
            'duplicates': [random.randint(1, 10) for _ in range(1000)]
        }
    
    @staticmethod
    def compare_algorithms(test_arrays):
        """Compare performance of all sorting algorithms"""
        algorithms = {
            'Bubble Sort': SortingAlgorithms.bubble_sort,
            'Selection Sort': SortingAlgorithms.selection_sort,
            'Insertion Sort': SortingAlgorithms.insertion_sort,
            'Merge Sort': SortingAlgorithms.merge_sort,
            'Quick Sort': SortingAlgorithms.quick_sort,
            'Heap Sort': SortingAlgorithms.heap_sort,
            'Counting Sort': SortingAlgorithms.counting_sort,
            'Radix Sort': SortingAlgorithms.radix_sort
        }
        
        results = {}
        
        for array_type, array in test_arrays.items():
            print(f"\n=== {array_type.replace('_', ' ').title()} Array ===")
            results[array_type] = {}
            
            for name, func in algorithms.items():
                try:
                    # Skip slow algorithms for large arrays
                    if len(array) > 100 and name in ['Bubble Sort', 'Selection Sort']:
                        continue
                    
                    execution_time, sorted_array = SortingAnalyzer.time_algorithm(func, array)
                    is_correct = SortingAnalyzer.is_sorted(sorted_array)
                    
                    results[array_type][name] = {
                        'time': execution_time,
                        'correct': is_correct
                    }
                    
                    print(f"{name}: {execution_time:.6f}s - {'✓' if is_correct else '✗'}")
                    
                except Exception as e:
                    print(f"{name}: Error - {str(e)}")
        
        return results


def test_sorting_algorithms():
    """Test all sorting algorithms"""
    print("=== Testing Sorting Algorithms ===\n")
    
    # Test with small array first
    test_arr = [64, 34, 25, 12, 22, 11, 90, 5]
    print(f"Original array: {test_arr}")
    print()
    
    sorter = SortingAlgorithms()
    
    # Test each algorithm
    algorithms = [
        ('Bubble Sort', sorter.bubble_sort),
        ('Selection Sort', sorter.selection_sort),
        ('Insertion Sort', sorter.insertion_sort),
        ('Merge Sort', sorter.merge_sort),
        ('Quick Sort', sorter.quick_sort),
        ('Heap Sort', sorter.heap_sort),
        ('Counting Sort', sorter.counting_sort),
        ('Radix Sort', sorter.radix_sort)
    ]
    
    for name, func in algorithms:
        try:
            result = func(test_arr)
            print(f"{name}: {result}")
            print(f"Correctly sorted: {SortingAnalyzer.is_sorted(result)}")
            print()
        except Exception as e:
            print(f"{name}: Error - {str(e)}")
            print()
    
    # Performance comparison
    print("=== Performance Analysis ===")
    analyzer = SortingAnalyzer()
    test_arrays = analyzer.generate_test_arrays()
    
    # Use smaller arrays for demonstration
    small_test_arrays = {
        'random': test_arrays['random'][:100],
        'sorted': test_arrays['sorted'][:100],
        'reverse_sorted': test_arrays['reverse_sorted'][:100]
    }
    
    analyzer.compare_algorithms(small_test_arrays)


if __name__ == "__main__":
    test_sorting_algorithms()
