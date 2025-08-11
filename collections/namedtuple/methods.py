"""
namedtuple methods - _replace, _asdict, _make and field access

namedtuple provides several useful methods for creating new instances,
converting to dictionaries, and working with field data efficiently.
"""

from collections import namedtuple

def replace_method():
    """Demonstrates _replace() method for creating modified copies"""
    
    print("--- _replace() Method ---")
    
    # Create a namedtuple for employee data
    Employee = namedtuple('Employee', ['name', 'department', 'salary', 'years'])
    
    john = Employee('John Doe', 'Engineering', 75000, 3)
    print(f"Original employee: {john}")
    
    # Give John a promotion (salary increase)
    john_promoted = john._replace(salary=85000)
    print(f"After promotion: {john_promoted}")
    print(f"Original unchanged: {john}")
    print()
    
    # Transfer to different department
    john_transferred = john._replace(department='Management', salary=90000)
    print(f"After transfer: {john_transferred}")
    
    # Multiple updates can be chained conceptually
    john_senior = john._replace(salary=95000)._replace(years=5)
    print(f"After senior promotion: {john_senior}")
    print()
    
    # Error handling
    print("--- Error Handling ---")
    try:
        john_invalid = john._replace(invalid_field='value')
    except TypeError as e:
        print(f"Invalid field error: {e}")
    print()

def asdict_method():
    """Demonstrates _asdict() method for dictionary conversion"""
    
    print("--- _asdict() Method ---")
    
    Book = namedtuple('Book', ['title', 'author', 'year', 'pages'])
    
    book = Book('1984', 'George Orwell', 1949, 328)
    print(f"Original book: {book}")
    
    # Convert to dictionary
    book_dict = book._asdict()
    print(f"As dictionary: {book_dict}")
    print(f"Dictionary type: {type(book_dict)}")
    print()
    
    # Dictionary can be modified
    print("--- Modifying Dictionary ---")
    book_dict['year'] = 1948  # Change publication year
    book_dict['edition'] = 'First'  # Add new field
    
    print(f"Modified dict: {book_dict}")
    
    # Create new namedtuple from modified dict (excluding extra fields)
    BookWithEdition = namedtuple('BookWithEdition', ['title', 'author', 'year', 'pages', 'edition'])
    
    # Can't directly use ** with extra fields for original Book
    try:
        book_updated = Book(**book_dict)
    except TypeError as e:
        print(f"Error with extra fields: {e}")
    
    # But can create new namedtuple type
    book_with_edition = BookWithEdition(**book_dict)
    print(f"New namedtuple with edition: {book_with_edition}")
    print()
    
    # Common pattern: update via dict manipulation
    print("--- Update Pattern ---")
    book_dict = book._asdict()
    book_dict.update({'pages': 350, 'year': 1950})  # Bulk update
    book_updated = Book(**{k: v for k, v in book_dict.items() if k in Book._fields})
    print(f"Bulk updated book: {book_updated}")
    print()

def make_method():
    """Demonstrates _make() method for creating from iterables"""
    
    print("--- _make() Method ---")
    
    Point = namedtuple('Point', ['x', 'y', 'z'])
    
    # Create from list
    coords_list = [1, 2, 3]
    point_from_list = Point._make(coords_list)
    print(f"From list {coords_list}: {point_from_list}")
    
    # Create from tuple
    coords_tuple = (4, 5, 6)
    point_from_tuple = Point._make(coords_tuple)
    print(f"From tuple {coords_tuple}: {point_from_tuple}")
    
    # Create from any iterable
    coords_range = range(7, 10)
    point_from_range = Point._make(coords_range)
    print(f"From range {list(coords_range)}: {point_from_range}")
    
    # Create from generator
    def coord_generator():
        yield 10
        yield 11
        yield 12
    
    point_from_gen = Point._make(coord_generator())
    print(f"From generator: {point_from_gen}")
    print()
    
    # Error handling
    print("--- Error Handling ---")
    try:
        Point._make([1, 2])  # Too few values
    except TypeError as e:
        print(f"Too few values: {e}")
    
    try:
        Point._make([1, 2, 3, 4])  # Too many values
    except TypeError as e:
        print(f"Too many values: {e}")
    print()

