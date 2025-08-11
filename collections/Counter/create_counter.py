"""
Creating a Counter - Basic initialization and creation methods

Counter is a subclass of dict that's designed for counting hashable objects.
It's particularly useful in DSA for frequency counting problems.
"""

from collections import Counter

def create_counter_examples():
    """Demonstrates different ways to create a Counter object"""
    
    # 1. Create from a list/sequence
    print("1. Creating Counter from a list:")
    numbers = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
    counter_from_list = Counter(numbers)
    print(f"Input: {numbers}")
    print(f"Counter: {counter_from_list}")
    print()
    
    # 2. Create from a string
    print("2. Creating Counter from a string:")
    text = "programming"
    counter_from_string = Counter(text)
    print(f"Input: '{text}'")
    print(f"Counter: {counter_from_string}")
    print()
    
    # 3. Create from keyword arguments
    print("3. Creating Counter from keyword arguments:")
    counter_from_kwargs = Counter(red=4, blue=2, green=1)
    print(f"Counter: {counter_from_kwargs}")
    print()
    
    # 4. Create from dictionary
    print("4. Creating Counter from dictionary:")
    freq_dict = {'a': 3, 'b': 1, 'c': 2}
    counter_from_dict = Counter(freq_dict)
    print(f"Input dict: {freq_dict}")
    print(f"Counter: {counter_from_dict}")
    print()
    
    # 5. Create empty Counter
    print("5. Creating empty Counter:")
    empty_counter = Counter()
    print(f"Empty Counter: {empty_counter}")
    print(f"Type: {type(empty_counter)}")

def dsa_use_case():
    """Common DSA use case: Finding character frequency in a string"""
    print("\n--- DSA Use Case: Character Frequency ---")
    
    # Problem: Check if two strings are anagrams
    def are_anagrams(str1, str2):
        return Counter(str1.lower()) == Counter(str2.lower())
    
    test_cases = [
        ("listen", "silent"),
        ("evil", "vile"),
        ("hello", "world"),
        ("stressed", "desserts")
    ]
    
    for str1, str2 in test_cases:
        result = are_anagrams(str1, str2)
        print(f"'{str1}' and '{str2}' are anagrams: {result}")

if __name__ == "__main__":
    create_counter_examples()
    dsa_use_case()
