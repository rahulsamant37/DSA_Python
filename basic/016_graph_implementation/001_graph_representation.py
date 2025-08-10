"""
001 - Graph Representation
==========================

Different ways to represent graphs in memory.

Representations covered:
1. Adjacency Matrix
2. Adjacency List
3. Edge List
4. Adjacency Set

Time/Space complexities for V vertices and E edges:

Adjacency Matrix:
- Space: O(V²)
- Add vertex: O(V²) (need to resize)
- Add edge: O(1)
- Remove edge: O(1)
- Check edge: O(1)

Adjacency List:
- Space: O(V + E)
- Add vertex: O(1)
- Add edge: O(1)
- Remove edge: O(V) worst case
- Check edge: O(V) worst case

Best choice depends on graph density and operations needed.
"""

from typing import List, Dict, Set, Tuple, Optional
from collections import defaultdict


class AdjacencyMatrixGraph:
    """Graph representation using adjacency matrix"""
    
    def __init__(self, num_vertices: int = 0, directed: bool = False):
        """
        Initialize graph with adjacency matrix
        
        Args:
            num_vertices: Initial number of vertices
            directed: Whether graph is directed
        """
        self.num_vertices = num_vertices
        self.directed = directed
        # Initialize matrix with False (no edges)
        self.matrix = [[False for _ in range(num_vertices)] 
                      for _ in range(num_vertices)]
        self.vertex_labels = {}  # Map vertex index to label
        self.label_to_index = {}  # Map label to vertex index
    
    def add_vertex(self, label: str = None) -> int:
        """Add a new vertex and return its index"""
        # Expand matrix
        new_size = self.num_vertices + 1
        
        # Add column to existing rows
        for row in self.matrix:
            row.append(False)
        
        # Add new row
        self.matrix.append([False] * new_size)
        
        # Update vertex mapping
        vertex_index = self.num_vertices
        if label:
            self.vertex_labels[vertex_index] = label
            self.label_to_index[label] = vertex_index
        else:
            self.vertex_labels[vertex_index] = str(vertex_index)
            self.label_to_index[str(vertex_index)] = vertex_index
        
        self.num_vertices = new_size
        return vertex_index
    
    def add_edge(self, from_vertex, to_vertex, weight: float = 1):
        """Add edge between vertices"""
        # Convert labels to indices if necessary
        from_idx = self._get_index(from_vertex)
        to_idx = self._get_index(to_vertex)
        
        if from_idx is None or to_idx is None:
            raise ValueError("Vertex not found")
        
        # Add edge
        self.matrix[from_idx][to_idx] = weight
        
        # If undirected, add reverse edge
        if not self.directed:
            self.matrix[to_idx][from_idx] = weight
    
    def remove_edge(self, from_vertex, to_vertex):
        """Remove edge between vertices"""
        from_idx = self._get_index(from_vertex)
        to_idx = self._get_index(to_vertex)
        
        if from_idx is None or to_idx is None:
            return False
        
        self.matrix[from_idx][to_idx] = False
        
        if not self.directed:
            self.matrix[to_idx][from_idx] = False
        
        return True
    
    def has_edge(self, from_vertex, to_vertex) -> bool:
        """Check if edge exists"""
        from_idx = self._get_index(from_vertex)
        to_idx = self._get_index(to_vertex)
        
        if from_idx is None or to_idx is None:
            return False
        
        return bool(self.matrix[from_idx][to_idx])
    
    def get_neighbors(self, vertex) -> List[str]:
        """Get all neighbors of a vertex"""
        vertex_idx = self._get_index(vertex)
        if vertex_idx is None:
            return []
        
        neighbors = []
        for i in range(self.num_vertices):
            if self.matrix[vertex_idx][i]:
                neighbors.append(self.vertex_labels[i])
        
        return neighbors
    
    def _get_index(self, vertex) -> Optional[int]:
        """Convert vertex label to index"""
        if isinstance(vertex, int):
            return vertex if 0 <= vertex < self.num_vertices else None
        return self.label_to_index.get(vertex)
    
    def display(self):
        """Display adjacency matrix"""
        print(f"Adjacency Matrix ({'Directed' if self.directed else 'Undirected'}):")
        
        # Print header
        labels = [self.vertex_labels[i] for i in range(self.num_vertices)]
        print("   " + " ".join(f"{label:>3}" for label in labels))
        
        # Print matrix
        for i in range(self.num_vertices):
            row_label = self.vertex_labels[i]
            row_values = " ".join(f"{int(bool(self.matrix[i][j])):>3}" 
                                 for j in range(self.num_vertices))
            print(f"{row_label:>2} {row_values}")


