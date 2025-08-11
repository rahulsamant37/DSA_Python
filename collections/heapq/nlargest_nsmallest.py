"""
heapq nlargest and nsmallest - Finding top/bottom N elements efficiently

nlargest() and nsmallest() provide efficient ways to find the N largest or smallest
elements without fully sorting the data. Essential for top-K problems in algorithms.
"""

import heapq
import random
import time

def nlargest_examples():
    """Demonstrates nlargest function usage"""
    
    print("--- heapq.nlargest Examples ---")
    
    # Basic usage
    numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(f"Numbers: {numbers}")
    
    # Find largest elements
    for k in [1, 3, 5]:
        largest = heapq.nlargest(k, numbers)
        print(f"Top {k} largest: {largest}")
    
    print()
    
    # Edge cases
    print("--- Edge Cases ---")
    
    # k larger than list size
    k_large = heapq.nlargest(20, numbers)
    print(f"Top 20 from {len(numbers)} elements: {k_large}")
    
    # k = 0
    k_zero = heapq.nlargest(0, numbers)
    print(f"Top 0 elements: {k_zero}")
    
    # Empty list
    k_empty = heapq.nlargest(3, [])
    print(f"Top 3 from empty list: {k_empty}")
    print()

def nsmallest_examples():
    """Demonstrates nsmallest function usage"""
    
    print("--- heapq.nsmallest Examples ---")
    
    numbers = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(f"Numbers: {numbers}")
    
    # Find smallest elements
    for k in [1, 3, 5]:
        smallest = heapq.nsmallest(k, numbers)
        print(f"Top {k} smallest: {smallest}")
    
    print()

def with_key_function():
    """Using key parameter for custom comparison"""
    
    print("--- Using Key Function ---")
    
    # Example 1: Find longest/shortest strings
    words = ["python", "java", "c", "javascript", "go", "rust", "typescript"]
    print(f"Words: {words}")
    
    longest = heapq.nlargest(3, words, key=len)
    shortest = heapq.nsmallest(3, words, key=len)
    
    print(f"3 longest words: {longest}")
    print(f"3 shortest words: {shortest}")
    print()
    
    # Example 2: Custom objects
    print("--- Custom Objects ---")
    
    class Student:
        def __init__(self, name, grade):
            self.name = name
            self.grade = grade
        
        def __repr__(self):
            return f"Student('{self.name}', {self.grade})"
    
    students = [
        Student("Alice", 85),
        Student("Bob", 92),
        Student("Charlie", 78),
        Student("Diana", 96),
        Student("Eve", 89)
    ]
    
    print("Students:", students)
    
    # Top students by grade
    top_students = heapq.nlargest(3, students, key=lambda s: s.grade)
    bottom_students = heapq.nsmallest(2, students, key=lambda s: s.grade)
    
    print(f"Top 3 students: {top_students}")
    print(f"Bottom 2 students: {bottom_students}")
    print()
    
    # Example 3: Multiple criteria
    print("--- Multiple Criteria ---")
    
    # Find by name length, then alphabetically
    longest_names = heapq.nlargest(3, words, key=lambda w: (len(w), w))
    print(f"Longest names (with tiebreaker): {longest_names}")
    print()

def performance_comparison():
    """Compare performance with sorting and other methods"""
    
    print("--- Performance Comparison ---")
    
    # Generate large dataset
    size = 1000000
    k = 10
    data = [random.randint(1, 1000000) for _ in range(size)]
    
    print(f"Dataset size: {size:,}, finding top {k}")
    
    # Method 1: Using nlargest
    start_time = time.time()
    result1 = heapq.nlargest(k, data)
    nlargest_time = time.time() - start_time
    
    # Method 2: Full sort + slice
    start_time = time.time()
    result2 = sorted(data, reverse=True)[:k]
    sort_time = time.time() - start_time
    
    # Method 3: Manual heap approach
    start_time = time.time()
    heap = []
    for num in data:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
    result3 = sorted(heap, reverse=True)
    manual_heap_time = time.time() - start_time
    
    print(f"nlargest time: {nlargest_time:.4f} seconds")
    print(f"Full sort time: {sort_time:.4f} seconds")
    print(f"Manual heap time: {manual_heap_time:.4f} seconds")
    
    print(f"nlargest is {sort_time/nlargest_time:.1f}x faster than sorting")
    print(f"Results match: {result1 == result2 == result3}")
    print()

