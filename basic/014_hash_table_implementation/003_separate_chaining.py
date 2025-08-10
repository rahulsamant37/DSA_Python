"""
003 - Hash Table with Separate Chaining
=======================================

Hash table implementation using separate chaining for collision resolution.

Time Complexity:
- Average case: O(1) for search, insert, delete
- Worst case: O(n) if all keys hash to same bucket
- Space complexity: O(n)

Collision resolution using linked lists.
"""

from hash_node_001 import HashNode
from hash_functions_002 import division_method_hash


class HashTableSeparateChaining:
    """Hash table implementation using separate chaining"""
    
    def __init__(self, initial_capacity=7):
        self.capacity = initial_capacity
        self.size = 0
        self.buckets = [None] * self.capacity
        self.load_factor_threshold = 0.75
    
    def _hash(self, key):
        """Hash function using division method"""
        return division_method_hash(key, self.capacity)
    
    def _load_factor(self):
        """Calculate current load factor"""
        return self.size / self.capacity
    
    def _resize(self):
        """Resize hash table when load factor exceeds threshold"""
        old_buckets = self.buckets
        self.capacity *= 2
        self.size = 0
        self.buckets = [None] * self.capacity
        
        # Rehash all existing key-value pairs
        for head in old_buckets:
            current = head
            while current:
                self.insert(current.key, current.value)
                current = current.next
    
    def insert(self, key, value):
        """Insert key-value pair into hash table"""
        # Check if resize is needed
        if self._load_factor() > self.load_factor_threshold:
            self._resize()
        
        index = self._hash(key)
        
        # If bucket is empty
        if self.buckets[index] is None:
            self.buckets[index] = HashNode(key, value)
            self.size += 1
            return
        
        # Search for existing key in chain
        current = self.buckets[index]
        while current:
            if current.key == key:
                current.value = value  # Update existing key
                return
            if current.next is None:
                break
            current = current.next
        
        # Add new node at end of chain
        current.next = HashNode(key, value)
        self.size += 1
    
    def search(self, key):
        """Search for value by key"""
        index = self._hash(key)
        current = self.buckets[index]
        
        while current:
            if current.key == key:
                return current.value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def delete(self, key):
        """Delete key-value pair from hash table"""
        index = self._hash(key)
        current = self.buckets[index]
        
        # If bucket is empty
        if current is None:
            raise KeyError(f"Key '{key}' not found")
        
        # If first node has the key
        if current.key == key:
            self.buckets[index] = current.next
            self.size -= 1
            return current.value
        
        # Search in chain
        while current.next:
            if current.next.key == key:
                deleted_value = current.next.value
                current.next = current.next.next
                self.size -= 1
                return deleted_value
            current = current.next
        
        raise KeyError(f"Key '{key}' not found")
    
    def contains(self, key):
        """Check if key exists in hash table"""
        try:
            self.search(key)
            return True
        except KeyError:
            return False
    
    def get_all_keys(self):
        """Get all keys in hash table"""
        keys = []
        for head in self.buckets:
            current = head
            while current:
                keys.append(current.key)
                current = current.next
        return keys
    
    def get_all_values(self):
        """Get all values in hash table"""
        values = []
        for head in self.buckets:
            current = head
            while current:
                values.append(current.value)
                current = current.next
        return values
    
    def display(self):
        """Display hash table contents"""
        print(f"Hash Table (size: {self.size}, capacity: {self.capacity}):")
        for i, head in enumerate(self.buckets):
            print(f"  Bucket {i}: ", end="")
            if head is None:
                print("Empty")
            else:
                current = head
                while current:
                    print(f"({current.key}: {current.value})", end="")
                    if current.next:
                        print(" -> ", end="")
                    current = current.next
                print()


def demo_hash_table_chaining():
    """Demonstrate hash table with separate chaining"""
    print("=== Hash Table with Separate Chaining Demo ===")
    
    # Create hash table
    ht = HashTableSeparateChaining(5)
    
    # Insert key-value pairs
    items = [
        ("apple", 100),
        ("banana", 200),
        ("cherry", 300),
        ("date", 400),
        ("elderberry", 500),
        ("fig", 600),
        ("grape", 700)
    ]
    
    print("Inserting items:")
    for key, value in items:
        ht.insert(key, value)
        print(f"  Inserted ({key}: {value})")
    
    print()
    ht.display()
    
    # Search operations
    print(f"\nSearch operations:")
    print(f"apple: {ht.search('apple')}")
    print(f"date: {ht.search('date')}")
    print(f"Contains 'grape': {ht.contains('grape')}")
    print(f"Contains 'orange': {ht.contains('orange')}")
    
    # Delete operation
    print(f"\nDeleting 'cherry': {ht.delete('cherry')}")
    ht.display()
    
    # Update operation
    print(f"\nUpdating 'apple' to 150:")
    ht.insert('apple', 150)
    print(f"apple: {ht.search('apple')}")


if __name__ == "__main__":
    demo_hash_table_chaining()
