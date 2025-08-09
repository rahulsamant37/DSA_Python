"""
008 - Queue Implementation
=========================

This module implements queue data structure using different approaches:
- Array-based Queue (Circular)
- Linked List-based Queue
- Priority Queue
- Deque (Double-ended Queue)
- Queue applications and problems

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Front/Rear: O(1)
- Search: O(n)

Queue follows FIFO (First In, First Out) principle.
Applications: CPU scheduling, breadth-first search, buffer for data streams, etc.
"""

class ArrayQueue:
    """Circular queue implementation using array"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = 0
        self.queue_size = 0
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.queue_size == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self.queue_size == self.capacity
    
    def size(self):
        """Return current size of queue"""
        return self.queue_size
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        if self.is_full():
            raise OverflowError("Queue overflow")
        
        self.data[self.rear] = item
        self.rear = (self.rear + 1) % self.capacity
        self.queue_size += 1
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("Queue underflow")
        
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.queue_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.data[self.front]
    
    def peek_rear(self):
        """Peek at rear item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        rear_index = (self.rear - 1) % self.capacity
        return self.data[rear_index]
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue (front to rear):")
        elements = []
        index = self.front
        for _ in range(self.queue_size):
            elements.append(str(self.data[index]))
            index = (index + 1) % self.capacity
        
        print("  " + " <- ".join(elements))


class QueueNode:
    """Node class for linked list queue"""
    
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListQueue:
    """Queue implementation using linked list"""
    
    def __init__(self):
        self.front = None
        self.rear = None
        self.queue_size = 0
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.front is None
    
    def size(self):
        """Return current size of queue"""
        return self.queue_size
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        new_node = QueueNode(item)
        
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        
        self.queue_size += 1
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("Queue underflow")
        
        item = self.front.data
        self.front = self.front.next
        
        if self.front is None:  # Queue became empty
            self.rear = None
        
        self.queue_size -= 1
        return item
    
    def peek_front(self):
        """Peek at front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.front.data
    
    def peek_rear(self):
        """Peek at rear item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.rear.data
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue (front to rear):")
        elements = []
        current = self.front
        
        while current:
            elements.append(str(current.data))
            current = current.next
        
        print("  " + " <- ".join(elements))


class PriorityQueueItem:
    """Item for priority queue with priority and data"""
    
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
    
    def __lt__(self, other):
        return self.priority < other.priority
    
    def __str__(self):
        return f"({self.data}, {self.priority})"


class PriorityQueue:
    """Priority queue implementation using array (simple version)"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if priority queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return current size of priority queue"""
        return len(self.items)
    
    def enqueue(self, data, priority):
        """Add item with priority to queue"""
        new_item = PriorityQueueItem(data, priority)
        
        # Insert in sorted order (higher priority first)
        inserted = False
        for i in range(len(self.items)):
            if new_item.priority > self.items[i].priority:
                self.items.insert(i, new_item)
                inserted = True
                break
        
        if not inserted:
            self.items.append(new_item)
    
    def dequeue(self):
        """Remove and return highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        return self.items.pop(0).data
    
    def peek(self):
        """Peek at highest priority item"""
        if self.is_empty():
            raise IndexError("Priority queue is empty")
        
        return self.items[0].data
    
    def display(self):
        """Display priority queue contents"""
        if self.is_empty():
            print("Priority queue is empty")
            return
        
        print("Priority Queue (highest to lowest priority):")
        for item in self.items:
            print(f"  {item}")


class Deque:
    """Double-ended queue implementation"""
    
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        """Check if deque is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Return current size of deque"""
        return len(self.items)
    
    def add_front(self, item):
        """Add item to front of deque"""
        self.items.insert(0, item)
    
    def add_rear(self, item):
        """Add item to rear of deque"""
        self.items.append(item)
    
    def remove_front(self):
        """Remove and return item from front"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items.pop(0)
    
    def remove_rear(self):
        """Remove and return item from rear"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items.pop()
    
    def peek_front(self):
        """Peek at front item"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items[0]
    
    def peek_rear(self):
        """Peek at rear item"""
        if self.is_empty():
            raise IndexError("Deque is empty")
        
        return self.items[-1]
    
    def display(self):
        """Display deque contents"""
        if self.is_empty():
            print("Deque is empty")
            return
        
        print("Deque:", self.items)


