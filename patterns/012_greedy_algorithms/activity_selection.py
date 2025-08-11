"""
Greedy Algorithm Pattern - Activity Selection
=============================================

Select maximum number of non-overlapping activities.

Time Complexity: O(n log n) for sorting
Space Complexity: O(1)
"""


def activity_selection(activities):
    """
    Select maximum number of non-overlapping activities.
    
    Args:
        activities: List of (start_time, end_time) tuples
        
    Returns:
        List of selected activities
    """
    if not activities:
        return []
    
    # Sort by end time (greedy choice)
    sorted_activities = sorted(activities, key=lambda x: x[1])
    
    selected = [sorted_activities[0]]  # Always select first activity
    last_end_time = sorted_activities[0][1]
    
    # Greedily select activities that don't overlap
    for start, end in sorted_activities[1:]:
        if start >= last_end_time:  # No overlap
            selected.append((start, end))
            last_end_time = end
    
    return selected


def example_usage():
    """Demonstrate activity selection"""
    # Activities: (start_time, end_time)
    activities = [
        (1, 4),   # Activity 1
        (3, 5),   # Activity 2
        (0, 6),   # Activity 3
        (5, 7),   # Activity 4
        (8, 9),   # Activity 5
        (5, 9)    # Activity 6
    ]
    
    print("Available activities (start, end):")
    for i, activity in enumerate(activities, 1):
        print(f"Activity {i}: {activity}")
    
    selected = activity_selection(activities)
    
    print(f"\nSelected activities: {selected}")
    print(f"Maximum number of activities: {len(selected)}")
    
    # Show the selection process
    print("\nGreedy selection process:")
    print("1. Sort by end time")
    print("2. Always pick activity that ends earliest")
    print("3. Skip overlapping activities")


if __name__ == "__main__":
    example_usage()
