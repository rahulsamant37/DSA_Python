"""
002 - Max Heap Implementation
=============================

Binary max-heap implementation using array representation.

Time Complexity:
- Insert: O(log n)
- Extract max: O(log n)
- Peek: O(1)
- Build heap: O(n)

Space Complexity: O(1) auxiliary (in-place operations)

Heap Property: Parent ≥ children (max-heap)
"""


class MaxHeap:
    """Max-heap implementation using array"""
    
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, index):
        """Get parent index"""
        return (index - 1) // 2
    
    def left_child(self, index):
        """Get left child index"""
        return 2 * index + 1
    
    def right_child(self, index):
        """Get right child index"""
        return 2 * index + 2
    
    def has_parent(self, index):
        """Check if node has parent"""
        return self.parent(index) >= 0
    
    def has_left_child(self, index):
        """Check if node has left child"""
        return self.left_child(index) < self.size
    
    def has_right_child(self, index):
        """Check if node has right child"""
        return self.right_child(index) < self.size
    
    def swap(self, index1, index2):
        """Swap elements at two indices"""
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    
    def peek(self):
        """Get maximum element without removing it"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def insert(self, item):
        """Insert item into heap"""
        self.heap.append(item)
        self.size += 1
        self.heapify_up()
    
    def extract_max(self):
        """Remove and return maximum element"""
        if self.size == 0:
            raise IndexError("Heap is empty")
        
        if self.size == 1:
            self.size -= 1
            return self.heap.pop()
        
        # Store max element
        max_item = self.heap[0]
        
        # Move last element to root and remove last
        self.heap[0] = self.heap.pop()
        self.size -= 1
        
        # Restore heap property
        self.heapify_down()
        
        return max_item
    
    def heapify_up(self):
        """Restore heap property upward (after insertion)"""
        index = self.size - 1
        while self.has_parent(index) and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(self.parent(index), index)
            index = self.parent(index)
    
    def heapify_down(self):
        """Restore heap property downward (after extraction)"""
        index = 0
        while self.has_left_child(index):
            larger_child_index = self.left_child(index)
            
            # Find larger of two children
            if (self.has_right_child(index) and 
                self.heap[self.right_child(index)] > self.heap[larger_child_index]):
                larger_child_index = self.right_child(index)
            
            # If heap property is satisfied, stop
            if self.heap[index] >= self.heap[larger_child_index]:
                break
            
            # Otherwise, swap and continue
            self.swap(index, larger_child_index)
            index = larger_child_index
    
    def is_empty(self):
        """Check if heap is empty"""
        return self.size == 0
    
    def get_size(self):
        """Get current size of heap"""
        return self.size
    
    def display(self):
        """Display heap as array"""
        print(f"Max-Heap (size: {self.size}): {self.heap[:self.size]}")


def demo_max_heap():
    """Demonstrate max-heap functionality"""
    print("=== Max Heap Demo ===")
    
    # Create max heap
    max_heap = MaxHeap()
    
    # Insert elements
    elements = [1, 3, 6, 5, 2, 4, 7, 9, 8, 10]
    print(f"Inserting elements: {elements}")
    
    for element in elements:
        max_heap.insert(element)
        print(f"Inserted {element}: ", end="")
        max_heap.display()
    
    print(f"\nFinal heap: ")
    max_heap.display()
    print(f"Maximum element (peek): {max_heap.peek()}")
    
    # Extract maximum elements
    print(f"\nExtracting maximum elements:")
    extracted = []
    while not max_heap.is_empty():
        max_val = max_heap.extract_max()
        extracted.append(max_val)
        print(f"Extracted: {max_val}, Remaining: ", end="")
        if not max_heap.is_empty():
            max_heap.display()
        else:
            print("[]")
    
    print(f"\nExtracted in descending order: {extracted}")
    print(f"This demonstrates heap sort for descending order!")
    
    print(f"\nMax-heap vs Min-heap:")
    print(f"- Max-heap: parent ≥ children (root = maximum)")
    print(f"- Min-heap: parent ≤ children (root = minimum)")
    print(f"- Both have same time complexities")
    print(f"- Choice depends on whether you need max or min priority")


if __name__ == "__main__":
    demo_max_heap()
