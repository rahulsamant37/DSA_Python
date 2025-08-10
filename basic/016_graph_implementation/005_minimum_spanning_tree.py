"""
005 - Minimum Spanning Tree
===========================

Minimum Spanning Tree (MST) algorithms for weighted undirected graphs.

A Minimum Spanning Tree connects all vertices with minimum total edge weight.

Algorithms implemented:
1. Kruskal's Algorithm - Uses Union-Find (Disjoint Set)
2. Prim's Algorithm - Uses priority queue

Properties of MST:
- Has exactly V-1 edges (V = number of vertices)
- Is acyclic (it's a tree)
- Connects all vertices
- Has minimum total weight among all spanning trees

Time Complexities:
- Kruskal: O(E log E) due to sorting edges
- Prim: O(E log V) with binary heap

Applications:
- Network design (minimize cable cost)
- Cluster analysis
- Approximation algorithms for TSP
"""

import heapq
from typing import List, Tuple, Dict, Set, Optional
from collections import defaultdict


class UnionFind:
    """Union-Find (Disjoint Set) data structure for Kruskal's algorithm"""
    
    def __init__(self, vertices: List[str]):
        """Initialize Union-Find structure"""
        self.parent = {v: v for v in vertices}
        self.rank = {v: 0 for v in vertices}
    
    def find(self, vertex: str) -> str:
        """Find root of vertex with path compression"""
        if self.parent[vertex] != vertex:
            self.parent[vertex] = self.find(self.parent[vertex])
        return self.parent[vertex]
    
    def union(self, vertex1: str, vertex2: str) -> bool:
        """
        Union two sets by rank
        
        Returns:
            True if union performed, False if already in same set
        """
        root1 = self.find(vertex1)
        root2 = self.find(vertex2)
        
        if root1 == root2:
            return False  # Already in same set
        
        # Union by rank
        if self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        elif self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        else:
            self.parent[root2] = root1
            self.rank[root1] += 1
        
        return True
    
    def connected(self, vertex1: str, vertex2: str) -> bool:
        """Check if two vertices are in same connected component"""
        return self.find(vertex1) == self.find(vertex2)


class MinimumSpanningTree:
    """MST algorithms for weighted undirected graphs"""
    
    def __init__(self, edges: List[Tuple[str, str, float]]):
        """
        Initialize with edge list
        
        Args:
            edges: List of (vertex1, vertex2, weight) tuples
        """
        self.edges = edges
        self.vertices = set()
        
        # Extract all vertices
        for v1, v2, _ in edges:
            self.vertices.add(v1)
            self.vertices.add(v2)
        
        # Create adjacency list for Prim's algorithm
        self.graph = defaultdict(list)
        for v1, v2, weight in edges:
            self.graph[v1].append((v2, weight))
            self.graph[v2].append((v1, weight))
    
    def kruskals_mst(self) -> Tuple[List[Tuple[str, str, float]], float]:
        """
        Kruskal's algorithm for MST using Union-Find
        
        Returns:
            Tuple of (mst_edges, total_weight)
        """
        if not self.edges:
            return [], 0.0
        
        # Sort edges by weight
        sorted_edges = sorted(self.edges, key=lambda x: x[2])
        
        # Initialize Union-Find
        union_find = UnionFind(list(self.vertices))
        
        mst_edges = []
        total_weight = 0.0
        
        for v1, v2, weight in sorted_edges:
            # If adding this edge doesn't create cycle
            if union_find.union(v1, v2):
                mst_edges.append((v1, v2, weight))
                total_weight += weight
                
                # MST complete when we have V-1 edges
                if len(mst_edges) == len(self.vertices) - 1:
                    break
        
        return mst_edges, total_weight
    
    def prims_mst(self, start: Optional[str] = None) -> Tuple[List[Tuple[str, str, float]], float]:
        """
        Prim's algorithm for MST using priority queue
        
        Args:
            start: Starting vertex (optional, picks first vertex if None)
        
        Returns:
            Tuple of (mst_edges, total_weight)
        """
        if not self.vertices:
            return [], 0.0
        
        if start is None:
            start = next(iter(self.vertices))
        
        mst_edges = []
        total_weight = 0.0
        visited = {start}
        
        # Priority queue: (weight, vertex1, vertex2)
        edge_queue = []
        
        # Add all edges from start vertex
        for neighbor, weight in self.graph[start]:
            heapq.heappush(edge_queue, (weight, start, neighbor))
        
        while edge_queue and len(visited) < len(self.vertices):
            weight, v1, v2 = heapq.heappop(edge_queue)
            
            # Skip if both vertices already in MST
            if v2 in visited:
                continue
            
            # Add edge to MST
            mst_edges.append((v1, v2, weight))
            total_weight += weight
            visited.add(v2)
            
            # Add all edges from newly added vertex
            for neighbor, edge_weight in self.graph[v2]:
                if neighbor not in visited:
                    heapq.heappush(edge_queue, (edge_weight, v2, neighbor))
        
        return mst_edges, total_weight
    
    def all_spanning_trees(self) -> List[List[Tuple[str, str, float]]]:
        """
        Find all spanning trees using backtracking (for small graphs only)
        
        Returns:
            List of all spanning trees, each as list of edges
        """
        if len(self.vertices) > 6:  # Limit for performance
            raise ValueError("Too many vertices for exhaustive search")
        
        all_trees = []
        vertices_list = list(self.vertices)
        n = len(vertices_list)
        
        def is_connected(edges):
            """Check if edges form connected graph"""
            if len(edges) != n - 1:
                return False
            
            # Use Union-Find to check connectivity
            uf = UnionFind(vertices_list)
            for v1, v2, _ in edges:
                uf.union(v1, v2)
            
            # Check if all vertices in same component
            root = uf.find(vertices_list[0])
            return all(uf.find(v) == root for v in vertices_list)
        
        def backtrack(edge_index, current_edges):
            if len(current_edges) == n - 1:
                if is_connected(current_edges):
                    all_trees.append(current_edges[:])
                return
            
            if edge_index >= len(self.edges):
                return
            
            # Try including current edge
            current_edges.append(self.edges[edge_index])
            backtrack(edge_index + 1, current_edges)
            current_edges.pop()
            
            # Try not including current edge
            backtrack(edge_index + 1, current_edges)
        
        backtrack(0, [])
        return all_trees
    
    def is_connected_graph(self) -> bool:
        """Check if graph is connected using DFS"""
        if not self.vertices:
            return True
        
        start = next(iter(self.vertices))
        visited = set()
        stack = [start]
        
        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, _ in self.graph[vertex]:
                    if neighbor not in visited:
                        stack.append(neighbor)
        
        return len(visited) == len(self.vertices)


