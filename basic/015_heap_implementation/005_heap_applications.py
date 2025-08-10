"""
005 - Heap Applications
=======================

Advanced heap applications and algorithms that use heap data structure.

Applications covered:
1. Median finding with two heaps
2. Top K elements problem
3. Merge K sorted arrays
4. Sliding window maximum
5. Dijkstra's algorithm (simplified)
6. Huffman coding tree

Time Complexities vary by application but generally leverage O(log n) heap operations.
"""

import heapq
from typing import List, Tuple, Optional
from collections import defaultdict


class MedianFinder:
    """
    Find median of a stream of numbers using two heaps
    
    Time Complexity:
    - Add number: O(log n)
    - Find median: O(1)
    
    Space Complexity: O(n)
    """
    
    def __init__(self):
        # Max heap for smaller half (use negative values)
        self.small = []  # max heap
        # Min heap for larger half
        self.large = []  # min heap
    
    def add_number(self, num: int):
        """Add number to data structure"""
        # Add to max heap (smaller half)
        heapq.heappush(self.small, -num)
        
        # Balance: move largest from small to large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        # Balance sizes: ensure size difference is at most 1
        if len(self.small) > len(self.large) + 1:
            val = -heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        elif len(self.large) > len(self.small) + 1:
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val)
    
    def find_median(self) -> float:
        """Find median of all numbers added so far"""
        if len(self.small) > len(self.large):
            return float(-self.small[0])
        elif len(self.large) > len(self.small):
            return float(self.large[0])
        else:
            return (-self.small[0] + self.large[0]) / 2.0


