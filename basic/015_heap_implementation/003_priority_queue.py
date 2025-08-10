"""
003 - Priority Queue Implementation
===================================

Priority queue implementation using both min-heap and max-heap.
Supports custom priority comparison and objects with priorities.

Time Complexity:
- Insert: O(log n)
- Extract: O(log n)
- Peek: O(1)

Space Complexity: O(n)

Use Cases:
- Task scheduling with priorities
- Dijkstra's algorithm
- Huffman coding
- Event simulation
"""

import heapq
from typing import Any, Tuple, List, Callable


class PriorityQueue:
    """Priority queue using Python's heapq (min-heap based)"""
    
    def __init__(self, reverse=False):
        """
        Initialize priority queue
        
        Args:
            reverse: If True, creates max-priority queue
        """
        self._heap = []
        self._index = 0  # For tie-breaking
        self.reverse = reverse
    
    def put(self, item: Any, priority: int = 0):
        """Add item with priority"""
        # For max-priority queue, negate priority
        if self.reverse:
            priority = -priority
        
        # Use index for tie-breaking to maintain insertion order
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
    
    def get(self) -> Any:
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        priority, _, item = heapq.heappop(self._heap)
        return item
    
    def peek(self) -> Any:
        """Get highest priority item without removing"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        return self._heap[0][2]
    
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Get queue size"""
        return len(self._heap)
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Priority Queue: []")
            return
        
        items = []
        for priority, _, item in self._heap:
            actual_priority = -priority if self.reverse else priority
            items.append(f"{item}(p:{actual_priority})")
        
        queue_type = "Max" if self.reverse else "Min"
        print(f"{queue_type}-Priority Queue: [{', '.join(items)}]")


class Task:
    """Task class for priority queue demonstration"""
    
    def __init__(self, name: str, priority: int, description: str = ""):
        self.name = name
        self.priority = priority
        self.description = description
    
    def __str__(self):
        return f"Task({self.name})"
    
    def __repr__(self):
        return self.__str__()


