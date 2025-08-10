"""
Greedy Algorithm Pattern

Greedy algorithms make the locally optimal choice at each step, hoping to find 
a global optimum. The key insight is that a locally optimal choice leads to a 
globally optimal solution. This approach works for optimization problems with 
the greedy-choice property and optimal substructure.

Time Complexity: Usually O(n log n) due to sorting
Space Complexity: Usually O(1) or O(n)

Common Problems:
- Activity Selection
- Fractional Knapsack
- Huffman Coding
- Job Scheduling
- Minimum Spanning Tree
- Dijkstra's Algorithm
"""

import heapq
from collections import defaultdict, Counter


def activity_selection(activities):
    """
    Select maximum number of activities that don't overlap.
    
    Args:
        activities: list of (start, end) tuples
    
    Returns:
        list of selected activities
    """
    # Sort by finish time
    activities.sort(key=lambda x: x[1])
    
    selected = [activities[0]]
    last_finish_time = activities[0][1]
    
    for i in range(1, len(activities)):
        start, end = activities[i]
        if start >= last_finish_time:
            selected.append(activities[i])
            last_finish_time = end
    
    return selected


def fractional_knapsack(items, capacity):
    """
    Solve fractional knapsack problem using greedy approach.
    
    Args:
        items: list of (value, weight) tuples
        capacity: knapsack capacity
    
    Returns:
        maximum value that can be obtained
    """
    # Calculate value-to-weight ratio and sort by it
    items_with_ratio = [(value/weight, value, weight) for value, weight in items]
    items_with_ratio.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = capacity
    
    for ratio, value, weight in items_with_ratio:
        if weight <= remaining_capacity:
            # Take the whole item
            total_value += value
            remaining_capacity -= weight
        else:
            # Take fraction of the item
            total_value += ratio * remaining_capacity
            break
    
    return total_value


def job_scheduling_max_profit(jobs):
    """
    Schedule jobs to maximize profit (each job has deadline and profit).
    
    Args:
        jobs: list of (profit, deadline) tuples
    
    Returns:
        (max_profit, selected_jobs)
    """
    # Sort jobs by profit in descending order
    jobs.sort(reverse=True)
    
    # Find maximum deadline
    max_deadline = max(job[1] for job in jobs)
    
    # Create schedule array
    schedule = [None] * max_deadline
    total_profit = 0
    selected_jobs = []
    
    for profit, deadline in jobs:
        # Find a free slot from deadline-1 to 0
        for slot in range(min(deadline - 1, max_deadline - 1), -1, -1):
            if schedule[slot] is None:
                schedule[slot] = (profit, deadline)
                total_profit += profit
                selected_jobs.append((profit, deadline))
                break
    
    return total_profit, selected_jobs


