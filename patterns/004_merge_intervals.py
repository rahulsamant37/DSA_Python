"""
Merge Intervals Pattern

The Merge Intervals pattern describes an efficient technique to deal with overlapping 
intervals. In a lot of problems involving intervals, we either need to find overlapping 
intervals or merge intervals if they overlap.

Time Complexity: Usually O(n log n) due to sorting
Space Complexity: O(n) for the result

Common Problems:
- Merge Intervals
- Insert Interval
- Intervals Intersection
- Conflicting Appointments
- Employee Free Time
"""

class Interval:
    """Class to represent an interval."""
    def __init__(self, start, end):
        self.start = start
        self.end = end
    
    def __repr__(self):
        return f"[{self.start}, {self.end}]"


def merge_intervals(intervals):
    """
    Merge all overlapping intervals.
    
    Args:
        intervals: list of intervals
    
    Returns:
        list of merged intervals
    """
    if len(intervals) < 2:
        return intervals
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x.start)
    
    merged_intervals = []
    start = intervals[0].start
    end = intervals[0].end
    
    for i in range(1, len(intervals)):
        interval = intervals[i]
        
        if interval.start <= end:  # overlapping intervals
            end = max(end, interval.end)  # merge intervals
        else:  # non-overlapping interval, add previous interval and reset
            merged_intervals.append(Interval(start, end))
            start = interval.start
            end = interval.end
    
    # Add the last interval
    merged_intervals.append(Interval(start, end))
    
    return merged_intervals


def insert_interval(intervals, new_interval):
    """
    Insert a new interval into a list of non-overlapping intervals.
    
    Args:
        intervals: list of non-overlapping intervals sorted by start time
        new_interval: interval to be inserted
    
    Returns:
        list of intervals after insertion
    """
    merged = []
    i = 0
    
    # Skip and add all intervals that come before the 'new_interval'
    while i < len(intervals) and intervals[i].end < new_interval.start:
        merged.append(intervals[i])
        i += 1
    
    # Merge all intervals that overlap with 'new_interval'
    while i < len(intervals) and intervals[i].start <= new_interval.end:
        new_interval.start = min(intervals[i].start, new_interval.start)
        new_interval.end = max(intervals[i].end, new_interval.end)
        i += 1
    
    # Insert the new_interval
    merged.append(new_interval)
    
    # Add all the remaining intervals
    while i < len(intervals):
        merged.append(intervals[i])
        i += 1
    
    return merged


def intervals_intersection(intervals_a, intervals_b):
    """
    Find intersection of two interval lists.
    
    Args:
        intervals_a: first list of intervals
        intervals_b: second list of intervals
    
    Returns:
        list of intersecting intervals
    """
    result = []
    i, j = 0, 0
    
    while i < len(intervals_a) and j < len(intervals_b):
        # Check if intervals overlap and find the intersection
        a_overlaps_b = intervals_a[i].start <= intervals_b[j].end
        b_overlaps_a = intervals_b[j].start <= intervals_a[i].end
        
        if a_overlaps_b and b_overlaps_a:
            start = max(intervals_a[i].start, intervals_b[j].start)
            end = min(intervals_a[i].end, intervals_b[j].end)
            result.append(Interval(start, end))
        
        # Move next from the interval which is finishing first
        if intervals_a[i].end < intervals_b[j].end:
            i += 1
        else:
            j += 1
    
    return result


def can_attend_all_appointments(intervals):
    """
    Check if a person can attend all appointments.
    
    Args:
        intervals: list of appointment intervals
    
    Returns:
        True if person can attend all appointments, False otherwise
    """
    # Sort intervals by start time
    intervals.sort(key=lambda x: x.start)
    
    for i in range(1, len(intervals)):
        # If current appointment starts before previous one ends
        if intervals[i].start < intervals[i - 1].end:
            return False  # overlap found
    
    return True


def min_meeting_rooms(intervals):
    """
    Find minimum number of meeting rooms required.
    
    Args:
        intervals: list of meeting intervals
    
    Returns:
        minimum number of meeting rooms required
    """
    if not intervals:
        return 0
    
    # Sort intervals by start time
    intervals.sort(key=lambda x: x.start)
    
    min_rooms = 0
    min_heap = []  # store end times of meetings
    
    for meeting in intervals:
        # Remove all meetings that have ended
        while min_heap and meeting.start >= min_heap[0]:
            import heapq
            heapq.heappop(min_heap)
        
        # Add the current meeting
        import heapq
        heapq.heappush(min_heap, meeting.end)
        
        # All active meetings are in min_heap, so we need rooms for all of them
        min_rooms = max(min_rooms, len(min_heap))
    
    return min_rooms


def find_employee_free_time(schedules):
    """
    Find intervals representing free time for all employees.
    
    Args:
        schedules: list of employee schedules (each schedule is a list of intervals)
    
    Returns:
        list of intervals representing common free time
    """
    # Flatten all schedules and sort by start time
    all_intervals = []
    for schedule in schedules:
        for interval in schedule:
            all_intervals.append(interval)
    
    all_intervals.sort(key=lambda x: x.start)
    
    # Merge overlapping intervals
    merged = merge_intervals(all_intervals)
    
    # Find gaps between merged intervals
    free_time = []
    for i in range(1, len(merged)):
        if merged[i - 1].end < merged[i].start:
            free_time.append(Interval(merged[i - 1].end, merged[i].start))
    
    return free_time


