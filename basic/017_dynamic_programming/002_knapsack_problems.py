"""
002 - Knapsack Problems
======================

Classic knapsack problems solved using dynamic programming.

Problems covered:
1. 0/1 Knapsack (each item can be taken at most once)
2. Unbounded Knapsack (unlimited items of each type)
3. Bounded Knapsack (limited quantity of each item)

Time Complexity: O(n * W) where n = items, W = capacity
Space Complexity: O(n * W) or O(W) with space optimization

Applications:
- Resource allocation
- Portfolio optimization
- Cutting stock problems
"""

from typing import List, Tuple, Dict


def knapsack_01(weights: List[int], values: List[int], capacity: int) -> Tuple[int, List[int]]:
    """
    0/1 Knapsack: Each item can be taken at most once
    
    Args:
        weights: List of item weights
        values: List of item values
        capacity: Knapsack capacity
    
    Returns:
        Tuple of (max_value, selected_items_indices)
    """
    n = len(weights)
    
    # DP table: dp[i][w] = max value using first i items with capacity w
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]
    
    # Fill DP table
    for i in range(1, n + 1):
        for w in range(capacity + 1):
            # Don't take item i-1
            dp[i][w] = dp[i-1][w]
            
            # Take item i-1 if possible
            if weights[i-1] <= w:
                dp[i][w] = max(dp[i][w], dp[i-1][w - weights[i-1]] + values[i-1])
    
    # Backtrack to find selected items
    selected_items = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i-1][w]:
            selected_items.append(i-1)  # Item index
            w -= weights[i-1]
    
    selected_items.reverse()
    return dp[n][capacity], selected_items


def knapsack_01_optimized(weights: List[int], values: List[int], capacity: int) -> int:
    """
    Space-optimized 0/1 Knapsack (only returns max value)
    
    Space Complexity: O(W) instead of O(n * W)
    """
    dp = [0] * (capacity + 1)
    
    for i in range(len(weights)):
        # Traverse backwards to avoid using updated values
        for w in range(capacity, weights[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - weights[i]] + values[i])
    
    return dp[capacity]


def knapsack_unbounded(weights: List[int], values: List[int], capacity: int) -> Tuple[int, Dict[int, int]]:
    """
    Unbounded Knapsack: Unlimited items of each type
    
    Returns:
        Tuple of (max_value, item_count_dict)
    """
    n = len(weights)
    dp = [0] * (capacity + 1)
    parent = [-1] * (capacity + 1)  # To track which item was used
    
    for w in range(1, capacity + 1):
        for i in range(n):
            if weights[i] <= w:
                new_value = dp[w - weights[i]] + values[i]
                if new_value > dp[w]:
                    dp[w] = new_value
                    parent[w] = i
    
    # Reconstruct solution
    item_count = {i: 0 for i in range(n)}
    w = capacity
    while w > 0 and parent[w] != -1:
        item_idx = parent[w]
        item_count[item_idx] += 1
        w -= weights[item_idx]
    
    return dp[capacity], item_count


def knapsack_bounded(weights: List[int], values: List[int], 
                    quantities: List[int], capacity: int) -> int:
    """
    Bounded Knapsack: Limited quantity of each item
    
    Args:
        weights: Item weights
        values: Item values
        quantities: Available quantity of each item
        capacity: Knapsack capacity
    
    Returns:
        Maximum value achievable
    """
    # Convert to 0/1 knapsack by expanding items
    expanded_weights = []
    expanded_values = []
    
    for i in range(len(weights)):
        for _ in range(quantities[i]):
            expanded_weights.append(weights[i])
            expanded_values.append(values[i])
    
    return knapsack_01_optimized(expanded_weights, expanded_values, capacity)


def knapsack_bounded_optimized(weights: List[int], values: List[int], 
                              quantities: List[int], capacity: int) -> int:
    """
    Optimized Bounded Knapsack using binary representation
    
    Uses binary representation to reduce items efficiently
    """
    expanded_weights = []
    expanded_values = []
    
    for i in range(len(weights)):
        qty = quantities[i]
        k = 1
        
        # Use binary representation
        while k < qty:
            expanded_weights.append(k * weights[i])
            expanded_values.append(k * values[i])
            qty -= k
            k *= 2
        
        # Add remaining quantity
        if qty > 0:
            expanded_weights.append(qty * weights[i])
            expanded_values.append(qty * values[i])
    
    return knapsack_01_optimized(expanded_weights, expanded_values, capacity)


def knapsack_fractional_greedy(weights: List[int], values: List[int], capacity: int) -> float:
    """
    Fractional Knapsack using greedy approach (not DP, but for comparison)
    
    Items can be taken partially
    """
    # Calculate value-to-weight ratio
    items = [(values[i] / weights[i], weights[i], values[i], i) 
             for i in range(len(weights))]
    
    # Sort by ratio in descending order
    items.sort(reverse=True)
    
    total_value = 0.0
    remaining_capacity = capacity
    
    for ratio, weight, value, idx in items:
        if weight <= remaining_capacity:
            # Take entire item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fractional part
            fraction = remaining_capacity / weight
            total_value += value * fraction
            break
    
    return total_value


