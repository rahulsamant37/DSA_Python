"""
Dynamic Programming Pattern - Fibonacci
========================================

Calculate Fibonacci number using dynamic programming (memoization).

Time Complexity: O(n)
Space Complexity: O(n)
"""


def fibonacci_dp(n, memo=None):
    """
    Calculate nth Fibonacci number using memoization.
    
    Args:
        n: Position in Fibonacci sequence (0-indexed)
        memo: Dictionary to store computed values
        
    Returns:
        nth Fibonacci number
    """
    if memo is None:
        memo = {}
    
    # Base cases
    if n <= 1:
        return n
    
    # Check if already computed
    if n in memo:
        return memo[n]
    
    # Compute and store result
    memo[n] = fibonacci_dp(n - 1, memo) + fibonacci_dp(n - 2, memo)
    return memo[n]


def fibonacci_iterative(n):
    """
    Calculate nth Fibonacci number iteratively (bottom-up DP).
    
    Args:
        n: Position in Fibonacci sequence
        
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    # Use only two variables instead of array
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def example_usage():
    """Demonstrate Fibonacci calculation"""
    n = 10
    
    # Using memoization (top-down)
    result1 = fibonacci_dp(n)
    print(f"Fibonacci({n}) using memoization: {result1}")
    
    # Using iterative approach (bottom-up)
    result2 = fibonacci_iterative(n)
    print(f"Fibonacci({n}) using iteration: {result2}")
    
    # Show first few Fibonacci numbers
    print("\nFirst 10 Fibonacci numbers:")
    for i in range(10):
        print(f"F({i}) = {fibonacci_iterative(i)}")


if __name__ == "__main__":
    example_usage()