def demo_network_design():
    """Demonstrate MST for network design problem"""
    print("=== Network Design Demo ===")
    
    # Cities and cable costs
    cities = ['A', 'B', 'C', 'D', 'E', 'F']
    cables = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', 1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2), ('D', 'F', 6),
        ('E', 'F', 3)
    ]
    
    print("Cities to connect:", cities)
    print("Cable costs:")
    for city1, city2, cost in cables:
        print(f"  {city1} -- {city2}: ${cost}k")
    
    mst = MinimumSpanningTree(cables)
    
    print(f"\nGraph is connected: {mst.is_connected_graph()}")
    
    # Kruskal's algorithm
    kruskal_edges, kruskal_cost = mst.kruskals_mst()
    print(f"\nKruskal's MST (cost: ${kruskal_cost}k):")
    for city1, city2, cost in kruskal_edges:
        print(f"  {city1} -- {city2}: ${cost}k")
    
    # Prim's algorithm
    prim_edges, prim_cost = mst.prims_mst('A')
    print(f"\nPrim's MST starting from A (cost: ${prim_cost}k):")
    for city1, city2, cost in prim_edges:
        print(f"  {city1} -- {city2}: ${cost}k")
    
    print(f"\nBoth algorithms found same cost: {kruskal_cost == prim_cost}")


def demo_small_graph_all_trees():
    """Demonstrate finding all spanning trees for small graph"""
    print("\n=== All Spanning Trees Demo ===")
    
    # Small graph for demonstration
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 2),
        ('B', 'C', 3),
        ('B', 'D', 4),
        ('C', 'D', 5)
    ]
    
    print("Small graph edges:")
    for v1, v2, weight in edges:
        print(f"  {v1} -- {v2}: {weight}")
    
    mst = MinimumSpanningTree(edges)
    
    try:
        all_trees = mst.all_spanning_trees()
        print(f"\nAll spanning trees ({len(all_trees)} total):")
        
        for i, tree in enumerate(all_trees, 1):
            total_weight = sum(weight for _, _, weight in tree)
            edge_str = ", ".join(f"{v1}-{v2}({w})" for v1, v2, w in tree)
            print(f"  {i}: [{edge_str}] = {total_weight}")
        
        # Find minimum weight trees
        min_weight = min(sum(w for _, _, w in tree) for tree in all_trees)
        min_trees = [tree for tree in all_trees 
                    if sum(w for _, _, w in tree) == min_weight]
        
        print(f"\nMinimum spanning trees (weight {min_weight}):")
        for tree in min_trees:
            edge_str = ", ".join(f"{v1}-{v2}" for v1, v2, _ in tree)
            print(f"  [{edge_str}]")
    
    except ValueError as e:
        print(f"Error: {e}")


