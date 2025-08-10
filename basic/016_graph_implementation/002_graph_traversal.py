"""
002 - Graph Traversal Algorithms
================================

Breadth-First Search (BFS) and Depth-First Search (DFS) implementations.

BFS (Breadth-First Search):
- Time Complexity: O(V + E)
- Space Complexity: O(V)
- Uses queue (FIFO)
- Explores level by level
- Finds shortest path in unweighted graphs

DFS (Depth-First Search):
- Time Complexity: O(V + E)
- Space Complexity: O(V)
- Uses stack (LIFO) or recursion
- Explores as far as possible before backtracking
- Used for topological sorting, cycle detection
"""

from collections import deque, defaultdict
from typing import List, Set, Dict, Optional, Callable


class GraphTraversal:
    """Graph traversal algorithms for adjacency list representation"""
    
    def __init__(self, adjacency_list: Dict[str, List[str]], directed: bool = False):
        """
        Initialize with adjacency list
        
        Args:
            adjacency_list: Graph as adjacency list
            directed: Whether graph is directed
        """
        self.graph = adjacency_list
        self.directed = directed
    
    def bfs(self, start: str, visit_callback: Optional[Callable] = None) -> List[str]:
        """
        Breadth-First Search traversal
        
        Args:
            start: Starting vertex
            visit_callback: Optional function called for each visited vertex
        
        Returns:
            List of vertices in BFS order
        """
        if start not in self.graph:
            return []
        
        visited = set()
        queue = deque([start])
        result = []
        
        while queue:
            vertex = queue.popleft()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                if visit_callback:
                    visit_callback(vertex)
                
                # Add unvisited neighbors to queue
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append(neighbor)
        
        return result
    
    def dfs_recursive(self, start: str, visit_callback: Optional[Callable] = None) -> List[str]:
        """
        Depth-First Search using recursion
        
        Args:
            start: Starting vertex
            visit_callback: Optional function called for each visited vertex
        
        Returns:
            List of vertices in DFS order
        """
        if start not in self.graph:
            return []
        
        visited = set()
        result = []
        
        def dfs_helper(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            if visit_callback:
                visit_callback(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor not in visited:
                    dfs_helper(neighbor)
        
        dfs_helper(start)
        return result
    
    def dfs_iterative(self, start: str, visit_callback: Optional[Callable] = None) -> List[str]:
        """
        Depth-First Search using iteration and stack
        
        Args:
            start: Starting vertex
            visit_callback: Optional function called for each visited vertex
        
        Returns:
            List of vertices in DFS order
        """
        if start not in self.graph:
            return []
        
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                if visit_callback:
                    visit_callback(vertex)
                
                # Add neighbors to stack (reverse order for left-to-right traversal)
                neighbors = self.graph.get(vertex, [])
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    def bfs_shortest_path(self, start: str, end: str) -> Optional[List[str]]:
        """
        Find shortest path between two vertices using BFS
        
        Args:
            start: Starting vertex
            end: Target vertex
        
        Returns:
            Shortest path as list of vertices, None if no path
        """
        if start not in self.graph or end not in self.graph:
            return None
        
        if start == end:
            return [start]
        
        visited = set()
        queue = deque([(start, [start])])  # (vertex, path)
        
        while queue:
            vertex, path = queue.popleft()
            
            if vertex in visited:
                continue
            
            visited.add(vertex)
            
            for neighbor in self.graph.get(vertex, []):
                if neighbor == end:
                    return path + [neighbor]
                
                if neighbor not in visited:
                    queue.append((neighbor, path + [neighbor]))
        
        return None  # No path found
    
    def bfs_level_order(self, start: str) -> Dict[int, List[str]]:
        """
        BFS traversal with level information
        
        Args:
            start: Starting vertex
        
        Returns:
            Dictionary mapping level to vertices at that level
        """
        if start not in self.graph:
            return {}
        
        visited = set()
        queue = deque([(start, 0)])  # (vertex, level)
        levels = defaultdict(list)
        
        while queue:
            vertex, level = queue.popleft()
            
            if vertex not in visited:
                visited.add(vertex)
                levels[level].append(vertex)
                
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        queue.append((neighbor, level + 1))
        
        return dict(levels)
    
    def connected_components(self) -> List[List[str]]:
        """
        Find all connected components using DFS
        
        Returns:
            List of connected components (each component is a list of vertices)
        """
        visited = set()
        components = []
        
        for vertex in self.graph:
            if vertex not in visited:
                component = []
                self._dfs_component(vertex, visited, component)
                components.append(component)
        
        return components
    
    def _dfs_component(self, vertex: str, visited: Set[str], component: List[str]):
        """Helper method for finding connected components"""
        visited.add(vertex)
        component.append(vertex)
        
        for neighbor in self.graph.get(vertex, []):
            if neighbor not in visited:
                self._dfs_component(neighbor, visited, component)
    
    def has_path(self, start: str, end: str) -> bool:
        """
        Check if path exists between two vertices
        
        Args:
            start: Starting vertex
            end: Target vertex
        
        Returns:
            True if path exists, False otherwise
        """
        if start not in self.graph or end not in self.graph:
            return False
        
        if start == end:
            return True
        
        visited = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            
            if vertex == end:
                return True
            
            if vertex not in visited:
                visited.add(vertex)
                
                for neighbor in self.graph.get(vertex, []):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return False
    
    def is_bipartite(self) -> bool:
        """
        Check if graph is bipartite using BFS coloring
        
        Returns:
            True if graph is bipartite, False otherwise
        """
        color = {}
        
        # Check each connected component
        for start in self.graph:
            if start not in color:
                # Color starting vertex with 0
                queue = deque([start])
                color[start] = 0
                
                while queue:
                    vertex = queue.popleft()
                    
                    for neighbor in self.graph.get(vertex, []):
                        if neighbor not in color:
                            # Color with opposite color
                            color[neighbor] = 1 - color[vertex]
                            queue.append(neighbor)
                        elif color[neighbor] == color[vertex]:
                            # Same color as current vertex - not bipartite
                            return False
        
        return True


def demo_graph_traversal():
    """Demonstrate graph traversal algorithms"""
    print("=== Graph Traversal Demo ===")
    
    # Create sample graph
    #     A
    #    / \
    #   B   C
    #  /   / \
    # D   E   F
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'E', 'F'],
        'D': ['B'],
        'E': ['C'],
        'F': ['C']
    }
    
    print("Graph structure:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")
    
    traversal = GraphTraversal(graph)
    
    # BFS traversal
    print(f"\nBFS from A: {traversal.bfs('A')}")
    print(f"DFS (recursive) from A: {traversal.dfs_recursive('A')}")
    print(f"DFS (iterative) from A: {traversal.dfs_iterative('A')}")
    
    # Shortest path
    path = traversal.bfs_shortest_path('A', 'E')
    print(f"Shortest path A -> E: {path}")
    
    # Level order
    levels = traversal.bfs_level_order('A')
    print(f"BFS levels from A: {levels}")
    
    # Connected components
    components = traversal.connected_components()
    print(f"Connected components: {components}")
    
    # Path existence
    print(f"Path A -> F exists: {traversal.has_path('A', 'F')}")
    
    # Bipartite check
    print(f"Is bipartite: {traversal.is_bipartite()}")


