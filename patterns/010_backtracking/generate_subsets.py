"""
Backtracking Pattern - Generate Subsets
========================================

Generate all possible subsets of a given set using backtracking.

Time Complexity: O(2^n)
Space Complexity: O(n) for recursion depth
"""


def generate_subsets(nums):
    """
    Generate all possible subsets using backtracking.
    
    Args:
        nums: List of integers
        
    Returns:
        List of all possible subsets
    """
    result = []
    
    def backtrack(start, current_subset):
        # Add current subset to result
        result.append(current_subset[:])  # Make a copy
        
        # Try adding each remaining element
        for i in range(start, len(nums)):
            # Choose: add current element
            current_subset.append(nums[i])
            
            # Explore: recurse with next index
            backtrack(i + 1, current_subset)
            
            # Unchoose: remove current element (backtrack)
            current_subset.pop()
    
    backtrack(0, [])
    return result


def example_usage():
    """Demonstrate subset generation"""
    nums = [1, 2, 3]
    subsets = generate_subsets(nums)
    
    print(f"Input: {nums}")
    print("All possible subsets:")
    for i, subset in enumerate(subsets):
        print(f"{i + 1}: {subset}")
    
    print(f"\nTotal subsets: {len(subsets)}")
    # For n elements, we get 2^n subsets


if __name__ == "__main__":
    example_usage()
