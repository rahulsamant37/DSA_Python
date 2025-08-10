"""
003 - Shortest Path Algorithms
==============================

Shortest path algorithms for weighted and unweighted graphs.

Algorithms implemented:
1. Dijkstra's Algorithm - Single source shortest path (non-negative weights)
2. Bellman-Ford Algorithm - Single source shortest path (handles negative weights)
3. Floyd-Warshall Algorithm - All pairs shortest path

Time Complexities:
- Dijkstra: O((V + E) log V) with binary heap
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)

Use Cases:
- Dijkstra: GPS navigation, network routing
- Bellman-Ford: Currency arbitrage detection
- Floyd-Warshall: All pairs distances, graph analysis
"""

import heapq
from typing import Dict, List, Tuple, Optional, Set
from collections import defaultdict
import math


class ShortestPath:
    """Shortest path algorithms for weighted graphs"""
    
    def __init__(self, graph: Dict[str, List[Tuple[str, float]]], directed: bool = True):
        """
        Initialize with weighted adjacency list
        
        Args:
            graph: Adjacency list with weights {vertex: [(neighbor, weight), ...]}
            directed: Whether graph is directed
        """
        self.graph = graph
        self.directed = directed
        self.vertices = set(graph.keys())
        for vertex in graph:
            for neighbor, _ in graph[vertex]:
                self.vertices.add(neighbor)
    
    def dijkstra(self, start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
        """
        Dijkstra's algorithm for single-source shortest paths
        
        Args:
            start: Starting vertex
        
        Returns:
            Tuple of (distances, previous) dictionaries
        """
        # Initialize distances and previous vertices
        distances = {vertex: float('inf') for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        distances[start] = 0
        
        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_dist, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            # Check neighbors
            for neighbor, weight in self.graph.get(current, []):
                if neighbor in visited:
                    continue
                
                new_dist = current_dist + weight
                
                if new_dist < distances[neighbor]:
                    distances[neighbor] = new_dist
                    previous[neighbor] = current
                    heapq.heappush(pq, (new_dist, neighbor))
        
        return distances, previous
    
    def get_path(self, previous: Dict[str, Optional[str]], start: str, end: str) -> Optional[List[str]]:
        """
        Reconstruct path from previous vertices dictionary
        
        Args:
            previous: Previous vertices from shortest path algorithm
            start: Starting vertex
            end: Ending vertex
        
        Returns:
            Path as list of vertices, None if no path
        """
        if previous[end] is None and start != end:
            return None
        
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        return path if path[0] == start else None
    
    def bellman_ford(self, start: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]], bool]:
        """
        Bellman-Ford algorithm for single-source shortest paths
        Handles negative edge weights and detects negative cycles
        
        Args:
            start: Starting vertex
        
        Returns:
            Tuple of (distances, previous, has_negative_cycle)
        """
        # Initialize distances and previous vertices
        distances = {vertex: float('inf') for vertex in self.vertices}
        previous = {vertex: None for vertex in self.vertices}
        distances[start] = 0
        
        # Relax edges V-1 times
        for _ in range(len(self.vertices) - 1):
            for vertex in self.graph:
                if distances[vertex] == float('inf'):
                    continue
                
                for neighbor, weight in self.graph[vertex]:
                    new_dist = distances[vertex] + weight
                    if new_dist < distances[neighbor]:
                        distances[neighbor] = new_dist
                        previous[neighbor] = vertex
        
        # Check for negative cycles
        has_negative_cycle = False
        for vertex in self.graph:
            if distances[vertex] == float('inf'):
                continue
            
            for neighbor, weight in self.graph[vertex]:
                if distances[vertex] + weight < distances[neighbor]:
                    has_negative_cycle = True
                    break
            
            if has_negative_cycle:
                break
        
        return distances, previous, has_negative_cycle
    
    def floyd_warshall(self) -> Dict[Tuple[str, str], float]:
        """
        Floyd-Warshall algorithm for all-pairs shortest paths
        
        Returns:
            Dictionary with (from, to) as key and shortest distance as value
        """
        vertices = list(self.vertices)
        n = len(vertices)
        
        # Initialize distance matrix
        dist = {}
        
        # Initialize with infinity
        for i in vertices:
            for j in vertices:
                if i == j:
                    dist[(i, j)] = 0
                else:
                    dist[(i, j)] = float('inf')
        
        # Set direct edge weights
        for vertex in self.graph:
            for neighbor, weight in self.graph[vertex]:
                dist[(vertex, neighbor)] = weight
        
        # Floyd-Warshall algorithm
        for k in vertices:
            for i in vertices:
                for j in vertices:
                    if dist[(i, k)] + dist[(k, j)] < dist[(i, j)]:
                        dist[(i, j)] = dist[(i, k)] + dist[(k, j)]
        
        return dist
    
    def a_star(self, start: str, goal: str, heuristic: Dict[str, float]) -> Optional[List[str]]:
        """
        A* algorithm for shortest path with heuristic
        
        Args:
            start: Starting vertex
            goal: Goal vertex
            heuristic: Heuristic function h(vertex) -> estimated distance to goal
        
        Returns:
            Shortest path as list of vertices, None if no path
        """
        # Priority queue: (f_score, vertex)
        open_set = [(heuristic.get(start, 0), start)]
        came_from = {}
        
        # g_score: cost from start to vertex
        g_score = defaultdict(lambda: float('inf'))
        g_score[start] = 0
        
        # f_score: g_score + heuristic
        f_score = defaultdict(lambda: float('inf'))
        f_score[start] = heuristic.get(start, 0)
        
        visited = set()
        
        while open_set:
            _, current = heapq.heappop(open_set)
            
            if current == goal:
                # Reconstruct path
                path = []
                while current in came_from:
                    path.append(current)
                    current = came_from[current]
                path.append(start)
                path.reverse()
                return path
            
            if current in visited:
                continue
            
            visited.add(current)
            
            for neighbor, weight in self.graph.get(current, []):
                if neighbor in visited:
                    continue
                
                tentative_g_score = g_score[current] + weight
                
                if tentative_g_score < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g_score
                    f_score[neighbor] = g_score[neighbor] + heuristic.get(neighbor, 0)
                    heapq.heappush(open_set, (f_score[neighbor], neighbor))
        
        return None  # No path found


