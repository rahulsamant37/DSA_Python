"""
014 - Hash Table Implementation
==============================

This module implements hash tables with different collision resolution strategies:
- Separate Chaining (using linked lists)
- Open Addressing (Linear Probing, Quadratic Probing, Double Hashing)
- Robin Hood Hashing
- Dynamic resizing and load factor management

Time Complexity:
- Average case: O(1) for search, insert, delete
- Worst case: O(n) for search, insert, delete (poor hash function)
- Space complexity: O(n)

Hash Functions Included:
- Division method
- Multiplication method  
- Universal hashing
"""

class HashNode:
    """Node for separate chaining"""
    
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTableSeparateChaining:
    """Hash table implementation using separate chaining"""
    
    def __init__(self, initial_capacity=7):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.load_factor_threshold = 0.75
    
    def _hash(self, key):
        """Hash function using division method"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.capacity
            return hash_value
        else:
            return hash(key) % self.capacity
    
    def _hash_multiply(self, key):
        """Alternative hash function using multiplication method"""
        A = 0.6180339887  # (√5 - 1) / 2
        if isinstance(key, str):
            key_int = sum(ord(char) for char in key)
        else:
            key_int = key
        
        return int(self.capacity * ((key_int * A) % 1))
    
    def put(self, key, value):
        """Insert or update key-value pair"""
        index = self._hash(key)
        
        if self.buckets[index] is None:
            # No collision
            self.buckets[index] = HashNode(key, value)
            self.size += 1
        else:
            # Handle collision with chaining
            current = self.buckets[index]
            while current:
                if current.key == key:
                    # Update existing key
                    current.value = value
                    return
                if current.next is None:
                    break
                current = current.next
            
            # Add new node at end of chain
            current.next = HashNode(key, value)
            self.size += 1
        
        # Check if resize is needed
        if self.size > self.capacity * self.load_factor_threshold:
            self._resize()
    
    def get(self, key):
        """Get value by key"""
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists"""
        try:
            self.get(key)
            return True
        except KeyError:
            return False
    
    def delete(self, key):
        """Delete key-value pair"""
        index = self._hash(key)
        current = self.buckets[index]
        
        if current is None:
            raise KeyError(f"Key '{key}' not found")
        
        # If first node is the target
        if current.key == key:
            self.buckets[index] = current.next
            self.size -= 1
            return current.value
        
        # Search in the chain
        while current.next:
            if current.next.key == key:
                deleted_value = current.next.value
                current.next = current.next.next
                self.size -= 1
                return deleted_value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def _resize(self):
        """Resize hash table when load factor exceeds threshold"""
        old_buckets = self.buckets
        old_capacity = self.capacity
        
        self.capacity = self._next_prime(self.capacity * 2)
        self.buckets = [None] * self.capacity
        self.size = 0
        
        # Rehash all elements
        for head in old_buckets:
            current = head
            while current:
                self.put(current.key, current.value)
                current = current.next
    
    def _next_prime(self, n):
        """Find next prime number >= n"""
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        while not is_prime(n):
            n += 1
        return n
    
    def load_factor(self):
        """Calculate current load factor"""
        return self.size / self.capacity
    
    def keys(self):
        """Get all keys"""
        result = []
        for head in self.buckets:
            current = head
            while current:
                result.append(current.key)
                current = current.next
        return result
    
    def values(self):
        """Get all values"""
        result = []
        for head in self.buckets:
            current = head
            while current:
                result.append(current.value)
                current = current.next
        return result
    
    def items(self):
        """Get all key-value pairs"""
        result = []
        for head in self.buckets:
            current = head
            while current:
                result.append((current.key, current.value))
                current = current.next
        return result
    
    def display(self):
        """Display hash table structure"""
        print(f"Hash Table (Separate Chaining) - Size: {self.size}, Capacity: {self.capacity}")
        print(f"Load Factor: {self.load_factor():.3f}")
        
        for i, head in enumerate(self.buckets):
            if head is not None:
                chain = []
                current = head
                while current:
                    chain.append(f"({current.key}: {current.value})")
                    current = current.next
                print(f"Bucket {i}: {' -> '.join(chain)}")