def maximum_cpu_load(jobs):
    """
    Find the maximum CPU load at any time for given jobs.
    
    Args:
        jobs: list of job intervals with cpu_load attribute
    
    Returns:
        maximum CPU load
    """
    # Sort jobs by start time
    jobs.sort(key=lambda x: x.start)
    
    max_cpu_load = 0
    current_cpu_load = 0
    min_heap = []  # store (end_time, cpu_load) of running jobs
    
    for job in jobs:
        # Remove all jobs that have ended
        while min_heap and job.start >= min_heap[0][0]:
            import heapq
            _, cpu_load = heapq.heappop(min_heap)
            current_cpu_load -= cpu_load
        
        # Add the current job
        import heapq
        heapq.heappush(min_heap, (job.end, job.cpu_load))
        current_cpu_load += job.cpu_load
        
        max_cpu_load = max(max_cpu_load, current_cpu_load)
    
    return max_cpu_load


class Job:
    """Class to represent a job with CPU load."""
    def __init__(self, start, end, cpu_load):
        self.start = start
        self.end = end
        self.cpu_load = cpu_load
    
    def __repr__(self):
        return f"[{self.start}, {self.end}, {self.cpu_load}]"


def interval_list_intersections(first_list, second_list):
    """
    Find intersection of two sorted interval lists.
    
    Args:
        first_list: first sorted list of intervals as [start, end] pairs
        second_list: second sorted list of intervals as [start, end] pairs
    
    Returns:
        list of intersection intervals
    """
    result = []
    i = j = 0
    
    while i < len(first_list) and j < len(second_list):
        # Check if intervals overlap
        start = max(first_list[i][0], second_list[j][0])
        end = min(first_list[i][1], second_list[j][1])
        
        if start <= end:  # Overlapping interval found
            result.append([start, end])
        
        # Move next from the interval which is finishing first
        if first_list[i][1] < second_list[j][1]:
            i += 1
        else:
            j += 1
    
    return result


# Example usage and test cases
if __name__ == "__main__":
    # Test merge_intervals
    print("=== Merge Intervals ===")
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    merged = merge_intervals(intervals)
    print(f"Input: {intervals}")
    print(f"Merged: {merged}")  # [[1, 5], [7, 9]]
    
    # Test insert_interval
    print("\n=== Insert Interval ===")
    intervals = [Interval(1, 3), Interval(5, 7), Interval(8, 12)]
    new_interval = Interval(4, 6)
    result = insert_interval(intervals, new_interval)
    print(f"Input: {intervals}")
    print(f"New interval: {new_interval}")
    print(f"After insertion: {result}")  # [[1, 3], [4, 7], [8, 12]]
    
    # Test intervals_intersection
    print("\n=== Intervals Intersection ===")
    intervals_a = [Interval(1, 3), Interval(5, 6), Interval(7, 9)]
    intervals_b = [Interval(2, 3), Interval(5, 7)]
    intersection = intervals_intersection(intervals_a, intervals_b)
    print(f"List A: {intervals_a}")
    print(f"List B: {intervals_b}")
    print(f"Intersection: {intersection}")  # [[2, 3], [5, 6], [7, 7]]
    
    # Test can_attend_all_appointments
    print("\n=== Conflicting Appointments ===")
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    result = can_attend_all_appointments(intervals)
    print(f"Appointments: {intervals}")
    print(f"Can attend all: {result}")  # False
    
    intervals = [Interval(6, 7), Interval(2, 4), Interval(8, 12)]
    result = can_attend_all_appointments(intervals)
    print(f"Appointments: {intervals}")
    print(f"Can attend all: {result}")  # True
    
    # Test min_meeting_rooms
    print("\n=== Minimum Meeting Rooms ===")
    intervals = [Interval(1, 4), Interval(2, 5), Interval(7, 9)]
    rooms = min_meeting_rooms(intervals)
    print(f"Meetings: {intervals}")
    print(f"Minimum rooms required: {rooms}")  # 2
    
    # Test maximum_cpu_load
    print("\n=== Maximum CPU Load ===")
    jobs = [Job(1, 4, 3), Job(2, 5, 4), Job(7, 9, 6)]
    max_load = maximum_cpu_load(jobs)
    print(f"Jobs: {jobs}")
    print(f"Maximum CPU load: {max_load}")  # 7
    
    # Test interval_list_intersections
    print("\n=== Interval List Intersections ===")
    first_list = [[0, 2], [5, 10], [13, 23], [24, 25]]
    second_list = [[1, 5], [8, 12], [15, 24], [25, 26]]
    result = interval_list_intersections(first_list, second_list)
    print(f"First list: {first_list}")
    print(f"Second list: {second_list}")
    print(f"Intersections: {result}")  # [[1, 2], [5, 5], [8, 10], [15, 23], [24, 24], [25, 25]]
