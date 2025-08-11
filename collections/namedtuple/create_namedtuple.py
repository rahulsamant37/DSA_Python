"""
namedtuple basics - Creating tuple subclasses with named fields

namedtuple creates tuple subclasses with named fields, providing both tuple efficiency
and dot notation access. Essential for creating lightweight, immutable data structures.
"""

from collections import namedtuple

def basic_namedtuple():
    """Demonstrates basic namedtuple creation and usage"""
    
    print("--- Basic namedtuple Usage ---")
    
    # Create a namedtuple class
    Point = namedtuple('Point', ['x', 'y'])
    print(f"Point class created: {Point}")
    print(f"Point.__name__: {Point.__name__}")
    print(f"Point._fields: {Point._fields}")
    print()
    
    # Create instances
    p1 = Point(3, 4)
    p2 = Point(x=1, y=2)  # Can use keyword arguments
    
    print(f"p1 = Point(3, 4): {p1}")
    print(f"p2 = Point(x=1, y=2): {p2}")
    print()
    
    # Access fields
    print("--- Field Access ---")
    print(f"p1.x: {p1.x}")
    print(f"p1.y: {p1.y}")
    print(f"p1[0]: {p1[0]}")  # Also supports indexing
    print(f"p1[1]: {p1[1]}")
    print()
    
    # namedtuple is still a tuple
    print("--- Tuple Behavior ---")
    print(f"isinstance(p1, tuple): {isinstance(p1, tuple)}")
    print(f"len(p1): {len(p1)}")
    print(f"p1 + p2: {p1 + p2}")  # Concatenation
    print(f"p1 * 2: {p1 * 2}")    # Repetition
    print()

def different_creation_methods():
    """Shows different ways to create namedtuple"""
    
    print("--- Different Creation Methods ---")
    
    # Method 1: List of field names
    Person1 = namedtuple('Person', ['name', 'age', 'city'])
    
    # Method 2: String with space-separated fields
    Person2 = namedtuple('Person', 'name age city')
    
    # Method 3: String with comma-separated fields
    Person3 = namedtuple('Person', 'name, age, city')
    
    # All create the same structure
    alice1 = Person1('Alice', 30, 'NYC')
    alice2 = Person2('Alice', 30, 'NYC')
    alice3 = Person3('Alice', 30, 'NYC')
    
    print(f"Method 1 (list): {alice1}")
    print(f"Method 2 (space): {alice2}")
    print(f"Method 3 (comma): {alice3}")
    print(f"All equal: {alice1 == alice2 == alice3}")
    print()

def namedtuple_parameters():
    """Demonstrates namedtuple parameters and options"""
    
    print("--- namedtuple Parameters ---")
    
    # Default behavior
    print("1. Default behavior:")
    try:
        BadExample = namedtuple('BadExample', ['field', 'class', 'def'])
    except ValueError as e:
        print(f"Error with keyword field names: {e}")
    
    # Using rename=True to handle invalid field names
    print("\n2. Using rename=True:")
    GoodExample = namedtuple('GoodExample', ['field', 'class', 'def'], rename=True)
    print(f"Fields with rename=True: {GoodExample._fields}")
    
    # Using defaults (Python 3.7+)
    print("\n3. Using defaults:")
    try:
        Config = namedtuple('Config', ['host', 'port', 'debug'], defaults=['localhost', 8080, False])
        print(f"Config fields: {Config._fields}")
        print(f"Config defaults: {Config._field_defaults}")
        
        # Create with defaults
        config1 = Config()  # All defaults
        config2 = Config('example.com')  # Override host
        config3 = Config('prod.com', 443, True)  # Override all
        
        print(f"config1 (all defaults): {config1}")
        print(f"config2 (override host): {config2}")
        print(f"config3 (override all): {config3}")
    except TypeError:
        print("defaults parameter requires Python 3.7+")
    print()

def namedtuple_methods():
    """Demonstrates namedtuple methods"""
    
    print("--- namedtuple Methods ---")
    
    Student = namedtuple('Student', ['name', 'grade', 'subject'])
    alice = Student('Alice', 'A', 'Math')
    
    print(f"Original: {alice}")
    
    # _replace() - create new instance with some fields changed
    print("\n1. _replace() method:")
    alice_physics = alice._replace(subject='Physics')
    alice_b_grade = alice._replace(grade='B')
    
    print(f"alice._replace(subject='Physics'): {alice_physics}")
    print(f"alice._replace(grade='B'): {alice_b_grade}")
    print(f"Original unchanged: {alice}")
    
    # _asdict() - convert to OrderedDict
    print("\n2. _asdict() method:")
    alice_dict = alice._asdict()
    print(f"alice._asdict(): {alice_dict}")
    print(f"Type: {type(alice_dict)}")
    
    # Can modify the dict and create new namedtuple
    alice_dict['grade'] = 'A+'
    alice_plus = Student(**alice_dict)
    print(f"Modified and recreated: {alice_plus}")
    
    # _make() - create instance from iterable
    print("\n3. _make() method:")
    data = ['Bob', 'B', 'Science']
    bob = Student._make(data)
    print(f"Student._make({data}): {bob}")
    
    # _fields - tuple of field names
    print(f"\n4. _fields attribute: {Student._fields}")
    print()

