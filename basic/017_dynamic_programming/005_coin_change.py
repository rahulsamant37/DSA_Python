"""
005 - Coin Change Problems
=========================

Classic dynamic programming problems involving making change with coins.

Problems covered:
1. Coin Change (minimum coins) - Find minimum number of coins
2. Coin Change Ways - Count number of ways to make change
3. Coin Change with specific denominations
4. Unbounded coin change variations

Time Complexity: O(amount * n) where n = number of coin types
Space Complexity: O(amount) or O(amount * n)

Applications:
- Currency systems and ATM programming
- Resource allocation optimization
- Greedy algorithm analysis
- Mathematical combinatorics
"""

from typing import List, Dict, Tuple, Optional
import math


def coin_change_min_coins(coins: List[int], amount: int) -> int:
    """
    Find minimum number of coins needed to make amount
    
    Args:
        coins: List of coin denominations
        amount: Target amount
    
    Returns:
        Minimum number of coins, -1 if impossible
    """
    if amount == 0:
        return 0
    
    # dp[i] = minimum coins needed to make amount i
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_coins(coins: List[int], amount: int) -> Tuple[int, List[int]]:
    """
    Find minimum coins and return the actual coins used
    
    Args:
        coins: List of coin denominations
        amount: Target amount
    
    Returns:
        Tuple of (min_coins, coins_used)
    """
    if amount == 0:
        return 0, []
    
    dp = [float('inf')] * (amount + 1)
    parent = [-1] * (amount + 1)  # Track which coin was used
    dp[0] = 0
    
    for coin in coins:
        for i in range(coin, amount + 1):
            if dp[i - coin] != float('inf') and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin
    
    if dp[amount] == float('inf'):
        return -1, []
    
    # Reconstruct solution
    result_coins = []
    current = amount
    while current > 0:
        coin_used = parent[current]
        result_coins.append(coin_used)
        current -= coin_used
    
    return dp[amount], result_coins


def coin_change_ways(coins: List[int], amount: int) -> int:
    """
    Count number of ways to make change
    
    Args:
        coins: List of coin denominations
        amount: Target amount
    
    Returns:
        Number of different ways to make the amount
    """
    # dp[i] = number of ways to make amount i
    dp = [0] * (amount + 1)
    dp[0] = 1  # One way to make 0: use no coins
    
    # Process coins one by one to avoid counting permutations
    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    
    return dp[amount]


def coin_change_ways_with_details(coins: List[int], amount: int) -> Tuple[int, List[List[int]]]:
    """
    Count ways and return all possible combinations
    
    Args:
        coins: List of coin denominations
        amount: Target amount
    
    Returns:
        Tuple of (count, list_of_combinations)
    """
    def backtrack(remaining: int, coin_index: int, current_combination: List[int]) -> List[List[int]]:
        if remaining == 0:
            return [current_combination[:]]
        
        if remaining < 0 or coin_index >= len(coins):
            return []
        
        combinations = []
        coin = coins[coin_index]
        
        # Try using 0, 1, 2, ... of current coin
        max_count = remaining // coin
        for count in range(max_count + 1):
            # Add 'count' coins of current denomination
            current_combination.extend([coin] * count)
            
            # Recurse with remaining coins
            combinations.extend(backtrack(remaining - count * coin, 
                                        coin_index + 1, 
                                        current_combination))
            
            # Backtrack
            for _ in range(count):
                current_combination.pop()
        
        return combinations
    
    all_combinations = backtrack(amount, 0, [])
    return len(all_combinations), all_combinations


def coin_change_limited_coins(coins: List[int], counts: List[int], amount: int) -> int:
    """
    Coin change with limited number of each coin type
    
    Args:
        coins: List of coin denominations
        counts: Number available of each coin type
        amount: Target amount
    
    Returns:
        Minimum number of coins, -1 if impossible
    """
    # Convert to 0/1 knapsack by expanding coins
    expanded_coins = []
    for coin, count in zip(coins, counts):
        expanded_coins.extend([coin] * count)
    
    # Use standard coin change on expanded list
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for coin in expanded_coins:
        # Process in reverse to avoid using same coin multiple times
        for i in range(amount, coin - 1, -1):
            if dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def coin_change_with_fees(coins: List[int], fees: List[int], amount: int) -> int:
    """
    Coin change with transaction fees for each coin type
    
    Args:
        coins: List of coin denominations
        fees: Transaction fee for each coin type
        amount: Target amount
    
    Returns:
        Minimum total cost (coins + fees)
    """
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    
    for i, coin in enumerate(coins):
        fee = fees[i]
        for j in range(coin, amount + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + coin + fee)
    
    return dp[amount] if dp[amount] != float('inf') else -1