def find_k_largest(nums: List[int], k: int) -> List[int]:
    """
    Find K largest elements using min-heap
    
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0:
        return []
    if k >= len(nums):
        return sorted(nums, reverse=True)
    
    # Use min-heap of size k
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:
            heapq.heapreplace(heap, num)
    
    # Return in descending order
    return sorted(heap, reverse=True)


def find_k_smallest(nums: List[int], k: int) -> List[int]:
    """
    Find K smallest elements using max-heap
    
    Time Complexity: O(n log k)
    Space Complexity: O(k)
    """
    if k <= 0:
        return []
    if k >= len(nums):
        return sorted(nums)
    
    # Use max-heap of size k (negative values)
    heap = []
    
    for num in nums:
        if len(heap) < k:
            heapq.heappush(heap, -num)
        elif num < -heap[0]:
            heapq.heapreplace(heap, -num)
    
    # Return in ascending order
    return sorted([-x for x in heap])


def merge_k_sorted_arrays(arrays: List[List[int]]) -> List[int]:
    """
    Merge K sorted arrays using min-heap
    
    Time Complexity: O(n log k) where n is total elements
    Space Complexity: O(k)
    """
    if not arrays:
        return []
    
    # Heap stores (value, array_index, element_index)
    heap = []
    result = []
    
    # Initialize heap with first element from each array
    for i, arr in enumerate(arrays):
        if arr:  # Check if array is not empty
            heapq.heappush(heap, (arr[0], i, 0))
    
    # Extract minimum and add next element from same array
    while heap:
        value, arr_idx, elem_idx = heapq.heappop(heap)
        result.append(value)
        
        # Add next element from same array if exists
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_val = arrays[arr_idx][elem_idx + 1]
            heapq.heappush(heap, (next_val, arr_idx, elem_idx + 1))
    
    return result


def sliding_window_maximum(nums: List[int], k: int) -> List[int]:
    """
    Find maximum in each sliding window using heap
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Note: This is not the optimal O(n) solution using deque,
    but demonstrates heap usage.
    """
    if not nums or k <= 0:
        return []
    
    result = []
    # Max heap with (value, index) - use negative for max heap
    heap = []
    
    for i, num in enumerate(nums):
        # Add current element
        heapq.heappush(heap, (-num, i))
        
        # Remove elements outside current window
        while heap and heap[0][1] <= i - k:
            heapq.heappop(heap)
        
        # Add maximum of current window to result
        if i >= k - 1:
            result.append(-heap[0][0])
    
    return result


class HuffmanNode:
    """Node for Huffman coding tree"""
    
    def __init__(self, char: str = None, freq: int = 0, left=None, right=None):
        self.char = char
        self.freq = freq
        self.left = left
        self.right = right
    
    def __lt__(self, other):
        return self.freq < other.freq


def huffman_coding(text: str) -> Tuple[dict, str]:
    """
    Build Huffman coding tree and encode text
    
    Time Complexity: O(n log n)
    Space Complexity: O(n)
    
    Returns:
        Tuple of (codes_dict, encoded_text)
    """
    if not text:
        return {}, ""
    
    # Count frequencies
    freq = defaultdict(int)
    for char in text:
        freq[char] += 1
    
    # Build heap of nodes
    heap = []
    for char, frequency in freq.items():
        node = HuffmanNode(char, frequency)
        heapq.heappush(heap, node)
    
    # Build Huffman tree
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        # Create internal node
        internal = HuffmanNode(
            freq=left.freq + right.freq,
            left=left,
            right=right
        )
        heapq.heappush(heap, internal)
    
    # Generate codes
    root = heap[0] if heap else None
    codes = {}
    
    def generate_codes(node, code=""):
        if node:
            if node.char:  # Leaf node
                codes[node.char] = code or "0"  # Handle single character
            else:
                generate_codes(node.left, code + "0")
                generate_codes(node.right, code + "1")
    
    generate_codes(root)
    
    # Encode text
    encoded = "".join(codes[char] for char in text)
    
    return codes, encoded


def dijkstra_shortest_path(graph: dict, start: str, end: str) -> Tuple[List[str], int]:
    """
    Simplified Dijkstra's algorithm using heap
    
    Time Complexity: O((V + E) log V)
    Space Complexity: O(V)
    
    Args:
        graph: Adjacency list with weights {node: [(neighbor, weight), ...]}
        start: Start node
        end: End node
    
    Returns:
        Tuple of (path, distance)
    """
    # Distance from start to each node
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    
    # Previous node for path reconstruction
    previous = {}
    
    # Priority queue: (distance, node)
    pq = [(0, start)]
    visited = set()
    
    while pq:
        current_dist, current = heapq.heappop(pq)
        
        if current in visited:
            continue
        
        visited.add(current)
        
        if current == end:
            break
        
        # Check neighbors
        for neighbor, weight in graph.get(current, []):
            if neighbor in visited:
                continue
            
            new_dist = current_dist + weight
            
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                previous[neighbor] = current
                heapq.heappush(pq, (new_dist, neighbor))
    
    # Reconstruct path
    path = []
    current = end
    while current in previous:
        path.append(current)
        current = previous[current]
    path.append(start)
    path.reverse()
    
    return path, distances[end]


def demo_applications():
    """Demonstrate various heap applications"""
    print("=== Heap Applications Demo ===")
    
    # 1. Median Finder
    print("\n1. Median Finder:")
    median_finder = MedianFinder()
    numbers = [1, 5, 2, 10, 7, 3]
    
    for num in numbers:
        median_finder.add_number(num)
        print(f"Added {num}, Median: {median_finder.find_median()}")
    
    # 2. Top K elements
    print("\n2. Top K Elements:")
    nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
    k = 3
    print(f"Array: {nums}")
    print(f"Top {k} largest: {find_k_largest(nums, k)}")
    print(f"Top {k} smallest: {find_k_smallest(nums, k)}")
    
    # 3. Merge K sorted arrays
    print("\n3. Merge K Sorted Arrays:")
    arrays = [
        [1, 4, 7],
        [2, 5, 8],
        [3, 6, 9]
    ]
    print(f"Arrays: {arrays}")
    print(f"Merged: {merge_k_sorted_arrays(arrays)}")
    
    # 4. Sliding window maximum
    print("\n4. Sliding Window Maximum:")
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print(f"Array: {nums}, Window size: {k}")
    print(f"Maximums: {sliding_window_maximum(nums, k)}")
    
    # 5. Huffman coding
    print("\n5. Huffman Coding:")
    text = "hello world"
    codes, encoded = huffman_coding(text)
    print(f"Text: '{text}'")
    print(f"Codes: {codes}")
    print(f"Encoded: {encoded}")
    print(f"Compression ratio: {len(encoded)} bits vs {len(text) * 8} bits")
    
    # 6. Dijkstra's algorithm
    print("\n6. Dijkstra's Shortest Path:")
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    start, end = 'A', 'E'
    path, distance = dijkstra_shortest_path(graph, start, end)
    print(f"Graph: {graph}")
    print(f"Shortest path from {start} to {end}: {' -> '.join(path)}")
    print(f"Distance: {distance}")


def performance_comparison():
    """Compare heap-based solutions with alternatives"""
    print("\n=== Performance Comparison ===")
    
    print("Heap-based solutions excel when:")
    print("✓ Need to maintain sorted order incrementally")
    print("✓ Only need top/bottom K elements")
    print("✓ Working with streaming data")
    print("✓ Memory constraints (don't need full sort)")
    
    print("\nTime complexities:")
    print("• Median finder: O(log n) insert, O(1) query")
    print("• Top K elements: O(n log k) vs O(n log n) full sort")
    print("• Merge K arrays: O(n log k) vs O(nk log(nk)) naive")
    print("• Sliding window max: O(n log n) vs O(n) with deque")
    print("• Huffman coding: O(n log n) for tree building")
    print("• Dijkstra: O((V+E) log V) vs O(V²) naive")


if __name__ == "__main__":
    demo_applications()
    performance_comparison()
