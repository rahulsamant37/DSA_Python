"""
016 - Graph Implementation
==========================

This module implements graphs with different representations and algorithms:
- Adjacency Matrix representation
- Adjacency List representation
- Graph traversals: DFS, BFS
- Shortest path algorithms: Dijkstra, Bellman-Ford, Floyd-Warshall
- Minimum Spanning Tree: Kruskal's and Prim's algorithms
- Topological sorting
- Cycle detection
- Connected components

Time Complexity:
- DFS/BFS: O(V + E)
- Dijkstra: O((V + E) log V) with min-heap
- Bellman-Ford: O(VE)
- Floyd-Warshall: O(V³)
- Kruskal's MST: O(E log E)
- Prim's MST: O((V + E) log V)

Space Complexity:
- Adjacency Matrix: O(V²)
- Adjacency List: O(V + E)
"""

from collections import defaultdict, deque
import heapq
import sys


class GraphAdjacencyMatrix:
    """Graph implementation using adjacency matrix"""
    
    def __init__(self, num_vertices, directed=False):
        self.num_vertices = num_vertices
        self.directed = directed
        self.matrix = [[0] * num_vertices for _ in range(num_vertices)]
        self.vertices = {}  # Map vertex names to indices
        self.vertex_names = {}  # Map indices to vertex names
        self.next_index = 0
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        if vertex not in self.vertices:
            if self.next_index >= self.num_vertices:
                raise ValueError("Maximum number of vertices reached")
            
            self.vertices[vertex] = self.next_index
            self.vertex_names[self.next_index] = vertex
            self.next_index += 1
    
    def add_edge(self, src, dest, weight=1):
        """Add an edge between two vertices"""
        if src not in self.vertices:
            self.add_vertex(src)
        if dest not in self.vertices:
            self.add_vertex(dest)
        
        src_idx = self.vertices[src]
        dest_idx = self.vertices[dest]
        
        self.matrix[src_idx][dest_idx] = weight
        if not self.directed:
            self.matrix[dest_idx][src_idx] = weight
    
    def has_edge(self, src, dest):
        """Check if edge exists between two vertices"""
        if src not in self.vertices or dest not in self.vertices:
            return False
        
        src_idx = self.vertices[src]
        dest_idx = self.vertices[dest]
        return self.matrix[src_idx][dest_idx] != 0
    
    def get_weight(self, src, dest):
        """Get weight of edge between two vertices"""
        if not self.has_edge(src, dest):
            return None
        
        src_idx = self.vertices[src]
        dest_idx = self.vertices[dest]
        return self.matrix[src_idx][dest_idx]
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        if vertex not in self.vertices:
            return []
        
        vertex_idx = self.vertices[vertex]
        neighbors = []
        
        for i in range(self.num_vertices):
            if self.matrix[vertex_idx][i] != 0:
                neighbors.append(self.vertex_names.get(i))
        
        return neighbors
    
    def display(self):
        """Display the adjacency matrix"""
        print("Adjacency Matrix:")
        
        # Print header
        print("   ", end="")
        for i in range(self.next_index):
            vertex_name = self.vertex_names.get(i, str(i))
            print(f"{vertex_name:>3}", end="")
        print()
        
        # Print matrix with row labels
        for i in range(self.next_index):
            vertex_name = self.vertex_names.get(i, str(i))
            print(f"{vertex_name:>2} ", end="")
            for j in range(self.next_index):
                print(f"{self.matrix[i][j]:>3}", end="")
            print()


