"""
Counter Arithmetic Operations - Adding, subtracting, and comparing counters

Counter supports mathematical operations like addition, subtraction, 
intersection, and union. Very useful for set operations and frequency analysis in DSA.
"""

from collections import Counter

def arithmetic_operations():
    """Demonstrates arithmetic operations between counters"""
    
    print("--- Counter Arithmetic Operations ---")
    
    # Setup two counters
    counter1 = Counter(['a', 'b', 'c', 'a', 'b', 'b'])
    counter2 = Counter(['a', 'b', 'b', 'd', 'e'])
    
    print(f"Counter 1: {counter1}")
    print(f"Counter 2: {counter2}")
    print()
    
    # 1. Addition - combines counts
    print("1. Addition (+):")
    sum_counter = counter1 + counter2
    print(f"counter1 + counter2 = {sum_counter}")
    print()
    
    # 2. Subtraction - subtracts counts (keeps only positive)
    print("2. Subtraction (-):")
    diff_counter = counter1 - counter2
    print(f"counter1 - counter2 = {diff_counter}")
    print()
    
    # 3. Intersection (&) - minimum of corresponding counts
    print("3. Intersection (&):")
    intersect_counter = counter1 & counter2
    print(f"counter1 & counter2 = {intersect_counter}")
    print()
    
    # 4. Union (|) - maximum of corresponding counts
    print("4. Union (|):")
    union_counter = counter1 | counter2
    print(f"counter1 | counter2 = {union_counter}")
    print()

def update_operations():
    """Demonstrates update operations"""
    
    print("--- Update Operations ---")
    
    # 1. update() - adds counts
    print("1. update() method:")
    counter = Counter(['a', 'b', 'c'])
    print(f"Original: {counter}")
    
    counter.update(['a', 'b', 'b', 'd'])
    print(f"After update(['a', 'b', 'b', 'd']): {counter}")
    
    counter.update({'e': 2, 'f': 1})
    print(f"After update({{'e': 2, 'f': 1}}): {counter}")
    print()
    
    # 2. subtract() - subtracts counts (can go negative)
    print("2. subtract() method:")
    counter = Counter(['a', 'a', 'b', 'c'])
    print(f"Original: {counter}")
    
    counter.subtract(['a', 'b', 'b', 'd'])
    print(f"After subtract(['a', 'b', 'b', 'd']): {counter}")
    print("Note: Can have negative counts")
    print()

def dsa_use_cases():
    """DSA applications of counter arithmetic"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Compare two strings for anagram with extra characters
    print("1. Anagram with Extra Characters:")
    def min_steps_to_anagram(s, t):
        """
        Find minimum steps to make s and t anagrams by removing characters.
        Return the number of characters to remove.
        """
        counter_s = Counter(s)
        counter_t = Counter(t)
        
        # Characters that need to be removed from both strings
        diff_s = counter_s - counter_t  # Extra chars in s
        diff_t = counter_t - counter_s  # Extra chars in t
        
        return sum(diff_s.values()) + sum(diff_t.values())
    
    s = "programming"
    t = "gaming"
    steps = min_steps_to_anagram(s, t)
    print(f"String 1: '{s}'")
    print(f"String 2: '{t}'")
    print(f"Minimum steps to make anagrams: {steps}")
    print()
    
    # Use Case 2: Find common elements between two arrays
    print("2. Common Elements in Arrays:")
    def intersect_arrays(nums1, nums2):
        """
        Find intersection of two arrays including duplicates.
        Time Complexity: O(m + n)
        """
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)
        intersection = counter1 & counter2
        
        result = []
        for num, count in intersection.items():
            result.extend([num] * count)
        
        return result
    
    nums1 = [1, 2, 2, 1]
    nums2 = [2, 2]
    intersection = intersect_arrays(nums1, nums2)
    print(f"Array 1: {nums1}")
    print(f"Array 2: {nums2}")
    print(f"Intersection: {intersection}")
    print()
    
    # Use Case 3: Merge frequency maps
    print("3. Merge Multiple Frequency Maps:")
    def merge_frequency_maps(*freq_maps):
        """
        Merge multiple frequency maps into one.
        Useful for combining results from different sources.
        """
        result = Counter()
        for freq_map in freq_maps:
            result.update(freq_map)
        return result
    
    map1 = {'apple': 3, 'banana': 2}
    map2 = {'apple': 1, 'orange': 4}
    map3 = {'banana': 1, 'grape': 2}
    
    merged = merge_frequency_maps(map1, map2, map3)
    print(f"Map 1: {map1}")
    print(f"Map 2: {map2}")
    print(f"Map 3: {map3}")
    print(f"Merged: {merged}")
    print()
    
    # Use Case 4: Check if array can be divided into pairs
    print("4. Check if Array Can Form Pairs:")
    def can_arrange_pairs(arr):
        """
        Check if array elements can be arranged in pairs.
        All elements must appear an even number of times.
        """
        counter = Counter(arr)
        for count in counter.values():
            if count % 2 != 0:
                return False
        return True
    
    test_arrays = [
        [1, 2, 3, 4, 1, 2, 3, 4],  # Can form pairs
        [1, 2, 3, 1, 2],           # Cannot form pairs
        [1, 1, 2, 2, 3, 3],        # Can form pairs
    ]
    
    for arr in test_arrays:
        result = can_arrange_pairs(arr)
        print(f"Array: {arr}")
        print(f"Can form pairs: {result}")
        print()

if __name__ == "__main__":
    arithmetic_operations()
    update_operations()
    dsa_use_cases()