def demo_disconnected_graph():
    """Demonstrate traversal on disconnected graph"""
    print("\n=== Disconnected Graph Demo ===")
    
    # Disconnected graph
    graph = {
        'A': ['B'],
        'B': ['A', 'C'],
        'C': ['B'],
        'X': ['Y'],
        'Y': ['X', 'Z'],
        'Z': ['Y']
    }
    
    print("Disconnected graph:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")
    
    traversal = GraphTraversal(graph)
    
    print(f"\nBFS from A: {traversal.bfs('A')}")
    print(f"BFS from X: {traversal.bfs('X')}")
    
    components = traversal.connected_components()
    print(f"Connected components: {components}")
    
    print(f"Path A -> X exists: {traversal.has_path('A', 'X')}")


def demo_bipartite_graph():
    """Demonstrate bipartite graph detection"""
    print("\n=== Bipartite Graph Demo ===")
    
    # Bipartite graph
    bipartite_graph = {
        'A': ['X', 'Y'],
        'B': ['X', 'Z'],
        'C': ['Y', 'Z'],
        'X': ['A', 'B'],
        'Y': ['A', 'C'],
        'Z': ['B', 'C']
    }
    
    print("Bipartite graph (A,B,C vs X,Y,Z):")
    for vertex, neighbors in bipartite_graph.items():
        print(f"{vertex}: {neighbors}")
    
    traversal = GraphTraversal(bipartite_graph)
    print(f"Is bipartite: {traversal.is_bipartite()}")
    
    # Non-bipartite graph (triangle)
    triangle_graph = {
        'A': ['B', 'C'],
        'B': ['A', 'C'],
        'C': ['A', 'B']
    }
    
    print(f"\nTriangle graph:")
    for vertex, neighbors in triangle_graph.items():
        print(f"{vertex}: {neighbors}")
    
    triangle_traversal = GraphTraversal(triangle_graph)
    print(f"Is bipartite: {triangle_traversal.is_bipartite()}")


def compare_bfs_dfs():
    """Compare BFS and DFS characteristics"""
    print("\n=== BFS vs DFS Comparison ===")
    
    print("Breadth-First Search (BFS):")
    print("✓ Finds shortest path in unweighted graphs")
    print("✓ Level-by-level exploration")
    print("✓ Good for finding nodes close to start")
    print("✗ Uses more memory (queue can be large)")
    print("Uses: Shortest path, level-order traversal, broadcasting")
    
    print("\nDepth-First Search (DFS):")
    print("✓ Uses less memory (stack depth = longest path)")
    print("✓ Natural for recursive problems")
    print("✓ Good for exploring full paths")
    print("✗ May find longer paths first")
    print("✗ Can get stuck in deep branches")
    print("Uses: Topological sort, cycle detection, maze solving")
    
    print("\nTime Complexity: O(V + E) for both")
    print("Space Complexity: O(V) for both")
    print("Choice depends on problem requirements!")


if __name__ == "__main__":
    demo_graph_traversal()
    demo_disconnected_graph()
    demo_bipartite_graph()
    compare_bfs_dfs()