def make_change_greedy(coins: List[int], amount: int) -> Tuple[bool, List[int]]:
    """
    Greedy algorithm for making change (works for canonical coin systems)
    
    Args:
        coins: List of coin denominations (sorted descending)
        amount: Target amount
    
    Returns:
        Tuple of (success, coins_used)
    """
    coins = sorted(coins, reverse=True)
    result = []
    
    for coin in coins:
        count = amount // coin
        if count > 0:
            result.extend([coin] * count)
            amount -= coin * count
    
    return amount == 0, result


def is_canonical_coin_system(coins: List[int], test_amount: int = 100) -> bool:
    """
    Test if coin system is canonical (greedy gives optimal solution)
    
    Args:
        coins: List of coin denominations
        test_amount: Maximum amount to test
    
    Returns:
        True if canonical system
    """
    for amount in range(1, test_amount + 1):
        # Get optimal solution using DP
        optimal = coin_change_min_coins(coins, amount)
        if optimal == -1:
            continue
        
        # Get greedy solution
        greedy_success, greedy_coins = make_change_greedy(coins, amount)
        
        if not greedy_success or len(greedy_coins) != optimal:
            return False
    
    return True


def demo_basic_coin_change():
    """Demonstrate basic coin change problems"""
    print("=== Basic Coin Change Demo ===")
    
    coins = [1, 3, 4]
    amount = 6
    
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    
    # Minimum coins
    min_coins = coin_change_min_coins(coins, amount)
    print(f"Minimum coins needed: {min_coins}")
    
    # Minimum coins with actual coins
    count, used_coins = coin_change_with_coins(coins, amount)
    print(f"Coins used: {used_coins}")
    print(f"Verification: {sum(used_coins)} = {amount}")
    
    # Number of ways
    ways = coin_change_ways(coins, amount)
    print(f"Number of ways to make change: {ways}")
    
    # All combinations (for small amounts)
    if amount <= 10:
        count, combinations = coin_change_ways_with_details(coins, amount)
        print(f"All combinations:")
        for i, combo in enumerate(combinations, 1):
            print(f"  {i}: {combo}")


def demo_us_currency():
    """Demonstrate with US currency system"""
    print("\n=== US Currency Demo ===")
    
    # US coins in cents
    us_coins = [1, 5, 10, 25]  # penny, nickel, dime, quarter
    coin_names = {1: "penny", 5: "nickel", 10: "dime", 25: "quarter"}
    
    amounts = [30, 67, 99]
    
    for amount in amounts:
        print(f"\nMaking change for {amount} cents:")
        
        # DP solution
        min_coins = coin_change_min_coins(us_coins, amount)
        count, used_coins = coin_change_with_coins(us_coins, amount)
        
        print(f"  Minimum coins (DP): {min_coins}")
        
        # Count each coin type
        coin_count = {coin: used_coins.count(coin) for coin in us_coins}
        for coin in us_coins:
            if coin_count[coin] > 0:
                print(f"    {coin_count[coin]} {coin_names[coin]}{'s' if coin_count[coin] > 1 else ''}")
        
        # Greedy solution
        greedy_success, greedy_coins = make_change_greedy(us_coins, amount)
        print(f"  Greedy gives same result: {len(greedy_coins) == min_coins}")
    
    # Test if US system is canonical
    is_canonical = is_canonical_coin_system(us_coins, 100)
    print(f"\nUS coin system is canonical: {is_canonical}")