def demo_dijkstra():
    """Demonstrate Dijkstra's algorithm"""
    print("=== Dijkstra's Algorithm Demo ===")
    
    # Create weighted graph
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 1), ('D', 5)],
        'C': [('D', 8), ('E', 10)],
        'D': [('E', 2)],
        'E': []
    }
    
    print("Weighted graph:")
    for vertex, edges in graph.items():
        edge_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in edges)
        print(f"{vertex}: [{edge_str}]")
    
    shortest_path = ShortestPath(graph)
    distances, previous = shortest_path.dijkstra('A')
    
    print(f"\nShortest distances from A:")
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        if dist == float('inf'):
            print(f"A -> {vertex}: No path")
        else:
            path = shortest_path.get_path(previous, 'A', vertex)
            path_str = " -> ".join(path) if path else "No path"
            print(f"A -> {vertex}: {dist} (path: {path_str})")


def demo_bellman_ford():
    """Demonstrate Bellman-Ford algorithm"""
    print("\n=== Bellman-Ford Algorithm Demo ===")
    
    # Graph with negative edge
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('C', -3), ('D', 2)],
        'C': [('D', 3)],
        'D': []
    }
    
    print("Graph with negative edge:")
    for vertex, edges in graph.items():
        edge_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in edges)
        print(f"{vertex}: [{edge_str}]")
    
    shortest_path = ShortestPath(graph)
    distances, previous, has_negative_cycle = shortest_path.bellman_ford('A')
    
    print(f"\nHas negative cycle: {has_negative_cycle}")
    print(f"Shortest distances from A:")
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        if dist == float('inf'):
            print(f"A -> {vertex}: No path")
        else:
            path = shortest_path.get_path(previous, 'A', vertex)
            path_str = " -> ".join(path) if path else "No path"
            print(f"A -> {vertex}: {dist} (path: {path_str})")


def demo_negative_cycle():
    """Demonstrate negative cycle detection"""
    print("\n=== Negative Cycle Detection Demo ===")
    
    # Graph with negative cycle
    graph = {
        'A': [('B', 1)],
        'B': [('C', -3)],
        'C': [('B', 1), ('D', 1)],
        'D': []
    }
    
    print("Graph with negative cycle (B -> C -> B):")
    for vertex, edges in graph.items():
        edge_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in edges)
        print(f"{vertex}: [{edge_str}]")
    
    shortest_path = ShortestPath(graph)
    distances, previous, has_negative_cycle = shortest_path.bellman_ford('A')
    
    print(f"\nHas negative cycle: {has_negative_cycle}")
    if has_negative_cycle:
        print("Note: Distances may not be meaningful due to negative cycle")


