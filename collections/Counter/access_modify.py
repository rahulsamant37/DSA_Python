"""
Counter Access and Modification - Getting, setting, and deleting counts

Counter behaves like a dictionary but returns 0 for missing keys instead of KeyError.
This makes it very convenient for frequency counting without checking key existence.
"""

from collections import Counter

def access_operations():
    """Demonstrates various ways to access counter values"""
    
    print("--- Counter Access Operations ---")
    
    counter = Counter(['a', 'b', 'b', 'c', 'c', 'c'])
    print(f"Counter: {counter}")
    print()
    
    # 1. Get count for existing key
    print("1. Access existing keys:")
    print(f"counter['a'] = {counter['a']}")
    print(f"counter['b'] = {counter['b']}")
    print(f"counter['c'] = {counter['c']}")
    print()
    
    # 2. Get count for non-existing key (returns 0, no KeyError)
    print("2. Access non-existing keys:")
    print(f"counter['d'] = {counter['d']}")  # Returns 0, not KeyError
    print(f"counter['xyz'] = {counter['xyz']}")
    print()
    
    # 3. Using get() method
    print("3. Using get() method:")
    print(f"counter.get('a') = {counter.get('a')}")
    print(f"counter.get('d') = {counter.get('d')}")
    print(f"counter.get('d', -1) = {counter.get('d', -1)}")  # Custom default
    print()
    
    # 4. Check if key exists
    print("4. Check key existence:")
    print(f"'a' in counter: {'a' in counter}")
    print(f"'d' in counter: {'d' in counter}")
    print()

def modification_operations():
    """Demonstrates how to modify counter values"""
    
    print("--- Counter Modification Operations ---")
    
    counter = Counter(['a', 'b', 'b'])
    print(f"Original counter: {counter}")
    
    # 1. Set count directly
    print("\n1. Direct assignment:")
    counter['c'] = 3
    counter['a'] = 5  # Overwrite existing
    print(f"After setting c=3, a=5: {counter}")
    
    # 2. Increment count
    print("\n2. Increment counts:")
    counter['b'] += 2
    counter['d'] += 1  # Creates new key with count 1
    print(f"After incrementing b by 2, d by 1: {counter}")
    
    # 3. Decrement count
    print("\n3. Decrement counts:")
    counter['a'] -= 2
    counter['c'] -= 1
    print(f"After decrementing a by 2, c by 1: {counter}")
    
    # 4. Delete entries
    print("\n4. Delete entries:")
    del counter['d']
    print(f"After deleting 'd': {counter}")
    
    # 5. Set count to 0 (doesn't automatically remove)
    counter['b'] = 0
    print(f"After setting b=0: {counter}")
    
    # 6. Remove zero and negative counts
    print("\n5. Clean up zero/negative counts:")
    counter['e'] = -1
    print(f"With negative count: {counter}")
    
    # +counter removes zero and negative counts
    cleaned_counter = +counter
    print(f"After +counter: {cleaned_counter}")
    print()

def dsa_use_cases():
    """DSA applications of counter access and modification"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Sliding window character frequency
    print("1. Sliding Window - Longest Substring Without Repeating Characters:")
    def length_of_longest_substring(s):
        """
        Find length of longest substring without repeating characters.
        Time Complexity: O(n)
        """
        char_count = Counter()
        left = 0
        max_length = 0
        
        for right in range(len(s)):
            # Add current character
            char_count[s[right]] += 1
            
            # Shrink window while we have duplicates
            while char_count[s[right]] > 1:
                char_count[s[left]] -= 1
                if char_count[s[left]] == 0:
                    del char_count[s[left]]
                left += 1
            
            max_length = max(max_length, right - left + 1)
        
        return max_length
    
    test_string = "abcabcbb"
    result = length_of_longest_substring(test_string)
    print(f"String: '{test_string}'")
    print(f"Longest substring length: {result}")
    print()
    
    # Use Case 2: Check if permutation exists
    print("2. Check Valid Permutation in String:")
    def check_inclusion(s1, s2):
        """
        Check if s1's permutation is a substring of s2.
        Time Complexity: O(n)
        """
        if len(s1) > len(s2):
            return False
        
        s1_count = Counter(s1)
        window_count = Counter()
        
        # Initialize sliding window
        for i in range(len(s1)):
            window_count[s2[i]] += 1
        
        if window_count == s1_count:
            return True
        
        # Slide the window
        for i in range(len(s1), len(s2)):
            # Add new character
            window_count[s2[i]] += 1
            
            # Remove old character
            old_char = s2[i - len(s1)]
            window_count[old_char] -= 1
            if window_count[old_char] == 0:
                del window_count[old_char]
            
            if window_count == s1_count:
                return True
        
        return False
    
    s1 = "ab"
    s2 = "eidbaooo"
    result = check_inclusion(s1, s2)
    print(f"s1: '{s1}', s2: '{s2}'")
    print(f"Permutation exists: {result}")
    print()
    
    # Use Case 3: Minimum window substring
    print("3. Character Frequency Tracking:")
    def min_window_substring(s, t):
        """
        Find minimum window in s that contains all characters of t.
        Returns the window substring.
        """
        if not s or not t or len(s) < len(t):
            return ""
        
        t_count = Counter(t)
        required = len(t_count)
        formed = 0
        
        window_count = Counter()
        left = 0
        min_len = float('inf')
        min_left = 0
        
        for right in range(len(s)):
            # Add character to window
            char = s[right]
            window_count[char] += 1
            
            # Check if frequency matches
            if char in t_count and window_count[char] == t_count[char]:
                formed += 1
            
            # Contract window
            while formed == required and left <= right:
                # Update minimum window
                if right - left + 1 < min_len:
                    min_len = right - left + 1
                    min_left = left
                
                # Remove leftmost character
                char = s[left]
                window_count[char] -= 1
                if char in t_count and window_count[char] < t_count[char]:
                    formed -= 1
                
                left += 1
        
        return s[min_left:min_left + min_len] if min_len != float('inf') else ""
    
    s = "ADOBECODEBANC"
    t = "ABC"
    result = min_window_substring(s, t)
    print(f"String: '{s}'")
    print(f"Target: '{t}'")
    print(f"Minimum window: '{result}'")

if __name__ == "__main__":
    access_operations()
    modification_operations()
    dsa_use_cases()