def minimum_platforms(arrivals, departures):
    """
    Find minimum number of platforms needed for a railway station.
    
    Args:
        arrivals: list of arrival times
        departures: list of departure times
    
    Returns:
        minimum number of platforms needed
    """
    arrivals.sort()
    departures.sort()
    
    platforms_needed = 0
    max_platforms = 0
    i = j = 0
    
    while i < len(arrivals) and j < len(departures):
        if arrivals[i] <= departures[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms


def huffman_coding(text):
    """
    Generate Huffman codes for characters in text.
    
    Args:
        text: input text
    
    Returns:
        dictionary mapping characters to their Huffman codes
    """
    if not text:
        return {}
    
    # Count frequency of each character
    frequency = Counter(text)
    
    # Create a min heap with frequencies
    heap = [[freq, char] for char, freq in frequency.items()]
    heapq.heapify(heap)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node
        merged = [left[0] + right[0], left, right]
        heapq.heappush(heap, merged)
    
    # Generate codes
    def generate_codes(node, code="", codes={}):
        if isinstance(node[1], str):  # Leaf node
            codes[node[1]] = code or "0"  # Handle single character case
        else:
            generate_codes(node[1], code + "0", codes)
            generate_codes(node[2], code + "1", codes)
        return codes
    
    if len(heap) == 1:
        return generate_codes(heap[0])
    return {}


def meeting_rooms_ii(intervals):
    """
    Find minimum number of meeting rooms required.
    
    Args:
        intervals: list of [start, end] intervals
    
    Returns:
        minimum number of meeting rooms
    """
    if not intervals:
        return 0
    
    # Separate start and end times
    starts = [interval[0] for interval in intervals]
    ends = [interval[1] for interval in intervals]
    
    starts.sort()
    ends.sort()
    
    rooms = 0
    end_idx = 0
    
    for start in starts:
        if start >= ends[end_idx]:
            end_idx += 1
        else:
            rooms += 1
    
    return rooms


def gas_station(gas, cost):
    """
    Find starting gas station index to complete circular tour.
    
    Args:
        gas: list of gas amounts at each station
        cost: list of costs to travel to next station
    
    Returns:
        starting station index, -1 if impossible
    """
    total_gas = sum(gas)
    total_cost = sum(cost)
    
    # If total gas < total cost, impossible to complete tour
    if total_gas < total_cost:
        return -1
    
    current_gas = 0
    start = 0
    
    for i in range(len(gas)):
        current_gas += gas[i] - cost[i]
        
        # If current gas becomes negative, start from next station
        if current_gas < 0:
            current_gas = 0
            start = i + 1
    
    return start


def candy_distribution(ratings):
    """
    Distribute minimum candies to children based on ratings.
    
    Args:
        ratings: list of ratings for each child
    
    Returns:
        minimum number of candies needed
    """
    n = len(ratings)
    candies = [1] * n
    
    # Left to right pass
    for i in range(1, n):
        if ratings[i] > ratings[i - 1]:
            candies[i] = candies[i - 1] + 1
    
    # Right to left pass
    for i in range(n - 2, -1, -1):
        if ratings[i] > ratings[i + 1]:
            candies[i] = max(candies[i], candies[i + 1] + 1)
    
    return sum(candies)


def jump_game(nums):
    """
    Check if you can reach the last index.
    
    Args:
        nums: list where each element represents max jump length
    
    Returns:
        True if last index is reachable, False otherwise
    """
    max_reach = 0
    
    for i in range(len(nums)):
        if i > max_reach:
            return False
        max_reach = max(max_reach, i + nums[i])
        
        if max_reach >= len(nums) - 1:
            return True
    
    return False


def jump_game_min_jumps(nums):
    """
    Find minimum number of jumps to reach the last index.
    
    Args:
        nums: list where each element represents max jump length
    
    Returns:
        minimum number of jumps needed
    """
    if len(nums) <= 1:
        return 0
    
    jumps = 0
    current_end = 0
    farthest = 0
    
    for i in range(len(nums) - 1):
        farthest = max(farthest, i + nums[i])
        
        if i == current_end:
            jumps += 1
            current_end = farthest
    
    return jumps


def merge_intervals_greedy(intervals):
    """
    Merge overlapping intervals using greedy approach.
    
    Args:
        intervals: list of [start, end] intervals
    
    Returns:
        list of merged intervals
    """
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        if current[0] <= last_merged[1]:  # Overlapping
            last_merged[1] = max(last_merged[1], current[1])
        else:
            merged.append(current)
    
    return merged


def minimum_arrows_burst_balloons(points):
    """
    Find minimum number of arrows to burst all balloons.
    
    Args:
        points: list of [start, end] coordinates of balloons
    
    Returns:
        minimum number of arrows needed
    """
    if not points:
        return 0
    
    # Sort by end coordinate
    points.sort(key=lambda x: x[1])
    
    arrows = 1
    arrow_position = points[0][1]
    
    for start, end in points[1:]:
        if start > arrow_position:
            arrows += 1
            arrow_position = end
    
    return arrows


def partition_labels(s):
    """
    Partition string into as many parts as possible where each letter appears in at most one part.
    
    Args:
        s: input string
    
    Returns:
        list of lengths of each part
    """
    # Find last occurrence of each character
    last = {char: i for i, char in enumerate(s)}
    
    result = []
    start = 0
    end = 0
    
    for i, char in enumerate(s):
        end = max(end, last[char])
        
        if i == end:  # Current partition ends here
            result.append(end - start + 1)
            start = i + 1
    
    return result


def remove_k_digits(num, k):
    """
    Remove k digits from number to make it smallest.
    
    Args:
        num: string representing the number
        k: number of digits to remove
    
    Returns:
        smallest possible number as string
    """
    stack = []
    to_remove = k
    
    for digit in num:
        # Remove larger digits from stack
        while stack and to_remove > 0 and stack[-1] > digit:
            stack.pop()
            to_remove -= 1
        stack.append(digit)
    
    # Remove remaining digits from the end
    while to_remove > 0:
        stack.pop()
        to_remove -= 1
    
    # Convert to string and remove leading zeros
    result = ''.join(stack).lstrip('0')
    return result or '0'


# Example usage and test cases
if __name__ == "__main__":
    # Test Activity Selection
    print("=== Activity Selection ===")
    activities = [(1, 3), (2, 4), (3, 5), (0, 6), (5, 7), (8, 9), (5, 9)]
    selected = activity_selection(activities)
    print(f"Activities: {activities}")
    print(f"Selected: {selected}")
    print(f"Number selected: {len(selected)}")
    
    # Test Fractional Knapsack
    print("\n=== Fractional Knapsack ===")
    items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
    capacity = 50
    max_value = fractional_knapsack(items, capacity)
    print(f"Items (value, weight): {items}")
    print(f"Capacity: {capacity}")
    print(f"Maximum value: {max_value}")
    
    # Test Job Scheduling
    print("\n=== Job Scheduling ===")
    jobs = [(20, 1), (15, 2), (10, 3), (5, 3), (1, 3)]  # (profit, deadline)
    max_profit, selected = job_scheduling_max_profit(jobs)
    print(f"Jobs (profit, deadline): {jobs}")
    print(f"Maximum profit: {max_profit}")
    print(f"Selected jobs: {selected}")
    
    # Test Minimum Platforms
    print("\n=== Minimum Platforms ===")
    arrivals = [900, 940, 950, 1100, 1500, 1800]
    departures = [910, 1200, 1120, 1130, 1900, 2000]
    platforms = minimum_platforms(arrivals[:], departures[:])
    print(f"Arrivals: {arrivals}")
    print(f"Departures: {departures}")
    print(f"Minimum platforms: {platforms}")
    
    # Test Gas Station
    print("\n=== Gas Station ===")
    gas = [1, 2, 3, 4, 5]
    cost = [3, 4, 5, 1, 2]
    start = gas_station(gas, cost)
    print(f"Gas: {gas}")
    print(f"Cost: {cost}")
    print(f"Starting station: {start}")
    
    # Test Candy Distribution
    print("\n=== Candy Distribution ===")
    ratings = [1, 0, 2]
    candies = candy_distribution(ratings)
    print(f"Ratings: {ratings}")
    print(f"Minimum candies: {candies}")
    
    # Test Jump Game
    print("\n=== Jump Game ===")
    nums = [2, 3, 1, 1, 4]
    can_reach = jump_game(nums)
    min_jumps = jump_game_min_jumps(nums)
    print(f"Array: {nums}")
    print(f"Can reach end: {can_reach}")
    print(f"Minimum jumps: {min_jumps}")
    
    # Test Minimum Arrows
    print("\n=== Minimum Arrows to Burst Balloons ===")
    balloons = [[10, 16], [2, 8], [1, 6], [7, 12]]
    arrows = minimum_arrows_burst_balloons(balloons)
    print(f"Balloons: {balloons}")
    print(f"Minimum arrows: {arrows}")
    
    # Test Partition Labels
    print("\n=== Partition Labels ===")
    s = "ababcbacadefegdehijhklij"
    partitions = partition_labels(s)
    print(f"String: {s}")
    print(f"Partition lengths: {partitions}")
    
    # Test Remove K Digits
    print("\n=== Remove K Digits ===")
    num = "1432219"
    k = 3
    result = remove_k_digits(num, k)
    print(f"Number: {num}")
    print(f"Remove {k} digits: {result}")