class AdjacencyListGraph:
    """Graph representation using adjacency list"""
    
    def __init__(self, directed: bool = False):
        """
        Initialize graph with adjacency list
        
        Args:
            directed: Whether graph is directed
        """
        self.directed = directed
        self.adjacency_list = defaultdict(list)
        self.vertices = set()
    
    def add_vertex(self, vertex: str):
        """Add a vertex to the graph"""
        self.vertices.add(vertex)
        if vertex not in self.adjacency_list:
            self.adjacency_list[vertex] = []
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float = 1):
        """Add edge between vertices"""
        # Ensure vertices exist
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge (store as tuple for weighted graphs)
        self.adjacency_list[from_vertex].append((to_vertex, weight))
        
        # If undirected, add reverse edge
        if not self.directed:
            self.adjacency_list[to_vertex].append((from_vertex, weight))
    
    def remove_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """Remove edge between vertices"""
        if from_vertex not in self.adjacency_list:
            return False
        
        # Remove edge
        original_length = len(self.adjacency_list[from_vertex])
        self.adjacency_list[from_vertex] = [
            (neighbor, weight) for neighbor, weight in self.adjacency_list[from_vertex]
            if neighbor != to_vertex
        ]
        
        edge_removed = len(self.adjacency_list[from_vertex]) < original_length
        
        # If undirected, remove reverse edge
        if not self.directed and to_vertex in self.adjacency_list:
            self.adjacency_list[to_vertex] = [
                (neighbor, weight) for neighbor, weight in self.adjacency_list[to_vertex]
                if neighbor != from_vertex
            ]
        
        return edge_removed
    
    def has_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """Check if edge exists"""
        if from_vertex not in self.adjacency_list:
            return False
        
        return any(neighbor == to_vertex 
                  for neighbor, _ in self.adjacency_list[from_vertex])
    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """Get all neighbors with weights"""
        return self.adjacency_list.get(vertex, [])
    
    def get_neighbor_names(self, vertex: str) -> List[str]:
        """Get neighbor names only"""
        return [neighbor for neighbor, _ in self.get_neighbors(vertex)]
    
    def get_vertices(self) -> Set[str]:
        """Get all vertices in the graph"""
        return self.vertices.copy()
    
    def get_edges(self) -> List[Tuple[str, str, float]]:
        """Get all edges as list of (from, to, weight) tuples"""
        edges = []
        for from_vertex in self.adjacency_list:
            for to_vertex, weight in self.adjacency_list[from_vertex]:
                if self.directed or from_vertex <= to_vertex:  # Avoid duplicates for undirected
                    edges.append((from_vertex, to_vertex, weight))
        return edges
    
    def display(self):
        """Display adjacency list"""
        print(f"Adjacency List ({'Directed' if self.directed else 'Undirected'}):")
        
        for vertex in sorted(self.vertices):
            neighbors = self.adjacency_list[vertex]
            if neighbors:
                neighbor_str = ", ".join(f"{neighbor}({weight})" 
                                       for neighbor, weight in neighbors)
                print(f"{vertex}: [{neighbor_str}]")
            else:
                print(f"{vertex}: []")


