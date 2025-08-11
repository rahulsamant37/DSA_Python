"""
OrderedDict move_to_end - Reordering elements efficiently

move_to_end() allows efficient reordering of elements in OrderedDict.
Essential for implementing LRU caches and maintaining priority-based ordering.
"""

from collections import OrderedDict

def basic_move_to_end():
    """Demonstrates basic move_to_end functionality"""
    
    print("--- Basic move_to_end Usage ---")
    
    od = OrderedDict([('a', 1), ('b', 2), ('c', 3), ('d', 4), ('e', 5)])
    print(f"Initial OrderedDict: {od}")
    print(f"Order: {list(od.keys())}")
    print()
    
    # Move to end (default: last=True)
    print("1. Moving to end (most recent):")
    od.move_to_end('b')
    print(f"After move_to_end('b'): {od}")
    print(f"Order: {list(od.keys())}")
    print()
    
    od.move_to_end('d')
    print(f"After move_to_end('d'): {od}")
    print(f"Order: {list(od.keys())}")
    print()
    
    # Move to beginning (last=False)
    print("2. Moving to beginning (least recent):")
    od.move_to_end('c', last=False)
    print(f"After move_to_end('c', last=False): {od}")
    print(f"Order: {list(od.keys())}")
    print()
    
    od.move_to_end('e', last=False)
    print(f"After move_to_end('e', last=False): {od}")
    print(f"Order: {list(od.keys())}")
    print()

def error_handling():
    """Demonstrates error handling with move_to_end"""
    
    print("--- Error Handling ---")
    
    od = OrderedDict([('x', 1), ('y', 2), ('z', 3)])
    print(f"OrderedDict: {od}")
    
    # Try to move non-existent key
    try:
        od.move_to_end('missing')
    except KeyError as e:
        print(f"move_to_end('missing'): KeyError - {e}")
    
    # Check that original order is unchanged
    print(f"Order unchanged: {list(od.keys())}")
    print()

def frequent_access_pattern():
    """Simulates frequent access pattern with reordering"""
    
    print("--- Frequent Access Pattern ---")
    
    # Simulate a cache with access frequency tracking
    cache = OrderedDict([
        ('user1', 'Alice'),
        ('user2', 'Bob'),
        ('user3', 'Charlie'),
        ('user4', 'Diana'),
        ('user5', 'Eve')
    ])
    
    print("Initial cache (oldest to newest):")
    for i, (key, value) in enumerate(cache.items(), 1):
        print(f"  {i}. {key}: {value}")
    print()
    
    # Simulate access pattern
    access_sequence = ['user3', 'user1', 'user5', 'user2', 'user3', 'user1']
    
    print("Simulating access pattern (moving accessed items to end):")
    for accessed_user in access_sequence:
        print(f"\nAccess {accessed_user}:")
        cache.move_to_end(accessed_user)
        
        print("  Cache order (oldest -> newest):")
        for i, (key, value) in enumerate(cache.items(), 1):
            print(f"    {i}. {key}: {value}")
    
    print(f"\nFinal order: {list(cache.keys())}")
    print("Most recently accessed items are at the end")
    print()

def priority_queue_simulation():
    """Uses move_to_end to implement priority changes"""
    
    print("--- Priority Queue with Dynamic Priorities ---")
    
    # Task queue with priorities (lower number = higher priority)
    tasks = OrderedDict([
        ('task_A', {'priority': 3, 'description': 'Low priority task'}),
        ('task_B', {'priority': 1, 'description': 'High priority task'}),
        ('task_C', {'priority': 2, 'description': 'Medium priority task'}),
        ('task_D', {'priority': 3, 'description': 'Another low priority task'})
    ])
    
    def sort_by_priority(task_dict):
        """Sort tasks by priority using move_to_end"""
        # Create list of (task_id, priority) sorted by priority
        sorted_tasks = sorted(task_dict.items(), key=lambda x: x[1]['priority'])
        
        # Move tasks to maintain priority order
        for task_id, _ in sorted_tasks:
            task_dict.move_to_end(task_id)
    
    def print_tasks(task_dict, title):
        print(f"{title}:")
        for i, (task_id, task_info) in enumerate(task_dict.items(), 1):
            priority = task_info['priority']
            desc = task_info['description']
            print(f"  {i}. {task_id} (priority {priority}): {desc}")
        print()
    
    print_tasks(tasks, "Initial task order")
    
    # Sort by priority
    sort_by_priority(tasks)
    print_tasks(tasks, "After sorting by priority")
    
    # Change priority of a task
    print("Changing task_A priority from 3 to 1 (highest):")
    tasks['task_A']['priority'] = 1
    sort_by_priority(tasks)
    print_tasks(tasks, "After priority change")
    
    # Add new urgent task
    print("Adding urgent task with priority 0:")
    tasks['task_E'] = {'priority': 0, 'description': 'URGENT task'}
    sort_by_priority(tasks)
    print_tasks(tasks, "After adding urgent task")