class QueueApplications:
    """Various queue applications and algorithms"""
    
    @staticmethod
    def breadth_first_search(graph, start):
        """BFS traversal using queue"""
        visited = set()
        queue = LinkedListQueue()
        result = []
        
        queue.enqueue(start)
        visited.add(start)
        
        while not queue.is_empty():
            vertex = queue.dequeue()
            result.append(vertex)
            
            for neighbor in graph.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.enqueue(neighbor)
        
        return result
    
    @staticmethod
    def generate_binary_numbers(n):
        """Generate binary representation of numbers 1 to n using queue"""
        queue = LinkedListQueue()
        result = []
        
        queue.enqueue("1")
        
        for i in range(n):
            binary = queue.dequeue()
            result.append(binary)
            
            # Generate next binary numbers
            queue.enqueue(binary + "0")
            queue.enqueue(binary + "1")
        
        return result
    
    @staticmethod
    def first_non_repeating_character(stream):
        """Find first non-repeating character in a stream using queue"""
        queue = LinkedListQueue()
        char_count = {}
        result = []
        
        for char in stream:
            # Update character count
            char_count[char] = char_count.get(char, 0) + 1
            
            # Add to queue if first occurrence
            if char_count[char] == 1:
                queue.enqueue(char)
            
            # Remove characters from front that are now repeating
            while not queue.is_empty() and char_count[queue.peek_front()] > 1:
                queue.dequeue()
            
            # Get first non-repeating character
            if queue.is_empty():
                result.append(None)
            else:
                result.append(queue.peek_front())
        
        return result
    
    @staticmethod
    def level_order_traversal(root):
        """Level order traversal of binary tree using queue"""
        if not root:
            return []
        
        queue = LinkedListQueue()
        result = []
        
        queue.enqueue(root)
        
        while not queue.is_empty():
            node = queue.dequeue()
            result.append(node.data)
            
            if hasattr(node, 'left') and node.left:
                queue.enqueue(node.left)
            if hasattr(node, 'right') and node.right:
                queue.enqueue(node.right)
        
        return result
    
    @staticmethod
    def sliding_window_maximum(arr, k):
        """Find maximum in each sliding window of size k using deque"""
        if not arr or k <= 0:
            return []
        
        deque = Deque()
        result = []
        
        for i in range(len(arr)):
            # Remove elements outside current window
            while not deque.is_empty() and deque.peek_front() <= i - k:
                deque.remove_front()
            
            # Remove smaller elements from rear
            while not deque.is_empty() and arr[deque.peek_rear()] <= arr[i]:
                deque.remove_rear()
            
            deque.add_rear(i)
            
            # Add maximum to result if window is complete
            if i >= k - 1:
                result.append(arr[deque.peek_front()])
        
        return result
    
    @staticmethod
    def hot_potato_game(names, num):
        """Simulate hot potato game using queue"""
        queue = LinkedListQueue()
        
        for name in names:
            queue.enqueue(name)
        
        while queue.size() > 1:
            # Pass the potato
            for _ in range(num):
                queue.enqueue(queue.dequeue())
            
            # Remove the person holding potato
            eliminated = queue.dequeue()
            print(f"{eliminated} is eliminated")
        
        return queue.dequeue()  # Winner


