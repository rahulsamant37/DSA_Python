"""
Creating defaultdict - Dictionary with default values for missing keys

defaultdict automatically creates missing keys with a default value using a factory function.
Eliminates the need for key existence checks, very useful in graph algorithms and counting.
"""

from collections import defaultdict

def create_defaultdict_examples():
    """Demonstrates different ways to create defaultdict objects"""
    
    # 1. defaultdict with int (default value 0)
    print("1. defaultdict with int (default value 0):")
    int_dict = defaultdict(int)
    print(f"Empty defaultdict(int): {dict(int_dict)}")
    
    # Accessing missing key creates it with default value
    print(f"int_dict['missing']: {int_dict['missing']}")
    print(f"After accessing 'missing': {dict(int_dict)}")
    
    # Useful for counting
    int_dict['a'] += 1
    int_dict['b'] += 3
    int_dict['a'] += 2
    print(f"After counting operations: {dict(int_dict)}")
    print()
    
    # 2. defaultdict with list (default value [])
    print("2. defaultdict with list (default value []):")
    list_dict = defaultdict(list)
    print(f"Empty defaultdict(list): {dict(list_dict)}")
    
    # Accessing missing key creates empty list
    list_dict['fruits'].append('apple')
    list_dict['fruits'].append('banana')
    list_dict['vegetables'].append('carrot')
    print(f"After adding items: {dict(list_dict)}")
    print()
    
    # 3. defaultdict with set (default value set())
    print("3. defaultdict with set (default value set()):")
    set_dict = defaultdict(set)
    set_dict['numbers'].add(1)
    set_dict['numbers'].add(2)
    set_dict['numbers'].add(1)  # Duplicate, won't be added
    set_dict['letters'].add('a')
    print(f"defaultdict(set): {dict(set_dict)}")
    print()
    
    # 4. defaultdict with str (default value '')
    print("4. defaultdict with str (default value ''):")
    str_dict = defaultdict(str)
    str_dict['greeting'] += 'Hello'
    str_dict['greeting'] += ' World'
    str_dict['empty_key']  # Just access, doesn't modify
    print(f"defaultdict(str): {dict(str_dict)}")
    print()

def custom_factory_functions():
    """Demonstrates custom factory functions"""
    
    print("--- Custom Factory Functions ---")
    
    # 1. Custom function returning a specific value
    def default_value():
        return "N/A"
    
    custom_dict = defaultdict(default_value)
    print(f"defaultdict with custom function:")
    print(f"custom_dict['missing']: {custom_dict['missing']}")
    print(f"Result: {dict(custom_dict)}")
    print()
    
    # 2. Lambda function
    lambda_dict = defaultdict(lambda: [0, 0])  # Default: [0, 0]
    lambda_dict['point1'][0] = 5  # x coordinate
    lambda_dict['point1'][1] = 3  # y coordinate
    lambda_dict['point2'][0] = 2
    print(f"defaultdict with lambda (points): {dict(lambda_dict)}")
    print()
    
    # 3. Nested defaultdict
    def make_dict():
        return defaultdict(int)
    
    nested_dict = defaultdict(make_dict)
    nested_dict['users']['alice'] += 1
    nested_dict['users']['bob'] += 2
    nested_dict['admins']['charlie'] += 1
    
    print(f"Nested defaultdict:")
    for key, value in nested_dict.items():
        print(f"  {key}: {dict(value)}")
    print()
    
    # 4. Using partial for parameterized defaults
    from functools import partial
    
    def default_counter(start=0):
        return start
    
    counter_dict = defaultdict(partial(default_counter, 100))
    counter_dict['item1'] += 5
    counter_dict['item2'] += 0  # Will be 100
    print(f"defaultdict with partial (start=100): {dict(counter_dict)}")
    print()

def converting_to_regular_dict():
    """Demonstrates conversion between defaultdict and regular dict"""
    
    print("--- Converting Between defaultdict and dict ---")
    
    # Create defaultdict
    dd = defaultdict(list)
    dd['a'].append(1)
    dd['b'].append(2)
    dd['c']  # Creates empty list
    
    print(f"Original defaultdict: {dict(dd)}")
    
    # Convert to regular dict
    regular_dict = dict(dd)
    print(f"Converted to dict: {regular_dict}")
    print(f"Type: {type(regular_dict)}")
    
    # Check behavior difference
    print("\nBehavior difference:")
    try:
        print(f"defaultdict['new_key']: {dd['new_key']}")
        print(f"After access: {dict(dd)}")
    except KeyError:
        print("This won't happen with defaultdict")
    
    try:
        print(f"regular_dict['new_key']: {regular_dict['new_key']}")
    except KeyError as e:
        print(f"regular_dict['new_key']: KeyError - {e}")
    
    # Create defaultdict from regular dict
    new_dd = defaultdict(int, regular_dict)
    print(f"\nCreated defaultdict from dict: {dict(new_dd)}")
    print(f"new_dd['another_key']: {new_dd['another_key']}")
    print()

def dsa_use_case():
    """Common DSA use case: Graph representation and traversal"""
    
    print("--- DSA Use Case: Graph Representation ---")
    
    # Adjacency list representation using defaultdict
    graph = defaultdict(list)
    
    # Add edges (no need to check if vertex exists)
    edges = [
        ('A', 'B'), ('A', 'C'), ('B', 'D'), 
        ('C', 'D'), ('C', 'E'), ('D', 'E')
    ]
    
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)  # Undirected graph
    
    print("Graph adjacency list:")
    for vertex in sorted(graph.keys()):
        print(f"  {vertex}: {graph[vertex]}")
    print()
    
    # BFS using defaultdict for visited tracking
    def bfs(graph, start):
        """BFS traversal using defaultdict for clean code"""
        from collections import deque
        
        visited = defaultdict(bool)  # Default: False
        queue = deque([start])
        visited[start] = True
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in graph[vertex]:
                if not visited[neighbor]:  # Clean check without KeyError
                    visited[neighbor] = True
                    queue.append(neighbor)
        
        return result
    
    traversal = bfs(graph, 'A')
    print(f"BFS traversal from 'A': {traversal}")
    
    # Count degrees (defaultdict makes this very clean)
    degree_count = defaultdict(int)
    for vertex, neighbors in graph.items():
        degree_count[len(neighbors)] += 1
    
    print(f"Degree distribution: {dict(degree_count)}")

if __name__ == "__main__":
    create_defaultdict_examples()
    custom_factory_functions()
    converting_to_regular_dict()
    dsa_use_case()