def field_access_patterns():
    """Demonstrates different field access patterns"""
    
    print("--- Field Access Patterns ---")
    
    Student = namedtuple('Student', ['name', 'age', 'major', 'gpa'])
    alice = Student('Alice Johnson', 20, 'Computer Science', 3.8)
    
    print(f"Student: {alice}")
    print()
    
    # 1. Dot notation (preferred)
    print("1. Dot notation access:")
    print(f"  Name: {alice.name}")
    print(f"  Age: {alice.age}")
    print(f"  Major: {alice.major}")
    print(f"  GPA: {alice.gpa}")
    print()
    
    # 2. Index access (tuple-like)
    print("2. Index access:")
    for i, field in enumerate(Student._fields):
        print(f"  {field}: {alice[i]}")
    print()
    
    # 3. Unpacking
    print("3. Unpacking:")
    name, age, major, gpa = alice
    print(f"  Unpacked: name={name}, age={age}, major={major}, gpa={gpa}")
    
    # Partial unpacking
    name, age, *rest = alice
    print(f"  Partial: name={name}, age={age}, rest={rest}")
    print()
    
    # 4. getattr for dynamic access
    print("4. Dynamic access with getattr:")
    field_name = 'major'
    value = getattr(alice, field_name)
    print(f"  getattr(alice, '{field_name}'): {value}")
    
    # Safe access with default
    safe_value = getattr(alice, 'nonexistent', 'Not found')
    print(f"  getattr(alice, 'nonexistent', 'Not found'): {safe_value}")
    print()

def advanced_patterns():
    """Demonstrates advanced usage patterns"""
    
    print("--- Advanced Patterns ---")
    
    # 1. Factory pattern with validation
    print("1. Factory Pattern with Validation:")
    
    class PersonFactory:
        Person = namedtuple('Person', ['name', 'age', 'email'])
        
        @classmethod
        def create_person(cls, name, age, email):
            """Create person with validation"""
            if not isinstance(name, str) or len(name) < 2:
                raise ValueError("Name must be a string with at least 2 characters")
            if not isinstance(age, int) or age < 0 or age > 150:
                raise ValueError("Age must be between 0 and 150")
            if '@' not in email:
                raise ValueError("Email must contain @")
            
            return cls.Person(name, age, email)
        
        @classmethod
        def from_string(cls, person_str):
            """Create person from string format 'name,age,email'"""
            parts = person_str.split(',')
            if len(parts) != 3:
                raise ValueError("String must have format 'name,age,email'")
            
            name, age_str, email = [part.strip() for part in parts]
            age = int(age_str)
            
            return cls.create_person(name, age, email)
    
    # Test factory
    person1 = PersonFactory.create_person("Alice Smith", 25, "alice@email.com")
    person2 = PersonFactory.from_string("Bob Jones, 30, bob@email.com")
    
    print(f"  Factory created: {person1}")
    print(f"  From string: {person2}")
    print()
    
    # 2. Transformation pipeline
    print("2. Transformation Pipeline:")
    
    def normalize_name(person):
        """Normalize name to title case"""
        return person._replace(name=person.name.title())
    
    def validate_age(person):
        """Ensure age is reasonable"""
        if person.age < 18:
            return person._replace(age=18)  # Minimum age
        return person
    
    def add_domain_if_missing(person):
        """Add default domain if email doesn't have one"""
        if '@' not in person.email:
            return person._replace(email=f"{person.email}@company.com")
        return person
    
    # Apply transformations
    raw_person = PersonFactory.Person("john doe", 15, "john.doe")
    
    print(f"  Raw: {raw_person}")
    
    # Transform step by step
    normalized = normalize_name(raw_person)
    age_validated = validate_age(normalized)
    email_fixed = add_domain_if_missing(age_validated)
    
    print(f"  Processed: {email_fixed}")
    print()