def test_queue_implementations():
    """Test all queue implementations"""
    print("=== Testing Queue Implementations ===\n")
    
    # Test Array Queue
    print("=== Array-based Circular Queue ===")
    array_queue = ArrayQueue(5)
    
    print("Enqueuing elements: 10, 20, 30")
    array_queue.enqueue(10)
    array_queue.enqueue(20)
    array_queue.enqueue(30)
    array_queue.display()
    print(f"Size: {array_queue.size()}")
    print(f"Front element: {array_queue.peek_front()}")
    print(f"Rear element: {array_queue.peek_rear()}")
    print()
    
    print("Dequeuing and enqueuing to test circular nature:")
    array_queue.dequeue()
    array_queue.dequeue()
    array_queue.enqueue(40)
    array_queue.enqueue(50)
    array_queue.enqueue(60)
    array_queue.display()
    print()
    
    # Test Linked List Queue
    print("=== Linked List-based Queue ===")
    ll_queue = LinkedListQueue()
    
    print("Enqueuing elements: A, B, C, D")
    for item in ['A', 'B', 'C', 'D']:
        ll_queue.enqueue(item)
    ll_queue.display()
    print(f"Size: {ll_queue.size()}")
    print()
    
    print("Dequeuing elements:")
    while not ll_queue.is_empty():
        dequeued = ll_queue.dequeue()
        print(f"Dequeued: {dequeued}")
        if not ll_queue.is_empty():
            ll_queue.display()
    print()
    
    # Test Priority Queue
    print("=== Priority Queue ===")
    pq = PriorityQueue()
    
    print("Enqueuing elements with priorities:")
    items = [('Task1', 3), ('Task2', 1), ('Task3', 5), ('Task4', 2)]
    for data, priority in items:
        pq.enqueue(data, priority)
        print(f"Added: {data} with priority {priority}")
    
    pq.display()
    print()
    
    print("Dequeuing by priority:")
    while not pq.is_empty():
        task = pq.dequeue()
        print(f"Processing: {task}")
    print()
    
    # Test Deque
    print("=== Double-ended Queue (Deque) ===")
    deque = Deque()
    
    print("Adding elements to both ends:")
    deque.add_rear(1)
    deque.add_rear(2)
    deque.add_front(0)
    deque.add_front(-1)
    deque.display()
    
    print("Removing from both ends:")
    print(f"Removed from front: {deque.remove_front()}")
    print(f"Removed from rear: {deque.remove_rear()}")
    deque.display()
    print()


def test_queue_applications():
    """Test queue applications"""
    print("=== Testing Queue Applications ===\n")
    
    apps = QueueApplications()
    
    # Test BFS
    print("=== Breadth-First Search ===")
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    bfs_result = apps.breadth_first_search(graph, 'A')
    print(f"BFS traversal starting from A: {bfs_result}")
    print()
    
    # Test binary number generation
    print("=== Generate Binary Numbers ===")
    n = 10
    binary_numbers = apps.generate_binary_numbers(n)
    print(f"Binary representation of numbers 1 to {n}:")
    for i, binary in enumerate(binary_numbers, 1):
        print(f"{i}: {binary}")
    print()
    
    # Test first non-repeating character
    print("=== First Non-Repeating Character ===")
    stream = "aabccxb"
    result = apps.first_non_repeating_character(stream)
    print(f"Stream: {stream}")
    print(f"First non-repeating chars: {result}")
    print()
    
    # Test sliding window maximum
    print("=== Sliding Window Maximum ===")
    arr = [1, 2, 3, 1, 4, 5, 2, 3, 6]
    k = 3
    max_values = apps.sliding_window_maximum(arr, k)
    print(f"Array: {arr}")
    print(f"Window size: {k}")
    print(f"Maximum in each window: {max_values}")
    print()
    
    # Test hot potato game
    print("=== Hot Potato Game ===")
    names = ["Alice", "Bob", "Charlie", "David", "Eve"]
    num = 3
    print(f"Players: {names}")
    print(f"Counting: {num}")
    winner = apps.hot_potato_game(names, num)
    print(f"Winner: {winner}")


if __name__ == "__main__":
    test_queue_implementations()
    print("\n" + "="*50 + "\n")
    test_queue_applications()
