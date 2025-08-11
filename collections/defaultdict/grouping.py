"""
defaultdict for grouping - Organizing data by keys

defaultdict is excellent for grouping data by categories without 
explicitly checking if keys exist. Very common in data processing and algorithms.
"""

from collections import defaultdict

def basic_grouping():
    """Demonstrates basic grouping operations with defaultdict"""
    
    print("--- Basic Grouping Operations ---")
    
    # Group words by their first letter
    words = ['apple', 'banana', 'cherry', 'apricot', 'blueberry', 'coconut']
    
    # Without defaultdict (verbose)
    groups_regular = {}
    for word in words:
        first_letter = word[0]
        if first_letter not in groups_regular:
            groups_regular[first_letter] = []
        groups_regular[first_letter].append(word)
    
    print("Grouping without defaultdict (verbose):")
    for letter in sorted(groups_regular.keys()):
        print(f"  {letter}: {groups_regular[letter]}")
    print()
    
    # With defaultdict (clean and concise)
    groups_default = defaultdict(list)
    for word in words:
        groups_default[word[0]].append(word)
    
    print("Grouping with defaultdict (clean):")
    for letter in sorted(groups_default.keys()):
        print(f"  {letter}: {groups_default[letter]}")
    print()

def group_by_length():
    """Group strings by their length"""
    
    print("--- Group by Length ---")
    
    words = ['cat', 'dog', 'elephant', 'bird', 'butterfly', 'ant', 'tiger']
    
    length_groups = defaultdict(list)
    for word in words:
        length_groups[len(word)].append(word)
    
    print("Words grouped by length:")
    for length in sorted(length_groups.keys()):
        print(f"  Length {length}: {length_groups[length]}")
    print()

def group_by_property():
    """Group numbers by various properties"""
    
    print("--- Group by Properties ---")
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 15, 16, 20]
    
    # Group by even/odd
    parity_groups = defaultdict(list)
    for num in numbers:
        parity_groups['even' if num % 2 == 0 else 'odd'].append(num)
    
    print("Numbers grouped by parity:")
    for parity in ['even', 'odd']:
        print(f"  {parity}: {parity_groups[parity]}")
    print()
    
    # Group by divisibility
    divisibility_groups = defaultdict(list)
    for num in numbers:
        if num % 3 == 0:
            divisibility_groups['divisible_by_3'].append(num)
        if num % 5 == 0:
            divisibility_groups['divisible_by_5'].append(num)
        if num % 2 == 0:
            divisibility_groups['divisible_by_2'].append(num)
    
    print("Numbers grouped by divisibility:")
    for key in sorted(divisibility_groups.keys()):
        print(f"  {key}: {divisibility_groups[key]}")
    print()

def nested_grouping():
    """Demonstrates nested grouping with multiple levels"""
    
    print("--- Nested Grouping ---")
    
    # Student data
    students = [
        {'name': 'Alice', 'grade': 'A', 'subject': 'Math'},
        {'name': 'Bob', 'grade': 'B', 'subject': 'Math'},
        {'name': 'Charlie', 'grade': 'A', 'subject': 'Science'},
        {'name': 'David', 'grade': 'B', 'subject': 'Science'},
        {'name': 'Eve', 'grade': 'A', 'subject': 'Math'},
        {'name': 'Frank', 'grade': 'C', 'subject': 'Math'},
    ]
    
    # Group by subject, then by grade
    def create_nested_dict():
        return defaultdict(list)
    
    nested_groups = defaultdict(create_nested_dict)
    
    for student in students:
        subject = student['subject']
        grade = student['grade']
        name = student['name']
        nested_groups[subject][grade].append(name)
    
    print("Students grouped by subject and grade:")
    for subject in sorted(nested_groups.keys()):
        print(f"  {subject}:")
        for grade in sorted(nested_groups[subject].keys()):
            print(f"    Grade {grade}: {nested_groups[subject][grade]}")
    print()