def demo_floyd_warshall():
    """Demonstrate Floyd-Warshall algorithm"""
    print("\n=== Floyd-Warshall Algorithm Demo ===")
    
    graph = {
        'A': [('B', 3), ('C', 8), ('E', -4)],
        'B': [('D', 1), ('E', 7)],
        'C': [('B', 4)],
        'D': [('A', 2), ('C', -5)],
        'E': [('D', 6)]
    }
    
    print("Graph for all-pairs shortest paths:")
    for vertex, edges in graph.items():
        edge_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in edges)
        print(f"{vertex}: [{edge_str}]")
    
    shortest_path = ShortestPath(graph)
    all_distances = shortest_path.floyd_warshall()
    
    vertices = sorted(['A', 'B', 'C', 'D', 'E'])
    
    print(f"\nAll-pairs shortest distances:")
    print("     " + "".join(f"{v:>8}" for v in vertices))
    
    for i in vertices:
        row = f"{i:>2}  "
        for j in vertices:
            dist = all_distances[(i, j)]
            if dist == float('inf'):
                row += f"{'∞':>8}"
            else:
                row += f"{dist:>8.0f}"
        print(row)


def demo_a_star():
    """Demonstrate A* algorithm"""
    print("\n=== A* Algorithm Demo ===")
    
    # Simple grid-like graph
    graph = {
        'A': [('B', 1), ('D', 1)],
        'B': [('A', 1), ('C', 1), ('E', 1)],
        'C': [('B', 1), ('F', 1)],
        'D': [('A', 1), ('E', 1)],
        'E': [('B', 1), ('D', 1), ('F', 1)],
        'F': [('C', 1), ('E', 1)]
    }
    
    # Manhattan distance heuristic (estimated)
    heuristic = {
        'A': 3, 'B': 2, 'C': 1,
        'D': 2, 'E': 1, 'F': 0
    }
    
    print("Graph with heuristic (goal is F):")
    for vertex, edges in graph.items():
        edge_str = ", ".join(f"{neighbor}({weight})" for neighbor, weight in edges)
        h_val = heuristic.get(vertex, 0)
        print(f"{vertex} (h={h_val}): [{edge_str}]")
    
    shortest_path = ShortestPath(graph)
    path = shortest_path.a_star('A', 'F', heuristic)
    
    if path:
        print(f"\nA* path from A to F: {' -> '.join(path)}")
        print(f"Path length: {len(path) - 1}")
    else:
        print("\nNo path found from A to F")


def compare_algorithms():
    """Compare shortest path algorithms"""
    print("\n=== Algorithm Comparison ===")
    
    print("Dijkstra's Algorithm:")
    print("✓ Efficient for single-source shortest paths")
    print("✓ Works with non-negative edge weights")
    print("✓ O((V + E) log V) with binary heap")
    print("✗ Cannot handle negative edge weights")
    print("Use: GPS navigation, network routing")
    
    print("\nBellman-Ford Algorithm:")
    print("✓ Handles negative edge weights")
    print("✓ Detects negative cycles")
    print("✓ Simpler implementation than Dijkstra")
    print("✗ Slower: O(VE) time complexity")
    print("Use: Currency arbitrage, cycle detection")
    
    print("\nFloyd-Warshall Algorithm:")
    print("✓ Finds all-pairs shortest paths")
    print("✓ Handles negative edges (no negative cycles)")
    print("✓ Simple implementation")
    print("✗ O(V³) time complexity")
    print("✗ O(V²) space complexity")
    print("Use: Dense graphs, all-pairs distances")
    
    print("\nA* Algorithm:")
    print("✓ Optimal with admissible heuristic")
    print("✓ Often faster than Dijkstra for specific goal")
    print("✓ Widely applicable with good heuristics")
    print("✗ Requires domain-specific heuristic function")
    print("✗ Memory usage can be high")
    print("Use: Pathfinding in games, robotics")


if __name__ == "__main__":
    demo_dijkstra()
    demo_bellman_ford()
    demo_negative_cycle()
    demo_floyd_warshall()
    demo_a_star()
    compare_algorithms()