def performance_comparison():
    """Compare performance of namedtuple methods"""
    
    print("--- Performance Comparison ---")
    
    import time
    
    Point = namedtuple('Point', ['x', 'y'])
    point = Point(3, 4)
    
    # Number of operations
    n = 1000000
    
    # Test _replace performance
    start_time = time.time()
    for i in range(n):
        new_point = point._replace(x=i)
    replace_time = time.time() - start_time
    
    # Test _asdict performance
    start_time = time.time()
    for i in range(n):
        point_dict = point._asdict()
    asdict_time = time.time() - start_time
    
    # Test _make performance
    data = [1, 2]
    start_time = time.time()
    for i in range(n):
        new_point = Point._make(data)
    make_time = time.time() - start_time
    
    print(f"Operations: {n:,}")
    print(f"_replace time: {replace_time:.4f} seconds")
    print(f"_asdict time: {asdict_time:.4f} seconds")
    print(f"_make time: {make_time:.4f} seconds")
    
    print(f"\nOperations per second:")
    print(f"_replace: {n/replace_time:,.0f} ops/sec")
    print(f"_asdict: {n/asdict_time:,.0f} ops/sec")
    print(f"_make: {n/make_time:,.0f} ops/sec")
    print()

def dsa_use_cases():
    """DSA applications of namedtuple methods"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: State management in graph algorithms
    print("1. State Management in Graph Traversal:")
    
    State = namedtuple('State', ['vertex', 'distance', 'path'])
    
    def dijkstra_step_demo():
        """Demonstrate state updates in Dijkstra's algorithm"""
        # Initial state
        start_state = State('A', 0, ['A'])
        print(f"  Initial state: {start_state}")
        
        # Update distance to neighbor
        neighbor_state = start_state._replace(
            vertex='B',
            distance=5,
            path=start_state.path + ['B']
        )
        print(f"  Move to B: {neighbor_state}")
        
        # Find shorter path
        shorter_state = neighbor_state._replace(distance=3)
        print(f"  Shorter path found: {shorter_state}")
    
    dijkstra_step_demo()
    print()
    
    # Use Case 2: Coordinate transformations
    print("2. Coordinate Transformations:")
    
    Point2D = namedtuple('Point2D', ['x', 'y'])
    
    def translate(point, dx, dy):
        """Translate point by offset"""
        return point._replace(x=point.x + dx, y=point.y + dy)
    
    def scale(point, factor):
        """Scale point by factor"""
        return point._replace(x=point.x * factor, y=point.y * factor)
    
    def rotate_90_ccw(point):
        """Rotate point 90 degrees counter-clockwise"""
        return point._replace(x=-point.y, y=point.x)
    
    # Transform a point
    original = Point2D(3, 4)
    transformed = translate(scale(rotate_90_ccw(original), 2), 1, 1)
    
    print(f"  Original: {original}")
    print(f"  After rotate, scale(2), translate(1,1): {transformed}")
    print()
    
    # Use Case 3: Binary tree node manipulation
    print("3. Binary Tree Node Updates:")
    
    TreeNode = namedtuple('TreeNode', ['value', 'left', 'right'])
    
    # Build a small tree
    #     1
    #    / \
    #   2   3
    leaf2 = TreeNode(2, None, None)
    leaf3 = TreeNode(3, None, None)
    root = TreeNode(1, leaf2, leaf3)
    
    print(f"  Original tree root: {root}")
    
    # Add a new left child to node 2
    new_leaf = TreeNode(4, None, None)
    updated_leaf2 = leaf2._replace(left=new_leaf)
    updated_root = root._replace(left=updated_leaf2)
    
    print(f"  After adding node 4: {updated_root}")
    
    # Convert tree to dict for analysis
    def tree_to_dict(node):
        """Convert tree node to dictionary"""
        if node is None:
            return None
        
        node_dict = node._asdict()
        node_dict['left'] = tree_to_dict(node_dict['left'])
        node_dict['right'] = tree_to_dict(node_dict['right'])
        return node_dict
    
    tree_dict = tree_to_dict(updated_root)
    print(f"  Tree as dict: {tree_dict}")

if __name__ == "__main__":
    replace_method()
    asdict_method()
    make_method()
    field_access_patterns()
    advanced_patterns()
    performance_comparison()
    dsa_use_cases()
