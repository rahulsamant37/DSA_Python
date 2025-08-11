"""
defaultdict for counting - Frequency counting without key checks

defaultdict(int) is perfect for counting operations since it automatically
initializes missing keys with 0. Essential for frequency analysis in algorithms.
"""

from collections import defaultdict

def basic_counting():
    """Demonstrates basic counting operations with defaultdict"""
    
    print("--- Basic Counting Operations ---")
    
    # Count characters in a string
    text = "programming"
    
    # Without defaultdict (verbose)
    char_count_regular = {}
    for char in text:
        if char in char_count_regular:
            char_count_regular[char] += 1
        else:
            char_count_regular[char] = 1
    
    print(f"Text: '{text}'")
    print("Character count without defaultdict:")
    for char in sorted(char_count_regular.keys()):
        print(f"  '{char}': {char_count_regular[char]}")
    print()
    
    # With defaultdict (clean)
    char_count_default = defaultdict(int)
    for char in text:
        char_count_default[char] += 1
    
    print("Character count with defaultdict:")
    for char in sorted(char_count_default.keys()):
        print(f"  '{char}': {char_count_default[char]}")
    print()

def count_list_elements():
    """Count elements in a list"""
    
    print("--- Count List Elements ---")
    
    numbers = [1, 2, 3, 2, 1, 3, 4, 2, 1, 5, 4, 3]
    
    # Count frequencies
    frequency = defaultdict(int)
    for num in numbers:
        frequency[num] += 1
    
    print(f"Numbers: {numbers}")
    print("Frequency count:")
    for num in sorted(frequency.keys()):
        print(f"  {num}: {frequency[num]} times")
    
    # Find most frequent element
    most_frequent = max(frequency.items(), key=lambda x: x[1])
    print(f"Most frequent: {most_frequent[0]} (appears {most_frequent[1]} times)")
    print()

def count_words():
    """Count words in text"""
    
    print("--- Word Counting ---")
    
    text = "the quick brown fox jumps over the lazy dog the fox is quick"
    words = text.split()
    
    word_count = defaultdict(int)
    for word in words:
        word_count[word.lower()] += 1
    
    print(f"Text: '{text}'")
    print("Word frequencies:")
    
    # Sort by frequency (descending)
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    for word, count in sorted_words:
        print(f"  '{word}': {count}")
    print()

def incremental_counting():
    """Demonstrates incremental counting operations"""
    
    print("--- Incremental Counting ---")
    
    counter = defaultdict(int)
    
    # Simulate events
    events = [
        ('login', 'user1'), ('purchase', 'user1'), ('login', 'user2'),
        ('logout', 'user1'), ('purchase', 'user2'), ('login', 'user1'),
        ('purchase', 'user1'), ('logout', 'user2')
    ]
    
    print("Processing events:")
    for event_type, user in events:
        counter[event_type] += 1
        print(f"Event: {event_type} by {user} - Count: {dict(counter)}")
    
    print(f"\nFinal event counts: {dict(counter)}")
    print()

def conditional_counting():
    """Count based on conditions"""
    
    print("--- Conditional Counting ---")
    
    data = [
        {'name': 'Alice', 'age': 25, 'city': 'NYC'},
        {'name': 'Bob', 'age': 30, 'city': 'LA'},
        {'name': 'Charlie', 'age': 25, 'city': 'NYC'},
        {'name': 'David', 'age': 35, 'city': 'Chicago'},
        {'name': 'Eve', 'age': 30, 'city': 'LA'},
        {'name': 'Frank', 'age': 25, 'city': 'Chicago'}
    ]
    
    # Count by city
    city_count = defaultdict(int)
    for person in data:
        city_count[person['city']] += 1
    
    print("Count by city:")
    for city, count in sorted(city_count.items()):
        print(f"  {city}: {count}")
    
    # Count by age group
    age_group_count = defaultdict(int)
    for person in data:
        age = person['age']
        if age < 30:
            age_group_count['young'] += 1
        elif age < 35:
            age_group_count['middle'] += 1
        else:
            age_group_count['senior'] += 1
    
    print("Count by age group:")
    for group, count in age_group_count.items():
        print(f"  {group}: {count}")
    print()

