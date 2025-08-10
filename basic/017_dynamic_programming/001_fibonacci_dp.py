"""
001 - Dynamic Programming Fibonacci
===================================

Classic fibonacci problem solved using different DP approaches.

Time Complexity:
- Naive recursive: O(2^n)
- Memoization: O(n)
- Tabulation: O(n)
- Space optimized: O(1)

Demonstrates the power of dynamic programming optimization.
"""

import time
from functools import lru_cache


def fibonacci_naive(n):
    """Naive recursive approach (exponential time)"""
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


def fibonacci_memoization(n, memo=None):
    """Top-down DP with memoization"""
    if memo is None:
        memo = {}
    
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


@lru_cache(maxsize=None)
def fibonacci_lru_cache(n):
    """Using Python's built-in LRU cache"""
    if n <= 1:
        return n
    return fibonacci_lru_cache(n - 1) + fibonacci_lru_cache(n - 2)


def fibonacci_tabulation(n):
    """Bottom-up DP with tabulation"""
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def fibonacci_space_optimized(n):
    """Space-optimized DP (O(1) space)"""
    if n <= 1:
        return n
    
    prev2, prev1 = 0, 1
    
    for i in range(2, n + 1):
        current = prev1 + prev2
        prev2, prev1 = prev1, current
    
    return prev1


def measure_time(func, n):
    """Measure execution time of a function"""
    start_time = time.time()
    result = func(n)
    end_time = time.time()
    return result, (end_time - start_time) * 1000  # milliseconds


def demo_fibonacci_dp():
    """Demonstrate different fibonacci DP approaches"""
    print("=== Dynamic Programming Fibonacci Demo ===")
    
    test_values = [10, 20, 30]
    
    for n in test_values:
        print(f"\nCalculating fibonacci({n}):")
        print("-" * 40)
        
        # Memoization
        result, time_taken = measure_time(fibonacci_memoization, n)
        print(f"Memoization:     {result:>10} ({time_taken:.2f} ms)")
        
        # LRU Cache
        fibonacci_lru_cache.cache_clear()  # Clear cache for fair comparison
        result, time_taken = measure_time(fibonacci_lru_cache, n)
        print(f"LRU Cache:       {result:>10} ({time_taken:.2f} ms)")
        
        # Tabulation
        result, time_taken = measure_time(fibonacci_tabulation, n)
        print(f"Tabulation:      {result:>10} ({time_taken:.2f} ms)")
        
        # Space optimized
        result, time_taken = measure_time(fibonacci_space_optimized, n)
        print(f"Space Optimized: {result:>10} ({time_taken:.2f} ms)")
        
        # Naive (only for small values)
        if n <= 20:
            result, time_taken = measure_time(fibonacci_naive, n)
            print(f"Naive Recursive: {result:>10} ({time_taken:.2f} ms)")
    
    print("\n" + "="*50)
    print("DP OPTIMIZATION SUMMARY:")
    print("="*50)
    print("1. Naive Recursive: O(2^n) - Very slow, exponential growth")
    print("2. Memoization: O(n) - Top-down, stores subproblem results")
    print("3. Tabulation: O(n) - Bottom-up, builds solution iteratively")
    print("4. Space Optimized: O(1) space - Only keeps necessary variables")
    print("\nKey Insight: DP reduces overlapping subproblems from exponential to linear!")


if __name__ == "__main__":
    demo_fibonacci_dp()
