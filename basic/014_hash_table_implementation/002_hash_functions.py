"""
002 - Hash Functions Implementation
===================================

Various hash functions for different data types and use cases.

Time Complexity: O(1) for most hash functions
Space Complexity: O(1)

Good hash functions should distribute keys uniformly.
"""


def division_method_hash(key, table_size):
    """Hash function using division method"""
    if isinstance(key, str):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char))
        return hash_value % table_size
    else:
        return hash(key) % table_size


def multiplication_method_hash(key, table_size):
    """Hash function using multiplication method"""
    A = 0.6180339887  # (sqrt(5) - 1) / 2, golden ratio constant
    
    if isinstance(key, str):
        hash_value = 0
        for char in key:
            hash_value = (hash_value * 31 + ord(char))
        key_numeric = hash_value
    else:
        key_numeric = hash(key)
    
    return int(table_size * ((key_numeric * A) % 1))


def polynomial_rolling_hash(string, base=31, mod=10**9 + 7):
    """Polynomial rolling hash for strings"""
    hash_value = 0
    power = 1
    
    for char in string:
        hash_value = (hash_value + ord(char) * power) % mod
        power = (power * base) % mod
    
    return hash_value


def djb2_hash(string):
    """DJB2 hash function for strings"""
    hash_value = 5381
    for char in string:
        hash_value = ((hash_value << 5) + hash_value + ord(char)) & 0xFFFFFFFF
    return hash_value


def fnv1a_hash(string):
    """FNV-1a hash function for strings"""
    FNV_OFFSET_BASIS = 2166136261
    FNV_PRIME = 16777619
    
    hash_value = FNV_OFFSET_BASIS
    for char in string:
        hash_value = hash_value ^ ord(char)
        hash_value = (hash_value * FNV_PRIME) & 0xFFFFFFFF
    
    return hash_value


def universal_hash_family(key, a, b, prime, table_size):
    """Universal hash function family"""
    if isinstance(key, str):
        key_numeric = sum(ord(char) for char in key)
    else:
        key_numeric = key
    
    return ((a * key_numeric + b) % prime) % table_size


def demo_hash_functions():
    """Demonstrate different hash functions"""
    print("=== Hash Functions Demo ===")
    
    test_keys = ["apple", "banana", "cherry", "date", "elderberry"]
    table_size = 7
    
    print(f"Testing hash functions with table size {table_size}:")
    print("Key        | Division | Multiplication | DJB2     | FNV-1a")
    print("-" * 60)
    
    for key in test_keys:
        div_hash = division_method_hash(key, table_size)
        mult_hash = multiplication_method_hash(key, table_size)
        djb2 = djb2_hash(key) % table_size
        fnv1a = fnv1a_hash(key) % table_size
        
        print(f"{key:10} | {div_hash:8} | {mult_hash:13} | {djb2:8} | {fnv1a}")
    
    print()
    print("Hash Function Properties:")
    print("- Division: Simple, fast, sensitive to table size")
    print("- Multiplication: Better distribution, less sensitive to table size")
    print("- DJB2: Good for strings, widely used")
    print("- FNV-1a: Fast, good distribution for strings")
    print("- Universal: Theoretical guarantees against worst-case inputs")


def analyze_hash_distribution(hash_func, keys, table_size):
    """Analyze hash distribution for given function and keys"""
    distribution = [0] * table_size
    
    for key in keys:
        hash_value = hash_func(key, table_size)
        distribution[hash_value] += 1
    
    print(f"\nDistribution analysis:")
    for i, count in enumerate(distribution):
        print(f"Bucket {i}: {count} keys {'*' * count}")
    
    # Calculate standard deviation to measure uniformity
    mean = len(keys) / table_size
    variance = sum((count - mean) ** 2 for count in distribution) / table_size
    std_dev = variance ** 0.5
    
    print(f"Standard deviation: {std_dev:.2f} (lower is better)")


if __name__ == "__main__":
    demo_hash_functions()
    
    # Analyze distribution
    test_keys = [f"key{i}" for i in range(20)]
    analyze_hash_distribution(division_method_hash, test_keys, 7)