def dsa_use_cases():
    """DSA applications of grouping with defaultdict"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Group anagrams
    print("1. Group Anagrams:")
    def group_anagrams(words):
        """
        Group words that are anagrams of each other.
        Time Complexity: O(n * m log m) where n is number of words, m is max word length
        """
        anagram_groups = defaultdict(list)
        
        for word in words:
            # Use sorted characters as key
            key = ''.join(sorted(word.lower()))
            anagram_groups[key].append(word)
        
        # Return only groups with more than one word
        return [group for group in anagram_groups.values() if len(group) > 1]
    
    words = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat', 'tab']
    anagram_groups = group_anagrams(words)
    print(f"Input words: {words}")
    print("Anagram groups:")
    for i, group in enumerate(anagram_groups, 1):
        print(f"  Group {i}: {group}")
    print()
    
    # Use Case 2: Group intervals by overlap
    print("2. Group Overlapping Intervals:")
    def group_overlapping_intervals(intervals):
        """
        Group intervals that overlap with each other.
        Simplified version - assumes intervals are sorted by start time.
        """
        if not intervals:
            return []
        
        groups = defaultdict(list)
        current_group = 0
        
        for i, interval in enumerate(intervals):
            if i == 0:
                groups[current_group].append(interval)
            else:
                # Check if overlaps with last interval in current group
                last_interval = groups[current_group][-1]
                if interval[0] <= last_interval[1]:  # Overlap
                    groups[current_group].append(interval)
                else:  # No overlap, start new group
                    current_group += 1
                    groups[current_group].append(interval)
        
        return list(groups.values())
    
    intervals = [[1, 3], [2, 6], [8, 10], [9, 12], [15, 18]]
    grouped_intervals = group_overlapping_intervals(intervals)
    print(f"Input intervals: {intervals}")
    print("Grouped overlapping intervals:")
    for i, group in enumerate(grouped_intervals, 1):
        print(f"  Group {i}: {group}")
    print()
    
    # Use Case 3: Build graph from edge list
    print("3. Build Graph from Edge List:")
    def build_graph(edges, directed=False):
        """
        Build adjacency list representation from edge list.
        Time Complexity: O(E) where E is number of edges
        """
        graph = defaultdict(list)
        
        for u, v in edges:
            graph[u].append(v)
            if not directed:
                graph[v].append(u)
        
        return graph
    
    edges = [('A', 'B'), ('B', 'C'), ('C', 'D'), ('A', 'C'), ('B', 'D')]
    
    undirected_graph = build_graph(edges, directed=False)
    directed_graph = build_graph(edges, directed=True)
    
    print(f"Edges: {edges}")
    print("Undirected graph:")
    for vertex in sorted(undirected_graph.keys()):
        print(f"  {vertex}: {undirected_graph[vertex]}")
    
    print("Directed graph:")
    for vertex in sorted(directed_graph.keys()):
        print(f"  {vertex}: {directed_graph[vertex]}")
    print()
    
    # Use Case 4: Group elements by frequency
    print("4. Group Elements by Frequency:")
    def group_by_frequency(elements):
        """
        Group elements by their frequency of occurrence.
        Time Complexity: O(n)
        """
        # Count frequencies
        frequency_count = defaultdict(int)
        for element in elements:
            frequency_count[element] += 1
        
        # Group by frequency
        frequency_groups = defaultdict(list)
        for element, freq in frequency_count.items():
            frequency_groups[freq].append(element)
        
        return frequency_groups
    
    elements = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5]
    freq_groups = group_by_frequency(elements)
    
    print(f"Input elements: {elements}")
    print("Elements grouped by frequency:")
    for freq in sorted(freq_groups.keys(), reverse=True):
        print(f"  Frequency {freq}: {freq_groups[freq]}")
    print()
    
    # Use Case 5: Partition array based on condition
    print("5. Partition Array:")
    def partition_array(arr, condition_func):
        """
        Partition array based on a condition function.
        Returns two groups: elements that satisfy condition and those that don't.
        """
        partitions = defaultdict(list)
        
        for element in arr:
            partition_key = 'satisfies' if condition_func(element) else 'not_satisfies'
            partitions[partition_key].append(element)
        
        return partitions
    
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Partition by even/odd
    even_odd_partition = partition_array(numbers, lambda x: x % 2 == 0)
    print(f"Numbers: {numbers}")
    print("Partitioned by even:")
    print(f"  Even (satisfies): {even_odd_partition['satisfies']}")
    print(f"  Odd (not satisfies): {even_odd_partition['not_satisfies']}")
    
    # Partition by greater than 5
    gt5_partition = partition_array(numbers, lambda x: x > 5)
    print("Partitioned by > 5:")
    print(f"  > 5 (satisfies): {gt5_partition['satisfies']}")
    print(f"  <= 5 (not satisfies): {gt5_partition['not_satisfies']}")

if __name__ == "__main__":
    basic_grouping()
    group_by_length()
    group_by_property()
    nested_grouping()
    dsa_use_cases()
