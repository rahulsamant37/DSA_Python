"""
004 - Topological Sort
======================

Topological sorting for Directed Acyclic Graphs (DAGs).

A topological sort is a linear ordering of vertices in a directed graph
such that for every directed edge (u, v), vertex u comes before v in the ordering.

Algorithms implemented:
1. Kahn's Algorithm (BFS-based using in-degrees)
2. DFS-based algorithm (using post-order traversal)

Time Complexity: O(V + E)
Space Complexity: O(V)

Applications:
- Task scheduling with dependencies
- Course prerequisite ordering
- Build systems (dependency resolution)
- Deadlock detection
"""

from collections import deque, defaultdict
from typing import List, Dict, Set, Optional, Tuple
from enum import Enum


class NodeState(Enum):
    """States for DFS-based topological sort"""
    WHITE = 0  # Unvisited
    GRAY = 1   # Visiting (in current path)
    BLACK = 2  # Visited (completely processed)


class TopologicalSort:
    """Topological sorting algorithms for directed graphs"""
    
    def __init__(self, adjacency_list: Dict[str, List[str]]):
        """
        Initialize with directed graph
        
        Args:
            adjacency_list: Directed graph as adjacency list
        """
        self.graph = adjacency_list
        self.vertices = set(adjacency_list.keys())
        
        # Add vertices that appear as neighbors but not as keys
        for vertex in adjacency_list:
            for neighbor in adjacency_list[vertex]:
                self.vertices.add(neighbor)
    
    def kahns_algorithm(self) -> Tuple[List[str], bool]:
        """
        Kahn's algorithm for topological sorting using in-degrees
        
        Returns:
            Tuple of (topological_order, is_dag)
            is_dag is False if graph has cycles
        """
        # Calculate in-degrees
        in_degree = {vertex: 0 for vertex in self.vertices}
        
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                in_degree[neighbor] += 1
        
        # Find vertices with no incoming edges
        queue = deque()
        for vertex in self.vertices:
            if in_degree[vertex] == 0:
                queue.append(vertex)
        
        topological_order = []
        
        while queue:
            # Remove vertex with no incoming edges
            vertex = queue.popleft()
            topological_order.append(vertex)
            
            # Remove this vertex from graph and update in-degrees
            for neighbor in self.graph.get(vertex, []):
                in_degree[neighbor] -= 1
                
                # If neighbor has no more incoming edges, add to queue
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        
        # Check if all vertices are included (no cycles)
        is_dag = len(topological_order) == len(self.vertices)
        
        return topological_order, is_dag
    
    def dfs_topological_sort(self) -> Tuple[List[str], bool]:
        """
        DFS-based topological sorting
        
        Returns:
            Tuple of (topological_order, is_dag)
            is_dag is False if graph has cycles
        """
        state = {vertex: NodeState.WHITE for vertex in self.vertices}
        result = []
        has_cycle = False
        
        def dfs(vertex):
            nonlocal has_cycle
            
            if has_cycle:
                return
            
            if state[vertex] == NodeState.GRAY:
                # Back edge found - cycle detected
                has_cycle = True
                return
            
            if state[vertex] == NodeState.BLACK:
                # Already processed
                return
            
            # Mark as visiting
            state[vertex] = NodeState.GRAY
            
            # Visit all neighbors
            for neighbor in self.graph.get(vertex, []):
                dfs(neighbor)
            
            # Mark as visited and add to result
            state[vertex] = NodeState.BLACK
            result.append(vertex)
        
        # Process all vertices
        for vertex in self.vertices:
            if state[vertex] == NodeState.WHITE:
                dfs(vertex)
        
        # Reverse to get correct topological order
        result.reverse()
        
        return result, not has_cycle
    
    def all_topological_sorts(self) -> List[List[str]]:
        """
        Find all possible topological sorts using backtracking
        
        Returns:
            List of all valid topological orderings
        """
        # Calculate in-degrees
        in_degree = {vertex: 0 for vertex in self.vertices}
        
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                in_degree[neighbor] += 1
        
        result = []
        current_order = []
        available = set()
        
        # Find initially available vertices (in-degree 0)
        for vertex in self.vertices:
            if in_degree[vertex] == 0:
                available.add(vertex)
        
        def backtrack():
            if len(current_order) == len(self.vertices):
                # Found complete topological order
                result.append(current_order[:])
                return
            
            # Try each available vertex
            for vertex in list(available):
                # Choose vertex
                available.remove(vertex)
                current_order.append(vertex)
                
                # Update available vertices
                newly_available = set()
                for neighbor in self.graph.get(vertex, []):
                    in_degree[neighbor] -= 1
                    if in_degree[neighbor] == 0:
                        available.add(neighbor)
                        newly_available.add(neighbor)
                
                # Recurse
                backtrack()
                
                # Backtrack
                current_order.pop()
                available.add(vertex)
                for neighbor in newly_available:
                    available.remove(neighbor)
                for neighbor in self.graph.get(vertex, []):
                    in_degree[neighbor] += 1
        
        backtrack()
        return result
    
    def has_cycle(self) -> bool:
        """
        Detect cycle in directed graph using DFS
        
        Returns:
            True if graph has cycle, False otherwise
        """
        state = {vertex: NodeState.WHITE for vertex in self.vertices}
        
        def dfs(vertex):
            if state[vertex] == NodeState.GRAY:
                return True  # Back edge found
            
            if state[vertex] == NodeState.BLACK:
                return False  # Already processed
            
            state[vertex] = NodeState.GRAY
            
            for neighbor in self.graph.get(vertex, []):
                if dfs(neighbor):
                    return True
            
            state[vertex] = NodeState.BLACK
            return False
        
        # Check from all vertices
        for vertex in self.vertices:
            if state[vertex] == NodeState.WHITE:
                if dfs(vertex):
                    return True
        
        return False
    
    def longest_path_in_dag(self) -> Dict[str, int]:
        """
        Find longest path from each vertex in DAG
        Only works if graph is acyclic
        
        Returns:
            Dictionary mapping vertex to longest path length from that vertex
        """
        if self.has_cycle():
            raise ValueError("Graph has cycles - longest path undefined")
        
        # Get topological order
        topo_order, _ = self.dfs_topological_sort()
        
        # Initialize distances
        longest_dist = {vertex: 0 for vertex in self.vertices}
        
        # Process vertices in reverse topological order
        for vertex in reversed(topo_order):
            for neighbor in self.graph.get(vertex, []):
                longest_dist[vertex] = max(longest_dist[vertex], 
                                         longest_dist[neighbor] + 1)
        
        return longest_dist