class GraphAdjacencyList:
    """Graph implementation using adjacency list"""
    
    def __init__(self, directed=False):
        self.directed = directed
        self.graph = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, vertex):
        """Add a vertex to the graph"""
        self.vertices.add(vertex)
        if vertex not in self.graph:
            self.graph[vertex] = []
    
    def add_edge(self, src, dest, weight=1):
        """Add an edge between two vertices"""
        self.add_vertex(src)
        self.add_vertex(dest)
        
        self.graph[src].append((dest, weight))
        if not self.directed:
            self.graph[dest].append((src, weight))
    
    def has_edge(self, src, dest):
        """Check if edge exists between two vertices"""
        if src not in self.graph:
            return False
        
        return any(neighbor == dest for neighbor, _ in self.graph[src])
    
    def get_weight(self, src, dest):
        """Get weight of edge between two vertices"""
        if src not in self.graph:
            return None
        
        for neighbor, weight in self.graph[src]:
            if neighbor == dest:
                return weight
        return None
    
    def get_neighbors(self, vertex):
        """Get all neighbors of a vertex"""
        return [neighbor for neighbor, _ in self.graph.get(vertex, [])]
    
    def get_edges(self):
        """Get all edges in the graph"""
        edges = []
        for src in self.graph:
            for dest, weight in self.graph[src]:
                if self.directed or src <= dest:  # Avoid duplicates for undirected
                    edges.append((src, dest, weight))
        return edges
    
    def display(self):
        """Display the adjacency list"""
        print("Adjacency List:")
        for vertex in sorted(self.vertices):
            neighbors = self.graph.get(vertex, [])
            neighbor_str = ", ".join([f"{dest}({weight})" for dest, weight in neighbors])
            print(f"{vertex}: [{neighbor_str}]")


