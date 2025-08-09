"""
017 - Dynamic Programming Implementation
======================================

This module implements classic dynamic programming problems and techniques:
- Fibonacci sequence with memoization and tabulation
- Longest Common Subsequence (LCS)
- Longest Increasing Subsequence (LIS)
- 0/1 Knapsack Problem
- Coin Change Problem
- Edit Distance (Levenshtein Distance)
- Matrix Chain Multiplication
- Longest Palindromic Subsequence
- Maximum Subarray Sum (Kadane's Algorithm)
- House Robber Problem

DP Techniques Covered:
1. Memoization (Top-down approach)
2. Tabulation (Bottom-up approach)
3. Space optimization techniques
4. State space reduction

Time Complexity varies by problem:
- Most problems: O(n), O(n²), or O(n³)
- Space complexity often optimizable from O(n²) to O(n)
"""

from functools import lru_cache
from typing import List, Dict, Tuple


class DynamicProgramming:
    """Collection of classic dynamic programming problems"""
    
    # =============================================================================
    # FIBONACCI SEQUENCE
    # =============================================================================
    
    @staticmethod
    def fibonacci_recursive(n):
        """Naive recursive Fibonacci - O(2^n) time, O(n) space"""
        if n <= 1:
            return n
        return DynamicProgramming.fibonacci_recursive(n-1) + DynamicProgramming.fibonacci_recursive(n-2)
    
    @staticmethod
    def fibonacci_memoization(n, memo=None):
        """Fibonacci with memoization - O(n) time, O(n) space"""
        if memo is None:
            memo = {}
        
        if n in memo:
            return memo[n]
        
        if n <= 1:
            return n
        
        memo[n] = DynamicProgramming.fibonacci_memoization(n-1, memo) + DynamicProgramming.fibonacci_memoization(n-2, memo)
        return memo[n]
    
    @staticmethod
    def fibonacci_tabulation(n):
        """Fibonacci with tabulation - O(n) time, O(n) space"""
        if n <= 1:
            return n
        
        dp = [0] * (n + 1)
        dp[1] = 1
        
        for i in range(2, n + 1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]
    
    @staticmethod
    def fibonacci_optimized(n):
        """Space-optimized Fibonacci - O(n) time, O(1) space"""
        if n <= 1:
            return n
        
        prev2, prev1 = 0, 1
        
        for i in range(2, n + 1):
            current = prev1 + prev2
            prev2, prev1 = prev1, current
        
        return prev1
    
    # =============================================================================
    # LONGEST COMMON SUBSEQUENCE (LCS)
    # =============================================================================
    
    @staticmethod
    def lcs_length(text1: str, text2: str) -> int:
        """Find length of longest common subsequence - O(mn) time and space"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        return dp[m][n]
    
    @staticmethod
    def lcs_string(text1: str, text2: str) -> str:
        """Find the actual longest common subsequence"""
        m, n = len(text1), len(text2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill DP table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    dp[i][j] = dp[i-1][j-1] + 1
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        
        # Reconstruct LCS
        lcs = []
        i, j = m, n
        
        while i > 0 and j > 0:
            if text1[i-1] == text2[j-1]:
                lcs.append(text1[i-1])
                i -= 1
                j -= 1
            elif dp[i-1][j] > dp[i][j-1]:
                i -= 1
            else:
                j -= 1
        
        return ''.join(reversed(lcs))
    
    @staticmethod
    def lcs_space_optimized(text1: str, text2: str) -> int:
        """Space-optimized LCS - O(mn) time, O(min(m,n)) space"""
        if len(text1) < len(text2):
            text1, text2 = text2, text1
        
        m, n = len(text1), len(text2)
        prev = [0] * (n + 1)
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i-1] == text2[j-1]:
                    curr[j] = prev[j-1] + 1
                else:
                    curr[j] = max(prev[j], curr[j-1])
            prev, curr = curr, prev
        
        return prev[n]
    
    # =============================================================================
    # LONGEST INCREASING SUBSEQUENCE (LIS)
    # =============================================================================
    
    @staticmethod
    def lis_length(nums: List[int]) -> int:
        """Find length of longest increasing subsequence - O(n²) time"""
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        
        return max(dp)
    
    @staticmethod
    def lis_binary_search(nums: List[int]) -> int:
        """Optimized LIS using binary search - O(n log n) time"""
        if not nums:
            return 0
        
        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                if arr[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return left
        
        tails = []
        
        for num in nums:
            pos = binary_search(tails, num)
            if pos == len(tails):
                tails.append(num)
            else:
                tails[pos] = num
        
        return len(tails)
    
    # =============================================================================
    # 0/1 KNAPSACK PROBLEM
    # =============================================================================
    
    @staticmethod
    def knapsack_01(weights: List[int], values: List[int], capacity: int) -> int:
        """0/1 Knapsack problem - O(nW) time and space"""
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                # Don't include current item
                dp[i][w] = dp[i-1][w]
                
                # Include current item if possible
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
        
        return dp[n][capacity]
    
    @staticmethod
    def knapsack_01_optimized(weights: List[int], values: List[int], capacity: int) -> int:
        """Space-optimized 0/1 Knapsack - O(nW) time, O(W) space"""
        dp = [0] * (capacity + 1)
        
        for i in range(len(weights)):
            # Traverse backwards to avoid using updated values
            for w in range(capacity, weights[i] - 1, -1):
                dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
        
        return dp[capacity]
    
    @staticmethod
    def knapsack_01_with_items(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
        """0/1 Knapsack returning items selected"""
        n = len(weights)
        dp = [[0] * (capacity + 1) for _ in range(n + 1)]
        
        # Fill DP table
        for i in range(1, n + 1):
            for w in range(capacity + 1):
                dp[i][w] = dp[i-1][w]
                if weights[i-1] <= w:
                    dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
        
        # Backtrack to find items
        w = capacity
        items = []
        for i in range(n, 0, -1):
            if dp[i][w] != dp[i-1][w]:
                items.append(i-1)  # 0-indexed
                w -= weights[i-1]
        
        return dp[n][capacity], list(reversed(items))
    
    # =============================================================================
    # COIN CHANGE PROBLEM
    # =============================================================================
    
    @staticmethod
    def coin_change_min_coins(coins: List[int], amount: int) -> int:
        """Minimum coins to make amount - O(amount * len(coins)) time"""
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    dp[i] = min(dp[i], dp[i - coin] + 1)
        
        return dp[amount] if dp[amount] != float('inf') else -1
    
    @staticmethod
    def coin_change_ways(coins: List[int], amount: int) -> int:
        """Number of ways to make amount"""
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]
        
        return dp[amount]
    
    # =============================================================================
    # EDIT DISTANCE (LEVENSHTEIN DISTANCE)
    # =============================================================================
    
    @staticmethod
    def edit_distance(word1: str, word2: str) -> int:
        """Minimum edit distance between two strings - O(mn) time and space"""
        m, n = len(word1), len(word2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Initialize base cases
        for i in range(m + 1):
            dp[i][0] = i
        for j in range(n + 1):
            dp[0][j] = j
        
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    dp[i][j] = dp[i-1][j-1]  # No operation needed
                else:
                    dp[i][j] = 1 + min(
                        dp[i-1][j],    # Delete
                        dp[i][j-1],    # Insert
                        dp[i-1][j-1]   # Replace
                    )
        
        return dp[m][n]
    
    @staticmethod
    def edit_distance_optimized(word1: str, word2: str) -> int:
        """Space-optimized edit distance - O(mn) time, O(min(m,n)) space"""
        if len(word1) < len(word2):
            word1, word2 = word2, word1
        
        m, n = len(word1), len(word2)
        prev = list(range(n + 1))
        curr = [0] * (n + 1)
        
        for i in range(1, m + 1):
            curr[0] = i
            for j in range(1, n + 1):
                if word1[i-1] == word2[j-1]:
                    curr[j] = prev[j-1]
                else:
                    curr[j] = 1 + min(prev[j], curr[j-1], prev[j-1])
            prev, curr = curr, prev
        
        return prev[n]
    
    # =============================================================================
    # MATRIX CHAIN MULTIPLICATION
    # =============================================================================
    
    @staticmethod
    def matrix_chain_multiplication(dimensions: List[int]) -> int:
        """Minimum scalar multiplications for matrix chain - O(n³) time"""
        n = len(dimensions) - 1  # Number of matrices
        if n <= 1:
            return 0
        
        dp = [[0] * n for _ in range(n)]
        
        # l is chain length
        for l in range(2, n + 1):
            for i in range(n - l + 1):
                j = i + l - 1
                dp[i][j] = float('inf')
                
                for k in range(i, j):
                    cost = (dp[i][k] + dp[k+1][j] + 
                           dimensions[i] * dimensions[k+1] * dimensions[j+1])
                    dp[i][j] = min(dp[i][j], cost)
        
        return dp[0][n-1]
    
    # =============================================================================
    # LONGEST PALINDROMIC SUBSEQUENCE
    # =============================================================================
    
    @staticmethod
    def longest_palindromic_subsequence(s: str) -> int:
        """Length of longest palindromic subsequence - O(n²) time and space"""
        n = len(s)
        dp = [[0] * n for _ in range(n)]
        
        # Every single character is a palindrome of length 1
        for i in range(n):
            dp[i][i] = 1
        
        # Fill for substrings of length 2 to n
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                
                if s[i] == s[j]:
                    if length == 2:
                        dp[i][j] = 2
                    else:
                        dp[i][j] = dp[i+1][j-1] + 2
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1])
        
        return dp[0][n-1]
    
    # =============================================================================
    # MAXIMUM SUBARRAY SUM (KADANE'S ALGORITHM)
    # =============================================================================
    
    @staticmethod
    def max_subarray_sum(nums: List[int]) -> int:
        """Maximum contiguous subarray sum - O(n) time, O(1) space"""
        if not nums:
            return 0
        
        max_sum = current_sum = nums[0]
        
        for i in range(1, len(nums)):
            current_sum = max(nums[i], current_sum + nums[i])
            max_sum = max(max_sum, current_sum)
        
        return max_sum
    
    @staticmethod
    def max_subarray_with_indices(nums: List[int]) -> Tuple[int, int, int]:
        """Maximum subarray sum with start and end indices"""
        if not nums:
            return 0, 0, 0
        
        max_sum = current_sum = nums[0]
        start = end = temp_start = 0
        
        for i in range(1, len(nums)):
            if current_sum < 0:
                current_sum = nums[i]
                temp_start = i
            else:
                current_sum += nums[i]
            
            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i
        
        return max_sum, start, end
    
    # =============================================================================
    # HOUSE ROBBER PROBLEM
    # =============================================================================
    
    @staticmethod
    def house_robber(nums: List[int]) -> int:
        """Maximum money that can be robbed - O(n) time, O(1) space"""
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            current = max(prev1, prev2 + nums[i])
            prev2, prev1 = prev1, current
        
        return prev1
    
    @staticmethod
    def house_robber_circular(nums: List[int]) -> int:
        """House robber with circular arrangement"""
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)
        
        def rob_linear(houses):
            prev2 = prev1 = 0
            for money in houses:
                current = max(prev1, prev2 + money)
                prev2, prev1 = prev1, current
            return prev1
        
        # Case 1: Rob houses 0 to n-2 (can't rob last house)
        # Case 2: Rob houses 1 to n-1 (can't rob first house)
        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))


def test_fibonacci():
    """Test different Fibonacci implementations"""
    print("=== Testing Fibonacci Implementations ===\n")
    
    test_cases = [0, 1, 5, 10, 20]
    
    for n in test_cases:
        print(f"Fibonacci({n}):")
        
        if n <= 30:  # Only test recursive for small n
            recursive_result = DynamicProgramming.fibonacci_recursive(n)
            print(f"  Recursive: {recursive_result}")
        
        memo_result = DynamicProgramming.fibonacci_memoization(n)
        tab_result = DynamicProgramming.fibonacci_tabulation(n)
        opt_result = DynamicProgramming.fibonacci_optimized(n)
        
        print(f"  Memoization: {memo_result}")
        print(f"  Tabulation: {tab_result}")
        print(f"  Optimized: {opt_result}")
        print()


def test_lcs():
    """Test Longest Common Subsequence"""
    print("=== Testing Longest Common Subsequence ===\n")
    
    test_cases = [
        ("ABCDGH", "AEDFHR"),
        ("AGGTAB", "GXTXAYB"),
        ("programming", "grading"),
        ("ABCD", "EFGH")
    ]
    
    for text1, text2 in test_cases:
        length = DynamicProgramming.lcs_length(text1, text2)
        lcs_str = DynamicProgramming.lcs_string(text1, text2)
        length_opt = DynamicProgramming.lcs_space_optimized(text1, text2)
        
        print(f"Text 1: '{text1}'")
        print(f"Text 2: '{text2}'")
        print(f"LCS Length: {length}")
        print(f"LCS String: '{lcs_str}'")
        print(f"Space Optimized Length: {length_opt}")
        print()


def test_knapsack():
    """Test 0/1 Knapsack Problem"""
    print("=== Testing 0/1 Knapsack Problem ===\n")
    
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    print(f"Weights: {weights}")
    print(f"Values: {values}")
    print(f"Capacity: {capacity}")
    print()
    
    max_value = DynamicProgramming.knapsack_01(weights, values, capacity)
    max_value_opt = DynamicProgramming.knapsack_01_optimized(weights, values, capacity)
    max_value_items, selected_items = DynamicProgramming.knapsack_01_with_items(weights, values, capacity)
    
    print(f"Maximum value: {max_value}")
    print(f"Maximum value (optimized): {max_value_opt}")
    print(f"Selected items (indices): {selected_items}")
    print(f"Selected weights: {[weights[i] for i in selected_items]}")
    print(f"Selected values: {[values[i] for i in selected_items]}")
    print()


def test_coin_change():
    """Test Coin Change Problem"""
    print("=== Testing Coin Change Problem ===\n")
    
    test_cases = [
        ([1, 2, 5], 11),
        ([2], 3),
        ([1, 3, 4], 6)
    ]
    
    for coins, amount in test_cases:
        min_coins = DynamicProgramming.coin_change_min_coins(coins, amount)
        ways = DynamicProgramming.coin_change_ways(coins, amount)
        
        print(f"Coins: {coins}, Amount: {amount}")
        print(f"Minimum coins needed: {min_coins}")
        print(f"Number of ways: {ways}")
        print()


def test_edit_distance():
    """Test Edit Distance"""
    print("=== Testing Edit Distance ===\n")
    
    test_cases = [
        ("horse", "ros"),
        ("intention", "execution"),
        ("kitten", "sitting"),
        ("saturday", "sunday")
    ]
    
    for word1, word2 in test_cases:
        distance = DynamicProgramming.edit_distance(word1, word2)
        distance_opt = DynamicProgramming.edit_distance_optimized(word1, word2)
        
        print(f"Word 1: '{word1}'")
        print(f"Word 2: '{word2}'")
        print(f"Edit Distance: {distance}")
        print(f"Edit Distance (optimized): {distance_opt}")
        print()


def test_other_problems():
    """Test other DP problems"""
    print("=== Testing Other DP Problems ===\n")
    
    # Longest Increasing Subsequence
    print("Longest Increasing Subsequence:")
    lis_test = [10, 9, 2, 5, 3, 7, 101, 18]
    lis_length = DynamicProgramming.lis_length(lis_test)
    lis_length_opt = DynamicProgramming.lis_binary_search(lis_test)
    print(f"Array: {lis_test}")
    print(f"LIS Length: {lis_length}")
    print(f"LIS Length (optimized): {lis_length_opt}")
    print()
    
    # Matrix Chain Multiplication
    print("Matrix Chain Multiplication:")
    matrix_dims = [1, 2, 3, 4, 5]
    mcm_result = DynamicProgramming.matrix_chain_multiplication(matrix_dims)
    print(f"Matrix dimensions: {matrix_dims}")
    print(f"Minimum scalar multiplications: {mcm_result}")
    print()
    
    # Longest Palindromic Subsequence
    print("Longest Palindromic Subsequence:")
    palindrome_test = "bbbab"
    lps_length = DynamicProgramming.longest_palindromic_subsequence(palindrome_test)
    print(f"String: '{palindrome_test}'")
    print(f"LPS Length: {lps_length}")
    print()
    
    # Maximum Subarray Sum
    print("Maximum Subarray Sum:")
    subarray_test = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    max_sum = DynamicProgramming.max_subarray_sum(subarray_test)
    max_sum_with_indices = DynamicProgramming.max_subarray_with_indices(subarray_test)
    print(f"Array: {subarray_test}")
    print(f"Maximum sum: {max_sum}")
    print(f"Maximum sum with indices: {max_sum_with_indices}")
    print()
    
    # House Robber
    print("House Robber:")
    houses = [2, 7, 9, 3, 1]
    max_money = DynamicProgramming.house_robber(houses)
    houses_circular = [2, 3, 2]
    max_money_circular = DynamicProgramming.house_robber_circular(houses_circular)
    print(f"Houses (linear): {houses}")
    print(f"Maximum money: {max_money}")
    print(f"Houses (circular): {houses_circular}")
    print(f"Maximum money (circular): {max_money_circular}")


def performance_comparison():
    """Compare performance of different DP approaches"""
    print("\n=== Performance Comparison ===\n")
    
    import time
    
    # Fibonacci performance comparison
    print("Fibonacci Performance (n=30):")
    n = 30
    
    # Memoization
    start_time = time.time()
    result_memo = DynamicProgramming.fibonacci_memoization(n)
    memo_time = time.time() - start_time
    
    # Tabulation
    start_time = time.time()
    result_tab = DynamicProgramming.fibonacci_tabulation(n)
    tab_time = time.time() - start_time
    
    # Optimized
    start_time = time.time()
    result_opt = DynamicProgramming.fibonacci_optimized(n)
    opt_time = time.time() - start_time
    
    print(f"Memoization: {result_memo} in {memo_time:.6f}s")
    print(f"Tabulation: {result_tab} in {tab_time:.6f}s")
    print(f"Optimized: {result_opt} in {opt_time:.6f}s")
    print()
    
    # LCS performance comparison
    print("LCS Performance:")
    text1 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    text2 = "ACEGIKMOQSUWY"
    
    start_time = time.time()
    lcs_normal = DynamicProgramming.lcs_length(text1, text2)
    normal_time = time.time() - start_time
    
    start_time = time.time()
    lcs_optimized = DynamicProgramming.lcs_space_optimized(text1, text2)
    optimized_time = time.time() - start_time
    
    print(f"Normal LCS: {lcs_normal} in {normal_time:.6f}s")
    print(f"Space-optimized LCS: {lcs_optimized} in {optimized_time:.6f}s")


if __name__ == "__main__":
    test_fibonacci()
    test_lcs()
    test_knapsack()
    test_coin_change()
    test_edit_distance()
    test_other_problems()
    performance_comparison()