def when_to_use():
    """Guidelines on when to use nlargest/nsmallest vs alternatives"""
    
    print("--- When to Use nlargest/nsmallest ---")
    
    print("Use nlargest/nsmallest when:")
    print("✓ k << n (finding few elements from many)")
    print("✓ You don't need the entire sorted array")
    print("✓ Memory efficiency is important")
    print("✓ You have custom comparison logic (key function)")
    print()
    
    print("Use sorting when:")
    print("✓ k is close to n")
    print("✓ You need the entire sorted array")
    print("✓ You'll be accessing elements in sorted order repeatedly")
    print()
    
    print("Use min/max when:")
    print("✓ k = 1 (finding single minimum/maximum)")
    print("✓ Simple comparison without custom key")
    print()

def dsa_use_cases():
    """DSA applications of nlargest and nsmallest"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Top K elements in array
    print("1. Top K Elements Problem:")
    def top_k_elements(nums, k):
        """
        Find k largest elements in array.
        Time Complexity: O(n log k) for nlargest
        """
        return heapq.nlargest(k, nums)
    
    nums = [3, 2, 1, 5, 6, 4]
    k = 2
    result = top_k_elements(nums, k)
    print(f"Array: {nums}, k={k}")
    print(f"Top {k} elements: {result}")
    print()
    
    # Use Case 2: Kth largest element
    print("2. Kth Largest Element:")
    def find_kth_largest(nums, k):
        """
        Find the kth largest element.
        Time Complexity: O(n log k)
        """
        return heapq.nlargest(k, nums)[-1]
    
    nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    k = 4
    result = find_kth_largest(nums, k)
    print(f"Array: {nums}")
    print(f"{k}th largest element: {result}")
    print()
    
    # Use Case 3: Top K frequent words
    print("3. Top K Frequent Words:")
    def top_k_frequent_words(words, k):
        """
        Find k most frequent words, sorted by frequency then lexicographically.
        """
        from collections import Counter
        
        count = Counter(words)
        
        # Use nlargest with custom key for frequency (desc) and word (asc)
        return heapq.nlargest(k, count.keys(), key=lambda w: (count[w], -ord(w[0])))
    
    words = ["i", "love", "leetcode", "i", "love", "coding"]
    k = 2
    result = top_k_frequent_words(words, k)
    print(f"Words: {words}")
    print(f"Top {k} frequent words: {result}")
    print()
    
    # Use Case 4: Closest points to origin
    print("4. K Closest Points to Origin:")
    def k_closest_points(points, k):
        """
        Find k points closest to origin (0, 0).
        Time Complexity: O(n log k)
        """
        def distance_squared(point):
            return point[0]**2 + point[1]**2
        
        return heapq.nsmallest(k, points, key=distance_squared)
    
    points = [[1, 1], [2, 2], [0, 1], [3, 1], [1, 0]]
    k = 2
    result = k_closest_points(points, k)
    print(f"Points: {points}")
    print(f"{k} closest points to origin: {result}")
    print()
    
    # Use Case 5: Meeting rooms - find rooms that end earliest
    print("5. Meeting Rooms - Earliest Ending:")
    def earliest_ending_meetings(meetings, k):
        """
        Find k meetings that end earliest.
        Each meeting is [start_time, end_time].
        """
        return heapq.nsmallest(k, meetings, key=lambda m: m[1])
    
    meetings = [[9, 10], [4, 6], [6, 8], [1, 3], [2, 4]]
    k = 3
    result = earliest_ending_meetings(meetings, k)
    print(f"Meetings: {meetings}")
    print(f"{k} earliest ending meetings: {result}")
    print()
    
    # Use Case 6: Stock picker - find best/worst performing stocks
    print("6. Stock Performance Analysis:")
    def analyze_stock_performance(stocks, k):
        """
        Find top k and bottom k performing stocks.
        Each stock is (symbol, return_percentage).
        """
        top_performers = heapq.nlargest(k, stocks, key=lambda s: s[1])
        worst_performers = heapq.nsmallest(k, stocks, key=lambda s: s[1])
        
        return top_performers, worst_performers
    
    stocks = [
        ("AAPL", 15.2), ("GOOGL", 8.7), ("TSLA", -5.3),
        ("MSFT", 12.1), ("AMZN", 3.4), ("META", -2.1),
        ("NVDA", 25.6), ("NFLX", -8.9)
    ]
    
    k = 3
    top, bottom = analyze_stock_performance(stocks, k)
    print(f"Stocks: {stocks}")
    print(f"Top {k} performers: {top}")
    print(f"Bottom {k} performers: {bottom}")

if __name__ == "__main__":
    nlargest_examples()
    nsmallest_examples()
    with_key_function()
    performance_comparison()
    when_to_use()
    dsa_use_cases()