class GraphTraversal:
    """Graph traversal algorithms"""
    
    @staticmethod
    def dfs_recursive(graph, start, visited=None):
        """Depth-First Search using recursion"""
        if visited is None:
            visited = set()
        
        result = []
        
        def dfs_util(vertex):
            visited.add(vertex)
            result.append(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_util(neighbor)
        
        dfs_util(start)
        return result
    
    @staticmethod
    def dfs_iterative(graph, start):
        """Depth-First Search using stack"""
        visited = set()
        stack = [start]
        result = []
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                result.append(vertex)
                
                # Add neighbors in reverse order to maintain left-to-right traversal
                neighbors = graph.get_neighbors(vertex)
                for neighbor in reversed(neighbors):
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return result
    
    @staticmethod
    def bfs(graph, start):
        """Breadth-First Search using queue"""
        visited = set()
        queue = deque([start])
        result = []
        
        visited.add(start)
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        return result
    
    @staticmethod
    def has_cycle_directed(graph):
        """Detect cycle in directed graph using DFS"""
        WHITE, GRAY, BLACK = 0, 1, 2
        color = {vertex: WHITE for vertex in graph.vertices}
        
        def dfs_visit(vertex):
            color[vertex] = GRAY
            
            for neighbor in graph.get_neighbors(vertex):
                if color[neighbor] == GRAY:  # Back edge found
                    return True
                elif color[neighbor] == WHITE and dfs_visit(neighbor):
                    return True
            
            color[vertex] = BLACK
            return False
        
        for vertex in graph.vertices:
            if color[vertex] == WHITE:
                if dfs_visit(vertex):
                    return True
        
        return False
    
    @staticmethod
    def has_cycle_undirected(graph):
        """Detect cycle in undirected graph using DFS"""
        visited = set()
        
        def dfs_visit(vertex, parent):
            visited.add(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    if dfs_visit(neighbor, vertex):
                        return True
                elif neighbor != parent:  # Back edge found
                    return True
            
            return False
        
        for vertex in graph.vertices:
            if vertex not in visited:
                if dfs_visit(vertex, None):
                    return True
        
        return False


class ShortestPath:
    """Shortest path algorithms"""
    
    @staticmethod
    def dijkstra(graph, start):
        """Dijkstra's shortest path algorithm"""
        distances = {vertex: float('infinity') for vertex in graph.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in graph.vertices}
        
        # Priority queue: (distance, vertex)
        pq = [(0, start)]
        visited = set()
        
        while pq:
            current_distance, current = heapq.heappop(pq)
            
            if current in visited:
                continue
            
            visited.add(current)
            
            # Check all neighbors
            for neighbor, weight in graph.graph.get(current, []):
                if neighbor not in visited:
                    distance = current_distance + weight
                    
                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        previous[neighbor] = current
                        heapq.heappush(pq, (distance, neighbor))
        
        return distances, previous
    
    @staticmethod
    def bellman_ford(graph, start):
        """Bellman-Ford shortest path algorithm (handles negative weights)"""
        distances = {vertex: float('infinity') for vertex in graph.vertices}
        distances[start] = 0
        previous = {vertex: None for vertex in graph.vertices}
        
        # Relax edges repeatedly
        for _ in range(len(graph.vertices) - 1):
            for src, dest, weight in graph.get_edges():
                if distances[src] != float('infinity'):
                    if distances[src] + weight < distances[dest]:
                        distances[dest] = distances[src] + weight
                        previous[dest] = src
        
        # Check for negative cycles
        for src, dest, weight in graph.get_edges():
            if distances[src] != float('infinity'):
                if distances[src] + weight < distances[dest]:
                    raise ValueError("Graph contains negative cycle")
        
        return distances, previous
    
    @staticmethod
    def floyd_warshall(graph):
        """Floyd-Warshall all-pairs shortest path algorithm"""
        vertices = list(graph.vertices)
        n = len(vertices)
        vertex_to_index = {v: i for i, v in enumerate(vertices)}
        
        # Initialize distance matrix
        dist = [[float('infinity')] * n for _ in range(n)]
        
        # Distance from vertex to itself is 0
        for i in range(n):
            dist[i][i] = 0
        
        # Fill in edge weights
        for src, dest, weight in graph.get_edges():
            i, j = vertex_to_index[src], vertex_to_index[dest]
            dist[i][j] = weight
        
        # Main Floyd-Warshall algorithm
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k] + dist[k][j] < dist[i][j]:
                        dist[i][j] = dist[i][k] + dist[k][j]
        
        # Convert back to vertex names
        result = {}
        for i, src in enumerate(vertices):
            result[src] = {}
            for j, dest in enumerate(vertices):
                result[src][dest] = dist[i][j]
        
        return result
    
    @staticmethod
    def reconstruct_path(previous, start, end):
        """Reconstruct path from previous array"""
        path = []
        current = end
        
        while current is not None:
            path.append(current)
            current = previous[current]
        
        path.reverse()
        
        if path[0] == start:
            return path
        else:
            return []  # No path found


class MinimumSpanningTree:
    """Minimum Spanning Tree algorithms"""
    
    class UnionFind:
        """Union-Find data structure for Kruskal's algorithm"""
        
        def __init__(self, vertices):
            self.parent = {v: v for v in vertices}
            self.rank = {v: 0 for v in vertices}
        
        def find(self, x):
            if self.parent[x] != x:
                self.parent[x] = self.find(self.parent[x])  # Path compression
            return self.parent[x]
        
        def union(self, x, y):
            px, py = self.find(x), self.find(y)
            
            if px == py:
                return False
            
            # Union by rank
            if self.rank[px] < self.rank[py]:
                px, py = py, px
            
            self.parent[py] = px
            if self.rank[px] == self.rank[py]:
                self.rank[px] += 1
            
            return True
    
    @staticmethod
    def kruskal(graph):
        """Kruskal's MST algorithm"""
        edges = graph.get_edges()
        edges.sort(key=lambda x: x[2])  # Sort by weight
        
        mst = []
        uf = MinimumSpanningTree.UnionFind(graph.vertices)
        total_weight = 0
        
        for src, dest, weight in edges:
            if uf.union(src, dest):
                mst.append((src, dest, weight))
                total_weight += weight
                
                if len(mst) == len(graph.vertices) - 1:
                    break
        
        return mst, total_weight
    
    @staticmethod
    def prim(graph, start):
        """Prim's MST algorithm"""
        mst = []
        visited = {start}
        total_weight = 0
        
        # Priority queue: (weight, src, dest)
        pq = []
        
        # Add all edges from start vertex
        for neighbor, weight in graph.graph.get(start, []):
            heapq.heappush(pq, (weight, start, neighbor))
        
        while pq and len(visited) < len(graph.vertices):
            weight, src, dest = heapq.heappop(pq)
            
            if dest in visited:
                continue
            
            # Add edge to MST
            mst.append((src, dest, weight))
            total_weight += weight
            visited.add(dest)
            
            # Add edges from new vertex
            for neighbor, edge_weight in graph.graph.get(dest, []):
                if neighbor not in visited:
                    heapq.heappush(pq, (edge_weight, dest, neighbor))
        
        return mst, total_weight


class TopologicalSort:
    """Topological sorting for directed acyclic graphs"""
    
    @staticmethod
    def kahn_algorithm(graph):
        """Topological sort using Kahn's algorithm (BFS-based)"""
        in_degree = {vertex: 0 for vertex in graph.vertices}
        
        # Calculate in-degrees
        for vertex in graph.vertices:
            for neighbor in graph.get_neighbors(vertex):
                in_degree[neighbor] += 1
        
        # Find vertices with no incoming edges
        queue = deque([v for v in graph.vertices if in_degree[v] == 0])
        result = []
        
        while queue:
            vertex = queue.popleft()
            result.append(vertex)
            
            # Remove this vertex and update in-degrees
            for neighbor in graph.get_neighbors(vertex):
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all vertices are included (no cycle)
        if len(result) != len(graph.vertices):
            raise ValueError("Graph contains a cycle")
        
        return result
    
    @staticmethod
    def dfs_based(graph):
        """Topological sort using DFS"""
        visited = set()
        stack = []
        
        def dfs_visit(vertex):
            visited.add(vertex)
            
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    dfs_visit(neighbor)
            
            stack.append(vertex)
        
        for vertex in graph.vertices:
            if vertex not in visited:
                dfs_visit(vertex)
        
        return stack[::-1]  # Reverse the stack


def test_graph_representations():
    """Test different graph representations"""
    print("=== Testing Graph Representations ===\n")
    
    # Test Adjacency Matrix
    print("=== Adjacency Matrix ===")
    matrix_graph = GraphAdjacencyMatrix(5, directed=False)
    
    # Add edges
    edges = [('A', 'B', 1), ('A', 'C', 4), ('B', 'C', 2), ('B', 'D', 5), ('C', 'D', 1)]
    
    for src, dest, weight in edges:
        matrix_graph.add_edge(src, dest, weight)
    
    matrix_graph.display()
    print(f"Neighbors of A: {matrix_graph.get_neighbors('A')}")
    print(f"Weight A->C: {matrix_graph.get_weight('A', 'C')}")
    print()
    
    # Test Adjacency List
    print("=== Adjacency List ===")
    list_graph = GraphAdjacencyList(directed=False)
    
    for src, dest, weight in edges:
        list_graph.add_edge(src, dest, weight)
    
    list_graph.display()
    print(f"Neighbors of A: {list_graph.get_neighbors('A')}")
    print(f"Weight A->C: {list_graph.get_weight('A', 'C')}")
    print()


def test_graph_traversal():
    """Test graph traversal algorithms"""
    print("=== Testing Graph Traversal ===\n")
    
    # Create test graph
    graph = GraphAdjacencyList(directed=False)
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'E'), ('D', 'F'), ('E', 'F')]
    
    for src, dest in edges:
        graph.add_edge(src, dest)
    
    graph.display()
    print()
    
    # Test traversals
    print("Graph Traversals starting from 'A':")
    dfs_recursive = GraphTraversal.dfs_recursive(graph, 'A')
    dfs_iterative = GraphTraversal.dfs_iterative(graph, 'A')
    bfs_result = GraphTraversal.bfs(graph, 'A')
    
    print(f"DFS (Recursive): {dfs_recursive}")
    print(f"DFS (Iterative): {dfs_iterative}")
    print(f"BFS: {bfs_result}")
    print()
    
    # Test cycle detection
    print("Cycle Detection:")
    print(f"Has cycle (undirected): {GraphTraversal.has_cycle_undirected(graph)}")
    
    # Test with directed graph
    directed_graph = GraphAdjacencyList(directed=True)
    directed_edges = [('A', 'B'), ('B', 'C'), ('C', 'A')]  # Has cycle
    
    for src, dest in directed_edges:
        directed_graph.add_edge(src, dest)
    
    print(f"Has cycle (directed): {GraphTraversal.has_cycle_directed(directed_graph)}")
    print()