def demo_course_scheduling():
    """Demonstrate topological sort for course scheduling"""
    print("=== Course Scheduling Demo ===")
    
    # Course prerequisites graph
    # Course -> List of prerequisites
    prerequisites = {
        'Math101': [],
        'Math201': ['Math101'],
        'Math301': ['Math201'],
        'CS101': [],
        'CS201': ['CS101', 'Math101'],
        'CS301': ['CS201', 'Math201'],
        'CS401': ['CS301'],
        'Physics101': ['Math101'],
        'Physics201': ['Physics101', 'Math201']
    }
    
    print("Course prerequisites:")
    for course, prereqs in prerequisites.items():
        if prereqs:
            print(f"{course}: requires {', '.join(prereqs)}")
        else:
            print(f"{course}: no prerequisites")
    
    # Convert to directed graph (prerequisite -> course)
    graph = defaultdict(list)
    all_courses = set(prerequisites.keys())
    
    for course, prereqs in prerequisites.items():
        for prereq in prereqs:
            graph[prereq].append(course)
    
    # Add courses with no prerequisites
    for course in all_courses:
        if course not in graph:
            graph[course] = []
    
    print(f"\nDependency graph:")
    for course in sorted(graph.keys()):
        dependents = graph[course]
        if dependents:
            print(f"{course} -> {', '.join(dependents)}")
        else:
            print(f"{course} -> (no dependents)")
    
    topo_sort = TopologicalSort(dict(graph))
    
    # Kahn's algorithm
    order1, is_dag1 = topo_sort.kahns_algorithm()
    print(f"\nCourse order (Kahn's): {' -> '.join(order1)}")
    print(f"Valid schedule: {is_dag1}")
    
    # DFS algorithm
    order2, is_dag2 = topo_sort.dfs_topological_sort()
    print(f"Course order (DFS): {' -> '.join(order2)}")
    print(f"Valid schedule: {is_dag2}")