def demo_non_canonical_system():
    """Demonstrate non-canonical coin system"""
    print("\n=== Non-Canonical System Demo ===")
    
    # Non-canonical system where greedy fails
    coins = [1, 3, 4]
    amount = 6
    
    print(f"Coins: {coins}")
    print(f"Amount: {amount}")
    
    # DP solution
    min_coins_dp = coin_change_min_coins(coins, amount)
    count, used_coins_dp = coin_change_with_coins(coins, amount)
    
    print(f"Optimal (DP): {min_coins_dp} coins")
    print(f"Coins used: {used_coins_dp}")
    
    # Greedy solution
    greedy_success, greedy_coins = make_change_greedy(coins, amount)
    
    print(f"Greedy: {len(greedy_coins) if greedy_success else 'Failed'} coins")
    if greedy_success:
        print(f"Coins used: {greedy_coins}")
    
    print(f"Greedy is optimal: {greedy_success and len(greedy_coins) == min_coins_dp}")
    
    # Test canonicality
    is_canonical = is_canonical_coin_system(coins, 20)
    print(f"System is canonical: {is_canonical}")


def demo_ways_counting():
    """Demonstrate counting ways to make change"""
    print("\n=== Ways Counting Demo ===")
    
    coins = [1, 2, 5]
    amounts = [4, 5, 8]
    
    print(f"Coins: {coins}")
    
    for amount in amounts:
        ways = coin_change_ways(coins, amount)
        print(f"\nAmount {amount}: {ways} ways")
        
        if amount <= 8:  # Show details for small amounts
            count, combinations = coin_change_ways_with_details(coins, amount)
            for i, combo in enumerate(combinations, 1):
                print(f"  {i}: {combo} (sum: {sum(combo)})")


def demo_limited_coins():
    """Demonstrate coin change with limited coins"""
    print("\n=== Limited Coins Demo ===")
    
    coins = [1, 3, 4]
    counts = [2, 1, 1]  # 2 ones, 1 three, 1 four
    amount = 6
    
    print(f"Coins: {coins}")
    print(f"Available: {counts}")
    print(f"Amount: {amount}")
    
    # Standard unlimited coin change
    unlimited = coin_change_min_coins(coins, amount)
    print(f"Unlimited coins: {unlimited}")
    
    # Limited coin change
    limited = coin_change_limited_coins(coins, counts, amount)
    print(f"Limited coins: {limited}")
    
    # Show why it's different
    print(f"\nWith unlimited coins: can use [3, 3] = 2 coins")
    print(f"With limited coins: only 1 three available, need different combination")


def demo_transaction_fees():
    """Demonstrate coin change with transaction fees"""
    print("\n=== Transaction Fees Demo ===")
    
    coins = [1, 5, 10, 25]
    fees = [0, 1, 2, 3]  # Fee for using each coin type
    amount = 30
    
    print(f"Coins: {coins}")
    print(f"Fees: {fees}")
    print(f"Amount: {amount}")
    
    # Without fees
    normal_cost = coin_change_min_coins(coins, amount)
    print(f"Without fees: {normal_cost} coins")
    
    # With fees
    total_cost = coin_change_with_fees(coins, fees, amount)
    print(f"With fees: total cost = {total_cost}")
    
    # Break down the optimal solution
    count, used_coins = coin_change_with_coins(coins, amount)
    fee_cost = sum(fees[coins.index(coin)] for coin in used_coins)
    print(f"Breakdown: {amount} (amount) + {fee_cost} (fees) = {amount + fee_cost}")


def analyze_complexity():
    """Analyze time and space complexity"""
    print("\n=== Complexity Analysis ===")
    
    print("Coin Change (Minimum Coins):")
    print("• Time: O(amount × number_of_coins)")
    print("• Space: O(amount)")
    print("• Bottom-up DP approach")
    
    print("\nCoin Change (Count Ways):")
    print("• Time: O(amount × number_of_coins)")
    print("• Space: O(amount)")
    print("• Avoids counting permutations")
    
    print("\nLimited Coins:")
    print("• Time: O(amount × total_coins)")
    print("• Space: O(amount)")
    print("• Reduces to 0/1 knapsack variant")
    
    print("\nGreedy Algorithm:")
    print("• Time: O(number_of_coins)")
    print("• Space: O(1)")
    print("• Works only for canonical systems")
    
    print("\nCanonical Systems:")
    print("• US currency: [1, 5, 10, 25] ✓")
    print("• Euro currency: [1, 2, 5, 10, 20, 50] ✓")
    print("• Example non-canonical: [1, 3, 4] ✗")


if __name__ == "__main__":
    demo_basic_coin_change()
    demo_us_currency()
    demo_non_canonical_system()
    demo_ways_counting()
    demo_limited_coins()
    demo_transaction_fees()
    analyze_complexity()