def test_shortest_path():
    """Test shortest path algorithms"""
    print("=== Testing Shortest Path Algorithms ===\n")
    
    # Create weighted graph
    graph = GraphAdjacencyList(directed=True)
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]
    
    for src, dest, weight in edges:
        graph.add_edge(src, dest, weight)
    
    graph.display()
    print()
    
    # Test Dijkstra's algorithm
    print("Dijkstra's Algorithm from 'A':")
    distances, previous = ShortestPath.dijkstra(graph, 'A')
    
    for vertex in sorted(distances.keys()):
        dist = distances[vertex]
        path = ShortestPath.reconstruct_path(previous, 'A', vertex)
        print(f"Distance to {vertex}: {dist}, Path: {' -> '.join(path)}")
    print()
    
    # Test Floyd-Warshall
    print("Floyd-Warshall All-Pairs Shortest Paths:")
    all_distances = ShortestPath.floyd_warshall(graph)
    
    vertices = sorted(graph.vertices)
    print("    ", end="")
    for v in vertices:
        print(f"{v:>8}", end="")
    print()
    
    for src in vertices:
        print(f"{src:>3} ", end="")
        for dest in vertices:
            dist = all_distances[src][dest]
            if dist == float('infinity'):
                print(f"{'∞':>8}", end="")
            else:
                print(f"{dist:>8}", end="")
        print()
    print()


