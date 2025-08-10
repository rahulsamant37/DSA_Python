"""
002 - Array-Based Queue Implementation
=====================================

Queue implementation using array (list) with fixed capacity.

Time Complexity:
- Enqueue: O(1)
- Dequeue: O(1)
- Peek: O(1)
- Search: O(n)

Queue follows FIFO (First In, First Out) principle.
"""

class ArrayQueue:
    """Queue implementation using array (list)"""
    
    def __init__(self, capacity=100):
        self.capacity = capacity
        self.data = [None] * capacity
        self.front = 0
        self.rear = -1
        self.size = 0
    
    def is_empty(self):
        """Check if queue is empty"""
        return self.size == 0
    
    def is_full(self):
        """Check if queue is full"""
        return self.size == self.capacity
    
    def get_size(self):
        """Return current size of queue"""
        return self.size
    
    def enqueue(self, item):
        """Add item to rear of queue"""
        if self.is_full():
            raise OverflowError("Queue overflow")
        
        self.rear = (self.rear + 1) % self.capacity
        self.data[self.rear] = item
        self.size += 1
    
    def dequeue(self):
        """Remove and return item from front of queue"""
        if self.is_empty():
            raise IndexError("Queue underflow")
        
        item = self.data[self.front]
        self.data[self.front] = None
        self.front = (self.front + 1) % self.capacity
        self.size -= 1
        return item
    
    def peek(self):
        """Peek at front item without removing it"""
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        return self.data[self.front]
    
    def display(self):
        """Display queue contents"""
        if self.is_empty():
            print("Queue is empty")
            return
        
        print("Queue (front to rear):", end=" ")
        i = self.front
        for _ in range(self.size):
            print(self.data[i], end=" ")
            i = (i + 1) % self.capacity
        print()


def demo_array_queue():
    """Demonstrate ArrayQueue functionality"""
    print("=== Array Queue Demo ===")
    
    # Create queue
    queue = ArrayQueue(5)
    
    # Enqueue elements
    print("Enqueuing elements: 10, 20, 30")
    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(30)
    queue.display()
    
    # Peek
    print(f"\nFront element (peek): {queue.peek()}")
    print(f"Queue size: {queue.get_size()}")
    
    # Dequeue elements
    print(f"\nDequeuing: {queue.dequeue()}")
    print(f"Dequeuing: {queue.dequeue()}")
    queue.display()
    
    # Add more elements
    print("\nEnqueuing: 40, 50")
    queue.enqueue(40)
    queue.enqueue(50)
    queue.display()


if __name__ == "__main__":
    demo_array_queue()