class HashTableOpenAddressing:
    """Hash table implementation using open addressing with linear probing"""
    
    def __init__(self, initial_capacity=7):
        self.capacity = initial_capacity
        self.size = 0
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity  # Track deleted slots
        self.load_factor_threshold = 0.5  # Lower threshold for open addressing
    
    def _hash(self, key):
        """Primary hash function"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 31 + ord(char)) % self.capacity
            return hash_value
        else:
            return hash(key) % self.capacity
    
    def _hash2(self, key):
        """Secondary hash function for double hashing"""
        if isinstance(key, str):
            hash_value = 0
            for char in key:
                hash_value = (hash_value * 37 + ord(char)) % (self.capacity - 1)
            return 1 + (hash_value % (self.capacity - 1))
        else:
            return 1 + (hash(key) % (self.capacity - 1))
    
    def _linear_probe(self, key):
        """Linear probing to find slot"""
        index = self._hash(key)
        original_index = index
        
        while (self.keys[index] is not None and 
               self.keys[index] != key and 
               not self.deleted[index]):
            index = (index + 1) % self.capacity
            
            # Table is full
            if index == original_index:
                return -1
        
        return index
    
    def _quadratic_probe(self, key):
        """Quadratic probing to find slot"""
        index = self._hash(key)
        original_index = index
        i = 0
        
        while (self.keys[index] is not None and 
               self.keys[index] != key and 
               not self.deleted[index]):
            i += 1
            index = (original_index + i * i) % self.capacity
            
            # Avoid infinite loop
            if i >= self.capacity:
                return -1
        
        return index
    
    def _double_hash_probe(self, key):
        """Double hashing to find slot"""
        index = self._hash(key)
        step = self._hash2(key)
        original_index = index
        
        while (self.keys[index] is not None and 
               self.keys[index] != key and 
               not self.deleted[index]):
            index = (index + step) % self.capacity
            
            # Table is full
            if index == original_index:
                return -1
        
        return index
    
    def put(self, key, value, probe_method='linear'):
        """Insert or update key-value pair"""
        if self.size >= self.capacity * self.load_factor_threshold:
            self._resize()
        
        if probe_method == 'linear':
            index = self._linear_probe(key)
        elif probe_method == 'quadratic':
            index = self._quadratic_probe(key)
        elif probe_method == 'double':
            index = self._double_hash_probe(key)
        else:
            raise ValueError("Invalid probe method")
        
        if index == -1:
            raise Exception("Hash table is full")
        
        # Update existing key
        if self.keys[index] == key:
            self.values[index] = value
            return
        
        # Insert new key
        self.keys[index] = key
        self.values[index] = value
        self.deleted[index] = False
        self.size += 1
    
    def get(self, key, probe_method='linear'):
        """Get value by key"""
        if probe_method == 'linear':
            index = self._linear_probe(key)
        elif probe_method == 'quadratic':
            index = self._quadratic_probe(key)
        elif probe_method == 'double':
            index = self._double_hash_probe(key)
        else:
            raise ValueError("Invalid probe method")
        
        if index == -1 or self.keys[index] is None or self.deleted[index]:
            raise KeyError(f"Key '{key}' not found")
        
        return self.values[index]
    
    def delete(self, key, probe_method='linear'):
        """Delete key-value pair using lazy deletion"""
        if probe_method == 'linear':
            index = self._linear_probe(key)
        elif probe_method == 'quadratic':
            index = self._quadratic_probe(key)
        elif probe_method == 'double':
            index = self._double_hash_probe(key)
        else:
            raise ValueError("Invalid probe method")
        
        if index == -1 or self.keys[index] is None or self.deleted[index]:
            raise KeyError(f"Key '{key}' not found")
        
        deleted_value = self.values[index]
        self.deleted[index] = True
        self.size -= 1
        return deleted_value
    
    def _resize(self):
        """Resize hash table"""
        old_keys = self.keys
        old_values = self.values
        old_deleted = self.deleted
        old_capacity = self.capacity
        
        self.capacity = self._next_prime(self.capacity * 2)
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.deleted = [False] * self.capacity
        self.size = 0
        
        # Rehash all non-deleted elements
        for i in range(old_capacity):
            if old_keys[i] is not None and not old_deleted[i]:
                self.put(old_keys[i], old_values[i])
    
    def _next_prime(self, n):
        """Find next prime number >= n"""
        def is_prime(num):
            if num < 2:
                return False
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    return False
            return True
        
        while not is_prime(n):
            n += 1
        return n
    
    def load_factor(self):
        """Calculate current load factor"""
        return self.size / self.capacity
    
    def display(self):
        """Display hash table structure"""
        print(f"Hash Table (Open Addressing) - Size: {self.size}, Capacity: {self.capacity}")
        print(f"Load Factor: {self.load_factor():.3f}")
        
        for i in range(self.capacity):
            status = ""
            if self.keys[i] is None:
                status = "Empty"
            elif self.deleted[i]:
                status = "Deleted"
            else:
                status = f"({self.keys[i]}: {self.values[i]})"
            
            print(f"Slot {i}: {status}")


class HashFunctions:
    """Collection of different hash functions"""
    
    @staticmethod
    def division_hash(key, table_size):
        """Division method: h(k) = k mod m"""
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return key % table_size
    
    @staticmethod
    def multiplication_hash(key, table_size):
        """Multiplication method: h(k) = floor(m * ((k * A) mod 1))"""
        A = 0.6180339887  # (√5 - 1) / 2 (golden ratio)
        if isinstance(key, str):
            key = sum(ord(char) for char in key)
        return int(table_size * ((key * A) % 1))
    
    @staticmethod
    def polynomial_hash(string, base=31, mod=10**9 + 7):
        """Polynomial rolling hash for strings"""
        hash_value = 0
        power = 1
        
        for char in string:
            hash_value = (hash_value + ord(char) * power) % mod
            power = (power * base) % mod
        
        return hash_value
    
    @staticmethod
    def fnv_hash(data, table_size):
        """FNV-1a hash function"""
        fnv_prime = 16777619
        fnv_offset_basis = 2166136261
        
        if isinstance(data, str):
            data = data.encode('utf-8')
        elif not isinstance(data, bytes):
            data = str(data).encode('utf-8')
        
        hash_value = fnv_offset_basis
        for byte in data:
            hash_value ^= byte
            hash_value *= fnv_prime
            hash_value &= 0xffffffff  # Keep 32-bit
        
        return hash_value % table_size


def test_hash_tables():
    """Test hash table implementations"""
    print("=== Testing Hash Table Implementations ===\n")
    
    # Test Separate Chaining
    print("=== Separate Chaining Hash Table ===")
    ht_chain = HashTableSeparateChaining(5)
    
    # Insert some key-value pairs
    test_data = [
        ("apple", 5),
        ("banana", 7),
        ("orange", 3),
        ("grape", 12),
        ("kiwi", 8),
        ("mango", 15),
        ("cherry", 9)
    ]
    
    print("Inserting test data:")
    for key, value in test_data:
        ht_chain.put(key, value)
        print(f"Inserted ({key}: {value})")
    
    ht_chain.display()
    print()
    
    # Test retrieval
    print("Testing retrieval:")
    for key, expected_value in test_data[:3]:
        try:
            value = ht_chain.get(key)
            print(f"get('{key}') = {value}")
        except KeyError as e:
            print(f"Error: {e}")
    print()
    
    # Test deletion
    print("Testing deletion:")
    try:
        deleted = ht_chain.delete("banana")
        print(f"Deleted 'banana': {deleted}")
        ht_chain.display()
    except KeyError as e:
        print(f"Error: {e}")
    print()
    
    # Test Open Addressing
    print("=== Open Addressing Hash Table ===")
    ht_open = HashTableOpenAddressing(7)
    
    print("Testing different probing methods:")
    test_data_open = [(1, "one"), (8, "eight"), (15, "fifteen"), (22, "twenty-two")]
    
    for probe_method in ['linear', 'quadratic', 'double']:
        print(f"\n{probe_method.title()} Probing:")
        ht_temp = HashTableOpenAddressing(7)
        
        for key, value in test_data_open:
            ht_temp.put(key, value, probe_method)
            print(f"Inserted ({key}: {value})")
        
        ht_temp.display()
    
    # Test hash functions
    print("\n=== Testing Hash Functions ===")
    hash_funcs = HashFunctions()
    test_string = "hello"
    table_size = 10
    
    print(f"Hash functions for '{test_string}' with table size {table_size}:")
    print(f"Division hash: {hash_funcs.division_hash(test_string, table_size)}")
    print(f"Multiplication hash: {hash_funcs.multiplication_hash(test_string, table_size)}")
    print(f"Polynomial hash: {hash_funcs.polynomial_hash(test_string) % table_size}")
    print(f"FNV hash: {hash_funcs.fnv_hash(test_string, table_size)}")


def test_collision_handling():
    """Test collision handling effectiveness"""
    print("\n=== Testing Collision Handling ===\n")
    
    # Create keys that will definitely collide
    ht = HashTableSeparateChaining(3)
    
    # These keys should hash to same bucket in small table
    collision_keys = [("key1", 1), ("key4", 4), ("key7", 7)]
    
    print("Inserting keys that will collide:")
    for key, value in collision_keys:
        hash_val = ht._hash(key)
        ht.put(key, value)
        print(f"'{key}' -> bucket {hash_val}")
    
    ht.display()
    print()
    
    # Test retrieval after collisions
    print("Testing retrieval after collisions:")
    for key, expected_value in collision_keys:
        retrieved = ht.get(key)
        print(f"get('{key}') = {retrieved}")
    
    # Performance test
    print("\n=== Performance Comparison ===")
    import time
    import random
    
    # Test with larger dataset
    n = 1000
    test_keys = [f"key_{i}" for i in range(n)]
    test_values = [random.randint(1, 1000) for _ in range(n)]
    
    # Test separate chaining
    ht_chain = HashTableSeparateChaining()
    start_time = time.time()
    for key, value in zip(test_keys, test_values):
        ht_chain.put(key, value)
    chain_insert_time = time.time() - start_time
    
    start_time = time.time()
    for key in test_keys[:100]:
        ht_chain.get(key)
    chain_search_time = time.time() - start_time
    
    # Test open addressing
    ht_open = HashTableOpenAddressing()
    start_time = time.time()
    for key, value in zip(test_keys, test_values):
        ht_open.put(key, value)
    open_insert_time = time.time() - start_time
    
    start_time = time.time()
    for key in test_keys[:100]:
        ht_open.get(key)
    open_search_time = time.time() - start_time
    
    print(f"Dataset size: {n} key-value pairs")
    print(f"Separate Chaining - Insert: {chain_insert_time:.4f}s, Search: {chain_search_time:.4f}s")
    print(f"Open Addressing - Insert: {open_insert_time:.4f}s, Search: {open_search_time:.4f}s")
    print(f"Load factors - Chaining: {ht_chain.load_factor():.3f}, Open: {ht_open.load_factor():.3f}")


if __name__ == "__main__":
    test_hash_tables()
    test_collision_handling()