def lru_cache_implementation():
    """Complete LRU cache implementation using move_to_end"""
    
    print("--- LRU Cache Implementation ---")
    
    class LRUCache:
        """
        LRU Cache implementation using OrderedDict and move_to_end.
        Time Complexity: O(1) for both get and put operations.
        """
        
        def __init__(self, capacity):
            self.capacity = capacity
            self.cache = OrderedDict()
        
        def get(self, key):
            """Get value and mark as most recently used"""
            if key not in self.cache:
                return -1
            
            # Move to end (most recently used)
            self.cache.move_to_end(key)
            return self.cache[key]
        
        def put(self, key, value):
            """Put key-value pair, evict LRU if necessary"""
            if key in self.cache:
                # Update existing key and move to end
                self.cache[key] = value
                self.cache.move_to_end(key)
            else:
                # Check capacity
                if len(self.cache) >= self.capacity:
                    # Remove least recently used (first item)
                    lru_key = next(iter(self.cache))
                    del self.cache[lru_key]
                    print(f"    Evicted LRU key: {lru_key}")
                
                # Add new key-value pair
                self.cache[key] = value
        
        def __str__(self):
            items = list(self.cache.items())
            return f"LRU[{items}] (LRU -> MRU)"
    
    # Demonstrate LRU cache
    cache = LRUCache(3)
    
    operations = [
        ('put', 1, 'A'),
        ('put', 2, 'B'),
        ('put', 3, 'C'),
        ('get', 1),      # Access 1
        ('put', 4, 'D'), # Should evict 2
        ('get', 2),      # Should return -1
        ('get', 3),      # Access 3
        ('get', 4),      # Access 4
        ('put', 5, 'E')  # Should evict 1
    ]
    
    print("LRU Cache operations (capacity = 3):")
    for op in operations:
        if op[0] == 'put':
            key, value = op[1], op[2]
            cache.put(key, value)
            print(f"  Put({key}, '{value}'): {cache}")
        else:  # get
            key = op[1]
            result = cache.get(key)
            print(f"  Get({key}): {result} -> {cache}")
    print()

def performance_comparison():
    """Compare move_to_end with alternative approaches"""
    
    print("--- Performance Comparison ---")
    
    import time
    
    # Method 1: Using move_to_end
    def access_with_move_to_end(od, key):
        """Access item using move_to_end"""
        if key in od:
            od.move_to_end(key)
            return od[key]
        return None
    
    # Method 2: Delete and re-insert (less efficient)
    def access_with_delete_insert(od, key):
        """Access item by deleting and re-inserting"""
        if key in od:
            value = od.pop(key)
            od[key] = value
            return value
        return None
    
    # Setup test data
    size = 10000
    od1 = OrderedDict((i, f"value_{i}") for i in range(size))
    od2 = OrderedDict((i, f"value_{i}") for i in range(size))
    
    # Test keys to access
    test_keys = list(range(0, size, 100))  # Every 100th key
    
    # Test move_to_end method
    start_time = time.time()
    for key in test_keys:
        access_with_move_to_end(od1, key)
    move_to_end_time = time.time() - start_time
    
    # Test delete-insert method
    start_time = time.time()
    for key in test_keys:
        access_with_delete_insert(od2, key)
    delete_insert_time = time.time() - start_time
    
    print(f"Accessing {len(test_keys)} keys in OrderedDict of size {size:,}:")
    print(f"move_to_end method: {move_to_end_time:.6f} seconds")
    print(f"delete-insert method: {delete_insert_time:.6f} seconds")
    print(f"move_to_end is {delete_insert_time/move_to_end_time:.1f}x faster")
    print()

def dsa_use_cases():
    """Additional DSA use cases for move_to_end"""
    
    print("--- Additional DSA Use Cases ---")
    
    # Use Case 1: MRU (Most Recently Used) List
    print("1. Most Recently Used (MRU) List:")
    class MRUList:
        """Maintains a list of most recently used items"""
        
        def __init__(self, max_size=5):
            self.max_size = max_size
            self.items = OrderedDict()
        
        def access(self, item):
            """Mark item as most recently used"""
            if item in self.items:
                self.items.move_to_end(item)
            else:
                if len(self.items) >= self.max_size:
                    # Remove least recently used
                    oldest = next(iter(self.items))
                    del self.items[oldest]
                self.items[item] = True
        
        def get_mru_list(self):
            """Get items in MRU order (most recent first)"""
            return list(reversed(self.items.keys()))
    
    mru = MRUList(4)
    access_sequence = ['file1.txt', 'file2.txt', 'file3.txt', 'file1.txt', 
                       'file4.txt', 'file5.txt', 'file2.txt']
    
    print("File access simulation:")
    for file in access_sequence:
        mru.access(file)
        print(f"  Access '{file}': MRU list = {mru.get_mru_list()}")
    print()
    
    # Use Case 2: Dynamic Priority Queue
    print("2. Dynamic Priority Reordering:")
    def reorder_by_priority(od, priorities):
        """Reorder OrderedDict based on new priorities"""
        # Sort items by their new priorities
        sorted_items = sorted(od.items(), key=lambda x: priorities.get(x[0], float('inf')))
        
        # Move items to maintain the new order
        for key, _ in sorted_items:
            if key in od:
                od.move_to_end(key)
    
    # Process queue
    processes = OrderedDict([
        ('proc_A', 'Process A'),
        ('proc_B', 'Process B'),
        ('proc_C', 'Process C'),
        ('proc_D', 'Process D')
    ])
    
    print(f"Initial process order: {list(processes.keys())}")
    
    # Change priorities
    new_priorities = {
        'proc_C': 1,    # Highest priority
        'proc_A': 2,
        'proc_D': 3,
        'proc_B': 4     # Lowest priority
    }
    
    reorder_by_priority(processes, new_priorities)
    print(f"After priority reordering: {list(processes.keys())}")
    print("Order now reflects: proc_C -> proc_A -> proc_D -> proc_B")

if __name__ == "__main__":
    basic_move_to_end()
    error_handling()
    frequent_access_pattern()
    priority_queue_simulation()
    lru_cache_implementation()
    performance_comparison()
    dsa_use_cases()
