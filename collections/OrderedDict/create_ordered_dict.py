"""
OrderedDict basics - Dictionary that remembers insertion order

OrderedDict maintains the order in which keys were first inserted.
While regular dicts in Python 3.7+ also maintain order, OrderedDict provides additional methods.
"""

from collections import OrderedDict

def create_ordered_dict():
    """Demonstrates creating OrderedDict in different ways"""
    
    print("--- Creating OrderedDict ---")
    
    # 1. Empty OrderedDict
    od1 = OrderedDict()
    print(f"Empty OrderedDict: {od1}")
    print(f"Type: {type(od1)}")
    print()
    
    # 2. From list of tuples
    od2 = OrderedDict([('a', 1), ('b', 2), ('c', 3)])
    print(f"From list of tuples: {od2}")
    print()
    
    # 3. From keyword arguments (order may not be preserved in older Python)
    od3 = OrderedDict(x=1, y=2, z=3)
    print(f"From keyword args: {od3}")
    print()
    
    # 4. From regular dict
    regular_dict = {'first': 1, 'second': 2, 'third': 3}
    od4 = OrderedDict(regular_dict)
    print(f"From regular dict: {od4}")
    print()
    
    # 5. Using dict comprehension-like syntax
    od5 = OrderedDict((str(i), i**2) for i in range(5))
    print(f"From generator: {od5}")
    print()

def insertion_order_demonstration():
    """Shows how OrderedDict maintains insertion order"""
    
    print("--- Insertion Order Demonstration ---")
    
    # Create OrderedDict and add items
    od = OrderedDict()
    
    items = [('z', 26), ('a', 1), ('m', 13), ('b', 2), ('y', 25)]
    
    print("Adding items in this order:")
    for key, value in items:
        od[key] = value
        print(f"Added '{key}': {value} -> {list(od.keys())}")
    
    print(f"\nFinal OrderedDict: {od}")
    print(f"Keys in insertion order: {list(od.keys())}")
    print(f"Values in insertion order: {list(od.values())}")
    print(f"Items in insertion order: {list(od.items())}")
    print()

def comparison_with_regular_dict():
    """Compares OrderedDict with regular dict"""
    
    print("--- OrderedDict vs Regular Dict ---")
    
    # Same data, different creation order
    data1 = [('a', 1), ('b', 2), ('c', 3)]
    data2 = [('b', 2), ('a', 1), ('c', 3)]  # Different order
    
    # Regular dicts
    dict1 = dict(data1)
    dict2 = dict(data2)
    
    # OrderedDicts
    od1 = OrderedDict(data1)
    od2 = OrderedDict(data2)
    
    print("Data 1:", data1)
    print("Data 2:", data2)
    print()
    
    print(f"Regular dict1: {dict1}")
    print(f"Regular dict2: {dict2}")
    print(f"dict1 == dict2: {dict1 == dict2}")  # True - content is same
    print()
    
    print(f"OrderedDict1: {od1}")
    print(f"OrderedDict2: {od2}")
    print(f"od1 == od2: {od1 == od2}")  # False - order matters!
    print()
    
    # Comparison with regular dict
    print(f"od1 == dict1: {od1 == dict1}")  # True - content comparison
    print()

def basic_operations():
    """Demonstrates basic dictionary operations on OrderedDict"""
    
    print("--- Basic Operations ---")
    
    od = OrderedDict([('name', 'Alice'), ('age', 30), ('city', 'NYC')])
    print(f"Initial: {od}")
    
    # Access
    print(f"od['name']: {od['name']}")
    print(f"od.get('age'): {od.get('age')}")
    print(f"od.get('missing', 'default'): {od.get('missing', 'default')}")
    
    # Modification
    od['age'] = 31  # Update existing key (preserves position)
    print(f"After updating age: {od}")
    
    od['country'] = 'USA'  # Add new key (goes to end)
    print(f"After adding country: {od}")
    
    # Deletion
    del od['city']
    print(f"After deleting city: {od}")
    
    # Re-adding deleted key (goes to end)
    od['city'] = 'Boston'
    print(f"After re-adding city: {od}")
    
    # Check membership
    print(f"'name' in od: {'name' in od}")
    print(f"'missing' in od: {'missing' in od}")
    
    # Length
    print(f"Length: {len(od)}")
    print()