def dsa_use_cases():
    """DSA applications of counting with defaultdict"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Two Sum with frequency count
    print("1. Two Sum with Duplicates:")
    def two_sum_count(nums, target):
        """
        Find all pairs that sum to target, handle duplicates.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        count = defaultdict(int)
        pairs = []
        
        # Count frequencies
        for num in nums:
            count[num] += 1
        
        seen = set()
        for num in nums:
            complement = target - num
            
            if complement in count and complement not in seen:
                if complement == num:
                    # Same number, need at least 2 occurrences
                    if count[num] >= 2:
                        pairs.append((num, complement))
                        seen.add(num)
                else:
                    # Different numbers
                    if num not in seen:
                        pairs.append((num, complement))
                        seen.add(num)
                        seen.add(complement)
        
        return pairs
    
    nums = [2, 7, 11, 15, 2, 3, 4]
    target = 9
    pairs = two_sum_count(nums, target)
    print(f"Array: {nums}, Target: {target}")
    print(f"Pairs that sum to {target}: {pairs}")
    print()
    
    # Use Case 2: First non-repeating character
    print("2. First Non-Repeating Character:")
    def first_non_repeating_char(s):
        """
        Find the first character that appears exactly once.
        Time Complexity: O(n), Space Complexity: O(1) for limited alphabet
        """
        count = defaultdict(int)
        
        # Count all characters
        for char in s:
            count[char] += 1
        
        # Find first character with count 1
        for char in s:
            if count[char] == 1:
                return char
        
        return None
    
    test_strings = ["leetcode", "loveleetcode", "programming", "aabbcc"]
    for s in test_strings:
        result = first_non_repeating_char(s)
        print(f"'{s}' -> First non-repeating: {result}")
    print()
    
    # Use Case 3: Majority element
    print("3. Majority Element (appears > n/2 times):")
    def find_majority_element(nums):
        """
        Find element that appears more than n/2 times.
        Time Complexity: O(n), Space Complexity: O(n)
        """
        count = defaultdict(int)
        n = len(nums)
        
        for num in nums:
            count[num] += 1
            if count[num] > n // 2:
                return num
        
        return None
    
    test_arrays = [
        [3, 2, 3],
        [2, 2, 1, 1, 1, 2, 2],
        [1, 1, 1, 2, 2, 3],
        [1]
    ]
    
    for arr in test_arrays:
        majority = find_majority_element(arr)
        print(f"{arr} -> Majority element: {majority}")
    print()
    
    # Use Case 4: Count valid triangles
    print("4. Count Valid Triangles:")
    def count_triangles(sides):
        """
        Count how many valid triangles can be formed.
        A triangle is valid if sum of any two sides > third side.
        """
        from collections import Counter
        
        # Count frequency of each side length
        side_count = defaultdict(int)
        for side in sides:
            side_count[side] += 1
        
        valid_triangles = 0
        sides_list = list(side_count.keys())
        n = len(sides_list)
        
        # Check all combinations
        for i in range(n):
            for j in range(i, n):
                for k in range(j, n):
                    a, b, c = sides_list[i], sides_list[j], sides_list[k]
                    
                    # Check triangle inequality
                    if a + b > c and b + c > a and a + c > b:
                        # Calculate number of such triangles based on frequency
                        if i == j == k:  # All same
                            freq = side_count[a]
                            if freq >= 3:
                                # C(freq, 3) combinations
                                valid_triangles += freq * (freq - 1) * (freq - 2) // 6
                        elif i == j:  # Two same, one different
                            freq_a = side_count[a]
                            freq_c = side_count[c]
                            if freq_a >= 2:
                                # C(freq_a, 2) * freq_c
                                valid_triangles += (freq_a * (freq_a - 1) // 2) * freq_c
                        elif j == k:  # Two same, one different
                            freq_a = side_count[a]
                            freq_b = side_count[b]
                            if freq_b >= 2:
                                valid_triangles += freq_a * (freq_b * (freq_b - 1) // 2)
                        else:  # All different
                            valid_triangles += side_count[a] * side_count[b] * side_count[c]
        
        return valid_triangles
    
    triangle_sides = [3, 4, 5, 3, 4, 6, 7, 8]
    count = count_triangles(triangle_sides)
    print(f"Side lengths: {triangle_sides}")
    print(f"Number of valid triangles: {count}")
    print()
    
    # Use Case 5: Degree distribution in graph
    print("5. Graph Degree Distribution:")
    def analyze_graph_degrees(edges):
        """
        Analyze the degree distribution of vertices in a graph.
        Time Complexity: O(E), Space Complexity: O(V)
        """
        vertex_degree = defaultdict(int)
        
        # Count degree for each vertex
        for u, v in edges:
            vertex_degree[u] += 1
            vertex_degree[v] += 1
        
        # Count vertices by degree
        degree_count = defaultdict(int)
        for vertex, degree in vertex_degree.items():
            degree_count[degree] += 1
        
        return vertex_degree, degree_count
    
    graph_edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'),
        ('C', 'D'), ('C', 'E'), ('D', 'E'), ('E', 'F')
    ]
    
    vertex_degrees, degree_distribution = analyze_graph_degrees(graph_edges)
    
    print(f"Graph edges: {graph_edges}")
    print("Vertex degrees:")
    for vertex in sorted(vertex_degrees.keys()):
        print(f"  {vertex}: {vertex_degrees[vertex]}")
    
    print("Degree distribution:")
    for degree in sorted(degree_distribution.keys()):
        count = degree_distribution[degree]
        print(f"  Degree {degree}: {count} vertices")

if __name__ == "__main__":
    basic_counting()
    count_list_elements()
    count_words()
    incremental_counting()
    conditional_counting()
    dsa_use_cases()