def demo_knapsack_problems():
    """Demonstrate different knapsack variants"""
    print("=== Knapsack Problems Demo ===")
    
    # Sample items
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    
    print(f"Items: weights={weights}, values={values}")
    print(f"Knapsack capacity: {capacity}")
    
    # 0/1 Knapsack
    max_value, selected = knapsack_01(weights, values, capacity)
    print(f"\n0/1 Knapsack:")
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {selected}")
    
    selected_weights = [weights[i] for i in selected]
    selected_values = [values[i] for i in selected]
    print(f"Selected weights: {selected_weights} (total: {sum(selected_weights)})")
    print(f"Selected values: {selected_values} (total: {sum(selected_values)})")
    
    # Unbounded Knapsack
    max_value_unbounded, item_counts = knapsack_unbounded(weights, values, capacity)
    print(f"\nUnbounded Knapsack:")
    print(f"Maximum value: {max_value_unbounded}")
    print(f"Item counts: {item_counts}")
    
    total_weight = sum(item_counts[i] * weights[i] for i in range(len(weights)))
    total_value = sum(item_counts[i] * values[i] for i in range(len(weights)))
    print(f"Total weight used: {total_weight}")
    print(f"Total value: {total_value}")
    
    # Bounded Knapsack
    quantities = [1, 2, 3]  # Limited quantities
    max_value_bounded = knapsack_bounded(weights, values, quantities, capacity)
    print(f"\nBounded Knapsack (quantities {quantities}):")
    print(f"Maximum value: {max_value_bounded}")
    
    # Fractional Knapsack
    max_value_fractional = knapsack_fractional_greedy(weights, values, capacity)
    print(f"\nFractional Knapsack (greedy):")
    print(f"Maximum value: {max_value_fractional:.2f}")


def demo_large_knapsack():
    """Demonstrate with larger problem instance"""
    print("\n=== Large Knapsack Demo ===")
    
    # Larger problem
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    values = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    capacity = 165
    
    print(f"Items: {len(weights)} items")
    print(f"Capacity: {capacity}")
    
    # Compare different approaches
    import time
    
    # 0/1 Knapsack
    start_time = time.time()
    max_value, selected = knapsack_01(weights, values, capacity)
    time_01 = time.time() - start_time
    
    print(f"\n0/1 Knapsack:")
    print(f"Maximum value: {max_value}")
    print(f"Selected items: {len(selected)} items")
    print(f"Time: {time_01:.4f} seconds")
    
    # Optimized 0/1 Knapsack
    start_time = time.time()
    max_value_opt = knapsack_01_optimized(weights, values, capacity)
    time_opt = time.time() - start_time
    
    print(f"\nOptimized 0/1 Knapsack:")
    print(f"Maximum value: {max_value_opt}")
    print(f"Time: {time_opt:.4f} seconds")
    print(f"Speedup: {time_01/time_opt:.2f}x")
    
    # Unbounded Knapsack
    start_time = time.time()
    max_value_unbounded, _ = knapsack_unbounded(weights, values, capacity)
    time_unbounded = time.time() - start_time
    
    print(f"\nUnbounded Knapsack:")
    print(f"Maximum value: {max_value_unbounded}")
    print(f"Time: {time_unbounded:.4f} seconds")


def knapsack_variations():
    """Discuss knapsack problem variations"""
    print("\n=== Knapsack Variations ===")
    
    print("1. 0/1 Knapsack:")
    print("   • Each item can be taken at most once")
    print("   • Most common variant")
    print("   • Used in resource allocation")
    
    print("\n2. Unbounded Knapsack:")
    print("   • Unlimited quantity of each item")
    print("   • Also called 'Coin Change' problem variant")
    print("   • Used in making change, cutting problems")
    
    print("\n3. Bounded Knapsack:")
    print("   • Limited quantity of each item")
    print("   • Real-world scenario")
    print("   • Can be reduced to 0/1 knapsack")
    
    print("\n4. Fractional Knapsack:")
    print("   • Items can be taken partially")
    print("   • Solved optimally by greedy algorithm")
    print("   • Not a DP problem")
    
    print("\n5. Multiple Knapsacks:")
    print("   • Multiple knapsacks with different capacities")
    print("   • NP-hard problem")
    print("   • Used in bin packing")
    
    print("\n6. Multi-dimensional Knapsack:")
    print("   • Multiple constraints (weight, volume, etc.)")
    print("   • More complex state space")
    print("   • Real-world packing problems")
    
    print("\nComplexity Analysis:")
    print("• Time: O(n * W) for basic variants")
    print("• Space: O(n * W) or O(W) with optimization")
    print("• Pseudo-polynomial (depends on capacity value)")
    print("• NP-hard in general case")


if __name__ == "__main__":
    demo_knapsack_problems()
    demo_large_knapsack()
    knapsack_variations()
