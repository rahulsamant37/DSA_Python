"""
Merge Intervals Pattern - Interval Operations
==============================================

Merge overlapping intervals and related operations.

Time Complexity: O(n log n) for sorting
Space Complexity: O(n)
"""


def merge_intervals(intervals):
    """
    Merge overlapping intervals.
    
    Args:
        intervals: List of [start, end] intervals
        
    Returns:
        List of merged intervals
    """
    if not intervals:
        return []
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        
        # Check if current interval overlaps with last merged
        if current[0] <= last_merged[1]:
            # Merge intervals
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add current interval
            merged.append(current)
    
    return merged


def insert_interval(intervals, new_interval):
    """
    Insert a new interval and merge if necessary.
    
    Args:
        intervals: List of non-overlapping sorted intervals
        new_interval: [start, end] interval to insert
        
    Returns:
        List of intervals after insertion and merging
    """
    result = []
    i = 0
    start, end = new_interval
    
    # Add all intervals that end before new interval starts
    while i < len(intervals) and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < len(intervals) and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    
    # Add the merged interval
    result.append([start, end])
    
    # Add remaining intervals
    while i < len(intervals):
        result.append(intervals[i])
        i += 1
    
    return result


def intervals_intersection(intervals1, intervals2):
    """
    Find intersection of two interval lists.
    
    Args:
        intervals1: First list of intervals
        intervals2: Second list of intervals
        
    Returns:
        List of intersection intervals
    """
    result = []
    i = j = 0
    
    while i < len(intervals1) and j < len(intervals2):
        # Find intersection
        start = max(intervals1[i][0], intervals2[j][0])
        end = min(intervals1[i][1], intervals2[j][1])
        
        # If valid intersection
        if start <= end:
            result.append([start, end])
        
        # Move pointer of interval that ends earlier
        if intervals1[i][1] < intervals2[j][1]:
            i += 1
        else:
            j += 1
    
    return result


def example_usage():
    """Demonstrate interval operations"""
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print("Original intervals:", intervals)
    
    merged = merge_intervals(intervals)
    print("Merged intervals:", merged)
    
    # Insert new interval
    new_interval = [4, 8]
    inserted = insert_interval([[1, 3], [6, 9]], new_interval)
    print(f"After inserting {new_interval}:", inserted)
    
    # Intersection
    list1 = [[1, 3], [5, 6], [7, 9]]
    list2 = [[2, 3], [5, 7]]
    intersection = intervals_intersection(list1, list2)
    print("Intersection:", intersection)


if __name__ == "__main__":
    example_usage()