def test_mst():
    """Test Minimum Spanning Tree algorithms"""
    print("=== Testing Minimum Spanning Tree ===\n")
    
    # Create weighted graph
    graph = GraphAdjacencyList(directed=False)
    edges = [
        ('A', 'B', 4), ('A', 'H', 8),
        ('B', 'C', 8), ('B', 'H', 11),
        ('C', 'D', 7), ('C', 'F', 4), ('C', 'I', 2),
        ('D', 'E', 9), ('D', 'F', 14),
        ('E', 'F', 10),
        ('F', 'G', 2),
        ('G', 'H', 1), ('G', 'I', 6),
        ('H', 'I', 7)
    ]
    
    for src, dest, weight in edges:
        graph.add_edge(src, dest, weight)
    
    print("Original Graph:")
    graph.display()
    print()
    
    # Test Kruskal's algorithm
    print("Kruskal's MST:")
    kruskal_mst, kruskal_weight = MinimumSpanningTree.kruskal(graph)
    for src, dest, weight in kruskal_mst:
        print(f"  {src} -- {dest}: {weight}")
    print(f"Total weight: {kruskal_weight}")
    print()
    
    # Test Prim's algorithm
    print("Prim's MST (starting from 'A'):")
    prim_mst, prim_weight = MinimumSpanningTree.prim(graph, 'A')
    for src, dest, weight in prim_mst:
        print(f"  {src} -- {dest}: {weight}")
    print(f"Total weight: {prim_weight}")
    print()


def test_topological_sort():
    """Test topological sorting"""
    print("=== Testing Topological Sort ===\n")
    
    # Create directed acyclic graph
    graph = GraphAdjacencyList(directed=True)
    edges = [
        ('A', 'C'), ('A', 'D'),
        ('B', 'C'), ('B', 'E'),
        ('C', 'F'),
        ('D', 'F'),
        ('E', 'F')
    ]
    
    for src, dest in edges:
        graph.add_edge(src, dest)
    
    print("Directed Acyclic Graph:")
    graph.display()
    print()
    
    # Test both algorithms
    print("Topological Orderings:")
    kahn_result = TopologicalSort.kahn_algorithm(graph)
    dfs_result = TopologicalSort.dfs_based(graph)
    
    print(f"Kahn's Algorithm: {kahn_result}")
    print(f"DFS-based: {dfs_result}")


if __name__ == "__main__":
    test_graph_representations()
    test_graph_traversal()
    test_shortest_path()
    test_mst()
    test_topological_sort()