def immutability_and_hashability():
    """Demonstrates immutability and hashability of namedtuples"""
    
    print("--- Immutability and Hashability ---")
    
    Coordinate = namedtuple('Coordinate', ['x', 'y'])
    point = Coordinate(3, 4)
    
    print(f"Point: {point}")
    
    # Immutability
    print("\n1. Immutability:")
    try:
        point.x = 5  # This will fail
    except AttributeError as e:
        print(f"Trying to modify point.x: {e}")
    
    # Hashability
    print("\n2. Hashability:")
    print(f"hash(point): {hash(point)}")
    
    # Can be used as dictionary keys
    point_data = {
        Coordinate(0, 0): 'origin',
        Coordinate(1, 1): 'diagonal',
        Coordinate(3, 4): 'our point'
    }
    
    print("Using as dictionary keys:")
    for coord, description in point_data.items():
        print(f"  {coord}: {description}")
    
    # Can be used in sets
    point_set = {
        Coordinate(0, 0),
        Coordinate(1, 1),
        Coordinate(3, 4),
        Coordinate(3, 4)  # Duplicate, will be ignored
    }
    
    print(f"\nSet of points: {point_set}")
    print(f"Set length (duplicates removed): {len(point_set)}")
    print()

def comparison_with_alternatives():
    """Compares namedtuple with other data structures"""
    
    print("--- Comparison with Alternatives ---")
    
    # Data to represent
    data = ('Alice', 25, 'Engineer')
    
    # 1. Regular tuple
    person_tuple = data
    
    # 2. Dictionary
    person_dict = {'name': 'Alice', 'age': 25, 'job': 'Engineer'}
    
    # 3. namedtuple
    Person = namedtuple('Person', ['name', 'age', 'job'])
    person_named = Person(*data)
    
    # 4. Class
    class PersonClass:
        def __init__(self, name, age, job):
            self.name = name
            self.age = age
            self.job = job
        def __repr__(self):
            return f"PersonClass('{self.name}', {self.age}, '{self.job}')"
    
    person_class = PersonClass(*data)
    
    print("Data representation comparison:")
    print(f"Tuple:     {person_tuple}")
    print(f"Dict:      {person_dict}")
    print(f"namedtuple: {person_named}")
    print(f"Class:     {person_class}")
    print()
    
    # Access patterns
    print("Access patterns:")
    print(f"Tuple[0]:       {person_tuple[0]}")
    print(f"Dict['name']:   {person_dict['name']}")
    print(f"namedtuple.name: {person_named.name}")
    print(f"Class.name:     {person_class.name}")
    print()
    
    # Memory usage (approximate)
    import sys
    print("Memory usage (bytes):")
    print(f"Tuple:     {sys.getsizeof(person_tuple)}")
    print(f"Dict:      {sys.getsizeof(person_dict)}")
    print(f"namedtuple: {sys.getsizeof(person_named)}")
    print(f"Class:     {sys.getsizeof(person_class)}")
    print()

def dsa_use_case():
    """DSA use case: Graph representation with namedtuples"""
    
    print("--- DSA Use Case: Graph with Named Edges ---")
    
    # Define structures for graph representation
    Edge = namedtuple('Edge', ['source', 'destination', 'weight'])
    Vertex = namedtuple('Vertex', ['id', 'label', 'data'])
    
    # Create vertices
    vertices = [
        Vertex('A', 'Start', {'visited': False}),
        Vertex('B', 'Middle', {'visited': False}),
        Vertex('C', 'End', {'visited': False}),
        Vertex('D', 'Junction', {'visited': False})
    ]
    
    # Create edges
    edges = [
        Edge('A', 'B', 5),
        Edge('A', 'C', 10),
        Edge('B', 'D', 3),
        Edge('C', 'D', 2),
        Edge('B', 'C', 1)
    ]
    
    print("Graph representation using namedtuples:")
    print("\nVertices:")
    for vertex in vertices:
        print(f"  {vertex.id}: {vertex.label} (data: {vertex.data})")
    
    print("\nEdges:")
    for edge in edges:
        print(f"  {edge.source} -> {edge.destination} (weight: {edge.weight})")
    
    # Build adjacency list using namedtuples
    from collections import defaultdict
    
    graph = defaultdict(list)
    for edge in edges:
        graph[edge.source].append((edge.destination, edge.weight))
    
    print("\nAdjacency list:")
    for vertex_id, neighbors in graph.items():
        print(f"  {vertex_id}: {neighbors}")
    
    # Find shortest path (simple example)
    def find_path(graph, start, end, path=[]):
        """Simple path finding using namedtuple-based graph"""
        path = path + [start]
        if start == end:
            return path
        
        for neighbor, weight in graph[start]:
            if neighbor not in path:
                newpath = find_path(graph, neighbor, end, path)
                if newpath:
                    return newpath
        return None
    
    path = find_path(graph, 'A', 'D')
    print(f"\nPath from A to D: {path}")
    
    # Calculate path weight
    if path:
        total_weight = 0
        for i in range(len(path) - 1):
            current, next_vertex = path[i], path[i + 1]
            for neighbor, weight in graph[current]:
                if neighbor == next_vertex:
                    total_weight += weight
                    break
        print(f"Total path weight: {total_weight}")

if __name__ == "__main__":
    basic_namedtuple()
    different_creation_methods()
    namedtuple_parameters()
    namedtuple_methods()
    immutability_and_hashability()
    comparison_with_alternatives()
    dsa_use_case()