class CustomPriorityQueue:
    """Priority queue with custom comparison function"""
    
    def __init__(self, key_func: Callable = None, reverse: bool = False):
        """
        Initialize with custom priority function
        
        Args:
            key_func: Function to extract priority from items
            reverse: If True, higher values have higher priority
        """
        self._heap = []
        self._index = 0
        self.key_func = key_func or (lambda x: x)
        self.reverse = reverse
    
    def put(self, item: Any):
        """Add item (priority extracted using key_func)"""
        priority = self.key_func(item)
        if self.reverse:
            priority = -priority
        
        heapq.heappush(self._heap, (priority, self._index, item))
        self._index += 1
    
    def get(self) -> Any:
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        _, _, item = heapq.heappop(self._heap)
        return item
    
    def peek(self) -> Any:
        """Get highest priority item without removing"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        return self._heap[0][2]
    
    def is_empty(self) -> bool:
        """Check if queue is empty"""
        return len(self._heap) == 0
    
    def size(self) -> int:
        """Get queue size"""
        return len(self._heap)


def demo_basic_priority_queue():
    """Demonstrate basic priority queue operations"""
    print("=== Basic Priority Queue Demo ===")
    
    # Min-priority queue
    min_pq = PriorityQueue()
    
    print("Min-Priority Queue (lower number = higher priority):")
    items = [("Email", 2), ("Call", 1), ("Meeting", 3), ("Coffee", 5), ("Urgent", 0)]
    
    for item, priority in items:
        min_pq.put(item, priority)
        print(f"Added {item} with priority {priority}")
    
    min_pq.display()
    
    print("\nProcessing tasks by priority:")
    while not min_pq.is_empty():
        task = min_pq.get()
        print(f"Processing: {task}")
    
    print("\n" + "="*40)
    
    # Max-priority queue
    max_pq = PriorityQueue(reverse=True)
    
    print("Max-Priority Queue (higher number = higher priority):")
    for item, priority in items:
        max_pq.put(item, priority)
        print(f"Added {item} with priority {priority}")
    
    max_pq.display()
    
    print("\nProcessing tasks by priority:")
    while not max_pq.is_empty():
        task = max_pq.get()
        print(f"Processing: {task}")


def demo_task_priority_queue():
    """Demonstrate priority queue with task objects"""
    print("\n=== Task Priority Queue Demo ===")
    
    # Create priority queue for tasks
    task_queue = CustomPriorityQueue(
        key_func=lambda task: task.priority,
        reverse=False  # Lower priority number = higher priority
    )
    
    # Create tasks
    tasks = [
        Task("Fix bug", 1, "Critical bug in production"),
        Task("Code review", 3, "Review teammate's code"),
        Task("Documentation", 4, "Update API documentation"),
        Task("Meeting", 2, "Sprint planning meeting"),
        Task("Security patch", 0, "Apply security update"),
        Task("Refactoring", 5, "Clean up old code")
    ]
    
    print("Adding tasks to priority queue:")
    for task in tasks:
        task_queue.put(task)
        print(f"Added: {task.name} (priority: {task.priority}) - {task.description}")
    
    print(f"\nTotal tasks: {task_queue.size()}")
    print(f"Next task: {task_queue.peek()}")
    
    print("\nProcessing tasks by priority:")
    while not task_queue.is_empty():
        task = task_queue.get()
        print(f"Processing: {task.name} (priority: {task.priority}) - {task.description}")


def demo_hospital_triage():
    """Demonstrate priority queue for hospital triage system"""
    print("\n=== Hospital Triage System Demo ===")
    
    # Patient class
    class Patient:
        def __init__(self, name: str, severity: int, arrival_time: int):
            self.name = name
            self.severity = severity  # 1=critical, 5=minor
            self.arrival_time = arrival_time
        
        def __str__(self):
            levels = {1: "Critical", 2: "High", 3: "Medium", 4: "Low", 5: "Minor"}
            return f"{self.name} ({levels[self.severity]})"
    
    # Create triage queue (lower severity = higher priority)
    triage_queue = CustomPriorityQueue(
        key_func=lambda patient: (patient.severity, patient.arrival_time),
        reverse=False
    )
    
    # Add patients
    patients = [
        Patient("Alice", 3, 1),    # Medium severity, arrived first
        Patient("Bob", 1, 2),      # Critical, arrived second
        Patient("Charlie", 5, 3),  # Minor, arrived third
        Patient("Diana", 2, 4),    # High severity, arrived fourth
        Patient("Eve", 1, 5),      # Critical, arrived fifth
        Patient("Frank", 4, 6)     # Low severity, arrived sixth
    ]
    
    print("Patients arriving at emergency room:")
    for patient in patients:
        triage_queue.put(patient)
        print(f"Arrived: {patient} at time {patient.arrival_time}")
    
    print(f"\nTriage queue size: {triage_queue.size()}")
    
    print("\nTreating patients by priority (severity, then arrival time):")
    while not triage_queue.is_empty():
        patient = triage_queue.get()
        print(f"Treating: {patient}")


def compare_implementations():
    """Compare different priority queue implementations"""
    print("\n=== Priority Queue Implementations Comparison ===")
    
    print("1. Python heapq module:")
    print("   - Built-in, efficient")
    print("   - Min-heap only (use negative values for max-heap)")
    print("   - Best for simple numeric priorities")
    
    print("\n2. Custom PriorityQueue class:")
    print("   - Wraps heapq with better interface")
    print("   - Supports both min and max priority")
    print("   - Handles tie-breaking automatically")
    
    print("\n3. CustomPriorityQueue with key function:")
    print("   - Most flexible approach")
    print("   - Supports complex objects")
    print("   - Custom priority extraction")
    
    print("\nTime Complexities (all implementations):")
    print("- Insert: O(log n)")
    print("- Extract: O(log n)")
    print("- Peek: O(1)")
    print("- Build from list: O(n)")
    
    print("\nUse Cases:")
    print("- Task scheduling systems")
    print("- Dijkstra's shortest path algorithm")
    print("- Huffman encoding")
    print("- Event-driven simulation")
    print("- Hospital triage systems")
    print("- CPU scheduling")


if __name__ == "__main__":
    demo_basic_priority_queue()
    demo_task_priority_queue()
    demo_hospital_triage()
    compare_implementations()