def key_position_matters():
    """Demonstrates scenarios where key position matters"""
    
    print("--- Why Order Matters ---")
    
    # Example 1: Configuration with precedence
    print("1. Configuration with precedence:")
    config = OrderedDict([
        ('env', 'production'),
        ('debug', False),
        ('database_url', 'prod://db'),
        ('cache_timeout', 3600)
    ])
    
    print("Configuration (order shows precedence):")
    for key, value in config.items():
        print(f"  {key}: {value}")
    
    # Override settings (maintain precedence order)
    overrides = OrderedDict([('debug', True), ('cache_timeout', 1800)])
    config.update(overrides)
    
    print("After applying overrides:")
    for key, value in config.items():
        print(f"  {key}: {value}")
    print()
    
    # Example 2: Steps in a process
    print("2. Process steps (order is crucial):")
    process_steps = OrderedDict([
        ('validate_input', 'Check input parameters'),
        ('authenticate', 'Verify user credentials'),
        ('authorize', 'Check user permissions'),
        ('process_request', 'Execute main logic'),
        ('log_result', 'Record operation result')
    ])
    
    print("Process execution order:")
    for i, (step, description) in enumerate(process_steps.items(), 1):
        print(f"  {i}. {step}: {description}")
    print()

def iteration_patterns():
    """Shows different ways to iterate over OrderedDict"""
    
    print("--- Iteration Patterns ---")
    
    od = OrderedDict([('first', 1), ('second', 2), ('third', 3), ('fourth', 4)])
    print(f"OrderedDict: {od}")
    
    # Forward iteration
    print("\n1. Forward iteration:")
    print("Keys:", end=" ")
    for key in od:
        print(key, end=" ")
    print()
    
    print("Values:", end=" ")
    for value in od.values():
        print(value, end=" ")
    print()
    
    print("Items:", end=" ")
    for key, value in od.items():
        print(f"({key},{value})", end=" ")
    print()
    
    # Reverse iteration
    print("\n2. Reverse iteration:")
    print("Keys (reversed):", end=" ")
    for key in reversed(od):
        print(key, end=" ")
    print()
    
    print("Items (reversed):", end=" ")
    for key, value in reversed(od.items()):
        print(f"({key},{value})", end=" ")
    print()
    print()

def dsa_use_case():
    """DSA use case: LRU Cache implementation foundation"""
    
    print("--- DSA Use Case: LRU Cache Foundation ---")
    
    class SimpleLRUCache:
        """
        Simple LRU Cache using OrderedDict.
        This demonstrates the foundation for LRU implementation.
        """
        
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key):
            """Get value and mark as recently used"""
            if key not in self.cache:
                return -1
            
            # Move to end (most recently used)
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        
        def put(self, key, value):
            """Put key-value pair, evict LRU if needed"""
            if key in self.cache:
                # Update existing key (move to end)
                self.cache.pop(key)
            elif len(self.cache) >= self.capacity:
                # Remove least recently used (first item)
                self.cache.popitem(last=False)
            
            # Add/update key as most recently used
            self.cache[key] = value
        
        def __str__(self):
            return f"LRUCache({list(self.cache.items())})"
    
    # Demonstrate LRU cache
    cache = SimpleLRUCache(3)
    
    print("LRU Cache with capacity 3:")
    
    operations = [
        ('put', 1, 'A'), ('put', 2, 'B'), ('put', 3, 'C'),
        ('get', 1), ('put', 4, 'D'), ('get', 2), ('get', 3), ('get', 4)
    ]
    
    for op in operations:
        if op[0] == 'put':
            cache.put(op[1], op[2])
            print(f"Put({op[1]}, '{op[2]}'): {cache}")
        else:  # get
            result = cache.get(op[1])
            print(f"Get({op[1]}): {result} -> {cache}")
    
    print("\nNote: OrderedDict makes LRU implementation clean and efficient!")

if __name__ == "__main__":
    create_ordered_dict()
    insertion_order_demonstration()
    comparison_with_regular_dict()
    basic_operations()
    key_position_matters()
    iteration_patterns()
    dsa_use_case()
