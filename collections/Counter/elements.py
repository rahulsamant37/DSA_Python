"""
Counter.elements() - Iterating over elements according to their count

The elements() method returns an iterator over elements repeating each 
as many times as its count. Useful for reconstructing original data or sampling.
"""

from collections import Counter

def elements_examples():
    """Demonstrates usage of the elements() method"""
    
    # 1. Basic usage
    print("1. Basic elements() usage:")
    counter = Counter({'a': 3, 'b': 1, 'c': 2})
    elements_list = list(counter.elements())
    print(f"Counter: {counter}")
    print(f"Elements: {elements_list}")
    print(f"Elements (sorted): {sorted(elements_list)}")
    print()
    
    # 2. Elements with zero or negative counts
    print("2. Elements with zero/negative counts:")
    counter = Counter({'a': 3, 'b': 0, 'c': -1, 'd': 2})
    elements_list = list(counter.elements())
    print(f"Counter: {counter}")
    print(f"Elements: {elements_list}")
    print("Note: Only positive counts are included")
    print()
    
    # 3. Empty counter
    print("3. Empty counter:")
    empty_counter = Counter()
    elements_list = list(empty_counter.elements())
    print(f"Empty counter elements: {elements_list}")
    print()

def dsa_use_cases():
    """DSA applications of elements() method"""
    
    print("--- DSA Use Cases ---")
    
    # Use Case 1: Reconstruct array from frequency map
    print("1. Reconstruct Array from Frequency:")
    def reconstruct_array(freq_map):
        """
        Given a frequency map, reconstruct the original array.
        Time Complexity: O(n) where n is total count
        """
        counter = Counter(freq_map)
        return list(counter.elements())
    
    freq_map = {'apple': 2, 'banana': 3, 'orange': 1}
    reconstructed = reconstruct_array(freq_map)
    print(f"Frequency map: {freq_map}")
    print(f"Reconstructed array: {reconstructed}")
    print()
    
    # Use Case 2: Random sampling based on frequency
    print("2. Weighted Random Sampling:")
    import random
    
    def weighted_random_choice(counter):
        """
        Choose a random element based on its frequency weight.
        Higher frequency = higher probability of selection.
        """
        elements = list(counter.elements())
        if not elements:
            return None
        return random.choice(elements)
    
    # Simulate rolling a biased die
    biased_die = Counter({1: 1, 2: 1, 3: 2, 4: 2, 5: 3, 6: 3})
    print(f"Biased die frequencies: {biased_die}")
    
    # Sample multiple times to see distribution
    samples = [weighted_random_choice(biased_die) for _ in range(20)]
    sample_counter = Counter(samples)
    print(f"20 random samples: {samples}")
    print(f"Sample distribution: {sample_counter}")
    print()
    
    # Use Case 3: Generate test data
    print("3. Generate Test Data:")
    def generate_test_data(pattern):
        """
        Generate test data based on a frequency pattern.
        Useful for creating test cases with specific distributions.
        """
        counter = Counter(pattern)
        return list(counter.elements())
    
    # Generate test data for sorting algorithm
    test_pattern = {'small': 3, 'medium': 5, 'large': 2}
    test_data = generate_test_data(test_pattern)
    print(f"Test pattern: {test_pattern}")
    print(f"Generated test data: {test_data}")
    print()
    
    # Use Case 4: Validate frequency distribution
    print("4. Validate Frequency Distribution:")
    def validate_distribution(original, counter):
        """
        Check if a counter correctly represents the frequency of original data.
        """
        reconstructed = sorted(counter.elements())
        original_sorted = sorted(original)
        return reconstructed == original_sorted
    
    original_data = ['a', 'b', 'b', 'c', 'c', 'c']
    counter = Counter(original_data)
    is_valid = validate_distribution(original_data, counter)
    
    print(f"Original data: {original_data}")
    print(f"Counter: {counter}")
    print(f"Validation passed: {is_valid}")
    
    # Test with modified counter
    modified_counter = Counter({'a': 1, 'b': 2, 'c': 2})  # Wrong count for 'c'
    is_valid_modified = validate_distribution(original_data, modified_counter)
    print(f"Modified counter: {modified_counter}")
    print(f"Modified validation passed: {is_valid_modified}")

if __name__ == "__main__":
    elements_examples()
    dsa_use_cases()
