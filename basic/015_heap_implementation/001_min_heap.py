"""
001 - Heap Node and Basic Structure
===================================

Basic heap implementation with min-heap and max-heap functionality.

Time Complexity:
- Insert: O(log n)
- Extract min/max: O(log n)  
- Peek: O(1)
- Build heap: O(n)

Space Complexity: O(n)
"""

class MinHeap:
    """Min heap implementation using array"""
    
    def __init__(self):
        self.heap = []
        self.size = 0
    
    def parent(self, i):
        """Get parent index"""
        return (i - 1) // 2
    
    def left_child(self, i):
        """Get left child index"""
        return 2 * i + 1
    
    def right_child(self, i):
        """Get right child index"""
        return 2 * i + 2
    
    def is_empty(self):
        """Check if heap is empty"""
        return self.size == 0
    
    def get_min(self):
        """Get minimum element (root)"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        return self.heap[0]
    
    def insert(self, value):
        """Insert value into heap"""
        self.heap.append(value)
        self.size += 1
        self._bubble_up(self.size - 1)
    
    def extract_min(self):
        """Remove and return minimum element"""
        if self.is_empty():
            raise IndexError("Heap is empty")
        
        min_val = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.heap.pop()
        self.size -= 1
        
        if not self.is_empty():
            self._bubble_down(0)
        
        return min_val
    
    def _bubble_up(self, index):
        """Bubble up element to maintain heap property"""
        while index > 0:
            parent_idx = self.parent(index)
            if self.heap[index] >= self.heap[parent_idx]:
                break
            
            # Swap with parent
            self.heap[index], self.heap[parent_idx] = self.heap[parent_idx], self.heap[index]
            index = parent_idx
    
    def _bubble_down(self, index):
        """Bubble down element to maintain heap property"""
        while self.left_child(index) < self.size:
            min_child_idx = self._get_min_child_index(index)
            
            if self.heap[index] <= self.heap[min_child_idx]:
                break
            
            # Swap with min child
            self.heap[index], self.heap[min_child_idx] = self.heap[min_child_idx], self.heap[index]
            index = min_child_idx
    
    def _get_min_child_index(self, index):
        """Get index of minimum child"""
        left_idx = self.left_child(index)
        right_idx = self.right_child(index)
        
        if right_idx >= self.size:
            return left_idx
        
        return left_idx if self.heap[left_idx] < self.heap[right_idx] else right_idx
    
    def display(self):
        """Display heap as array"""
        print(f"Min Heap: {self.heap}")


def demo_min_heap():
    """Demonstrate min heap functionality"""
    print("=== Min Heap Demo ===")
    
    heap = MinHeap()
    
    # Insert elements
    values = [20, 15, 30, 10, 8, 25, 40]
    print(f"Inserting values: {values}")
    
    for value in values:
        heap.insert(value)
        print(f"  Inserted {value}: ", end="")
        heap.display()
    
    print(f"\nMinimum element: {heap.get_min()}")
    
    # Extract minimums
    print("\nExtracting minimums:")
    while not heap.is_empty():
        min_val = heap.extract_min()
        print(f"  Extracted {min_val}: ", end="")
        heap.display()


if __name__ == "__main__":
    demo_min_heap()
