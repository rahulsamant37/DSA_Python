"""
Counter.most_common() - Finding the most frequently occurring elements

The most_common() method returns a list of (element, count) tuples,
ordered from most common to least common. Essential for top-k problems in DSA.
"""

from collections import Counter

def most_common_examples():
    """Demonstrates various uses of the most_common() method"""
    
    # 1. Basic usage - all elements
    print("1. Getting all elements by frequency:")
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    counter = Counter(numbers)
    most_common_all = counter.most_common()
    print(f"Input: {numbers}")
    print(f"Most common (all): {most_common_all}")
    print()
    
    # 2. Top N most common elements
    print("2. Getting top N most common elements:")
    text = "programming language python"
    char_counter = Counter(text.replace(" ", ""))
    top_3 = char_counter.most_common(3)
    print(f"Input: '{text}' (spaces removed)")
    print(f"Top 3 most common characters: {top_3}")
    print()
    
    # 3. Empty counter
    print("3. Most common on empty counter:")
    empty_counter = Counter()
    print(f"Empty counter most_common(): {empty_counter.most_common()}")
    print()

def dsa_use_cases():
    """Common DSA applications of most_common()"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Top K Frequent Elements
    print("1. Top K Frequent Elements Problem:")
    def top_k_frequent(nums, k):
        """
        Given an array and k, return the k most frequent elements.
        Time Complexity: O(n log k) where n is length of nums
        """
        counter = Counter(nums)
        return [element for element, count in counter.most_common(k)]
    
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    result = top_k_frequent(nums, k)
    print(f"Input: {nums}, k={k}")
    print(f"Top {k} frequent elements: {result}")
    print()
    
    # Use Case 2: Majority Element
    print("2. Majority Element Problem:")
    def majority_element(nums):
        """
        Find the element that appears more than n/2 times.
        Time Complexity: O(n)
        """
        counter = Counter(nums)
        most_common = counter.most_common(1)
        return most_common[0][0] if most_common else None
    
    nums = [2, 2, 1, 1, 1, 2, 2]
    result = majority_element(nums)
    print(f"Input: {nums}")
    print(f"Majority element: {result}")
    print()
    
    # Use Case 3: First Unique Character
    print("3. First Unique Character Problem:")
    def first_unique_char(s):
        """
        Find the first character that appears exactly once.
        Time Complexity: O(n)
        """
        counter = Counter(s)
        for i, char in enumerate(s):
            if counter[char] == 1:
                return i
        return -1
    
    test_string = "leetcode"
    result = first_unique_char(test_string)
    print(f"Input: '{test_string}'")
    print(f"First unique character index: {result}")
    if result != -1:
        print(f"Character: '{test_string[result]}'")
    print()
    
    # Use Case 4: Sort Characters by Frequency
    print("4. Sort Characters by Frequency:")
    def frequency_sort(s):
        """
        Sort characters in string by frequency (descending).
        Time Complexity: O(n log n)
        """
        counter = Counter(s)
        result = ""
        for char, count in counter.most_common():
            result += char * count
        return result
    
    test_string = "tree"
    result = frequency_sort(test_string)
    print(f"Input: '{test_string}'")
    print(f"Sorted by frequency: '{result}'")

if __name__ == "__main__":
    most_common_examples()
    dsa_use_cases()
