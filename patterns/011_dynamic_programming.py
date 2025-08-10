"""
Dynamic Programming Pattern

Dynamic Programming is an algorithmic paradigm that solves complex problems by 
breaking them down into simpler subproblems. It is applicable to problems 
exhibiting overlapping subproblems and optimal substructure properties.

Key Techniques:
1. Memoization (Top-down approach)
2. Tabulation (Bottom-up approach)

Time Complexity: Usually O(n), O(n^2), or O(n*m)
Space Complexity: Often O(n) or O(n*m)

Common Problems:
- Fibonacci Numbers
- Climbing Stairs
- House Robber
- Coin Change
- Longest Common Subsequence
- Knapsack Problem
"""

def fibonacci_memoization(n, memo={}):
    """
    Calculate nth Fibonacci number using memoization.
    
    Args:
        n: position in Fibonacci sequence
        memo: memoization dictionary
    
    Returns:
        nth Fibonacci number
    """
    if n in memo:
        return memo[n]
    
    if n <= 1:
        return n
    
    memo[n] = fibonacci_memoization(n - 1, memo) + fibonacci_memoization(n - 2, memo)
    return memo[n]


def fibonacci_tabulation(n):
    """
    Calculate nth Fibonacci number using tabulation.
    
    Args:
        n: position in Fibonacci sequence
    
    Returns:
        nth Fibonacci number
    """
    if n <= 1:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climbing_stairs(n):
    """
    Calculate number of ways to climb n stairs (1 or 2 steps at a time).
    
    Args:
        n: number of stairs
    
    Returns:
        number of ways to climb stairs
    """
    if n <= 2:
        return n
    
    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    
    for i in range(3, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    
    return dp[n]


def climbing_stairs_optimized(n):
    """
    Space-optimized version of climbing stairs.
    
    Args:
        n: number of stairs
    
    Returns:
        number of ways to climb stairs
    """
    if n <= 2:
        return n
    
    prev1, prev2 = 2, 1
    
    for i in range(3, n + 1):
        current = prev1 + prev2
        prev2 = prev1
        prev1 = current
    
    return prev1


def house_robber(nums):
    """
    Find maximum money that can be robbed without robbing adjacent houses.
    
    Args:
        nums: array representing money in each house
    
    Returns:
        maximum money that can be robbed
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    dp = [0] * len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    
    for i in range(2, len(nums)):
        dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
    
    return dp[-1]


def house_robber_optimized(nums):
    """
    Space-optimized version of house robber.
    
    Args:
        nums: array representing money in each house
    
    Returns:
        maximum money that can be robbed
    """
    if not nums:
        return 0
    if len(nums) == 1:
        return nums[0]
    
    prev1 = max(nums[0], nums[1])
    prev2 = nums[0]
    
    for i in range(2, len(nums)):
        current = max(prev1, prev2 + nums[i])
        prev2 = prev1
        prev1 = current
    
    return prev1


def coin_change(coins, amount):
    """
    Find minimum number of coins to make the amount.
    
    Args:
        coins: array of coin denominations
        amount: target amount
    
    Returns:
        minimum number of coins, -1 if impossible
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_ways(coins, amount):
    """
    Find number of ways to make the amount using given coins.
    
    Args:
        coins: array of coin denominations
        amount: target amount
    
    Returns:
        number of ways to make the amount
    """
    dp = [0] * (amount + 1)
    dp[0] = 1
    
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


def longest_common_subsequence(text1, text2):
    """
    Find length of longest common subsequence between two strings.
    
    Args:
        text1: first string
        text2: second string
    
    Returns:
        length of longest common subsequence
    """
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    
    return dp[m][n]


def longest_increasing_subsequence(nums):
    """
    Find length of longest increasing subsequence.
    
    Args:
        nums: array of integers
    
    Returns:
        length of longest increasing subsequence
    """
    if not nums:
        return 0
    
    dp = [1] * len(nums)
    
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    return max(dp)


def knapsack_01(weights, values, capacity):
    """
    Solve 0/1 Knapsack problem.
    
    Args:
        weights: array of item weights
        values: array of item values
        capacity: knapsack capacity
    
    Returns:
        maximum value that can be obtained
    """
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(
                    values[i - 1] + dp[i - 1][w - weights[i - 1]],  # include item
                    dp[i - 1][w]  # exclude item
                )
            else:
                dp[i][w] = dp[i - 1][w]  # exclude item
    
    return dp[n][capacity]


def unbounded_knapsack(weights, values, capacity):
    """
    Solve Unbounded Knapsack problem (unlimited items).
    
    Args:
        weights: array of item weights
        values: array of item values
        capacity: knapsack capacity
    
    Returns:
        maximum value that can be obtained
    """
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        for w in range(weights[i], capacity + 1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def word_break(s, word_dict):
    """
    Check if string can be segmented into words from dictionary.
    
    Args:
        s: input string
        word_dict: dictionary of valid words
    
    Returns:
        True if string can be segmented, False otherwise
    """
    dp = [False] * (len(s) + 1)
    dp[0] = True
    word_set = set(word_dict)
    
    for i in range(1, len(s) + 1):
        for j in range(i):
            if dp[j] and s[j:i] in word_set:
                dp[i] = True
                break
    
    return dp[len(s)]


def edit_distance(word1, word2):
    """
    Find minimum edit distance between two strings.
    
    Args:
        word1: first string
        word2: second string
    
    Returns:
        minimum number of operations to convert word1 to word2
    """
    m, n = len(word1), len(word2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    
    # Initialize base cases
    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(
                    dp[i - 1][j],      # delete
                    dp[i][j - 1],      # insert
                    dp[i - 1][j - 1]   # replace
                )
    
    return dp[m][n]


def maximum_subarray_sum(nums):
    """
    Find maximum sum of contiguous subarray (Kadane's algorithm).
    
    Args:
        nums: array of integers
    
    Returns:
        maximum sum of contiguous subarray
    """
    max_sum = current_sum = nums[0]
    
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum


def unique_paths(m, n):
    """
    Find number of unique paths from top-left to bottom-right in m x n grid.
    
    Args:
        m: number of rows
        n: number of columns
    
    Returns:
        number of unique paths
    """
    dp = [[1] * n for _ in range(m)]
    
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
    
    return dp[m - 1][n - 1]


def unique_paths_optimized(m, n):
    """
    Space-optimized version of unique paths.
    
    Args:
        m: number of rows
        n: number of columns
    
    Returns:
        number of unique paths
    """
    dp = [1] * n
    
    for i in range(1, m):
        for j in range(1, n):
            dp[j] += dp[j - 1]
    
    return dp[n - 1]


def minimum_path_sum(grid):
    """
    Find minimum path sum from top-left to bottom-right.
    
    Args:
        grid: 2D grid of non-negative numbers
    
    Returns:
        minimum path sum
    """
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    
    dp[0][0] = grid[0][0]
    
    # Initialize first row
    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + grid[0][j]
    
    # Initialize first column
    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    
    # Fill the rest of the table
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i - 1][j], dp[i][j - 1]) + grid[i][j]
    
    return dp[m - 1][n - 1]


# Example usage and test cases
if __name__ == "__main__":
    # Test Fibonacci
    print("=== Fibonacci ===")
    n = 10
    result_memo = fibonacci_memoization(n)
    result_tab = fibonacci_tabulation(n)
    print(f"Fibonacci({n}) - Memoization: {result_memo}")
    print(f"Fibonacci({n}) - Tabulation: {result_tab}")
    
    # Test Climbing Stairs
    print("\n=== Climbing Stairs ===")
    n = 5
    result = climbing_stairs(n)
    result_opt = climbing_stairs_optimized(n)
    print(f"Ways to climb {n} stairs: {result}")
    print(f"Ways to climb {n} stairs (optimized): {result_opt}")
    
    # Test House Robber
    print("\n=== House Robber ===")
    houses = [1, 2, 3, 1]
    result = house_robber(houses)
    result_opt = house_robber_optimized(houses)
    print(f"Houses: {houses}")
    print(f"Maximum money: {result}")
    print(f"Maximum money (optimized): {result_opt}")
    
    # Test Coin Change
    print("\n=== Coin Change ===")
    coins = [1, 3, 4]
    amount = 6
    result = coin_change(coins, amount)
    ways = coin_change_ways(coins, amount)
    print(f"Coins: {coins}, Amount: {amount}")
    print(f"Minimum coins: {result}")
    print(f"Number of ways: {ways}")
    
    # Test Longest Common Subsequence
    print("\n=== Longest Common Subsequence ===")
    text1, text2 = "abcde", "ace"
    result = longest_common_subsequence(text1, text2)
    print(f"Text1: {text1}, Text2: {text2}")
    print(f"LCS length: {result}")  # 3
    
    # Test Longest Increasing Subsequence
    print("\n=== Longest Increasing Subsequence ===")
    nums = [10, 9, 2, 5, 3, 7, 101, 18]
    result = longest_increasing_subsequence(nums)
    print(f"Array: {nums}")
    print(f"LIS length: {result}")  # 4
    
    # Test 0/1 Knapsack
    print("\n=== 0/1 Knapsack ===")
    weights = [1, 3, 4, 5]
    values = [1, 4, 5, 7]
    capacity = 7
    result = knapsack_01(weights, values, capacity)
    print(f"Weights: {weights}, Values: {values}, Capacity: {capacity}")
    print(f"Maximum value: {result}")  # 9
    
    # Test Edit Distance
    print("\n=== Edit Distance ===")
    word1, word2 = "horse", "ros"
    result = edit_distance(word1, word2)
    print(f"Word1: {word1}, Word2: {word2}")
    print(f"Edit distance: {result}")  # 3
    
    # Test Maximum Subarray Sum
    print("\n=== Maximum Subarray Sum ===")
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    result = maximum_subarray_sum(nums)
    print(f"Array: {nums}")
    print(f"Maximum subarray sum: {result}")  # 6
    
    # Test Unique Paths
    print("\n=== Unique Paths ===")
    m, n = 3, 7
    result = unique_paths(m, n)
    result_opt = unique_paths_optimized(m, n)
    print(f"Grid: {m} x {n}")
    print(f"Unique paths: {result}")
    print(f"Unique paths (optimized): {result_opt}")
    
    # Test Minimum Path Sum
    print("\n=== Minimum Path Sum ===")
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    result = minimum_path_sum(grid)
    print(f"Grid: {grid}")
    print(f"Minimum path sum: {result}")  # 7