def demo_build_system():
    """Demonstrate topological sort for build dependencies"""
    print("\n=== Build System Demo ===")
    
    # Build dependencies (file -> dependencies)
    dependencies = {
        'main.o': ['main.cpp', 'utils.h'],
        'utils.o': ['utils.cpp', 'utils.h'],
        'math.o': ['math.cpp', 'math.h'],
        'app': ['main.o', 'utils.o', 'math.o'],
        'main.cpp': [],
        'utils.cpp': [],
        'math.cpp': [],
        'utils.h': [],
        'math.h': []
    }
    
    print("Build dependencies:")
    for target, deps in dependencies.items():
        if deps:
            print(f"{target}: depends on {', '.join(deps)}")
        else:
            print(f"{target}: source file")
    
    # Convert to graph (dependency -> dependent)
    graph = defaultdict(list)
    all_files = set(dependencies.keys())
    
    for target, deps in dependencies.items():
        for dep in deps:
            graph[dep].append(target)
    
    # Add source files
    for file in all_files:
        if file not in graph:
            graph[file] = []
    
    topo_sort = TopologicalSort(dict(graph))
    build_order, is_dag = topo_sort.kahns_algorithm()
    
    print(f"\nBuild order: {' -> '.join(build_order)}")
    print(f"Valid build (no circular dependencies): {is_dag}")


def demo_cyclic_dependency():
    """Demonstrate cycle detection"""
    print("\n=== Cyclic Dependency Demo ===")
    
    # Graph with cycle
    cyclic_graph = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['B']  # Creates cycle B -> C -> D -> B
    }
    
    print("Graph with cycle:")
    for vertex, neighbors in cyclic_graph.items():
        print(f"{vertex} -> {', '.join(neighbors)}")
    
    topo_sort = TopologicalSort(cyclic_graph)
    
    print(f"\nHas cycle: {topo_sort.has_cycle()}")
    
    order1, is_dag1 = topo_sort.kahns_algorithm()
    print(f"Kahn's result: {order1}")
    print(f"Is DAG: {is_dag1}")
    
    order2, is_dag2 = topo_sort.dfs_topological_sort()
    print(f"DFS result: {order2}")
    print(f"Is DAG: {is_dag2}")


def demo_all_topological_sorts():
    """Demonstrate finding all possible topological sorts"""
    print("\n=== All Topological Sorts Demo ===")
    
    # Small DAG with multiple valid orderings
    graph = {
        'A': ['C'],
        'B': ['C', 'D'],
        'C': ['E'],
        'D': ['E'],
        'E': []
    }
    
    print("Small DAG:")
    for vertex, neighbors in graph.items():
        if neighbors:
            print(f"{vertex} -> {', '.join(neighbors)}")
        else:
            print(f"{vertex} -> (no outgoing edges)")
    
    topo_sort = TopologicalSort(graph)
    all_sorts = topo_sort.all_topological_sorts()
    
    print(f"\nAll possible topological sorts ({len(all_sorts)} total):")
    for i, sort in enumerate(all_sorts, 1):
        print(f"{i}: {' -> '.join(sort)}")


def demo_longest_path():
    """Demonstrate longest path in DAG"""
    print("\n=== Longest Path in DAG Demo ===")
    
    # DAG for longest path
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': ['F'],
        'F': []
    }
    
    print("DAG for longest path:")
    for vertex, neighbors in graph.items():
        if neighbors:
            print(f"{vertex} -> {', '.join(neighbors)}")
    
    topo_sort = TopologicalSort(graph)
    longest_paths = topo_sort.longest_path_in_dag()
    
    print(f"\nLongest path from each vertex:")
    for vertex in sorted(longest_paths.keys()):
        print(f"From {vertex}: {longest_paths[vertex]} edges")


def compare_algorithms():
    """Compare topological sorting algorithms"""
    print("\n=== Algorithm Comparison ===")
    
    print("Kahn's Algorithm (BFS-based):")
    print("✓ Intuitive: removes vertices with no dependencies")
    print("✓ Can detect cycles easily")
    print("✓ Stable: preserves order when possible")
    print("✓ Good for online algorithms")
    print("✗ Requires extra space for in-degree calculation")
    
    print("\nDFS-based Algorithm:")
    print("✓ Simple recursive implementation")
    print("✓ Can detect cycles during traversal")
    print("✓ Uses implicit stack (recursion)")
    print("✗ May not be stable")
    print("✗ Can have stack overflow for deep graphs")
    
    print("\nBoth algorithms:")
    print("• Time Complexity: O(V + E)")
    print("• Space Complexity: O(V)")
    print("• Work only on DAGs (Directed Acyclic Graphs)")


if __name__ == "__main__":
    demo_course_scheduling()
    demo_build_system()
    demo_cyclic_dependency()
    demo_all_topological_sorts()
    demo_longest_path()
    compare_algorithms()