class EdgeListGraph:
    """Graph representation using edge list"""
    
    def __init__(self, directed: bool = False):
        """
        Initialize graph with edge list
        
        Args:
            directed: Whether graph is directed
        """
        self.directed = directed
        self.edges = []  # List of (from, to, weight) tuples
        self.vertices = set()
    
    def add_vertex(self, vertex: str):
        """Add a vertex to the graph"""
        self.vertices.add(vertex)
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float = 1):
        """Add edge between vertices"""
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        
        # Add edge
        self.edges.append((from_vertex, to_vertex, weight))
        
        # If undirected, add reverse edge
        if not self.directed:
            self.edges.append((to_vertex, from_vertex, weight))
    
    def remove_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """Remove edge between vertices"""
        original_length = len(self.edges)
        
        # Remove edge
        self.edges = [(f, t, w) for f, t, w in self.edges 
                     if not (f == from_vertex and t == to_vertex)]
        
        # If undirected, remove reverse edge
        if not self.directed:
            self.edges = [(f, t, w) for f, t, w in self.edges 
                         if not (f == to_vertex and t == from_vertex)]
        
        return len(self.edges) < original_length
    
    def has_edge(self, from_vertex: str, to_vertex: str) -> bool:
        """Check if edge exists"""
        return any(f == from_vertex and t == to_vertex 
                  for f, t, _ in self.edges)
    
    def get_neighbors(self, vertex: str) -> List[Tuple[str, float]]:
        """Get all neighbors with weights"""
        neighbors = []
        for from_v, to_v, weight in self.edges:
            if from_v == vertex:
                neighbors.append((to_v, weight))
        return neighbors
    
    def get_vertices(self) -> Set[str]:
        """Get all vertices in the graph"""
        return self.vertices.copy()
    
    def get_edges(self) -> List[Tuple[str, str, float]]:
        """Get all edges"""
        if self.directed:
            return self.edges[:]
        else:
            # Remove duplicates for undirected graph
            unique_edges = []
            seen = set()
            for f, t, w in self.edges:
                edge = tuple(sorted([f, t])) + (w,)
                if edge not in seen:
                    seen.add(edge)
                    unique_edges.append((f, t, w))
            return unique_edges
    
    def display(self):
        """Display edge list"""
        print(f"Edge List ({'Directed' if self.directed else 'Undirected'}):")
        edges = self.get_edges()
        
        if not edges:
            print("No edges")
            return
        
        for from_v, to_v, weight in edges:
            direction = " -> " if self.directed else " -- "
            print(f"{from_v}{direction}{to_v} (weight: {weight})")


def demo_graph_representations():
    """Demonstrate different graph representations"""
    print("=== Graph Representations Demo ===")
    
    # Create same graph using different representations
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B', 2), ('B', 'C', 3), ('C', 'D', 1), ('A', 'D', 4)]
    
    print("\nCreating undirected weighted graph:")
    print("Vertices:", vertices)
    print("Edges:", edges)
    
    # 1. Adjacency Matrix
    print("\n1. Adjacency Matrix Representation:")
    matrix_graph = AdjacencyMatrixGraph(directed=False)
    
    # Add vertices
    for vertex in vertices:
        matrix_graph.add_vertex(vertex)
    
    # Add edges
    for from_v, to_v, weight in edges:
        matrix_graph.add_edge(from_v, to_v, weight)
    
    matrix_graph.display()
    print(f"Neighbors of A: {matrix_graph.get_neighbors('A')}")
    
    # 2. Adjacency List
    print("\n2. Adjacency List Representation:")
    list_graph = AdjacencyListGraph(directed=False)
    
    for from_v, to_v, weight in edges:
        list_graph.add_edge(from_v, to_v, weight)
    
    list_graph.display()
    print(f"Neighbors of A: {list_graph.get_neighbor_names('A')}")
    
    # 3. Edge List
    print("\n3. Edge List Representation:")
    edge_graph = EdgeListGraph(directed=False)
    
    for from_v, to_v, weight in edges:
        edge_graph.add_edge(from_v, to_v, weight)
    
    edge_graph.display()
    print(f"Neighbors of A: {[n for n, w in edge_graph.get_neighbors('A')]}")


def compare_representations():
    """Compare different graph representations"""
    print("\n=== Representation Comparison ===")
    
    print("Adjacency Matrix:")
    print("✓ Fast edge lookup: O(1)")
    print("✓ Fast edge addition/removal: O(1)")
    print("✗ Space inefficient for sparse graphs: O(V²)")
    print("✗ Adding vertices is expensive: O(V²)")
    print("Best for: Dense graphs, frequent edge queries")
    
    print("\nAdjacency List:")
    print("✓ Space efficient: O(V + E)")
    print("✓ Fast vertex addition: O(1)")
    print("✓ Efficient neighbor iteration: O(degree)")
    print("✗ Slower edge lookup: O(degree)")
    print("✗ Edge removal can be slow: O(degree)")
    print("Best for: Sparse graphs, traversal algorithms")
    
    print("\nEdge List:")
    print("✓ Simple implementation")
    print("✓ Space efficient: O(E)")
    print("✓ Good for algorithms that process all edges")
    print("✗ Slow neighbor queries: O(E)")
    print("✗ Slow edge existence checks: O(E)")
    print("Best for: Algorithms like Kruskal's MST, simple storage")
    
    print("\nRecommendations:")
    print("• Dense graph (E ≈ V²): Adjacency Matrix")
    print("• Sparse graph (E << V²): Adjacency List")
    print("• Many edge operations: Adjacency Matrix")
    print("• Graph traversals: Adjacency List")
    print("• Simple edge processing: Edge List")


if __name__ == "__main__":
    demo_graph_representations()
    compare_representations()