def demo_disconnected_graph():
    """Demonstrate MST on disconnected graph"""
    print("\n=== Disconnected Graph Demo ===")
    
    # Disconnected graph (two components)
    edges = [
        ('A', 'B', 1),
        ('B', 'C', 2),
        ('X', 'Y', 3),
        ('Y', 'Z', 4)
    ]
    
    print("Disconnected graph edges:")
    for v1, v2, weight in edges:
        print(f"  {v1} -- {v2}: {weight}")
    
    mst = MinimumSpanningTree(edges)
    
    print(f"\nGraph is connected: {mst.is_connected_graph()}")
    
    kruskal_edges, kruskal_cost = mst.kruskals_mst()
    print(f"\nKruskal's result (Minimum Spanning Forest):")
    print(f"Edges found: {len(kruskal_edges)}")
    print(f"Expected for MST: {len(mst.vertices) - 1}")
    
    if kruskal_edges:
        print("Edges in spanning forest:")
        for v1, v2, weight in kruskal_edges:
            print(f"  {v1} -- {v2}: {weight}")
        print(f"Total weight: {kruskal_cost}")
    
    print("\nNote: For disconnected graphs, algorithms find Minimum Spanning Forest")


def demo_performance_comparison():
    """Compare Kruskal vs Prim performance characteristics"""
    print("\n=== Performance Comparison Demo ===")
    
    # Dense graph
    dense_edges = []
    vertices = ['A', 'B', 'C', 'D', 'E']
    weight = 1
    
    # Create complete graph
    for i, v1 in enumerate(vertices):
        for v2 in vertices[i+1:]:
            dense_edges.append((v1, v2, weight))
            weight += 1
    
    print(f"Dense graph with {len(vertices)} vertices, {len(dense_edges)} edges:")
    
    mst = MinimumSpanningTree(dense_edges)
    
    kruskal_edges, kruskal_cost = mst.kruskals_mst()
    prim_edges, prim_cost = mst.prims_mst()
    
    print(f"Kruskal's MST cost: {kruskal_cost}")
    print(f"Prim's MST cost: {prim_cost}")
    print(f"Results match: {kruskal_cost == prim_cost}")
    
    print(f"\nAlgorithm characteristics:")
    print(f"Kruskal's: O(E log E) - good for sparse graphs")
    print(f"Prim's: O(E log V) - good for dense graphs")
    print(f"Dense graph (E ≈ V²): Prim's typically better")
    print(f"Sparse graph (E ≈ V): Kruskal's typically better")


def compare_mst_algorithms():
    """Compare MST algorithms"""
    print("\n=== MST Algorithms Comparison ===")
    
    print("Kruskal's Algorithm:")
    print("✓ Uses Union-Find data structure")
    print("✓ Processes edges in order of weight")
    print("✓ Good for sparse graphs")
    print("✓ Works on disconnected graphs (finds forest)")
    print("✗ Requires sorting all edges: O(E log E)")
    print("✗ More complex implementation")
    
    print("\nPrim's Algorithm:")
    print("✓ Uses priority queue (heap)")
    print("✓ Grows MST incrementally from starting vertex")
    print("✓ Good for dense graphs")
    print("✓ Simpler conceptually")
    print("✗ Requires connected graph")
    print("✗ Choice of starting vertex can affect performance")
    
    print("\nBoth algorithms:")
    print("• Guaranteed to find MST if graph is connected")
    print("• Greedy algorithms with optimal substructure")
    print("• Handle negative edge weights correctly")
    print("• Output MST may not be unique")
    
    print("\nApplications:")
    print("• Network design (minimize connection cost)")
    print("• Clustering (minimum distance connections)")
    print("• Approximation for Traveling Salesman Problem")
    print("• Image segmentation")
    print("• Transportation planning")


if __name__ == "__main__":
    demo_network_design()
    demo_small_graph_all_trees()
    demo_disconnected_graph()
    demo_performance_comparison()
    compare_mst_algorithms()
